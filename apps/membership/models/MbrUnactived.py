from .MbrCommon import MbrCommon

class MbrUnactived(MbrCommon):
    class Meta:
        verbose_name = '未激活用户'
        verbose_name_plural = verbose_name
        proxy = True
