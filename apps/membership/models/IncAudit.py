from .MbrInc import MbrInc

class IncAudit(MbrInc):
    """
    代理类，仅用来为xadmin提供视图所需要的模型
    """
    class Meta:
        verbose_name = '待审核理事单位'
        verbose_name_plural = verbose_name
        proxy = True  # 不会生成新的表