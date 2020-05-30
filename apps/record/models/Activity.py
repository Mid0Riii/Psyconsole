from django.db import models


class Activity(models.Model):
    class Meta:
        verbose_name = "活动管理"
        verbose_name_plural  =verbose_name

    def __str__(self):
        return self.act_title

    act_is_available = models.BooleanField(verbose_name="活动是否结束",
                                           null=True,
                                           blank=True,
                                           default=False
                                           )
    act_need_audit = models.BooleanField(verbose_name='是否需要审核',
                                         null=True,
                                         blank=True,
                                         default=False
                                         )
    act_title = models.CharField(verbose_name="活动标题",
                                 max_length=128,
                                 null=True,
                                 blank=True
                                 )
    act_date = models.DateField(verbose_name="活动时间",
                                null=True,
                                blank=True)
    act_loc = models.CharField(verbose_name="活动地点",
                               max_length=128,
                               null=True,
                               blank=True)
    act_method = models.CharField(verbose_name="活动方式",
                                  max_length=128,
                                  null=True,
                                  blank=True)
    act_description = models.TextField(verbose_name="活动描述",
                                       null=True,
                                       blank=True
                                       )
    def save(self, *args,**kwargs):
        from .Audit import Audit
        from .Diary import Diary
        super(Activity, self).save(*args, **kwargs)
        if self.act_is_available==True:
            if self.act_need_audit:
                queryset = Audit.objects.filter(relate_activity=self,audit_status='4001')
                for q in queryset:
                    Diary.objects.create(related_act = self,related_user = q.audit_user,diary_title=self.act_title,diary_date = self.act_date,
                                         diary_loc = self.act_loc,diary_method = self.act_method)
            else:
                queryset = Audit.objects.filter(relate_activity=self)
                for q in queryset:
                    Diary.objects.create(related_act = self,related_user = q.audit_user,diary_title=self.act_title,diary_date = self.act_date,
                                         diary_loc = self.act_loc,diary_method = self.act_method)
