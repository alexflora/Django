from django.db import models
class Authour (models.Model):
    name=models.CharField("Name",max_length=255,null=True,blank=False)
    code=models.CharField("Code",max_length=200,null=True,blank=False)

    def __str__(self):
        return self.name


class Book (models.Model):
    Name=models.CharField("Name",max_length=200,null=True,blank=False)
    code=models.CharField("code",max_length=200,null=True,blank=False)
    authour=models.OneToOneField(Authour,on_delete= models.CASCADE,null=True,blank=False)

    def __str__(self):
        return self.Name

# Create your models here.
 