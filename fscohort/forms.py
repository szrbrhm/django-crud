from django import forms
from .models import Student
from django.forms import fields

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"