from django.db import models
from admin_master.models import *

# # Create your models here.
# class EmployeeReg(models.Model):


class  EmployeeDesignation(models.Model):
    empid=models.ForeignKey('EmployeeRegistration', on_delete=models.CASCADE)
    designationid=models.ForeignKey(Designation,on_delete=models.CASCADE)
    fromdate=models.DateField()
    todate=models.DateField(null=True,blank=True)

class EmpSalary(models.Model):
     empid=models.ForeignKey('EmployeeRegistration', on_delete=models.CASCADE)
     salary=models.DecimalField(max_digits=10, decimal_places=2)
     fromdate=models.DateField()
     todate=models.DateField(null=True,blank=True)

class Department_employee(models.Model):
     deptid= models.ForeignKey(Department,on_delete=models.CASCADE)
     empid=models.ForeignKey('EmployeeRegistration',on_delete=models.CASCADE)
     fromdate=models.DateField()
     todate=models.DateField(null=True,blank=True)




class EmployeeRegistration(models.Model):
    empcatid= models.ForeignKey(Employee,on_delete=models.CASCADE)
    empname = models.CharField(max_length=255)
    EMP_GENDER=[
        (1,'Male'),
        (2,'Female'),
        (3, 'Non-binary'),
        (4, 'Other'),
       

    ]
    gender=models.IntegerField(choices=EMP_GENDER)
    dob = models.DateField()
    mob = models.PositiveIntegerField()
    email = models.EmailField()
    address = models.TextField()
    jdate = models.DateField()
    deptid= models.ForeignKey(Department,on_delete=models.CASCADE)
    desid= models.ForeignKey(Designation,on_delete=models.CASCADE)
    qualid= models.ForeignKey(Qualification,on_delete=models.CASCADE)
    salary =models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='employees_photos/', blank=True, null=True)
    barcode=models.ImageField(upload_to='barcode/',blank=True, null=True)
    status=models.IntegerField(default=1)

class scd(models.Model):
    empid=models.ForeignKey('EmployeeRegistration',on_delete=models.CASCADE)
    classid=models.ForeignKey(adminClass,on_delete=models.CASCADE)
    divid= models.ForeignKey(Division,on_delete=models.CASCADE)
    subid=models.ForeignKey(Subject,on_delete=models.CASCADE)

