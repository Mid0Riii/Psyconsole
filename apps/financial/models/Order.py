from django.db import models
from myauth.models import CustomUser
from membership.models import MbrCommon, MbrInc


class Order(models.Model):
    class Meta:
        verbose_name = '个人订单信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    # TODO oid生成规则
    relate_user = models.ForeignKey(CustomUser,
                                    verbose_name="关联用户",
                                    on_delete=models.CASCADE,
                                    )
    relate_member = models.ForeignKey(MbrCommon,
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
                              choices=(('0', '未缴费'), ('1', '用户缴费，等待审核'), ('2', '审核不通过'), ('3', '审核通过')),
                              default=0
                              )

    def save(self, *args, **kwargs):
        from certification.models import MbrCert
        super(Order, self).save(*args, **kwargs)
        m = self.relate_member
        if self.status == '3':
            m.mbse_status = 6
            m.save(update_fields=["mbse_status"])
            MbrCert.objects.update_or_create(relate_member = self.relate_member)
        elif self.status == '2':
            m.mbse_status = 5
            m.save(update_fields=["mbse_status"])


