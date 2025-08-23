from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path("createProduct/",views.createProduct),
    path("createPhone/",views.createPhoneView),
    path("createContact/",views.createContactView),
    path("createcar/",views.carCreateView),
    path("carlist",views.carListView)
]
