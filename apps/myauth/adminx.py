import xadmin
from .models import CustomUser
from django import forms
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm,
                                       AdminPasswordChangeForm, PasswordChangeForm)
from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model
from xadmin.layout import Fieldset, Main, Side, Row
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from django.contrib.auth.forms import UserCreationForm, UsernameField
from import_export.results import RowResult
from django.contrib.auth.hashers import make_password
User = get_user_model()


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "identity")
        field_classes = {"username": UsernameField, }



class UserResources(resources.ModelResource):
    #TODO CODEVIEW import_export工作流
    def before_import_row(self, row, **kwargs):
        """
        对excel里的明文密码进行加密
        """
        row['password'] = make_password(row['password'])
        print(row)
    class Meta:
        model=User
        skip_unchanged=True
        report_skipped=True
        import_id_fields = ('username',)
        fields=("id","username","identity","password","first_name",'phone')


# class CustomUserAdmin(object):
#     # import_export_args = {'import_resource_class': UserResources}
#     list_display = ['id', 'name', 'username' 'phone', 'identity']
#     list_filter = ['username', 'phone', 'identity']
#     list_editable = ['username', 'phone', ]
#     show_bookmarks = False


class UserAdmin(object):
    change_user_password_template = None
    import_export_args = {'import_resource_class': UserResources}
    list_display = ['username', 'phone', 'identity', 'is_active']
    list_filter = ['username', 'phone', ]
    list_editable = ['username', 'phone']
    show_bookmarks = False
    ordering = ('username',)
    style_fields = {'user_permissions': 'm2m_transfer'}
    model_icon = 'fa fa-user'
    relfield_style = 'fk-ajax'

    def get_model_form(self, **kwargs):
        if self.org_obj is None:
            self.form = MyUserCreationForm
        else:
            self.form = UserChangeForm
        return super(UserAdmin, self).get_model_form(**kwargs)

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset(_('Personal info'),
                             'username',
                             'password',
                             'phone',
                             'identity',
                             ),
                    Fieldset(_('权限信息'),
                             'groups', 'user_permissions', 'first_name', 'last_name', 'email',
                             ),
                    Fieldset(_('Important dates'),
                             'last_login', 'date_joined'
                             ),
                    Fieldset(_('用户状态'),
                             'is_active', 'is_staff', 'is_superuser',
                             )
                ),
            )
        return super(UserAdmin, self).get_form_layout()


xadmin.site.unregister(CustomUser)
xadmin.site.register(CustomUser, UserAdmin)
