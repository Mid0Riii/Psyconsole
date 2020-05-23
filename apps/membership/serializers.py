from rest_framework import serializers
from .models import MbrCommon,MbrBase

class MbrCommonSerializers(serializers.ModelSerializer):
    class Meta:
        model = MbrCommon
        fields="__all__"