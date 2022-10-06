from django.urls import clear_script_prefix
from rest_framework import serializers
from dataclasses import fields
from .models import *


class movieserializer (serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def to_representation(self, instance):
        res = super().to_representation(instance)
        st = []
        shows = res['show']
        for show in shows:
            showid = instance.show.all().get(id=show)
            dt = {'id': showid.id, 'name': showid.name}
            st.append(dt)
        res['show'] = st

        lt = []
        language = res['language']
        for lan in language:
            languageid = instance.language.all().get(id=lan)
            dt = {'id': languageid.id, 'name': languageid.name}
            lt.append(dt)
        res['language'] = lt

        return res


class Languageserializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class Showserializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = '__all__'
