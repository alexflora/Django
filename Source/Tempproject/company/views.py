from django.shortcuts import render
from.models import *
"""def base(request):
    return render(request,"base.html")"""

def domain(request):
    Dvalue=Domains.objects.all()
    return render(request,"Domain.html",{'values':Dvalue})
    
def HR(request):
    Hvalue=Hr_domain.objects.all()
    return render(request,"Hrdomain.html",{'values':Hvalue})

def employee(request):
    Evalue=Employee.objects.all()
    return render (request,"Employee.html",{'values':Evalue})

def worker(request):
    Wvalue=workers.objects.all()
    return render(request,"workers.html",{'values':Wvalue})

# Create your views here.
