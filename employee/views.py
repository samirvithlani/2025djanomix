from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.

def createEmployee(request):
    form = forms.EmployeeForm()
    if request.method =="POST":
        form =forms.EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_employee')
        else:
            form = forms.EmployeeForm()
            
    return render(request,"employee/employee_create.html",{"form":form})        


def list_Employee(request):
    employees = models.Employee.objects.all().values()
    return render(request,"employee/list_employee.html",{"employees":employees})


def delete_employee(request,pk):
    print(f"pk {pk}")
    employee = models.Employee.objects.get(id=pk)
    print(employee)
    if request.method =="POST":
        employee.delete()
        #if 
        return redirect("list_employee")
    
    return render(request,"employee/delete_confirm.html",{"employee":employee})         