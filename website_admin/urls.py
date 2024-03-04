from django.urls import path, include
from . import views

urlpatterns = [
    path("custom-admin-login/",views.admin_login,name='admin_login'),
    path("register/",views.admin_register,name='admin_register'),
    path("logout/",views.logout,name='logout'),
]