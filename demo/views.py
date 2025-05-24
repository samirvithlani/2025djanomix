from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return HttpResponse("HOME")

def aboutUs(request):
    company ={
        "name":"TCS",
        "FOUNDER":"TATA",
        "YEAR":2000
    }
    return render(request,"aboutus.html",{'company':company})

def contactUs(request):
    user = {
        "name":"Amit",
        "age":25,
        "city":"Ahemdabad",
        "salary":25800
    }
    return render(request,"demo/contactus.html",{"user":user})