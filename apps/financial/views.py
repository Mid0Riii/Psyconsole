from .serializers import OrderSerializers, OrderIncSerializers
from .models import Order, OrderInc
from rest_framework import status
from rest_framework import viewsets, filters
from rest_framework.mixins import ListModelMixin
from utils.drf import FormatResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

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
    # queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(relate_user=self.request.user)

    def update(self, request, pk):
        """
        更新订单
        """
        try:
            s = Order.objects.get(id=pk)
            ser = OrderSerializers(instance=s, data=request.data, context={'request': request})
            if ser.status != "0" or ser.status != "1":
                return FormatResponse(code=400, msg="错误", data="权限不足",
                                      status=status.HTTP_400_BAD_REQUEST)
            if ser.is_valid():
                ser.save()
                return FormatResponse(code=201, msg="修改成功", data=ser.data, status=status.HTTP_201_CREATED)
            else:
                return FormatResponse(code=400, msg="错误", data=str(ser.errors),
                                      status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return FormatResponse(code=400, msg="错误", data=str(e), status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True)
    def MbrJudgePass(self, request, pk):
        try:
            s = Order.objects.get(id=pk)
            s.status = '3'
            s.save()
            return FormatResponse(code=200, msg="成功", data="", status=status.HTTP_200_OK)
        except Exception as e:
            return FormatResponse(code=400, msg="错误", data=str(e), status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True)
    def MbrJudgeDeny(self, request, pk):
        try:
            s = Order.objects.get(id=pk)
            s.status = '2'
            s.save()
            return FormatResponse(code=200, msg="成功", data="", status=status.HTTP_200_OK)
        except Exception as e:
            return FormatResponse(code=400, msg="错误", data=str(e), status=status.HTTP_400_BAD_REQUEST)


class OrderIncViewSet(viewsets.GenericViewSet, OrderListMixin):
    serializer_class = OrderIncSerializers
    # queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return OrderInc.objects.filter(relate_user=self.request.user)

    def update(self, request, pk):
        """
        更新订单
        """
        try:
            s = OrderInc.objects.get(id=pk)
            ser = OrderIncSerializers(instance=s, data=request.data, context={'request': request})
            if ser.status != "0" or ser.status != "1":
                return FormatResponse(code=400, msg="错误", data="权限不足",
                                      status=status.HTTP_400_BAD_REQUEST)
            if ser.is_valid():
                ser.save()
                return FormatResponse(code=201, msg="修改成功", data=ser.data, status=status.HTTP_201_CREATED)
            else:
                return FormatResponse(code=400, msg="错误", data=str(ser.errors),
                                      status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return FormatResponse(code=400, msg="错误", data=str(e), status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True)
    def IncJudgePass(self, request, pk):
        try:
            s = OrderInc.objects.get(id=pk)
            s.status = '3'
            s.save()
            return FormatResponse(code=200, msg="成功", data="", status=status.HTTP_200_OK)
        except Exception as e:
            return FormatResponse(code=400, msg="错误", data=str(e), status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True)
    def IncJudgeDeny(self, request, pk):
        try:
            s = OrderInc.objects.get(id=pk)
            s.status = '2'
            s.save()
            return FormatResponse(code=200, msg="成功", data="", status=status.HTTP_200_OK)
        except Exception as e:
            return FormatResponse(code=400, msg="错误", data=str(e), status=status.HTTP_400_BAD_REQUEST)
