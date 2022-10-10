from dataclasses import fields
from rest_framework import serializers
from .models import *


class Branchserializers (serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['theatername'] = {"id": instance.theatername.id if instance.theatername else '',
                              "name": instance.theatername.name if instance.theatername else ''}
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
        res['role'] = {"id": instance.role.id,
                       "value": instance.role.name}
        res['branch'] = {"id": instance.branch.id,
                         "value": instance.branch.name}
        res['gender'] = {"value": instance.gender,
                         "label": instance.get_gender_display()}
        return res
