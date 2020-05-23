from .MbrInc import MbrInc

class IncFromal(MbrInc):
    class Meta:
        verbose_name = '理事单位会员'
        verbose_name_plural = verbose_name
        proxy = True  # 不会生成新的表