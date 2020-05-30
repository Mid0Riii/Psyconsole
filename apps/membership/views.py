from .serializers import MbrCommonSerializers, MbrIncSerializers,MbrAvatarSerializers
from .models import MbrCommon, MbrInc
from rest_framework import status
from rest_framework import viewsets, filters
from rest_framework.mixins import ListModelMixin
from utils.drf import FormatResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django_filters import rest_framework as drf_filter
import django_filters


class MbrListMixin(ListModelMixin):
    def list(self, request, *args, **kwargs):
        try:
            response = super().list(request, *args, **kwargs)
            return FormatResponse(code=200, msg="获取成功", data=response.data, status=status.HTTP_200_OK)
        except Exception as e:
            return FormatResponse(code=400, msg="错误", data=str(e), status=status.HTTP_400_BAD_REQUEST)


class MemberViewSet(viewsets.GenericViewSet, MbrListMixin):
    serializer_class = MbrCommonSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MbrCommon.objects.filter(mbse_user=self.request.user)

    # @action(methods=['post'],detail=False)
    def create(self, request):
        """
        新建会员申请
        """
        rawdata = request.data
        try:
            s = MbrCommonSerializers(data=rawdata, context={'request': request})
            if s.is_valid():
                s.validated_data.mbse_user = request.user.id
                s.save()
                return FormatResponse(code=201, msg="提交成功", data=s.data, status=status.HTTP_201_CREATED)
            else:
                return FormatResponse(code=400, msg="错误", data=str(s.errors),
                                      status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return FormatResponse(code=400, msg="提交失败", data=str(e), status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['patch'], detail=True, url_path='update')
    def updateP(self, request, pk):
        """
        编辑会员申请
        """
        try:
            s = MbrCommon.objects.get(id=pk)
            ser = MbrCommonSerializers(instance=s, data=request.data, context={'request': request})
            if ser.is_valid():
                ser.save()
                return FormatResponse(code=201, msg="修改成功", data=ser.data, status=status.HTTP_201_CREATED)
            else:
                return FormatResponse(code=400, msg="错误", data=str(ser.errors),
                                      status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return FormatResponse(code=400, msg="错误", data=str(e), status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=False, )
    def is_user(self, request):
        """
        查询是否为本单位会员
        """
        data = request.data
        name = data['name']
        phone = data['phone']
        id = data['id']
        try:
            s = MbrCommon.objects.get(mbse_name=name, mbr_phone=phone, mbr_id_num=id)
            if s.mbse_status == '2006' and s.mbse_user.identity != '1000':
                return FormatResponse(code=200, msg="您是本协会的会员", data="", status=status.HTTP_200_OK)
            else:
                return FormatResponse(code=400, msg="未查询到符合条件的信息或申请正在审核中", data="", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return FormatResponse(code=400, msg="未查询到符合条件的信息或申请正在审核中", data=str(e), status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True)
    def MbrJudgePass(self, request, pk):
        try:
            s = MbrCommon.objects.get(id=pk)
            s.mbse_status = '2003'
            s.save()
            return FormatResponse(code=200, msg="成功", data="", status=status.HTTP_200_OK)
        except Exception as e:
            return FormatResponse(code=400, msg="错误", data=str(e), status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True)
    def MbrJudgeDeny(self, request, pk):
        try:
            s = MbrCommon.objects.get(id=pk)
            s.mbse_status = '2002'
            s.save()
            return FormatResponse(code=200, msg="成功", data="", status=status.HTTP_200_OK)
        except Exception as e:
            return FormatResponse(code=400, msg="错误", data=str(e), status=status.HTTP_400_BAD_REQUEST)
    # @action(methods=['delete'], detail=True)
    # def delete(self, request, pk):
    #     """
    #     删除会员申请
    #     """
    #     try:
    #         s = MbrCommon.objects.get(id=pk)
    #         s.delete()
    #         return FormatResponse(code=200, msg="删除成功", data="", status=status.HTTP_200_OK)
    #     except Exception as e:
    #         return FormatResponse(code=400, msg="错误", data=str(e), status=status.HTTP_400_BAD_REQUEST)


class IncViewSet(viewsets.GenericViewSet, MbrListMixin):
    serializer_class = MbrIncSerializers

    def get_queryset(self):

        return MbrInc.objects.filter(mbse_user=self.request.user)

    # @action(methods=['post'],detail=False)
    def create(self, request):
        """
        新建理事单位申请
        """
        rawdata = request.data
        try:
            s = MbrIncSerializers(data=rawdata, context={'request': request})
            if s.is_valid():
                s.save()
                return FormatResponse(code=201, msg="提交成功", data=s.data, status=status.HTTP_201_CREATED)
            else:
                return FormatResponse(code=400, msg="错误", data=str(s.errors),
                                      status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return FormatResponse(code=400, msg="提交失败", data=str(e), status=status.HTTP_400_BAD_REQUEST)

    # @action(methods=['patch'], detail=True,)
    def update(self, request, pk):
        """
        编辑理事单位申请
        """
        try:
            s = MbrInc.objects.get(id=pk)
            ser = MbrIncSerializers(instance=s, data=request.data, context={'request': request})
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
            s = MbrInc.objects.get(id=pk)
            s.mbse_status = '2003'
            s.save()
            return FormatResponse(code=200, msg="成功", data="", status=status.HTTP_200_OK)
        except Exception as e:
            return FormatResponse(code=400, msg="错误", data=str(e), status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True)
    def IncJudgeDeny(self, request, pk):
        try:
            s = MbrInc.objects.get(id=pk)
            s.mbse_status = '2002'
            s.save()
            return FormatResponse(code=200, msg="成功", data="", status=status.HTTP_200_OK)
        except Exception as e:
            return FormatResponse(code=400, msg="错误", data=str(e), status=status.HTTP_400_BAD_REQUEST)

#TODO CODEVIEW 比较好的图片上传逻辑：前端在用户选择图片后立刻上传，同时后端回传图片上传后的url

class AvatarViewSet(viewsets.GenericViewSet):
    serializer_class = MbrAvatarSerializers
    queryset = MbrCommon.objects.all()
    permission_classes = [IsAuthenticated]
    @action(methods=['post'],detail=True)
    def uploadImg(self,request,pk):
        try:
            s = MbrCommon.objects.get(id=pk)
            ser = MbrAvatarSerializers(instance=s,data=request.data)
            if ser.is_valid():
                ser.save()
                return FormatResponse(code=200, msg="成功", data=ser.data, status=status.HTTP_200_OK)
            else:
                return FormatResponse(code=400, msg="错误", data=str(s.errors), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return FormatResponse(code=400, msg="错误", data=str(e), status=status.HTTP_400_BAD_REQUEST)