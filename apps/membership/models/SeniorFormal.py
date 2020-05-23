from .MbrCommon import MbrCommon

class SeniorFormal(MbrCommon):
    class Meta:
        verbose_name = '高级会员'
        verbose_name_plural = verbose_name
        proxy = True