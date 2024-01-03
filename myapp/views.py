from django.shortcuts import render,redirect
from .forms import DepartmentForm,FacultyForm
from .models import Department,Faculty
# Create your views here.

def index(request):
    return render(request,'index.html')

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

def update_department(request,id):
    department=Department.objects.get(id=id)
    form=DepartmentForm(instance=department)
    if request.method=='POST':
        form=DepartmentForm(request.POST,instance=department)
        if form.is_valid():
            form.save()
            return redirect('show-departments')
    context={'form':form}
    return render(request,'update-department.html',context)

def delete_department(request,id):
    department=Department.objects.get(id=id)
    if request.method=='POST':
        department.delete()
        return redirect('show-departments')
    context={'department':department}
    return render(request,'delete-department.html',context)

def show_faculties(request):
    faculties=Faculty.objects.all()
    context={'faculties':faculties}
    return render(request,'show-faculties.html',context)

def create_faculty(request):
    form=FacultyForm()
    if request.method=='POST':
        form=FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show-faculties')
    context={'form':form}
    return render(request,'create-faculty.html',context)

def update_faculty(request,id):
    faculty=Faculty.objects.get(id=id)
    form=FacultyForm(instance=faculty)
    if request.method=='POST':
        form=FacultyForm(data=request.POST,instance=faculty)
        if form.is_valid():
            form.save()
            return redirect('show-faculties')
    context={'form':form}
    return render(request,'update-faculty.html',context)

def delete_faculty(request,id):
    faculty=Faculty.objects.get(id=id)
    if request.method=='POST':
        faculty.delete()
        return redirect('show-faculties')
    context={'faculty',faculty}
    return render(request,'delete-faculty.html')