from rest_framework import viewsets
import imp
from django.shortcuts import render
from .models import *
from .serializers import *
# Create your views here.


class personalview(viewsets.ModelViewSet):
    queryset = personal.objects.all()
    serializer_class = personalserializers


class countryview(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = countryserializers


class languageview(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = languageserializers
