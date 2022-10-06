from rest_framework import serializers
from .models import *


class bookseriazlier(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
