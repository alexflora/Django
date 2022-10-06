from dataclasses import fields
from rest_framework import serializers
from .models import *


class Branchserializers (serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['theatername'] = instance.theatername.name
        res['movieName'] = instance.movieName.name
        return res


class Theraterserializer(serializers.ModelSerializer):
    class Meta:
        model = Theater
        fields = '__all__'


class Hallserializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = '__all__'


class Roleserializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['role'] = instance.role.name
        res['branch'] = instance.branch.name
        res['gender'] = {"value": instance.gender,
                         "label": instance.get_gender_display()}
        return res
