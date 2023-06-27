from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.db.models import *


# Create your views here.



def adddepartment(request):
    form = departmentForm()
    if request.method == 'POST':
        form = departmentForm(request.POST)
        if form.is_valid():
             form.save()
             messages.success(request,"New Department has been added successfully")
             return redirect('showdept')
        
    return render(request,'adddept.html',{'form': form})


def showdepartment(request):
    dept = department.objects.all()
    messages.success(request,"Here's all your Department Details")
    return render(request,"showdept.html",{'dept':dept})
    
    

def updatedepartment(request,id):
    dept = department.objects.get(id=id)
    form = departmentForm(instance=dept)
    
    if request.method == 'POST':
        form = departmentForm(request.POST,instance=dept)
        if form.is_valid():
             form.save()
             messages.success(request,"Department details has been Updated successfully")
        
    return render(request,'adddept.html',{'form': form})
    
    
    
def deletedepartment(request,id):
    try:
        dept = department.objects.get(id=id)
        
    except:
        {'msg':"Record NOT FOUND"}
        
    else :
        
        dept.delete()
        messages.success(request,"Department has been deleted successfully")
        return redirect('showdept')
    
    
   #for employee 
    
    
def addemployee(request):
    form = employeeForm()
    if request.method == 'POST':
        form = employeeForm(request.POST)
        if form.is_valid():
             form.save()
             messages.success(request,"Employee has been added successfully")
             return redirect("showemp")

    messages.success(request,"Welcome to HL Company portal")   
    return render(request,'addemp.html',{'form': form})




def showemployee(request):
    emp = employee.objects.all()
    messages.success(request,"here's all your employee details")
    return render (request,"showemp.html",{'emp':emp})
   
   
def updateemployee(request,id):
    emp = employee.objects.get(id=id)
    form = employeeForm(instance=emp)
    if request.method =='POST':
            form = employeeForm(request.POST,instance=emp)
            if form.is_valid():
                form.save()
                messages.success(request,"Employee data has been Updated successfully")
                return redirect('showemp')
        
    
    return render(request,"addemp.html",{'form': form})




def deleteemployee(request,id):
    try:
        emp = employee.objects.get(id=id)
    except:
        {'msg':"No Matching Record Found"}
    else:
        emp.delete()
        messages.success(request,"The record has been deleted successfully")
        return redirect('showemp')
    
    
    
def filter(request):
    if request.method=='POST':
        search = request.POST['search']
        emp = employee.objects.all()
        if search is not None:
            emp =  employee.objects.filter(Q(name__icontains=se)|Q(department__contains =se))
        if search:
            emp =employee.objects.filter(id__contains=se).order_by('id')
        if search:
            emp =employee.objects.filter(department__contains=se).order_by('department')
        else:
            messages.success(request,"Theres No such matching Record")
        
        return render(request,'showemp.html', {'emp':emp})
    else:
        messages.success(request,"You can't access filter")
    





