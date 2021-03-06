from django.db import models
from myauth.models import CustomUser


class MbrBase(models.Model):
    """
    成员基类，字段前缀mbse
    该类存储在全部会员类型（普通会员、高级会员、理事单位）通用的字段
    抽象模型，不建表
    """

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
                                   choices=(('2000', '已注册，未提交申请'), ('2001', '申请审核中'),
                                            ('2002', '申请驳回，请检查申请信息'), ('2003', '审核通过，等待缴费'),
                                            ('2004', '缴费校验中'), ('2005', '缴费校验不通过，请重新确认'),
                                            ('2006', '已成为正式会员'),
                                            ),
                                   default='2001',
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
    class Meta:
        verbose_name = '成员基类'
        verbose_name_plural = verbose_name
        abstract = True # 抽象模型

    def mbse_identity(self):
        c = self.mbse_user
        # print(c.get_identity_display())
        return c.get_identity_display()

    mbse_identity.short_description = "用户身份"
