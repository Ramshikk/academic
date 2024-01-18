from django.db import models

# Create your models here.
class Department(models.Model):
    depname=models.CharField(max_length=200)
    depcode=models.CharField(max_length=200)
    status=models.IntegerField(default=1)

class Designation(models.Model):
    desname=models.CharField(max_length=200,blank=False, null=False)
    descode=models.CharField(max_length=200,blank=False, null=False)
    status=models.IntegerField(default=1)

class Division(models.Model):
    divname=models.CharField(max_length=200,blank=False, null=False)
    status=models.IntegerField(default=1)
    
class adminClass(models.Model):
    clsname=models.CharField(max_length=200,blank=False, null=False)
    status=models.IntegerField(default=1)


class Qualification(models.Model):
    qualname=models.CharField(max_length=200,blank=False, null=False)
    status=models.IntegerField(default=1)



class Employee(models.Model):
    EMPLOYEE_CATEGORY_CHOICE=[
    (1,'Accountant'),
    (2,'Teacher'),
    (3,'cafteria'),
    (4,'Librarian'),
    (5,'Others')
]
    empname=models.CharField(max_length=200,blank=False, null=False)
    emparea=models.IntegerField(choices=EMPLOYEE_CATEGORY_CHOICE)
    status=models.IntegerField(default=1)

class Subject(models.Model):
    subjectname=models.CharField(max_length=200,blank=False, null=False)
    status=models.IntegerField(default=1)
    
class SujectClass(models.Model):
     classid=models.ForeignKey('adminClass', on_delete=models.CASCADE)
     sujectid=models.ForeignKey('Subject', on_delete=models.CASCADE)
    
    