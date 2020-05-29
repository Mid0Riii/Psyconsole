from django.shortcuts import render
from .models import MbrCert, IncCert
from rest_framework.views import APIView
import qrcode
from utils.drf import FormatResponse
from django.conf import settings
from rest_framework import status


# Create your views here.

def generateQRcode(code, host):
    url = host+"/cert/"+str(code)+"/"
    img = qrcode.make(url)
    imgurl = settings.MEDIA_ROOT +"/cert/"+ code + '.png'
    print(imgurl)
    with open(imgurl, 'wb') as f:
        img.save(f)


def MbrQRAuth(request, pk):
    try:
        MbrCert.objects.get(relate_member__mbse_code=pk)
        return render(request, 'apps/cert/AuthResult.html', {"data": True})
    except Exception as e:
        return render(request, 'apps/cert/AuthResult.html', {"data": False})


class GenerateCertfication(APIView):
    def get(self, request, *args, **kwargs):
        try:
            m = MbrCert.objects.get(relate_member__mbse_user=request.user)
            generateQRcode(m.relate_member.mbse_code, request.get_host())
            return FormatResponse(code=200,msg="成功",data="",status=status.HTTP_200_OK)
        except Exception as e:
            return FormatResponse(code=400, msg="错误", data=str(e),
                                  status=status.HTTP_400_BAD_REQUEST)
