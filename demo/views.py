from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.db.models import Q


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

# def products(request):
#     productData = [
#         {"name":"iphon1","price":1200,"qty":1,"color":"blue"},
#         {"name":"ipad ","price":1000,"qty":2,"color":"silver"},
#         {"name":"charger","price":200,"qty":2,"color":"black"},
#         {"name":"laptop","price":700,"qty":4,"color":"black"},
#     ]
#     return render(request,"demo/productList.html",{'products':productData})

def getProducts(request):
    
    #select * from product;
    #ModelName.Objects.all()
    #products = Product.objects.all().values_list()
    #print(f"Products: {products}")
    # product = Product.objects.get(pk=1)
    # print(f"Product: {product.id} {product.name} {product.price} {product.stock} {product.color} {product.status} {product.ratings}")
    
    #select * from product where status = true;
    # products = Product.objects.filter(status = False).values()
    # print(f"Products: {products}")
    # products = Product.objects.filter(status = True,stock=1000).values()
    # print(f"Products: {products}")
    #orderby
    
    # products  = Product.objects.all().order_by('-stock').values()
    # print(f"Products: {products}")
    #[1:8:3]
    #limit
    #products = Product.objects.all()[:1].values()
    #products = Product.objects.all().values_list('name','price')
    #products = Product.objects.all().exclude(field_name="color").values()
    #print(f"Products: {products}")
    
    #lookups
    #products = Product.objects.filter(name__contains="t").values()
    #products = Product.objects.filter(name__icontains="t").values()
    #products = Product.objects.filter(name__startswith="t").values()
    #products = Product.objects.filter(price__gt=1200).values()
    #products = Product.objects.filter(price__gte=1200).values()
    #products = Product.objects.filter(color__in=["silver","blue"]).values('name')
    #range
    #products = Product.objects.filter(price__range=(800,1200)).values('name')
    
    # true &
    # false |
    #or condiotns
    products = Product.objects.filter(Q (name = "abc") | Q(name__contains="t") & Q(price__gte=100)).values('name')
    #products = Product.objects.filter(~Q (name__contains="t")).values('name')
    
    print(f"Products: {products}")
    
    
    return HttpResponse("Products fetch successfully..")