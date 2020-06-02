from __future__ import absolute_import
import xadmin
from .models import UserSettings, Log
from xadmin.layout import *
from .menuLayouts import set_menu
from django.utils.translation import ugettext_lazy as _, ugettext

class UserSettingsAdmin(object):
    model_icon = 'fa fa-cog'
    hidden_menu = True

xadmin.site.register(UserSettings, UserSettingsAdmin)

class LogAdmin(object):

    def link(self, instance):
        if instance.content_type and instance.object_id and instance.action_flag != 'delete':
            admin_url = self.get_admin_url('%s_%s_change' % (instance.content_type.app_label, instance.content_type.model), 
                instance.object_id)
            return "<a href='%s'>%s</a>" % (admin_url, _('Admin Object'))
        else:
            return ''
    link.short_description = ""
    link.allow_tags = True
    link.is_column = False

    list_display = ('action_time', 'user', 'ip_addr', '__str__', 'link')
    list_filter = ['user', 'action_time']
    search_fields = ['ip_addr', 'message']
    model_icon = 'fa fa-cog'

xadmin.site.register(Log, LogAdmin)

from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

@xadmin.sites.register(views.CommAdminView)
class GlobalSetting(object):
    # 菜单样式改为折叠
    menu_style = 'accordion'
    # 页头
    site_title = '江西心理咨询师培训中心报名后台'
    # 页脚
    site_footer = 'Aldrich from NCUTEA'
    def get_site_menu(self):
        return set_menu(self)

xadmin.site.register(views.BaseAdminView, BaseSetting)