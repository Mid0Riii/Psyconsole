import xadmin
from .models import Order,OrderInc
from .plugins import OrderJudgeButton
from xadmin.views import ModelFormAdminView
@xadmin.sites.register(Order)
class OrderAdmin(object):
    list_display=['name','oid','price','method','exp','date','status']
    list_filter=[]
    model_icon="fa fa-money"
    show_bookmarks=False
    OrderJudgeButtonAllow = True

@xadmin.sites.register(OrderInc)
class OrderIncAdmin(object):
    list_display=['name','oid','price','method','exp','date','status']
    list_filter=[]
    model_icon="fa fa-money"
    show_bookmarks=False
    OrderIncJudgeButtonAllow = True
