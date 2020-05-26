# -*- coding:utf-8 -*-
from .models import CustomUser
from rest_framework_jwt.utils import jwt_decode_handler
from .serializers import CustomUserSerializers
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.contrib.auth.backends import ModelBackend
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
from rest_framework.exceptions import APIException


class CustomBackend(ModelBackend):
    """
    用户自定义用户验证
    """

    def authenticate(self, request, username=None, password=None, **kwargs):  # 重写这个函数
        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):  # 加密后比对前端密码
                return user
        except Exception as e:
            detail = "无此用户"
            print(isinstance(detail,dict))
            # 异常信息UserProfile matching query does not exist
            raise APIException(detail=detail)
        else:
            detail = "无此用户"
            raise APIException(detail=detail)


class CustomUserViewSet(viewsets.GenericViewSet):
    serializer_class = CustomUserSerializers
    queryset = CustomUser.objects.all()


    @action(methods=["post"], detail=False)
    def signup(self, request):
        serializer_class = CustomUserSerializers
        rawData = request.data
        username = rawData['username']
        password = rawData['password']
        phone = rawData['phone']
        r = CustomUser.objects.filter(username=username)
        if r.exists():
            return Response({"code": 400, "message": "该用户名已被注册", "data": ""}, status=status.HTTP_400_BAD_REQUEST)
        else:
            u = CustomUser.objects.create(username=username, phone=phone)
            u.set_password(password)
            u.save()
            return Response({"code": 201, "message": "注册成功", "data": {"id":u.id,"username": username, "password": password}},
                            status=status.HTTP_201_CREATED)

    @action(methods=['post'],detail=False)
    def updateUser(self, request):
        rawData = request.data
        new_password = rawData["password"]
        phone = rawData['phone']
        try:
            id = request.user.id
        except Exception as e:
            return Response({"code": 400, "message": "错误", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        try:
            q = CustomUser.objects.get(id=id)
            q.set_password(new_password)
            q.save()
            return Response({"code": 200, "message": "修改成功", "data": ""}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"code": 400, "message": "错误", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)
