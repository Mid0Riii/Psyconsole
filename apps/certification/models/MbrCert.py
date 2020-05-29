from django.db import models
from membership.models import MbrCommon
class MbrCert(models.Model):
    class Meta:
        verbose_name='个人证书'
        verbose_name_plural = verbose_name
    QRCode = models.ImageField(upload_to='QRCodes/inc/',
                               null=True,
                               blank=True)
    cert_type = models.CharField(verbose_name='证书类型',
                                 max_length=128,
                                 null=True,
                                 blank=True
                                 )
    relate_member = models.ForeignKey(MbrCommon,
                                      verbose_name='关联用户',
                                      on_delete=models.CASCADE,
                                      null=True,
                                      blank=True
                                      )