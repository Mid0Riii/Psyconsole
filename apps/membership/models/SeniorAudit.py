from .MbrCommon import MbrCommon

class SeniorAudit(MbrCommon):
    """
    代理类，仅用来为xadmin提供视图所需要的模型
    """
    class Meta:
        verbose_name = '待审核高级会员'
        verbose_name_plural = verbose_name
        proxy = True