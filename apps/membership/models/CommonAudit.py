from .MbrCommon import MbrCommon

class CommonAudit(MbrCommon):
    """
    代理类，仅用来为xadmin提供视图所需要的模型
    """
    class Meta:
        verbose_name = '待审核普通会员'
        verbose_name_plural = verbose_name
        proxy = True