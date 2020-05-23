from .MbrInc import MbrInc

class IncAudit(MbrInc):
    class Meta:
        verbose_name = '待审核理事单位'
        verbose_name_plural = verbose_name
        proxy = True  # 不会生成新的表