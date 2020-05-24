from django.db import models
from .Activity import Activity
from .Audit import Audit
from myauth.models import CustomUser
class Diary(models.Model):

    class Meta:
        verbose_name = '活动足迹'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.related_act)+"-"+str(self.related_user)

    related_act = models.ForeignKey(Activity,
                                    verbose_name="关联活动",
                                    on_delete=models.CASCADE)
    related_user = models.ForeignKey(CustomUser,
                                     verbose_name="关联用户",
                                     on_delete=models.CASCADE)
    diary_title = models.CharField(verbose_name="活动标题",
                                 max_length=128,
                                 null=True,
                                 blank=True
                                 )
    diary_date = models.DateField(verbose_name="活动时间",
                                null=True,
                                blank=True)
    diary_loc = models.CharField(verbose_name="活动地点",
                               max_length=128,
                               null=True,
                               blank=True)
    diary_method = models.CharField(verbose_name="活动方式",
                                  max_length=128,
                                  null=True,
                                  blank=True)
    diary_exp = models.TextField(verbose_name="活动感悟",
                                 null=True,
                                 blank=True)
    diary_advice = models.TextField(verbose_name="活动建议",
                                    max_length=128,
                                    null=True,
                                    blank=True
                                    )