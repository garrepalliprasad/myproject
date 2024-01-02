from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    dob=models.DateTimeField(auto_now_add=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)




