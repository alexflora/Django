from django.db import models
from configration .models import *
from django.forms import ValidationError
import datetime
import re
#from phonenumber_field.modelfields import PhoneNumberField


class Department(models.Model):
    Name=models.CharField("Department",max_length=255,null=True,blank=False)
    code=models.CharField("Dep_Code",max_length=100,null=True,blank=False)

    def __str__(self):
        return self.Name
    
class Staff(models.Model):
    Name=models.CharField("Name",max_length=255,null=True,blank=False)
    Age=models.IntegerField("Age",null=True,blank=False)
    Gender=models.CharField("Gender",choices=[('Male','Male'),('Female','Female')],max_length=100,null=True,blank=False)
    birthdate=models.DateField("DOB",null=True,blank=False)
    Qualification=models.CharField("Qualification",max_length=255,null=True,blank=False)
    Phone=models.BigIntegerField("Phone",null=True,blank=False)
    email=models.EmailField(verbose_name="Email",default="asdf@gmail.com")
    knownLanguage=models.ManyToManyField(Language)
    Language=models.ForeignKey(Language,verbose_name="Mother Language",on_delete=models.SET_NULL,null=True,blank=False,related_name="Lang")
    department=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,blank=False)
    country=models.ForeignKey(Country,on_delete=models.CASCADE,null=True,blank=True)
    state=models.ForeignKey(State,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.Name + "-"+str(self.state.state)

class Student(models.Model):
    Name=models.CharField("Name",max_length=255,null=True,blank=False)
    Age=models.IntegerField("Age",null=True,blank=False)
    Gender=models.CharField("Gender",choices=[('Male','Male'),('Female','Female')],max_length=100,null=True,blank=False)
    birthdate=models.DateField("DOB",null=True,blank=False)
    Phone=models.BigIntegerField("Phone",null=True,blank=False)
    #phone=PhoneNumberField()
    email=models.EmailField("Email")
    department=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,blank=True)
    MotherLanguage=models.ForeignKey(Language,verbose_name="Language",on_delete=models.SET_NULL,null=True,related_name="Lang1",blank=False)
    knownLanguage=models.ManyToManyField(Language)
    country=models.ForeignKey(Country,on_delete=models.CASCADE,null=True,blank=True)
    state=models.ForeignKey(State,on_delete=models.CASCADE,null=True,blank=True)
    image=models.ImageField("Photo",upload_to='image/',null=True,blank=True)
    #slug=models.SlugField(null=True,blank=True,max_length=255)

    def __str__(self):
        return self.Name


    class Meta:
        verbose_name_plural='Student'
        ordering=('-Name',)
    
    
    # def clean(self):
    #     if(self.birthdate)>(datetime.date.today()):
    #         raise ValidationError("Please Enter valid date")
        
    #     if self.Age<25:
    #         print("Eligible")
    #     else:
    #         raise ValidationError("Age between 1 to 25")
        
        
    #     """if (self.Phone) and re.match('[6-9]{1}[0-9]{9}',self.Phone)==None:
    #         print("sucess")
    #     else:
    #         raise ValidationError("Please Enter the valid Phone Number")"""
        
    #     return super().clean()
    
    # def save(self):
    #     self.Name=self.Name.capitalize()
        
            
 
  
# Create your models here.
