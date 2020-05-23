from .MbrInc import MbrInc

class IncUnactived(MbrInc):
    class Meta:
        verbose_name = '未激活机构'
        verbose_name_plural = verbose_name
        proxy = True