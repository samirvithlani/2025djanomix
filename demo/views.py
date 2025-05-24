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

def studentList(request):
    # students ={
    #     "students":["amit","raj","kunal","shyam","ram","hari"]
    # }
    #students = ["amit","raj","kunal","shyam","ram","hari"]
    students = []
    return render(request,"demo/studentlist.html",{'students':students})

def products(request):
    productData = [
        {"name":"iphon1","price":1200,"qty":1,"color":"blue"},
        {"name":"ipad ","price":1000,"qty":2,"color":"silver"},
        {"name":"charger","price":200,"qty":2,"color":"black"},
        {"name":"laptop","price":700,"qty":4,"color":"black"},
    ]
    return render(request,"demo/productList.html",{'products':productData})