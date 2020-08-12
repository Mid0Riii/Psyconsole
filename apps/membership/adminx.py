import xadmin
from django.utils.html import format_html
from .models import CommonAudit, SeniorAudit, CommonFormal, SeniorFormal, IncAudit, IncFormal, IncUnactived, \
    MbrUnactived, MbrCommon
from .layouts import MbrLayout, IncLayout
from .plugins import MbrJudgeButton
from xadmin.views import BaseAdminView
from django.forms import ModelForm, widgets
from django import forms
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from myauth.models import CustomUser


# @xadmin.sites.register(MbrCommon)
# class MbrCommonAdmin(object):
#     pass
class MemberResources(resources.ModelResource):
    class UserForeignWidget(ForeignKeyWidget):
        def get_queryset(self, value, row, *args, **kwargs):
            return CustomUser.objects.filter(
                username__iexact=row["mbse_user"]
            )

    mbse_user = fields.Field(
        attribute='mbse_user',
        column_name='mbse_user',
        widget=UserForeignWidget(CustomUser, 'username')
    )

    class Meta:
        model = MbrCommon
        import_id_fields = ('id',)
        # 导入数据时，如果该条数据未修改过，则会忽略
        skip_unchanged = True
        # 在导入预览页面中显示跳过的记录
        report_skipped = True
        fields = (
            'id',
            "mbse_user", "mbse_status", "mbse_judge", "mbse_code", "mbse_exp", "mbse_name", "mbr_gender", "mbr_birth",
            "mbr_political", "mbr_folk", "mbr_title", "mbr_id_num", "mbr_graduate", "mbr_graduate_time",
            "mbr_training_ins", "mbr_training_date", "mbr_job", "mbr_loc", "mbr_zip", "mbr_email", "mbr_phone",
            "mbr_cert", "mbr_cert_date", "mbr_cert_code", "mbr_achievement"
        )


@xadmin.sites.register(MbrUnactived.MbrUnactived)
class MbrUnactivedAdmin(object):
    """
    未激活个人用户
    """

    list_display = [
        'mbse_user', 'mbse_identity', 'mbse_status',
    ]
    list_filter = ['mbse_user', 'mbse_user__identity', 'mbse_status']
    # list_editable = list_display
    model_icon = "fa fa-user-o"
    show_bookmarks = False
    MbrJudgeButtonAllow = True
    import_export_args = {'import_resource_class': MemberResources}
    def get_form_layout(self):
        self.form_layout = MbrLayout
        return super().get_form_layout()

    def queryset(self):
        qs = super().queryset()
        qs = qs.filter(mbse_user__identity='1000')
        return qs


@xadmin.sites.register(IncUnactived.IncUnactived)
class IncUnactivedAdmin(object):
    """
    未激活理事用户
    """

    list_display = [
        'mbse_user', 'mbse_identity', 'mbse_status',
    ]
    list_filter = ['mbse_user', 'mbse_user__identity', 'mbse_status']
    # list_editable = list_display
    model_icon = "fa fa-user-o"
    show_bookmarks = False

    def get_form_layout(self):
        self.form_layout = MbrLayout
        return super().get_form_layout()

    def queryset(self):
        qs = super().queryset()
        qs = qs.filter(mbse_user__identity='1000')
        return qs


@xadmin.sites.register(CommonFormal.CommonFormal)
class CommonFormalAdmin(object):
    """
    普通正式会员
    """

    list_display = [
        'mbse_name', 'mbse_identity', 'mbse_status', 'mbse_code', 'mbse_exp',
    ]
    list_filter = [
        'mbse_code', 'mbse_exp', 'mbse_name', 'mbr_gender', 'mbr_birth', 'mbr_political', 'mbr_folk',
        'mbr_title', 'mbr_id_num', 'mbr_graduate', 'mbr_graduate_time', 'mbr_training_ins', 'mbr_training_date',
        'mbr_job', 'mbr_loc', 'mbr_zip', 'mbr_phone', 'mbr_email', 'mbr_cert', 'mbr_cert_date', 'mbr_cert_code',
    ]
    list_editable = list_display
    readonly_fields = [
        'mbse_user', 'mbse_name', 'mbse_status', 'mbse_code',
        'mbr_gender', 'mbr_birth', 'mbr_political', 'mbr_folk', 'mbr_achievement',
        'mbr_title', 'mbr_id_num', 'mbr_graduate', 'mbr_graduate_time', 'mbr_training_ins', 'mbr_training_date',
        'mbr_job', 'mbr_loc', 'mbr_zip', 'mbr_phone', 'mbr_email', 'mbr_cert', 'mbr_cert_date', 'mbr_cert_code',
    ]
    show_bookmarks = False
    model_icon = "fa fa-user"

    def get_form_layout(self):
        self.form_layout = MbrLayout
        return super().get_form_layout()

    def queryset(self):
        qs = super().queryset()
        qs = qs.filter(mbse_user__identity='1001', mbse_status='2006')
        return qs


@xadmin.sites.register(CommonAudit.CommonAudit)
class CommonAuditAdmin(object):
    """
    普通待审核会员
    """
    list_display = [
        'mbse_name', 'mbse_identity', 'mbse_status', 'mbse_code', 'mbse_exp',
    ]
    list_filter = [
        'mbse_code', 'mbse_status', 'mbse_exp', 'mbse_name', 'mbr_gender', 'mbr_birth', 'mbr_political', 'mbr_folk',
        'mbr_title', 'mbr_id_num', 'mbr_graduate', 'mbr_graduate_time', 'mbr_training_ins', 'mbr_training_date',
        'mbr_job', 'mbr_loc', 'mbr_zip', 'mbr_phone', 'mbr_email', 'mbr_cert', 'mbr_cert_date', 'mbr_cert_code',
    ]

    readonly_fields = [
        'mbse_name', 'mbr_gender', 'mbr_birth', 'mbr_political', 'mbr_folk',
        'mbr_title', 'mbr_id_num', 'mbr_graduate', 'mbr_graduate_time', 'mbr_training_ins',
        'mbr_training_date', 'mbse_status',
        'mbr_job', 'mbr_loc', 'mbr_zip', 'mbr_phone', 'mbr_email', 'mbr_cert', 'mbr_cert_date',
        'mbr_cert_code', 'mbr_achievement', 'mbse_user'
    ]
    list_editable = list_display
    show_bookmarks = False
    MbrJudgeButtonAllow = True
    model_icon = "fa fa-user-o"

    def get_form_layout(self):
        self.form_layout = MbrLayout
        return super().get_form_layout()

    def queryset(self):
        qs = super().queryset()
        qs = qs.filter(mbse_user__identity='1001').exclude(mbse_status='2006')
        return qs


@xadmin.sites.register(SeniorFormal.SeniorFormal)
class SeniorFormalAdmin(object):
    """
    高级正式会员
    """

    list_display = [
        'mbse_name', 'mbse_identity', 'mbse_status', 'mbse_code', 'mbse_exp',
    ]
    list_filter = [
        'mbse_code', 'mbse_exp', 'mbse_name', 'mbr_gender', 'mbr_birth', 'mbr_political', 'mbr_folk', 'mbr_avatar',
        'mbr_title', 'mbr_id_num', 'mbr_graduate', 'mbr_graduate_time', 'mbr_training_ins', 'mbr_training_date',
        'mbr_job', 'mbr_loc', 'mbr_zip', 'mbr_phone', 'mbr_email', 'mbr_cert', 'mbr_cert_date', 'mbr_cert_code',
    ]
    readonly_fields = [
        'mbse_name', 'mbse_status', 'mbr_gender', 'mbr_birth', 'mbr_political', 'mbr_folk',
        'mbr_title', 'mbr_id_num', 'mbr_graduate', 'mbr_graduate_time', 'mbr_training_ins',
        'mbr_training_date',
        'mbr_job', 'mbr_loc', 'mbr_zip', 'mbr_phone', 'mbr_email', 'mbr_cert', 'mbr_cert_date',
        'mbr_cert_code', 'mbr_achievement', 'mbse_user'
    ]
    list_editable = list_display
    show_bookmarks = False
    model_icon = "fa fa-user-circle"

    def get_form_layout(self):
        self.form_layout = MbrLayout
        return super().get_form_layout()

    def queryset(self):
        qs = super().queryset()
        qs = qs.filter(mbse_user__identity='1002', mbse_status='2006')
        return qs


@xadmin.sites.register(SeniorAudit.SeniorAudit)
class SeniorAuditAdmin(object):
    """
    高级待审核会员
    """
    list_display = [
        'mbse_name', 'mbse_identity', 'mbse_status', 'mbse_code', 'mbse_exp',
    ]
    list_filter = [
        'mbse_code', 'mbse_exp', 'mbse_name', 'mbr_gender', 'mbr_birth', 'mbr_political', 'mbr_folk', 'mbr_avatar',
        'mbr_title', 'mbr_id_num', 'mbr_graduate', 'mbr_graduate_time', 'mbr_training_ins', 'mbr_training_date',
        'mbr_job', 'mbr_loc', 'mbr_zip', 'mbr_phone', 'mbr_email', 'mbr_cert', 'mbr_cert_date', 'mbr_cert_code',
    ]
    readonly_fields = [
        'mbse_name', 'mbse_status', 'mbr_gender', 'mbr_birth', 'mbr_political', 'mbr_folk',
        'mbr_title', 'mbr_id_num', 'mbr_graduate', 'mbr_graduate_time', 'mbr_training_ins',
        'mbr_training_date',
        'mbr_job', 'mbr_loc', 'mbr_zip', 'mbr_phone', 'mbr_email', 'mbr_cert', 'mbr_cert_date',
        'mbr_cert_code', 'mbr_achievement', 'mbse_user'
    ]
    list_editable = list_display
    show_bookmarks = False
    MbrJudgeButtonAllow = True
    model_icon = "fa fa-user-circle-o"

    def get_form_layout(self):
        self.form_layout = MbrLayout
        return super().get_form_layout()

    def queryset(self):
        qs = super().queryset()
        qs = qs.filter(mbse_user__identity='1002').exclude(mbse_status='2006')
        return qs


@xadmin.sites.register(IncFormal.IncFromal)
class IncFormalAdmin(object):
    """
    理事单位会员
    """
    list_display = [
        'mbse_name', 'mbse_identity', 'mbse_status', 'mbse_code', 'mbse_exp',
    ]
    list_filter = [
        'mbse_name', 'inc_loc', 'inc_phone', 'inc_fax', 'inc_email', 'inc_site', 'inc_charge',
        'inc_charge_code', 'inc_corporate', 'inc_corp_phone', 'inc_director', 'inc_director_phone',
        'inc_info',
    ]
    readonly_fields = ['mbse_name', 'inc_loc', 'inc_code', 'inc_phone', 'inc_fax',
                       'inc_email', 'inc_site', 'inc_charge', 'inc_charge_code', 'inc_corporate',
                       'inc_corp_phone', 'inc_director', 'inc_director_phone', 'inc_info', 'mbse_status', 'mbse_user',
                       'inc_opinion', ]
    show_bookmarks = False
    model_icon = "fa fa-group"

    def queryset(self):
        qs = super().queryset()
        qs = qs.filter(mbse_user__identity='1003', mbse_status='2006')
        return qs

    def get_form_layout(self):
        self.form_layout = IncLayout
        return super().get_form_layout()


@xadmin.sites.register(IncAudit.IncAudit)
class IncAuditAdmin(object):
    """
    待审核理事单位会员
    """
    list_display = [
        'mbse_name', 'mbse_status', 'mbse_code', 'mbse_exp',
    ]
    list_filter = [
        'mbse_name', 'inc_loc', 'inc_phone', 'inc_fax', 'inc_email', 'inc_site', 'inc_charge',
        'inc_charge_code', 'inc_corporate', 'inc_corp_phone', 'inc_director', 'inc_director_phone',
        'inc_info',
    ]
    readonly_fields = ['mbse_name', 'inc_loc', 'inc_code', 'inc_phone', 'inc_fax',
                       'inc_email', 'inc_site', 'inc_charge', 'inc_charge_code', 'inc_corporate',
                       'inc_corp_phone', 'inc_director', 'inc_director_phone', 'inc_info', 'mbse_status', 'mbse_user',
                       'inc_opinion', ]
    show_bookmarks = False
    model_icon = "fa fa-group"
    IncJudgeButtonAllow = True

    def queryset(self):
        qs = super().queryset()
        qs = qs.filter(mbse_user__identity='1003').exclude(mbse_status='2006')
        return qs

    def get_form_layout(self):
        self.form_layout = IncLayout
        return super().get_form_layout()
