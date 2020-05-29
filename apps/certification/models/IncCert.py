from django.db import models
from membership.models import MbrCommon,MbrInc



class IncCert(models.Model):
    class Meta:
        verbose_name='单位证书'
        verbose_name_plural = verbose_name
    QRCode = models.ImageField(upload_to='QRCodes/inc/',
                               null=True,
                               blank=True)
    cert_code = models.CharField(verbose_name='证书编号',
                                 max_length=128,
                                 null=True,
                                 blank=True
                                 )
    mbr_code = models.DateField(verbose_name='会员编号',
                                null=True,
                                blank=True
                                )
    exp = models.DateField(verbose_name='有效期',
                                null=True,
                                blank=True
                                )