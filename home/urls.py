from django.urls import path
from . import views
# settings
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    # for routing only foam load
    path('customerform', views.customerForm, name='customerform'),
    path('companyform', views.companyForm, name='companyform'),
    path('designform', views.designForm, name='designform'),
    path('invoiceform', views.invoiceForm, name='invoiceform'),
    # to mark invoice status
    path('checkinvoiceform', views.checkInvoiceForm, name='checkinvoiceform'),
    path('save_invoice', views.saveInvoice, name='save_invoice'),
    path('typeform', views.typeForm, name='typeform'),
    # action to perform
    path('addcustomer/', views.addCustomer, name='addcustomer'),
    path('addcompany/', views.addCompany, name='addcompany'),
    path('adddesign/', views.addDesign, name='adddesign'),
    path('adddesigntypes/', views.addDesignTypes, name='adddesigntypes'),
    # Viewing actions
    path('viewcustomer/', views.viewCustomer, name='viewcustomer'),
    path('viewcompany/', views.viewCompany, name='viewcompany'),
    path('viewdesign/', views.viewDesign, name='viewdesign'),
    path('viewinvoice/', views.viewInvoice, name='viewinvoice'),
    # edit actions
    path('editcustomer/<int:id>', views.editCustomer, name='editcustomer'),
    path('editcompany/<int:id>', views.editCompany, name='editcompany'),
    path('editdesign/<int:id>', views.editDesign, name='editcdesign'),
    # update actions
    path('updatecustomer/', views.updateCustomer, name='updatecustomer'),
    path('updatecompany/', views.updateCompany, name='updatecompany'),
    path('updatedesign/', views.updateDesign, name='updatedesign'),
    # delete actions
    path('deletecustomer/<int:id>', views.deleteCustomer, name='deletecustomer'),
    path('deletecompany/<int:id>', views.deleteCompany, name='deletecompany'),
    path('deletedesign/<int:id>', views.deleteDesign, name='deletedesign'),
    path('deleteinvoice/<int:id>', views.deleteInvoice, name='deleteinvoice'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
