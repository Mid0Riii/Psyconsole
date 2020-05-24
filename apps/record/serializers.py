from rest_framework import serializers
from .models import Audit,Activity,Diary

class AuditSerializers(serializers.ModelSerializer):
    class Meta:
        model = Audit
        fields = "__all__"

class DiarySerializers(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = "__all__"

class ActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"
