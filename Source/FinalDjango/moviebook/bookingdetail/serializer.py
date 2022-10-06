from rest_framework import serializers
from dataclasses import fields
from .models import *


class Bookingserializer (serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['coustomername'] = {"id": instance.coustomername.id,
                                "Name": instance.coustomername.name}
        res['branch'] = instance.branch.name
        res['movie'] = instance.movie.name
        res['hall'] = instance.hall.name
        res['status'] = instance.status.name
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
        res['name'] = instance.name.customername.name
        res['amount'] = instance.name.totalamount
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
