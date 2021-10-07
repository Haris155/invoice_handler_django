from django.contrib import admin
from .models import ModelCompany, ModelCustomer, ModelDesigns, ModelType

# Register your models here.
admin.site.register(ModelCompany)
admin.site.register(ModelDesigns)
admin.site.register(ModelCustomer)
admin.site.register(ModelType)
