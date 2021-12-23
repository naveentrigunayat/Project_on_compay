from django.db import models
from django.db import connections
 

# Create your models here.

class Designation(models.Model):
    id = models.AutoField(primary_key=True)
    designation_id = models.CharField(max_length=20) 
    designation_name = models.CharField(max_length=20)


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    department_id = models.CharField(max_length=20) 
    department_name = models.CharField(max_length=25)


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    eid = models.CharField(max_length=25) 
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=20)
    eemail= models.EmailField(max_length=25)
    eage = models.CharField(max_length=25)
    edob = models.DateTimeField()
    edoj = models.DateTimeField()
    esalary = models.DecimalField(max_digits=20, decimal_places=2)
    edesignation = models.ForeignKey("Designation",on_delete=models.DO_NOTHING)
    edepartment = models.ForeignKey("Department",on_delete=models.DO_NOTHING)