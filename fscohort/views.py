from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.

def home(request):
    return render(request, "fscohort/home.html")


def student_list(request):
<<<<<<< HEAD
    students = Student.objects.all()
    context = {
        "students": students,
    }
    return render(request, "fscohort/student_list.html", context)
    
def student_add(request):
    pass
def student_detail(request):
    pass
def student_update(request):
    pass
=======
    
    students = Student.objects.all()
    
    context = {
        "students":students
    }
    
    return render(request, "fscohort/student_list.html", context)

def student_add(request):
    pass

def student_detail(request):
    pass

def student_update(request):
    pass

>>>>>>> 93d9cb5b57871a4c6a94dcc1709c65b56f3514fe
def student_delete(request):
    pass