from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# Create your models here.
class UserProfile(AbstractUser):
    """
    主用户
    """
    objects = UserManager()

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    # 重载为了打印自定义的字符串
    def __unicode__(self):
        return self.username

    def __str__(self):
        return "User Class"


class PersonalProfile(UserProfile):
    """
    管理员功能
    """
    Clear_Password = models.CharField(max_length=16, null=False, default='123456')

    def __str__(self):
        return "Personal Profile"


class RootProfile(UserProfile):
    """
    主管理员
    """
    def __str__(self):
        return "RootProfile Profile"
