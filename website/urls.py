from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path("service/",views.service,name='service'),
    path("aboutUs/",views.aboutUs,name='aboutUs'),
    path("contact/",views.contact,name='contact'),
    path("case/",views.case,name='case'),
    path("news/",views.news,name='news'),
]