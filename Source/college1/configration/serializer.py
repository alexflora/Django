from dataclasses import fields
from rest_framework import serializers
from .models import *


class Stateserializers (serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class Countryserializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
