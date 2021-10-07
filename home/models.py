from django.db import models


# Create your models here.
class ModelCustomer(models.Model):
    customerid = models.AutoField(primary_key=True, default=None)
    fname = models.CharField(max_length=20)
    contact = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.fname


class ModelCompany(models.Model):
    companyid = models.AutoField(primary_key=True, default=None)
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=150)
    zipcode = models.IntegerField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    custid = models.OneToOneField('ModelCustomer', on_delete=models.CASCADE, blank=True, null=True, default=None)

    def __str__(self):
        return self.name + " " + self.city + " " + self.state


class ModelDesigns(models.Model):
    did = models.AutoField(primary_key=True, default=None)
    orderid = models.IntegerField(default=None, null=True)
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='home/images/', default=None, null=True)
    price = models.IntegerField(default=0, null=True)
    ispaid = models.BooleanField(default=False, null=True)
    type = models.ForeignKey('ModelType', on_delete=models.CASCADE, blank=True, null=True)
    custid = models.ForeignKey('ModelCustomer', on_delete=models.CASCADE, blank=True, null=True, default=None)

    def __str__(self):
        return self.name


class ModelType(models.Model):
    tid = models.AutoField(primary_key=True, default=None)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class ModelInvoice(models.Model):
    invoice_id = models.AutoField(primary_key=True, default=None)
    month = models.DateField()
    ispaid = models.BooleanField(null=True, blank=True)
    customer_id = models.ForeignKey('ModelCustomer', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.type

