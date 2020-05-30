from rest_framework import serializers
from .models import Audit,Activity,Diary

#TODO 问问前端能不能获取member
class AuditSerializers(serializers.ModelSerializer):
    class Meta:
        model = Audit
        fields = "__all__"
    read_only_fields=['audit_status','relate_activity','audit_user','audit_member']

class DiarySerializers(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = "__all__"
    #TODO codeview ModelSerializer中使用read_only_fields
    read_only_fields=['related_act','related_user','diary_title','diary_date','diary_loc','diary_method']

class ActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id','act_is_available','act_need_audit','act_title','act_date',
                  'act_loc','act_method','act_description','audit_status']
    audit_status = serializers.SerializerMethodField()

    def get_audit_status(self,obj):
        user = self.context['request'].user
        try:
            m = Audit.objects.get(relate_activity=obj,audit_user=user)
            return m.audit_status
        except Exception as e:
            return "您未申请该活动"


