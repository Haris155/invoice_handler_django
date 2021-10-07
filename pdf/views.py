import sys

from django.shortcuts import render

sys.path.append('..')

import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
import datetime
from home.models import ModelCompany, ModelCustomer, ModelDesigns, ModelInvoice


def test(request):
    return render(request, 'pdf/pdf.html')


def create_pdf(request):
    if request.method == 'POST':
        customerid = request.POST['customer']
        dateTime = request.POST['datetime']
        flag = request.POST.get('previewOnly', 'off')
        selectedcustomer = ModelCustomer.objects.get(customerid=customerid)
        customerCompany = ModelCompany.objects.filter(custid=customerid).first()
        customerDesigns = ModelDesigns.objects.filter(custid=customerid)

        inc = make_inc(flag)

        # count Total price of targeted customer
        total = countTotal(customerDesigns)
        # getting current date in format
        x = datetime.datetime.now().strftime("%d-%B-%Y")
        invoice_name_date = datetime.datetime.now().strftime("%B-%Y")
        context = {
            'cust': selectedcustomer, 'comp': customerCompany,
            'designs': customerDesigns, 'total': total, 'date': dateTime,
            'crt_date': x, 'inv_no': inc()
        }

        response = HttpResponse(content_type='application/pdf')
        file_name = f'{selectedcustomer}-{invoice_name_date}'
        response['content-Disposition'] = f'filename="{file_name}.pdf"'

        template = get_template('pdf/pdf.html')
        html = template.render(context)

        pisa_status = pisa.CreatePDF(html, dest=response)
        designsPaid(customerDesigns, flag)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response


def countTotal(obj):
    count = 0
    for o in obj:
        if not o.ispaid:
            count += int(o.price)
    return count


def designsPaid(obj, flag):
    for o in obj:
        if flag == 'on':
            pass
        else:
            o.ispaid = True
            o.save()


def make_inc(flag):
    val = [0]
    if flag != 'on':
        def inc():
            val[0] += 1
            print(val[0])
            return val[0]

        return inc
    else:
        temp = 'Preview Only'
        return temp
