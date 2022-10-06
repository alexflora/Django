from django.db import models
class student (models.Model):
    name=models.CharField("Name",max_length=255,null=True,blank=False)
    age=models.IntegerField("Age",null=True,blank=False)
    gender=models.CharField("Gender",choices=[('Male','Male'),('Female','Female')],max_length=7,null=True)
    date=models.DateField()
    time=models.TimeField(null=True)
    datetime=models.DateTimeField(null=True)
    duration=models.DurationField()
    floats=models.FloatField(null=True)
    text=models.TextField()
    
# Create your models here.
