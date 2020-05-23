import xadmin
from .models import Order

@xadmin.sites.register(Order)
class OrderAdmin(object):
    list_display=['user','oid','price','method','exp','date','status']
    list_filter=[]
    model_icon="fa fa-money"
    show_bookmarks=False