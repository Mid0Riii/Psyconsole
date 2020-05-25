from rest_framework import serializers
from .models import MbrCommon,MbrBase,MbrInc

class MbrCommonSerializers(serializers.ModelSerializer):
    class Meta:
        model = MbrCommon
        # fields="__all__"
        exclude = ['mbse_status','mbse_judge','mbse_code','mbse_exp']

class MbrIncSerializers(serializers.ModelSerializer):
    class Meta:
        model = MbrInc
        # fields="__all__"
        exclude = ['mbse_user','mbse_status','mbse_judge','mbse_code','mbse_exp']
