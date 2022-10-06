from dataclasses import fields
from rest_framework import serializers
from .models import *


class personalserializers(serializers.ModelSerializer):
    class Meta:
        model = personal
        fields = '__all__'

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result['country'] = {"id": instance.country.id,
                             "name": instance.country.name}
        result['gender'] = {"value": instance.gender,
                            "label": instance.get_gender_display()}
        return result


class countryserializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class languageserializers(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
