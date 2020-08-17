from .MbrInc import MbrInc

class IncUnactived(MbrInc):
    """
        代理类，仅用来为xadmin提供视图所需要的模型
    """
    class Meta:
        verbose_name = '未激活机构'
        verbose_name_plural = verbose_name
        proxy = True