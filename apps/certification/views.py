from django.shortcuts import render
from .models import MbrCert, IncCert
from rest_framework.views import APIView
from membership.models import MbrCommon
from myauth.models import CustomUser
import qrcode
import datetime
from utils.drf import FormatResponse
from django.conf import settings
from rest_framework import status
from .utils import generateCert


# Create your views here.


def MbrQRAuth(request, pk):
    try:
        MbrCert.objects.get(relate_member__mbse_code=pk)
        return render(request, 'apps/cert/AuthResult.html', {"data": True})
    except Exception as e:
        return render(request, 'apps/cert/AuthResult.html', {"data": False})


class GenerateCertfication(APIView):
    def get(self, request, *args, **kwargs):
        try:
            m = MbrCommon.objects.get(mbse_user=request.user)
            u = request.user
            year = datetime.datetime.strftime(m.mbse_exp, '%Y')
            mouth = datetime.datetime.strftime(m.mbse_exp, '%m')
            day = datetime.datetime.strftime(m.mbse_exp, '%d')

            base64img = generateCert(request, u.get_identity_display(), m.mbse_code, m.mbse_name, m.mbr_job, m.mbr_edu,
                                     m.mbr_graduate, m.mbr_cert, m.mbr_title,year,mouth,day,avatar=m.mbr_avatar)
            return FormatResponse(code=200, msg="成功", data={"base64img": base64img}, status=status.HTTP_200_OK)
        except Exception as e:
            return FormatResponse(code=400, msg="错误", data=str(e),
                                  status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        data = request.data
        u = request.user
        try:
            # print(data)
            type = data["type"]
            code = data["code"]
            name = data["name"]
            gender = data["gender"]
            unit = data["unit"]
            grade = data["grade"]
            title = data["title"]
            avai_year = data["avai_year"]
            avai_mouth = data["avai_mouth"]
            avai_day = data["avai_day"]
            avatar = data["avatar"]
            base64img = generateCert(request, type, code, name, gender, unit, grade, title, avai_year, avai_mouth,
                                     avai_day, u,
                                     avatar, b64=True)
            return FormatResponse(code=200, msg="成功", data={"base64img": base64img}, status=status.HTTP_200_OK)
        except Exception as e:
            return FormatResponse(code=400, msg="错误", data=str(e),
                                  status=status.HTTP_400_BAD_REQUEST)
