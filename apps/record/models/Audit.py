from django.db import models
from .Activity import Activity
from myauth.models import CustomUser
from membership.models import MbrBase, MbrCommon


class Audit(models.Model):
    def __str__(self):
        return self.audit_member.mbse_name + self.relate_activity.act_title + "申请"

    class Meta:
        verbose_name = '活动参加申请管理'
        verbose_name_plural = verbose_name
        # 联合去重，类似联合主键
        unique_together = (("audit_user", "relate_activity"),)

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
    audit_member = models.ForeignKey(MbrCommon,
                                     verbose_name="关联会员信息",
                                     on_delete=models.CASCADE)
    audit_status = models.CharField(verbose_name="申请结果",
                                    choices=(('4000', '申请未处理'), ('4001', '申请通过'), ('4002', '申请拒绝')),
                                    max_length=128,
                                    default='4002',
                                    )

    def save(self, *args, **kwargs):
        self.audit_member = MbrCommon.objects.get(mbse_user=self.audit_user)
        if self.relate_activity.act_need_audit is False:
            self.audit_status = '4001'
        super(Audit, self).save(*args, **kwargs)
