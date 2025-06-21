from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #localhost:8000/demo/home
    path("home/",views.Home),
    path("aboutus/",views.aboutUs),
    path("contactus/",views.contactUs),
    path("studentlist/",views.studentList),
    path("productlist/",views.getProducts),
    path("swiggyuser/",views.getSwiggyUser),
    path("teams/",views.getTeams),
    path("students/",views.getStudentDetail),
    
]
