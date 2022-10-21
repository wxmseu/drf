from django.db import models


# Create your models here.
class UserInfo(models.Model):
    user_type_choice = (
        (1, '管理员'),
        (2, '普通用户'),
        (3, 'vip用户'),
        (4, '游客'),
    )
    username = models.CharField(verbose_name='用户名', max_length=64)
    user_type = models.SmallIntegerField(verbose_name='用户类型', choices=user_type_choice)
    password = models.CharField(verbose_name='密码', max_length=32)


class UserToken(models.Model):
    username = models.OneToOneField(verbose_name='用户名', to='UserInfo')
    token = models.CharField(verbose_name='token', max_length=128)
