from rest_framework import serializers
from .models import MbrCommon, MbrBase, MbrInc


class MbrCommonSerializers(serializers.ModelSerializer):
    class Meta:
        model = MbrCommon
        fields = "__all__"
        read_only_fields = ['mbse_status', 'mbse_judge', 'mbse_code', 'mbse_exp']


class MbrIncSerializers(serializers.ModelSerializer):
    class Meta:
        model = MbrInc
        fields = "__all__"
        # 只读字段
        read_only_fields = ['mbse_status', 'mbse_judge', 'mbse_code', 'mbse_exp']


class MbrAvatarSerializers(serializers.ModelSerializer):
    class Meta:
        model = MbrCommon
        fields = ['id', 'mbr_avatar']

    def create(self, validated_data):
        print(validated_data)
        return MbrCommon.objects.create(**validated_data)
