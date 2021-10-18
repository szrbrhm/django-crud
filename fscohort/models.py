from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
<<<<<<< HEAD
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    
    GENDER = (
        ("1","Female"),
        ("2","Male"),
        ("3","Other"),
        ("4","Prefer Not Say"),
    )    
    gender = models.CharField(max_length=40, choices=GENDER)
=======
    email = models.EmailField(max_length=154)
    phone = models.CharField(max_length=50)
    
    GENDER =(
        ("1", "Female"),
        ("2", "Male"),
        ("3", "Other"),
        ("4", "Prefer Not Say"),   
    )
    
    gender = models.CharField(max_length=50, choices=GENDER)
>>>>>>> 93d9cb5b57871a4c6a94dcc1709c65b56f3514fe
    number = models.CharField(max_length=50)
    image = models.ImageField(upload_to="student/", default="avatar.png")
    
    def __str__(self):
<<<<<<< HEAD
        return (f"{self.number}-{self.first_name}")
=======
        return self.number + " " + self.first_name
    
    
    
    
    
>>>>>>> 93d9cb5b57871a4c6a94dcc1709c65b56f3514fe
