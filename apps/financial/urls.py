from django.urls import path,re_path
from django.conf.urls import include, url
from rest_framework import routers
from . import views

routers = routers.DefaultRouter()
routers.register(r'mbr',views.OrderViewSet,basename='order')
routers.register(r'inc',views.OrderIncViewSet,basename='orderInc')


urlpatterns=[
    # path(r'',views.StrategyApiView.as_view()),
    # url('getMember/',views.MemberViewSet.as_view({'get':'list'})),
    path('',include(routers.urls))
]