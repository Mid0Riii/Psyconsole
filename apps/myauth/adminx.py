import xadmin
from .models import CustomUser
from django import forms
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm,
                                       AdminPasswordChangeForm, PasswordChangeForm)
from django.utils.translation import ugettext as _

from django.contrib.auth import get_user_model
from xadmin.layout import Fieldset, Main, Side, Row

User = get_user_model()




class CustomUserAdmin(object):
    list_display = ['id', 'name','username' 'phone', ]
    list_filter = ['username', 'phone', ]
    list_editable = [ 'username', 'phone', ]
    show_bookmarks = False


class UserAdmin(object):
    change_user_password_template = None
    list_display = ['username', 'phone',]
    list_filter = ['username', 'phone', ]
    list_editable = [ 'username', 'phone']
    show_bookmarks = False
    ordering = ('username',)
    style_fields = {'user_permissions': 'm2m_transfer'}
    model_icon = 'fa fa-user'
    relfield_style = 'fk-ajax'

    def get_model_form(self, **kwargs):
        if self.org_obj is None:
            self.form = UserCreationForm
        else:
            self.form = UserChangeForm
        return super(UserAdmin, self).get_model_form(**kwargs)

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset(_('Personal info'),
                             'name',
                             'phone',
                             ),
                    Fieldset('账号信息',
                             'username', 'password',
                             css_class='unsort no_title'
                             ),
                    Fieldset(None,
                             'groups', 'user_permissions','first_name','last_name','email',**{"style":"display:None"}
                             ),
                    Fieldset(_('Important dates'),
                             'last_login', 'date_joined'
                             ),
                ),
                Side(
                    Fieldset(None,
                             'is_active', 'is_staff', 'is_superuser',**{"style":"display:None"}
                             ),
                )
            )
        return super(UserAdmin, self).get_form_layout()
xadmin.site.unregister(CustomUser)
xadmin.site.register(CustomUser,UserAdmin)