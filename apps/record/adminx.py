import xadmin
from django.utils.html import format_html
from .models import Activity,Audit,Diary
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, BooleanWidget
from django.apps import apps

@xadmin.sites.register(Activity)
class ActivityAdmin(object):
    """
    活动管理
    """
    show_bookmarks=False
    list_display = ['act_title','act_is_available','act_need_audit','act_date','act_loc','act_method']
    list_filter = list_display

@xadmin.sites.register(Audit)
class AuditAdmin(object):
    """
    申请管理
    """
    show_bookmarks = False
    list_display = ['relate_activity','audit_user','audit_name','audit_status']
    list_filter = ['relate_activity','audit_user','audit_status']

@xadmin.sites.register(Diary)
class DiaryAdmin(object):
    """
    活动心得管理
    """
    show_bookmarks = False
    list_display = ['related_act','related_user','diary_title','diary_date','diary_loc']
    list_filter = list_display
