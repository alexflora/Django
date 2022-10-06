from rest_framework import viewsets
from django.shortcuts import render
from .serializer import *
from .models import *


class StateView (viewsets.ModelViewSet):
    serializer_class = Stateserializers
    queryset = State.objects.all()


class CountryView (viewsets.ModelViewSet):
    serializer_class = Countryserializers
    queryset = Country.objects.all()


# Create your views here.
