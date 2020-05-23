from .MbrCommon import MbrCommon

class CommonAudit(MbrCommon):
    class Meta:
        verbose_name = '待审核普通会员'
        verbose_name_plural = verbose_name
        proxy = True