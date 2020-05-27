from xadmin.views import BaseAdminPlugin
from django.template import loader
import xadmin
from xadmin.views import ModelFormAdminView,UpdateAdminView,BaseAdminView


class OrderJudgeButton(BaseAdminPlugin):
    OrderJudgeButtonAllow = False

    def init_request(self, *args, **kwargs):
        return bool(self.OrderJudgeButtonAllow)

    def block_submit_more_btns(self, context, nodes):
        return nodes.append(loader.render_to_string("apps/financial/OrderJudgeButton.html"))

xadmin.site.register_plugin(OrderJudgeButton, ModelFormAdminView)


class OrderIncJudgeButton(BaseAdminPlugin):
    OrderIncJudgeButtonAllow = False

    def init_request(self, *args, **kwargs):
        return bool(self.OrderIncJudgeButtonAllow)

    def block_submit_more_btns(self, context, nodes):
        return nodes.append(loader.render_to_string("apps/financial/OrderIncJudgeButton.html"))


xadmin.site.register_plugin(OrderIncJudgeButton, ModelFormAdminView)

