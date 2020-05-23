from django.urls import path,re_path
from django.conf.urls import include, url
from rest_framework import routers
from . import views

routers = routers.DefaultRouter()
routers.register(r'',views.CustomUserViewSet)

urlpatterns=[
    path('',include(routers.urls))
]