from statistics import mode
from django.db import models

class Domains(models.Model):
    name=models.CharField("Domain_Name",max_length=255,null=True,blank=False)
    code=models.CharField("D_code",max_length=255,null=True,blank=False)
    
    def __str__(self):
        return self.name

class Hr_domain(models.Model):
    name=models.CharField("Name",max_length=255,null=True,blank=False)
    gender=models.CharField("Gender",choices=[('Male','Male'),('Female','Female')],max_length=20,null=True,blank=False)
    age=models.IntegerField("Age",null=True,blank=True)
    Domains=models.ForeignKey(Domains,on_delete=models.SET_NULL,null=True,blank=False)
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField("Name",max_length=255,null=True,blank=False)
    gender=models.CharField("Gender",choices=[('M','Male'),('F','Female')],max_length=20,null=True,blank=False)
    age=models.IntegerField("Age",null=True,blank=True)
    Domains=models.ForeignKey(Domains,on_delete=models.SET_NULL,null=True,blank=True)
    Hr=models.ForeignKey(Hr_domain,on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class workers(models.Model):
    name=models.CharField("Name",max_length=255,null=True,blank=False)
    gender=models.CharField("Gender",choices=[('M','Male'),('F','Female')],max_length=20,null=True,blank=False)
    age=models.IntegerField("Age",null=True,blank=True)
    Domains=models.ForeignKey(Domains,on_delete=models.SET_NULL,null=True,blank=True) 
    
    
    def __str__(self):
        return self.name

    
# Create your models here.
