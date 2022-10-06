from rest_framework import serializers
from.models import *

class staffserializers(serializers.ModelSerializer):
    class Meta:
        model=Staff
        fields='__all__'

class Countryserializers(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields='__all__'
                