from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path("createemployee/",views.createEmployee,name="create_employee"),
    path("listemployee/",views.list_Employee,name="list_employee"),
    path("deleteemployee/<int:pk>/",views.delete_employee,name="delete_employee"),
    path("updateemployee/<int:pk>/",views.update_employee,name="update_employee"),
]