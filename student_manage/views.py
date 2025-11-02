from django.shortcuts import render, HttpResponse
from .models import Student
from .forms import StudentInfoForm
from django.http import HttpResponseRedirect
from django.db.models import Q


# Create your views here.

def list_student(request):
    student=Student.objects.all()
    return render(request, 'curd/list_student.html',{"student": student})

def update_student(request,id):
    if request.method=="POST":
        student=Student.object.get(pk=id)
        fm=StudentInfoForm(request.POST,instance=student)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
        else:
            student=Student.objects.get(pk=id)
            fm=StudentInfoForm(instance=student)
        return render(request, "curd/update_student.html",{"form": fm})
    

def delete_student(request,id):
    if request.method=="POST":
        student=Student.object.get(pk=id)
        student.delete()
        return HttpResponseRedirect("/")


def add_student(request):
    if request.method=="POST":
        fm=StudentInfoForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
    else:
        fm=StudentInfoForm()
    return render(request, "curd/add.html",{"form":fm})


def search_student(request):
    if request.method=="POST":
        search=request.POST.get("output")
        print(search)
        student=Student.objects.all()
        std=None
        if search:
            std=student.filter(
                Q(fname_icontains=search)|
                Q(lname_icontains=search)|
                Q(email_icontains=search)|
                Q(phone_icontains=search)|
                Q(branch_icontains=search))
            print(std.count())
        
        return render(request,"curd/list_student.html",{"student": std})
    else:
        return HttpResponse("An error occurred")
