from rest_framework import serializers
from dataclasses import fields
from pyexpat import model
from .models import *


class Userserializer (serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
