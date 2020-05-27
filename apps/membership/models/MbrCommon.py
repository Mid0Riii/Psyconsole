from django.db import models
from .MbrBase import MbrBase
from django.utils.html import format_html


class MbrCommon(MbrBase):
    class Meta:
        verbose_name = '成员'
        verbose_name_plural = verbose_name
        abstract = False

    def __str__(self):
        return self.mbse_name

    mbr_avatar = models.ImageField(upload_to='avatars/',null=True,blank=True,verbose_name="照片")

    mbr_gender = models.CharField(verbose_name='性别',
                                  max_length=128,
                                  null=True,
                                  blank=True
                                  )
    mbr_birth = models.CharField(verbose_name='出生年月',
                                 max_length=128,
                                 null=True,
                                 blank=True
                                 )
    mbr_political = models.CharField(verbose_name='政治面貌',
                                     max_length=128,
                                     null=True,
                                     blank=True
                                     )
    mbr_folk = models.CharField(verbose_name='民族',
                                max_length=128,
                                null=True,
                                blank=True
                                )
    mbr_title = models.CharField(verbose_name='技术职称',
                                 max_length=128,
                                 null=True,
                                 blank=True
                                 )
    mbr_id_num = models.CharField(verbose_name='身份证号',
                                  max_length=128,
                                  null=True,
                                  blank=True
                                  )
    mbr_graduate = models.CharField(verbose_name='毕业院校及专业',
                                    max_length=128,
                                    null=True,
                                    blank=True
                                    )
    mbr_graduate_time = models.CharField(verbose_name='毕业时间',
                                         max_length=128,
                                         null=True,
                                         blank=True
                                         )
    mbr_training_ins = models.CharField(verbose_name='资格证培训机构',
                                        max_length=128,
                                        null=True,
                                        blank=True
                                        )
    mbr_training_date = models.CharField(verbose_name='培训时间',
                                         max_length=128,
                                         null=True,
                                         blank=True
                                         )
    mbr_job = models.CharField(verbose_name='工作单位及职务',
                               max_length=128,
                               null=True,
                               blank=True
                               )
    mbr_loc = models.CharField(verbose_name='通讯地址',
                               max_length=128,
                               null=True,
                               blank=True
                               )
    mbr_zip = models.CharField(verbose_name='邮编',
                               max_length=128,
                               null=True,
                               blank=True
                               )
    mbr_email = models.CharField(verbose_name='电子邮件',
                                 max_length=128,
                                 null=True,
                                 blank=True
                                 )
    mbr_phone = models.CharField(verbose_name='手机',
                                 max_length=128,
                                 null=True,
                                 blank=True
                                 )
    mbr_cert = models.CharField(verbose_name='心理咨询师级别',
                                max_length=128,
                                null=True,
                                blank=True
                                )
    mbr_cert_date = models.CharField(verbose_name='获证年份',
                                     max_length=128,
                                     null=True,
                                     blank=True
                                     )
    mbr_cert_code = models.CharField(verbose_name='证书编号',
                                     max_length=128,
                                     null=True,
                                     blank=True
                                     )
    mbr_achievement = models.TextField(verbose_name='近五年承担的科研课题；著作、学术论文',
                                       null=True,
                                       blank=True
                                       )

    objects = models.Manager()

    def save(self, *args, **kwargs):
        from financial.models import Order
        super(MbrCommon, self).save(*args, **kwargs)
        if self.mbse_status == '3' and self.mbse_user.identity == '1':

            Order.objects.update_or_create(relate_user=self.mbse_user,relate_member=self, name=self.mbse_name, price="60")
        elif self.mbse_status == '3' and self.mbse_user.identity == '2':
            Order.objects.update_or_create(relate_user=self.mbse_user,relate_member=self, name=self.mbse_name, price="100")


