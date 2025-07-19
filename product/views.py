from django.shortcuts import render
from .forms import ProductForm,PhoneForm
from .models import Product

# Create your views here.

def createProduct(request):
    productForm = ProductForm()
    if request.method == "POST":
        print("form subbmited....")
        form = ProductForm(request.POST)
        if  form.is_valid():
            print("form is valid...")
            print(form.cleaned_data)
            #save...
            product = Product(**form.cleaned_data)
            # product.name = form.cleaned_data["name"]
            # product.description = form.cleaned_data["description"]
            # product.price = form.cleaned_data["price"]
            # product.stock = form.cleaned_data["stock"]        
            
            product.save()
            print("product created successfully...")

    return render(request,"product/createProduct.html",{"form": productForm})
    

def createPhoneView(request):
        phoneForm = PhoneForm()
        
        if request.method == "POST":
            form = PhoneForm(request.POST)
            #print(form.data["brand"])
            if form.is_valid():
                print(form.cleaned_data)
                form.save()
            
        
        return render(request,"product/createPhone.html",{"form":phoneForm})
    
    