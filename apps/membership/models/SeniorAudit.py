from .MbrCommon import MbrCommon

class SeniorAudit(MbrCommon):
    class Meta:
        verbose_name = '待审核高级会员'
        verbose_name_plural = verbose_name
        proxy = True