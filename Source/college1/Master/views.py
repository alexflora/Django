from django.shortcuts import render,HttpResponse
from.models import *
import datetime
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from.serializers import *

def test(request):
    date=datetime.datetime.now()
    #return HttpResponse("<h1>Hello world</h1>")
    return render(request,"index.html",{"name":"Alexander"})

def table(request):
    #---------------filter methods------------------------------------
    #student=Student.objects.filter(Name='test').values()---particular record
    #student=Student.objects.filter(Name='willson',id=1).values() --AND condition is used here separated by comma
    #student=Student.objects.filter(Name='test').values()| Student.objects.filter(Name='jesus').values() -----OR condition
    #student=Student.objects.filter(Name__istartswith='w').values()---print the record like starting letter
    #student=Student.objects.filter(Name__iendswith='r').values() ---print the record like ending the letter
    #student=Student.objects.filter(Name__in=['Alexander','test','Antony'])--use in keyword
    #student=Student.objects.filter(Age__gt=20)
    #student=Student.objects.filter(Age__gte=20)
    #student=Student.objects.filter(Age__lt=22)
    #student=Student.objects.filter(Age__lte=20)
    #student=Student.objects.filter(Age__range=(14,20))---range filter (should give start and end point)
    #student=Student.objects.filter(Name__range=('A','r'))--not working
    #student=Student.objects.order_by('Name')
    student=Student.objects.order_by('Name')
    return render(request,"masterdemo/index.html",{"Student":student})

def dep(request):
    return render(request,"masterdemo/dep.html")

   # hour=int(date.strftime())
    #if hour<12:
     #   text+="Good Morning"
    #else:
     #   text+="Goodofternoon"""
    # Create your views here.

class Studentview (viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=Studentserializers