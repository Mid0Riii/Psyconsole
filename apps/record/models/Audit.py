from django.db import models
from .Activity import Activity
from myauth.models import CustomUser
from membership.models import MbrBase,MbrCommon


class Audit(models.Model):

    class Meta:
        verbose_name = '活动参加申请管理'
        verbose_name_plural = verbose_name
    # def __str__(self):
    #     return str(self.relate_activity)+"-"+str(self.audit_name)

    relate_activity = models.ForeignKey(Activity,
                                        verbose_name="关联活动",
                                        on_delete=models.CASCADE
                                        )
    audit_user = models.ForeignKey(CustomUser,
                                   verbose_name="申请人账号",
                                   on_delete=models.CASCADE
                                   )

    audit_status = models.CharField(verbose_name="申请结果",
                                    choices=(('0','申请未处理'),('1','申请通过'),('2','申请拒绝')),
                                    max_length=128,
                                    default='0',
                                    )
    def audit_name(self):
        m = MbrCommon.objects.get(mbse_user = self.audit_user.id)
        return m.mbse_name

    def save(self, *args, **kwargs):
        super(Audit, self).save(*args, **kwargs)
        print(MbrCommon.objects.get(mbse_user=1))

