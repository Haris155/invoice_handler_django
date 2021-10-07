from django.urls import path
from . import views


urlpatterns = [
    path('', views.loginPage, name='loginpage'),
    path('logout/', views.logoutUser, name='logout'),
    path('loginuser/', views.loginUser, name='loginuser'),
]