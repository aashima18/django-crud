
from django.db import models

class Dept(models.Model):
    Dept_name=models.CharField(max_length=20)
    def __str__(self):
        return self.Dept_name



  
    
class Employee(models.Model):
    dept=models.ForeignKey(Dept,on_delete=models.CASCADE)
    First_name=models.CharField(max_length=30)
    emp_desg=models.CharField(max_length=50)   
    objects=models.Manager() 
    def __str__(self):
        return self.First_name

