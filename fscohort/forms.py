<<<<<<< HEAD
from django import forms
from .models import Student
from django.forms import fields
=======
from django import  forms
from django.forms import fields
from .models import Student

>>>>>>> c77fcfcc5a93b394af36cd26e844a69ed322219d

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"