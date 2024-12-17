from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_name=models.CharField(max_length=50)
    emp_department=models.CharField(max_length=50)

class Leave(models.Model):
    employee_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    leave_type=models.CharField(max_length=20)
    start_date=models.DateField()
    end_date=models.DateField()
    status=models.CharField(max_length=10)

