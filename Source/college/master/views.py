from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import *
from .form import DepartmentForm
from rest_framework import viewsets
from.serializers import *


"""def department_view(request):
    data = Department.objects.all()
    return render(request, 'master/department/department_list.html', {'data': data})


def department_create(request):
    if request.method == 'POST':
        dept = Department(name=request.POST['name'], code=request.POST['code'])
        dept.save()
        return HttpResponseRedirect('/master/department')
    return render(request, 'master/department/department_create.html')


def department_update(request, id=None):
    rec_id = Department.objects.get(id=id)
    if request.method == 'POST':
        rec_id.name = request.POST['name']
        rec_id.code = request.POST['code']
        rec_id.save()
        return HttpResponseRedirect('/master/department')
    return render(request, 'master/department/department_update.html', {'rec': rec_id})


def department_delete(request, id=None):
    if id:
        rec_id = Department.objects.get(id=id)
        rec_id.delete()
    return HttpResponseRedirect('/master/department')"""

"""def staff_view(request):
    data = Staff.objects.all()
    return render(request,'master/staff/staff_list.html', {'data': data})

def staff_create(request):
    if request.method == 'POST':
        sta = Staff(name=request.POST['name'], staff_code=request.POST['code'], gender=request.POST['gender'])
        sta.save()
        return HttpResponseRedirect('/master/staff')
    return render(request, 'master/staff/staff_create.html')

def staff_update(request, id=None):
    rec_id = Staff.objects.get(id=id)
    if request.method == 'POST':
        rec_id.name = request.POST['name']
        rec_id.staff_code = request.POST['code']
        rec_id.gender=request.POST['gender']
        rec_id.save()
        return HttpResponseRedirect('/master/staff')
    return render(request, 'master/staff/staff_update.html', {'rec': rec_id})

def staff_delete(request, id=None):
    if id:
        rec_id = Staff.objects.get(id=id)
        rec_id.delete()
    return HttpResponseRedirect('/master/staff')"""
    
    
class staffview(viewsets.ModelViewSet):
    queryset=Staff.objects.all()
    serializer_class=staffserializers
    
class countryview(viewsets.ModelViewSet):
    queryset=Country.objects.all()
    serializer_class=Countryserializers

    
    
    