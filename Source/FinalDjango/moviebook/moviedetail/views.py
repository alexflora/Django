from django.shortcuts import render

from rest_framework import viewsets
from .serializer import *
from .models import *


class moviewview (viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = movieserializer


class Languageview(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = Languageserializer


class Showview(viewsets.ModelViewSet):
    queryset = Show.objects.all()
    serializer_class = Showserializer

# Create your views here.

# Create your views here.
