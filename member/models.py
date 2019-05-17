from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.postgres.fields import JSONField
from django.db import models


# Create your models here.


# Create your models here.
class Member(AbstractUser):
    """
    会员信息
    """
    objects = UserManager()

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    # 重载为了打印自定义的字符串
    def __unicode__(self):
        return self.username

    def __str__(self):
        return "User Class"


class EmailMember(models.Model):
    """
    订阅邮箱用户
    """
    email_member_number = models.CharField(max_length=32, null=False, verbose_name='订阅客户编号')
    email_member_email = models.CharField(max_length=32, null=False, verbose_name='订阅客户EMAIL')
    email_member_ip = models.CharField(max_length=64, null=False, verbose_name='订阅客户IP')
    email_member_address = models.CharField(max_length=64, null=False, verbose_name='订阅客户地址')
    email_member_ip_json = JSONField(db_index=True, verbose_name='订阅客户IP查询')
    email_member_is_activity = models.BooleanField(default=True, validators='订阅客户是否活动')
    email_member_OSVersion = models.CharField(max_length=64, null=False, verbose_name='订阅客户操作系统')  # 获取操作系统版本号
    email_member_add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    remarks = models.CharField(max_length=5000, null=False, verbose_name='备注')

    # 重载为了打印自定义的字符串
    def __unicode__(self):
        return self.email_member_email

    def __str__(self):
        return "Email Member Class"
