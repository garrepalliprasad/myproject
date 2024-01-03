from django.db import models
from datetime import date
from django import forms

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    doj=models.DateField(default=date.today(),null=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    




