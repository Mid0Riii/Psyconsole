from django.db import models
from myauth.models import CustomUser


class MbrBase(models.Model):
    class Meta:
        verbose_name = '成员基类'
        verbose_name_plural = verbose_name
        abstract = True

    # mbse_type = models.CharField(verbose_name='用户类型',
    #                              max_length=16,
    #                              choices=(('0', '未激活'), ('1', '普通会员'), ('2', '高级会员'), ('3', '理事会员')),
    #                              default='0',
    #                              )
    mbse_user = models.OneToOneField(CustomUser,
                                     on_delete=models.CASCADE,
                                     verbose_name='关联用户',
                                     )
    mbse_status = models.CharField(verbose_name='状态',
                                   max_length=128,
                                   choices=(('0', '已注册，未提交申请'), ('1', '申请审核中'),
                                            ('2', '申请驳回，请检查申请信息'), ('3', '审核通过，等待缴费'),
                                            ('4', '缴费校验中'), ('5', '缴费校验不通过，请重新确认'),
                                            ('6', '已成为正式会员'),
                                            ),
                                   default='1',
                                   )
    mbse_judge = models.TextField(verbose_name='协会审批意见',
                                  null=True,
                                  blank=True
                                  )
    mbse_code = models.CharField(verbose_name="会员编号",
                                 max_length=128,
                                 null=True,
                                 blank=True)
    mbse_exp = models.DateField(verbose_name='有效期',
                                null=True,
                                blank=True
                                )
    mbse_name = models.CharField(verbose_name="姓名",
                                 max_length=128,
                                 null=True,
                                 blank=True,
                                 default='空'
                                 )

    def mbse_identity(self):
        c = self.mbse_user
        print(c.get_identity_display())
        return c.get_identity_display()
    mbse_identity.short_description="用户身份"

