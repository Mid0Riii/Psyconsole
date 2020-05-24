from django.db import models
from myauth.models import CustomUser
class Order(models.Model):
    class Meta:
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name
    #TODO oid生成规则
    user = models.ForeignKey(CustomUser,verbose_name="关联用户",on_delete=models.CASCADE)
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
                                  null=True,
                                  blank=True
                                  )
    # def save(self,*args,**kwargs):
    #     super(Order,self).save(*args,**kwargs)
    #     if self.
