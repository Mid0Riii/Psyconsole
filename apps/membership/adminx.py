import xadmin
from django.utils.html import format_html
from .models import CommonAudit, SeniorAudit, CommonFormal, SeniorFormal, IncAudit, IncFormal, IncUnactived, \
    MbrUnactived,MbrCommon
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, BooleanWidget
from django.apps import apps
from .layouts import MbrLayout


@xadmin.sites.register(MbrCommon)
class MbrCommonAdmin(object):
    pass

@xadmin.sites.register(MbrUnactived.MbrUnactived)
class MbrUnactivedAdmin(object):
    """
    未激活用户
    """

    list_display = [
        'mbse_user', 'mbse_type', 'mbse_status',
    ]
    list_filter = list_display
    list_editable = list_display
    model_icon="fa fa-user-o"
    show_bookmarks = False

    def get_form_layout(self):
        self.form_layout = MbrLayout
        return super().get_form_layout()

    def queryset(self):
        qs = super().queryset()
        qs = qs.filter(mbse_type='0')
        return qs


@xadmin.sites.register(CommonFormal.CommonFormal)
class CommonFormalAdmin(object):
    """
    普通正式会员
    """

    list_display = [
        'mbr_name', 'mbse_type', 'mbse_status', 'mbse_code', 'mbse_exp',
    ]
    list_filter = [
        'mbse_code', 'mbse_exp', 'mbr_name', 'mbr_gender', 'mbr_birth', 'mbr_political', 'mbr_folk',
        'mbr_title', 'mbr_id_num', 'mbr_graduate', 'mbr_graduate_time', 'mbr_training_ins', 'mbr_training_date',
        'mbr_job', 'mbr_loc', 'mbr_zip', 'mbr_phone', 'mbr_email', 'mbr_cert', 'mbr_cert_date', 'mbr_cert_code',
    ]
    list_editable = list_display
    readonly_fields = [
        'mbse_user','mbr_name', 'mbse_type', 'mbse_status', 'mbse_code', 'mbse_exp',
        'mbr_gender', 'mbr_birth', 'mbr_political', 'mbr_folk',
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
        qs = qs.filter(mbse_type='1', mbse_status='6')
        return qs


@xadmin.sites.register(CommonAudit.CommonAudit)
class CommonAuditAdmin(object):
    """
    普通待审核会员
    """
    list_display = [
        'mbr_name', 'mbse_type', 'mbse_status', 'mbse_code', 'mbse_exp',
    ]
    list_filter = [
        'mbse_code', 'mbse_exp', 'mbr_name', 'mbr_gender', 'mbr_birth', 'mbr_political', 'mbr_folk',
        'mbr_title', 'mbr_id_num', 'mbr_graduate', 'mbr_graduate_time', 'mbr_training_ins', 'mbr_training_date',
        'mbr_job', 'mbr_loc', 'mbr_zip', 'mbr_phone', 'mbr_email', 'mbr_cert', 'mbr_cert_date', 'mbr_cert_code',
    ]

    readonly_fields = [
        'mbr_name', 'mbr_gender', 'mbr_birth', 'mbr_political', 'mbr_folk',
        'mbr_title', 'mbr_id_num', 'mbr_graduate', 'mbr_graduate_time', 'mbr_training_ins',
        'mbr_training_date',
        'mbr_job', 'mbr_loc', 'mbr_zip', 'mbr_phone', 'mbr_email', 'mbr_cert', 'mbr_cert_date',
        'mbr_cert_code','mbr_achievement','mbse_user'
    ]
    list_editable = list_display
    show_bookmarks = False
    model_icon = "fa fa-user-o"
    def get_form_layout(self):
        self.form_layout = MbrLayout
        return super().get_form_layout()

    def queryset(self):
        qs = super().queryset()
        qs = qs.filter(mbse_type='1').exclude(mbse_status='6')
        return qs


@xadmin.sites.register(SeniorFormal.SeniorFormal)
class SeniorFormalAdmin(object):
    """
    高级正式会员
    """

    list_display = [
        'mbr_name', 'mbse_type', 'mbse_status', 'mbse_code', 'mbse_exp',
    ]
    list_filter = [
        'mbse_code', 'mbse_exp', 'mbr_name', 'mbr_gender', 'mbr_birth', 'mbr_political', 'mbr_folk',
        'mbr_title', 'mbr_id_num', 'mbr_graduate', 'mbr_graduate_time', 'mbr_training_ins', 'mbr_training_date',
        'mbr_job', 'mbr_loc', 'mbr_zip', 'mbr_phone', 'mbr_email', 'mbr_cert', 'mbr_cert_date', 'mbr_cert_code',
    ]
    list_editable = list_display
    show_bookmarks = False
    model_icon="fa fa-user-circle"

    def get_form_layout(self):
        self.form_layout = MbrLayout
        return super().get_form_layout()

    def queryset(self):
        qs = super().queryset()
        qs = qs.filter(mbse_type='2', mbse_status='6')
        return qs


@xadmin.sites.register(SeniorAudit.SeniorAudit)
class SeniorAuditAdmin(object):
    """
    高级待审核会员
    """
    list_display = [
        'mbr_name', 'mbse_type', 'mbse_status', 'mbse_code', 'mbse_exp',
    ]
    list_filter = [
        'mbse_code', 'mbse_exp', 'mbr_name', 'mbr_gender', 'mbr_birth', 'mbr_political', 'mbr_folk',
        'mbr_title', 'mbr_id_num', 'mbr_graduate', 'mbr_graduate_time', 'mbr_training_ins', 'mbr_training_date',
        'mbr_job', 'mbr_loc', 'mbr_zip', 'mbr_phone', 'mbr_email', 'mbr_cert', 'mbr_cert_date', 'mbr_cert_code',
    ]
    list_editable = list_display
    show_bookmarks = False
    model_icon = "fa fa-user-circle-o"
    def get_form_layout(self):
        self.form_layout = MbrLayout
        return super().get_form_layout()

    def queryset(self):
        qs = super().queryset()
        qs = qs.filter(mbse_type='2').exclude(mbse_status='6')
        return qs


# @xadmin.sites.register(IncUnactived.IncUnactived)
# class IncUnactivedAdmin(object):
#     """
#     未激活理事单位
#     """
#     list_display = [
#         'mbse_user', 'mbse_type', 'mbse_status',
#     ]
#     list_filter = list_display
#     list_editable = list_display
#     model_icon = "fa fa-user-o"
#     show_bookmarks = False
#
#     def get_form_layout(self):
#         self.form_layout = MbrLayout
#         return super().get_form_layout()
#
#     def queryset(self):
#         qs = super().queryset()
#         qs = qs.filter(mbse_type='0')
#         return qs
#

@xadmin.sites.register(IncFormal.IncFromal)
class IncFormalAdmin(object):
    """
    理事单位会员
    """
    list_display = [
        'inc_name', 'mbse_type', 'mbse_status', 'mbse_code', 'mbse_exp',
    ]
    list_filter = [
        'inc_name', 'inc_loc', 'inc_phone', 'inc_fax', 'inc_email', 'inc_site', 'inc_charge',
        'inc_charge_code', 'inc_corporate', 'inc_corp_phone', 'inc_director', 'inc_director_phone',
        'inc_info',
    ]
    list_editable = list_display
    show_bookmarks = False
    model_icon = "fa fa-group"
    def queryset(self):
        qs = super().queryset()
        qs = qs.filter(mbse_type='3', mbse_status='6')
        return qs


@xadmin.sites.register(IncAudit.IncAudit)
class IncAuditAdmin(object):
    """
    待审核理事单位会员
    """
    list_display = [
        'inc_name', 'mbse_type', 'mbse_status', 'mbse_code', 'mbse_exp',
    ]
    list_filter = [
        'inc_name', 'inc_loc', 'inc_phone', 'inc_fax', 'inc_email', 'inc_site', 'inc_charge',
        'inc_charge_code', 'inc_corporate', 'inc_corp_phone', 'inc_director', 'inc_director_phone',
        'inc_info',
    ]
    list_editable = list_display
    show_bookmarks = False
    model_icon = "fa fa-group"

    def queryset(self):
        qs = super().queryset()
        qs = qs.filter(mbse_type='3').exclude(mbse_status='6')
        return qs
