import os
from django.shortcuts import render, redirect
from .models import ModelCustomer, ModelCompany, ModelDesigns, ModelType, ModelInvoice
from django.contrib import messages
from .helper import countDesigns
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    customers = len(ModelCustomer.objects.all())
    totalDesign = len(ModelDesigns.objects.all())
    designs = ModelDesigns.objects.all()
    paid, unpaid = countDesigns(designs)
    context = {'no_of_customers': customers, 'no_of_designs': totalDesign,
               'paid': paid, 'unpaid': unpaid}
    return render(request, 'home/home.html', context)


@login_required
def customerForm(request):
    return render(request, 'home/addcustomer.html')
    # return HttpResponse('customeer added')


@login_required
def companyForm(request):
    customers = ModelCustomer.objects.all()
    context = {'customers': customers}
    return render(request, 'home/addcompany.html', context)


@login_required
def designForm(request):
    customers = ModelCustomer.objects.all()
    designtype = ModelType.objects.all()
    context = {'customers': customers, 'designtype': designtype}
    return render(request, 'home/adddesign.html', context)
    # return HttpResponse('customeer added')


@login_required
def invoiceForm(request):
    customers = ModelCustomer.objects.all()
    context = {'customers': customers}
    return render(request, 'home/invoice.html', context)


@login_required
def checkInvoiceForm(request):
    customers = ModelCustomer.objects.all()
    context = {'customers': customers}
    return render(request, 'home/checkinvoice.html', context)


def saveInvoice(request):
    if request.method == 'POST':
        try:
            month = request.POST['invoicedate']
            customer_id = request.POST['customer']
            customer = ModelCustomer.objects.get(customerid=customer_id)
            ispaid = request.POST.get('paid', 'off')

            flag = None
            if ispaid == "on":
                flag = True
            else:
                flag = False

            mark_paid = ModelInvoice(month=month, ispaid=flag, customer_id=customer)
            mark_paid.save()
        except Exception as e:
            print(e)
        messages.success(request, "Invoice Recorded, Successfully!!!")
        return redirect('checkinvoiceform')


@login_required
def typeForm(request):
    return render(request, 'home/adddesigntype.html')
    # return HttpResponse('customeer added')


def addCustomer(request):
    if request.method == "POST":
        fname = request.POST['fname']
        contact = request.POST['contact']
        email = request.POST['email']

        customer = ModelCustomer(fname=fname, contact=contact, email=email)
        customer.save()

        messages.success(request, "Customer Added Successfully")
        return render(request, 'home/addcustomer.html')


def addCompany(request):
    if request.method == 'POST':
        try:
            cname = request.POST['cname']
            address = request.POST['address']
            zipcode = request.POST['zipcode']
            city = request.POST['city']
            state = request.POST['state']
            customerid = request.POST['customer']
            selectedcustomer = ModelCustomer.objects.get(customerid=customerid)

            company = ModelCompany(name=cname, address=address, zipcode=zipcode,
                                   city=city, state=state, custid=selectedcustomer)
            company.save()
            messages.success(request, "Company Added Successfully")
        except:
            messages.warning(request, '''Customer, Already Added in a Company.
             A Customer Can't be Enrolled in Different Companies. ''')
        return redirect('companyform')


def addDesign(request):
    if request.method == 'POST':
        dname = request.POST['dname']
        orderid = request.POST['orderid']
        image = request.FILES.get('image')
        price = request.POST['price']
        cid = request.POST['customer']
        tid = request.POST['types']
        check = cid.isnumeric()
        if check is True:
            customer = ModelCustomer.objects.get(customerid=cid)
            designtype = ModelType.objects.get(tid=tid)
            design = ModelDesigns(name=dname, orderid=orderid, image=image, price=price, custid=customer, type=designtype)
            design.save()
            messages.success(request, "Design Added Successfully")
            # return render(request, 'home/adddesign.html')
            return redirect('designform')
        else:
            messages.ERROR(request, "Select Customer form the list")
            return redirect('designform')


def addDesignTypes(request):
    if request.method == 'POST':
        typename = request.POST['types']
        designtype = ModelType(type=typename)
        designtype.save()
        messages.success(request, "Design Types Added Successfully")
        return redirect('typeform')


@login_required
def viewCustomer(request):
    allData = ModelCustomer.objects.all()
    context = {'allData': allData}
    return render(request, 'home/viewcustomer.html', context)


@login_required
def viewCompany(request):
    companyData = ModelCompany.objects.all()
    context = {'allData': companyData}
    return render(request, 'home/viewcompany.html', context)


@login_required
def viewDesign(request):
    allData = ModelDesigns.objects.all()
    context = {'allData': allData}
    return render(request, 'home/viewdesign.html', context)


@login_required
def viewInvoice(request):
    allData = ModelInvoice.objects.all()
    context = {'allData': allData}
    return render(request, 'home/viewinvoices.html', context)


def editCustomer(request, id):
    customer = ModelCustomer.objects.get(customerid=id)
    context = {"cust": customer}
    return render(request, 'home/updatecustomer.html', context)


def editCompany(request, id):
    company = ModelCompany.objects.get(companyid=id)
    customerName = company.custid
    customer = ModelCustomer.objects.get(fname=customerName)
    context = {"comp": company, 'cust': customer}
    return render(request, 'home/updatecompany.html', context)


def editDesign(request, id):
    design = ModelDesigns.objects.get(did=id)
    customer = design.custid
    dType = design.type
    customer = ModelCustomer.objects.get(fname=customer)
    designType = ModelDesigns.objects.filter(type=dType).first()
    context = {"d": design, 'cust': customer, 'type': designType}
    return render(request, 'home/updatedesign.html', context)


def updateCustomer(request):
    if request.method == "POST":
        cid = request.POST['cid']
        fname = request.POST['fname']
        contact = request.POST['contact']
        email = request.POST['email']

        customer = ModelCustomer.objects.get(customerid=cid)
        customer.fname = fname
        customer.contact = contact
        customer.email = email
        customer.save()

        messages.success(request, "Data Updated Successfully")
        return redirect('viewcustomer')
    return render(request, 'home/updatecustomer.html')


def updateCompany(request):
    if request.method == "POST":
        # getting data
        cid = request.POST['cid']
        cname = request.POST['cname']
        address = request.POST['address']
        zipcode = request.POST['zipcode']
        city = request.POST['city']
        state = request.POST['state']
        # updating data
        company = ModelCompany.objects.get(companyid=cid)
        company.name = cname
        company.address = address
        company.zipcode = zipcode
        company.city = city
        company.state = state
        company.save()
        messages.success(request, "Data Updated Successfully")
        return redirect('viewcompany')
    return render(request, 'home/updatecustomer.html')


def updateDesign(request):
    if request.method == 'POST':
        # get data
        did = request.POST['did']
        designM = ModelDesigns.objects.get(did=did)
        dname = request.POST['dname']
        orderid = request.POST['orderid']
        image = request.FILES.get('image')
        price = request.POST['price']
        status = request.POST.get('ispaid', False)
        # tid = request.POST['types']

        # update data
        design = ModelDesigns.objects.get(did=did)
        if len(request.FILES) != 0:
            if len(design.image) > 0:
                os.remove(design.image.path)
            design.image = image
        design.name = dname
        if status == 'on':
            design.ispaid = True
        else:
            design.ispaid = False
        design.orderid = orderid
        design.price = price
        design.save()
        messages.success(request, "Data Updated Successfully")
        return redirect('viewdesign')
    return render(request, 'home/updatedesign.html')


def deleteCustomer(request, id):
    customer = ModelCustomer.objects.filter(customerid=id).delete()
    messages.success(request, "Data Deleted Successfully")
    return redirect('viewcustomer')


def deleteCompany(request, id):
    customer = ModelCompany.objects.filter(companyid=id).delete()
    messages.success(request, "Data Deleted Successfully")
    return redirect('viewcompany')


def deleteDesign(request, id):
    design = ModelDesigns.objects.filter(did=id).delete()
    messages.success(request, "Data Deleted Successfully")
    return redirect('viewdesign')


def deleteInvoice(request, id):
    ModelInvoice.objects.filter(invoice_id=id).delete()
    messages.success(request, "Data Deleted Successfully")
    return redirect('viewinvoice')

