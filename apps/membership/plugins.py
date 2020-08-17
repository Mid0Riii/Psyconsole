from xadmin.views import BaseAdminPlugin
from django.template import loader
import xadmin
from xadmin.views import ModelFormAdminView,UpdateAdminView,BaseAdminView

# 人类会员"审核通过" 按钮
class MbrJudgeButton(BaseAdminPlugin):
    MbrJudgeButtonAllow = False

    def init_request(self, *args, **kwargs):
        return bool(self.MbrJudgeButtonAllow)

    def block_submit_more_btns(self, context, nodes):
        return nodes.append(loader.render_to_string("apps/membership/MbrJudgeButton.html"))
xadmin.site.register_plugin(MbrJudgeButton, ModelFormAdminView)

# 理事单位会员"审核通过" 按钮
class IncJudgeButton(BaseAdminPlugin):
    IncJudgeButtonAllow = False

    def init_request(self, *args, **kwargs):
        return bool(self.IncJudgeButtonAllow)

    def block_submit_more_btns(self, context, nodes):
        return nodes.append(loader.render_to_string("apps/membership/IncJudgeButton.html"))


xadmin.site.register_plugin(IncJudgeButton, ModelFormAdminView)

