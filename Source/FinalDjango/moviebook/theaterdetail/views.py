from rest_framework import viewsets
from .serializer import *
from .models import *


class Branchview (viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = Branchserializers


class Theaterview(viewsets.ModelViewSet):
    queryset = Theater.objects.all()
    serializer_class = Theraterserializer


class Hallview(viewsets.ModelViewSet):
    queryset = Hall.objects.all()
    serializer_class = Hallserializer


class Roleview(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = Roleserializer


class Employeeview(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer


# Create your views here.
