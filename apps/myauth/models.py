from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None, ):
        if not username:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
        )
        user.is_active = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email):
        user = self.create_user(
            username=username,
        )
        user.set_password(password)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    objects = MyUserManager()
    id = models.AutoField(verbose_name="id", primary_key=True)
    username = models.CharField(max_length=255, verbose_name="用户名", unique=True)
    phone = models.CharField(max_length=128, verbose_name="手机号", null=True, blank=True)
    identity = models.CharField(verbose_name='用户类型',
                                max_length=16,
                                choices=(('0', '未激活'), ('1001', '普通会员'), ('1002', '高级会员'), ('1003', '理事会员')),
                                default='0',
                                )

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_staff
