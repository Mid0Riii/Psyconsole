from .MbrCommon import MbrCommon

class CommonFormal(MbrCommon):
    class Meta:
        verbose_name = '普通会员'
        verbose_name_plural = verbose_name
        proxy = True