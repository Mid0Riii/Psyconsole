from rest_framework import serializers
from .models import Audit,Activity,Diary

class AuditSerializers(serializers.ModelSerializer):
    class Meta:
        model = Audit
        fields = "__all__"
    read_only_fields=['audit_status','relate_activity','audit_user']

class DiarySerializers(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = "__all__"
    #TODO codeview ModelSerializer中使用read_only_fields
    read_only_fields=['related_act','related_user','diary_title','diary_date','diary_loc','diary_method']

class ActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"
