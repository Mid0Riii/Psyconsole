from django.shortcuts import render
from .serializers import OrderSerializers
from .models import Order
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets,filters
from rest_framework.mixins import ListModelMixin
from rest_framework.decorators import action
from utils.drf import FormatResponse
# Create your views here.

class OrderListMixin(ListModelMixin):
    def list(self, request, *args, **kwargs):
        try:
            response = super().list(request, *args, **kwargs)
            return FormatResponse(code=200, msg="获取成功", data=response.data, status=status.HTTP_200_OK)
        except Exception as e:
            return FormatResponse(code=400, msg="错误", data=str(e), status=status.HTTP_400_BAD_REQUEST)


class OrderViewSet(viewsets.GenericViewSet, OrderListMixin):
    serializer_class = OrderSerializers
    queryset = Order.objects.all()

    # # @action(methods=['post'],detail=False)
    # def create(self, request):
    #     """
    #     """
    #
    #     rawdata = request.data
    #     try:
    #         s = OrderSerializers(data=rawdata, context={'request': request})
    #         if s.is_valid():
    #             s.save()
    #             return FormatResponse(code=201, msg="提交成功", data=s.data, status=status.HTTP_201_CREATED)
    #         else:
    #             return FormatResponse(code=400, msg="错误", data=str(s.errors),
    #                                   status=status.HTTP_400_BAD_REQUEST)
    #     except Exception as e:
    #         return FormatResponse(code=400, msg="提交失败", data=str(e), status=status.HTTP_400_BAD_REQUEST)

    # @action(methods=['patch'], detail=True,)
    def update(self, request, pk):
        """
        更新订单

        """
        try:
            s = Order.objects.get(id=pk)
            ser = OrderSerializers(instance=s, data=request.data, context={'request': request})
            if ser.is_valid():
                ser.save()
                return FormatResponse(code=201, msg="修改成功", data=ser.data, status=status.HTTP_201_CREATED)
            else:
                return FormatResponse(code=400, msg="错误", data=str(ser.errors),
                                      status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return FormatResponse(code=400, msg="错误", data=str(e), status=status.HTTP_400_BAD_REQUEST)

    # @action(methods=['delete'], detail=True)
    # def delete(self, request, pk):
    #     """
    #     删除订单，没什么用
    #     """
    #     try:
    #         s = Order.objects.get(id=pk)
    #         s.delete()
    #         return FormatResponse(code=200, msg="删除成功", data="", status=status.HTTP_200_OK)
    #     except Exception as e:
    #         return FormatResponse(code=400, msg="错误", data=str(e), status=status.HTTP_400_BAD_REQUEST)
    #


