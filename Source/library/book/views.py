from rest_framework import viewsets
from django.shortcuts import render
from .serializers import *


class bookview (viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = bookseriazlier

# Create your views here.
