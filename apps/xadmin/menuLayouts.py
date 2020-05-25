from financial.models import Order
from membership.models import MbrCommon,MbrUnactived,CommonFormal,CommonAudit,SeniorAudit,SeniorFormal,IncUnactived,IncAudit,IncFormal
from myauth.models import CustomUser
def set_menu(self):
    defaultLayoutList = [
        {
            'title': '会员信息管理',
            'icon':'fa fa-address-book',
            'menus':
                (
                    {
                        'title': '未激活用户',
                        'perm': self.get_model_perm(MbrUnactived.MbrUnactived, 'view'),
                        'url': self.get_model_url(MbrUnactived.MbrUnactived, 'changelist'),
                        'icon': 'fa fa-user-o'
                    },
                    {
                        'title': '普通会员',
                        'perm': self.get_model_perm(CommonFormal.CommonFormal, 'view'),
                        'url': self.get_model_url(CommonFormal.CommonFormal, 'changelist'),
                        'icon': 'fa fa-user'
                    },
                    {
                        'title':'待审核普通会员',
                        'perm':self.get_model_perm(CommonAudit.CommonAudit,'view'),
                        'url':self.get_model_url(CommonAudit.CommonAudit,'changelist'),
                        'icon':'fa fa-user-o'
                    },
                    {
                        'title': '高级会员',
                        'perm': self.get_model_perm(SeniorFormal.SeniorFormal, 'view'),
                        'url': self.get_model_url(SeniorFormal.SeniorFormal, 'changelist'),
                        'icon': 'fa fa-user-circle'
                    },
                    {
                        'title': '待审核高级会员',
                        'perm': self.get_model_perm(SeniorAudit.SeniorAudit, 'view'),
                        'url': self.get_model_url(SeniorAudit.SeniorAudit, 'changelist'),
                        'icon': 'fa fa-user-circle-o'
                    },
                    {
                        'title': '理事单位会员',
                        'perm': self.get_model_perm(IncFormal.IncFromal, 'view'),
                        'url': self.get_model_url(IncFormal.IncFromal, 'changelist'),
                        'icon': 'fa fa-group'
                    },
                    {
                        'title':'待审核理事单位会员',
                        'perm':self.get_model_perm(IncAudit.IncAudit,'view'),
                        'url':self.get_model_url(IncAudit.IncAudit,'changelist'),
                        'icon': 'fa fa-group'

                    },
                )
        },
        # {
        #     'title': '缴费信息管理',
        #     'icon': 'fa fa-money',
        #     'menus':
        #         (
        #             {
        #                 'title': '缴费信息',
        #                 'perm': self.get_model_perm(Order, 'view'),
        #                 'url': self.get_model_url(Order, 'changelist'),
        #                 'icon': 'fa fa-money'
        #             },
        #         )
        # },
        {
            'title':'用户管理',
            'icon':'fa fa-user',
            'menus':
                (
                    {
                        'title':'用户管理',
                        'perm':self.get_model_perm(CustomUser,'view'),
                        'url':self.get_model_url(CustomUser,'changelist'),
                        'icon':'fa fa-user'
                    },
                )
        },
    ]
    return defaultLayoutList