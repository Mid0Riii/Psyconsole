from django.db import models


class Activity(models.Model):
    class Meta:
        verbose_name = "活动管理"
        verbose_name_plural  =verbose_name

    def __str__(self):
        return self.act_title

    act_is_available = models.BooleanField(verbose_name="活动是否结束",
                                           null=True,
                                           blank=True,
                                           default=False
                                           )
    act_need_audit = models.BooleanField(verbose_name='是否需要审核',
                                         null=True,
                                         blank=True,
                                         default=False
                                         )
    act_title = models.CharField(verbose_name="活动标题",
                                 max_length=128,
                                 null=True,
                                 blank=True
                                 )
    act_date = models.DateField(verbose_name="活动时间",
                                null=True,
                                blank=True)
    act_loc = models.CharField(verbose_name="活动地点",
                               max_length=128,
                               null=True,
                               blank=True)
    act_method = models.CharField(verbose_name="活动方式",
                                  max_length=128,
                                  null=True,
                                  blank=True)
    act_description = models.CharField(verbose_name="活动描述",
                                       max_length=1024,
                                       null=True,
                                       blank=True
                                       )
