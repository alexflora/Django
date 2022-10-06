from rest_framework import serializers
from.models import *
from datetime import datetime,date


class Studentserializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
     
    def to_representation(self, instance):
        res=super().to_representation(instance)
        res['MotherLanguage']=[instance.MotherLanguage.id,instance.MotherLanguage.Lan]
        res['Age']=date.today().year-datetime.strptime(res['birthdate'],"%Y-%m-%d").year
        res['birthdate']=datetime.strptime(res['birthdate'],"%Y-%m-%d").strftime("%B-%Y")
        res['country']=[instance.country.id,instance.country.country]
        lt=[]
        languages=res['knownLanguage']
        for lang in languages:
            lang_id=instance.knownLanguage.all().get(id=lang)
            dt={"id":lang_id.id,"name":lang_id.Lan}
            lt.append(dt)
        
        res['knownLanguage']=lt 
        return res
        
    
