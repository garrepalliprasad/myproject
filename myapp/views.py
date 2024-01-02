from django.shortcuts import render,redirect
from .forms import DepartmentForm
from .models import Department,Faculty
# Create your views here.

def create_department(request):
    form=DepartmentForm()
    if request.method=='POST':
        form=DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show-departments')
    context={'form':form}
    return render(request,'create-department.html',context)

def show_departments(request):
    departments=Department.objects.all()
    context={'departments':departments}
    return render(request,'show-departments.html',context)

def update_department(request,pk):
    department=Department.objects.get(id=pk)
    form=DepartmentForm(instance=department)
    if request.method=='POST':
        print(request.POST)
        form=DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show-departments')
    context={'form':form}
    return render(request,'update-department.html',context)

def delete_department(request,pk):
    department=Department.objects.get(id=pk)
    if request.method=='POST':
        department.delete()
        return redirect('show-departments')
    context={'department':department}
    return render(request,'delete-department.html',context)