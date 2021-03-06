from .serializers import ActivitySerializers, AuditSerializers, DiarySerializers
from .models import Activity, Audit, Diary
from rest_framework import status
from rest_framework import viewsets, filters
from rest_framework.mixins import ListModelMixin
from utils.drf import FormatResponse
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from utils.drf import IsFormalMember
from .models import MbrCommon

class MyListMixin(ListModelMixin):
    def list(self, request, *args, **kwargs):
        try:
            response = super().list(request, *args, **kwargs)
            return FormatResponse(code=200, msg="获取成功", data=response.data, status=status.HTTP_200_OK)
        except Exception as e:
            return FormatResponse(code=400, msg="错误", data=str(e), status=status.HTTP_400_BAD_REQUEST)


class ActivityViewSet(viewsets.GenericViewSet, MyListMixin):
    serializer_class = ActivitySerializers
    queryset = Activity.objects.all()
    permission_classes = [IsAuthenticated,IsFormalMember]



class AuditViewSet(viewsets.GenericViewSet, MyListMixin):
    serializer_class = AuditSerializers
    permission_classes = [IsAuthenticated, IsFormalMember]

    def get_queryset(self):
        return Audit.objects.filter(audit_user = self.request.user)
    def create(self, request):
        """
        新建申请
        """
        rawdata = request.data
        try:
            s = AuditSerializers(data=rawdata, context={'request': request})
            if s.is_valid():
                s.save()
                return FormatResponse(code=201, msg="提交成功", data=s.data, status=status.HTTP_201_CREATED)
            else:
                return FormatResponse(code=400, msg="错误", data=str(s.errors),
                                      status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return FormatResponse(code=400, msg="提交失败", data=str(e), status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['delete'], detail=True)
    def delete(self, request, pk):
        """
        删除申请，此处的id为关联活动id
        """
        try:
            s = Audit.objects.get(relate_activity__id=pk,audit_user = request.user)
            s.delete()
            return FormatResponse(code=200, msg="删除成功", data="", status=status.HTTP_200_OK)
        except Exception as e:
            return FormatResponse(code=400, msg="错误", data=str(e), status=status.HTTP_400_BAD_REQUEST)

class DiaryViewSet(viewsets.GenericViewSet,MyListMixin):
    serializer_class = DiarySerializers
    queryset = Diary.objects.all()

    def get_queryset(self):
        return Diary.objects.filter(related_user=self.request.user)

    def update(self,request,pk):
        """
        编辑活动足迹
        """
        try:
            s = Diary.objects.get(id=pk)
            ser = DiarySerializers(instance=s, data=request.data, context={'request': request})
            if ser.is_valid():
                ser.save()
                return FormatResponse(code=201, msg="修改成功", data=ser.data, status=status.HTTP_201_CREATED)
            else:
                return FormatResponse(code=400, msg="错误", data=str(ser.errors),
                                      status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return FormatResponse(code=400, msg="错误", data=str(e), status=status.HTTP_400_BAD_REQUEST)

