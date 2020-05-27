import xadmin
from django.utils.html import format_html
from .models import Activity,Audit,Diary
from django.utils.translation import ugettext as _
from django.http import HttpResponse,HttpResponseRedirect
from xadmin.plugins.actions import BaseActionView

class AuditJudgeAction(BaseActionView):

    # 这里需要填写三个属性
    action_name = "AuditJudgeAction"    #: 相当于这个 Action 的唯一标示, 尽量用比较针对性的名字
    description = _(u'批准已选择申请 %(verbose_name_plural)s') #: 描述, 出现在 Action 菜单中, 可以使用 ``%(verbose_name_plural)s`` 代替 Model 的名字.
    model_perm = 'change'    #: 该 Action 所需权限

    # 而后实现 do_action 方法
    def do_action(self, queryset):
        # queryset 是包含了已经选择的数据的 queryset
        for obj in queryset:
            obj.audit_status = '1'
            obj.save()
        # 返回 HttpResponse
        return HttpResponseRedirect("/xadmin/record/audit/")

@xadmin.sites.register(Activity)
class ActivityAdmin(object):
    """
    活动管理
    """
    show_bookmarks=False
    list_display = ['act_title','act_is_available','act_need_audit','act_date','act_loc','act_method']
    list_filter = list_display
    list_editable=['act_is_available']

@xadmin.sites.register(Audit)
class AuditAdmin(object):
    """
    申请管理
    """
    actions=[AuditJudgeAction]
    show_bookmarks = False
    list_display = ['relate_activity','audit_user','audit_member','audit_status']
    list_filter = ['relate_activity__act_title','audit_user','audit_status']

@xadmin.sites.register(Diary)
class DiaryAdmin(object):
    """
    活动心得管理
    """
    show_bookmarks = False
    list_display = ['related_act','related_user','diary_title','diary_date','diary_loc']
    list_filter = list_display


#申请审批action
