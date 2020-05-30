from django.db import models
from membership.models import MbrInc
from myauth.models import CustomUser


class OrderInc(models.Model):
    class Meta:
        verbose_name = '理事订单信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    # TODO oid生成规则
    relate_user = models.ForeignKey(CustomUser,
                                    verbose_name="关联用户",
                                    on_delete=models.CASCADE,
                                    )
    relate_member = models.ForeignKey(MbrInc,
                                      verbose_name="关联会员",
                                      on_delete=models.CASCADE,
                                      null=True,
                                      blank=True
                                      )

    name = models.CharField(verbose_name="姓名",
                            max_length=128,
                            null=True,
                            blank=True
                            )

    oid = models.CharField(verbose_name='订单号',
                           max_length=128,
                           null=True,
                           blank=True
                           )
    price = models.CharField(verbose_name='应缴金额',
                             max_length=128,
                             null=True,
                             blank=True
                             )
    method = models.CharField(verbose_name='缴费方式',
                              max_length=128,
                              null=True,
                              blank=True
                              )
    exp = models.CharField(verbose_name='会员有效期',
                           max_length=128,
                           null=True,
                           blank=True
                           )
    date = models.CharField(verbose_name='订单形成时间',
                            max_length=128,
                            null=True,
                            blank=True
                            )
    status = models.CharField(verbose_name='订单状态',
                              max_length=128,
                              choices=(('3000', '未缴费'), ('3001', '用户缴费，等待审核'), ('3002', '审核不通过'), ('3003', '审核通过')),
                              default='3000'
                              )

    def save(self, *args, **kwargs):
        super(OrderInc, self).save(*args, **kwargs)
        m = self.relate_member
        if self.status == '3003':
            m.mbse_status = '2006'
            m.save(update_fields=["mbse_status"])
        elif self.status == '3002':
            m.mbse_status = '2005'
            m.save(update_fields=["mbse_status"])
