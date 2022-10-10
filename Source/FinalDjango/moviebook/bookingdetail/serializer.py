from rest_framework import serializers
from dataclasses import fields
from .models import *


class Bookingserializer (serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['branch'] = {"id": instance.branch.id if instance.branch else '',
                         "name": instance.branch.name if instance.branch else ''}
        res['movie'] = {"id": instance.movie.id,
                        "name": instance.movie.name}
        res['hall'] = {"id": instance.hall.id,
                       "name": instance.hall.name}
        res['halltype'] = {"value": instance.halltype,
                           "label": instance.get_halltype_display()}
        # res['status'] = instance.status.name
        return res


class Statusserializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class Paymentserializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['name'] = {"id": instance.name.id,
                       "name": instance.name.customername}
        res['moviename'] = instance.name.movie.name
        res['hall'] = instance.name.hall.name
        res['halltype'] = instance.name.halltype
        res['noofseats'] = instance.name.noofseats
        res['amount'] = instance.name.totalamount
        res['type'] = {"value": instance.type,
                       "label": instance.get_type_display()}
        return res


class Customerserializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'dob', 'age', 'gender',
                  'phone', 'email', 'address')

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['gender'] = {"value": instance.gender,
                         "label": instance.get_gender_display()}
        return res
