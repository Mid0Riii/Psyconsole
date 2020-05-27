from xadmin.views import BaseAdminPlugin
from django.template import loader
import xadmin
from xadmin.views import ModelFormAdminView,UpdateAdminView,BaseAdminView


class MbrJudgeButton(BaseAdminPlugin):
    MbrJudgeButtonAllow = False

    def init_request(self, *args, **kwargs):
        return bool(self.MbrJudgeButtonAllow)

    def block_submit_more_btns(self, context, nodes):
        return nodes.append(loader.render_to_string("apps/membership/MbrJudgeButton.html"))
xadmin.site.register_plugin(MbrJudgeButton, ModelFormAdminView)


class IncJudgeButton(BaseAdminPlugin):
    IncJudgeButtonAllow = False

    def init_request(self, *args, **kwargs):
        return bool(self.IncJudgeButtonAllow)

    def block_submit_more_btns(self, context, nodes):
        return nodes.append(loader.render_to_string("apps/membership/IncJudgeButton.html"))


xadmin.site.register_plugin(IncJudgeButton, ModelFormAdminView)

