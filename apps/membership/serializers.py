from rest_framework import serializers
from .models import MbrCommon,MbrBase,MbrInc

class MbrCommonSerializers(serializers.ModelSerializer):
    class Meta:
        model = MbrCommon
        fields="__all__"

class MbrIncSerializers(serializers.ModelSerializer):
    class Meta:
        model = MbrInc
        fields="__all__"