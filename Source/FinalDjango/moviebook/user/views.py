from rest_framework import viewsets
from django.shortcuts import render
from .models import *
from .serializer import *


class Userview (viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = Userserializer

# Create your views here.
