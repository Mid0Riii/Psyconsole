from .MbrBase import MbrBase
from django.db import models


class MbrInc(MbrBase):
    """
    理事单位基类
    """
    inc_loc = models.CharField(verbose_name='所在地区及办公地址',
                               max_length=128,
                               null=True,
                               blank=True
                               )
    inc_code = models.CharField(verbose_name='邮编',
                                max_length=128,
                                null=True,
                                blank=True
                                )
    inc_phone = models.CharField(verbose_name='电话',
                                 max_length=128,
                                 null=True,
                                 blank=True
                                 )
    inc_fax = models.CharField(verbose_name='传真',
                               max_length=128,
                               null=True,
                               blank=True
                               )
    inc_email = models.CharField(verbose_name='电子邮箱',
                                 max_length=128,
                                 null=True,
                                 blank=True
                                 )
    inc_site = models.CharField(verbose_name='网址',
                                max_length=128,
                                null=True,
                                blank=True
                                )
    inc_charge = models.CharField(verbose_name='主管机关',
                                  max_length=128,
                                  null=True,
                                  blank=True
                                  )
    inc_charge_code = models.CharField(verbose_name='组织机构代码',
                                       max_length=128,
                                       null=True,
                                       blank=True
                                       )
    inc_corporate = models.CharField(verbose_name='法人代表',
                                     max_length=128,
                                     null=True,
                                     blank=True
                                     )
    inc_corp_phone = models.CharField(verbose_name='法人代表联系方式',
                                      max_length=128,
                                      null=True,
                                      blank=True
                                      )
    inc_director = models.CharField(verbose_name='推举理事',
                                    max_length=128,
                                    null=True,
                                    blank=True
                                    )
    inc_director_phone = models.CharField(verbose_name='理事手机',
                                          max_length=128,
                                          null=True,
                                          blank=True
                                          )
    inc_opinion = models.TextField(verbose_name="审批理事单位负责人意见",
                                   null=True,
                                   blank=True,
                                   )
    inc_info = models.TextField(verbose_name='备注',
                                null=True,
                                blank=True
                                )

    class Meta:
        verbose_name = '理事单位会员'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.mbse_name

    # 逻辑相同，参考MbrCommon的save方法
    def save(self, *args, **kwargs):
        from financial.models import OrderInc
        super(MbrInc, self).save(*args, **kwargs)
        if self.mbse_status == '2003' and self.mbse_user.identity == '1003':
            OrderInc.objects.update_or_create(relate_user=self.mbse_user, relate_member=self, name=self.mbse_name)
