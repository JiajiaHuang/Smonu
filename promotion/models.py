from django.db import models

from blog.models import Blog
from user.models import UserProfile


class IconCollection(models.Model):
    """
    图标集合
    """
    icon_collection_number = models.CharField(max_length=32, null=False, verbose_name='图标编号')
    icon_collection_name = models.CharField(max_length=32, null=False, verbose_name='图标名称')
    icon_collection_alt = models.CharField(max_length=64, null=False, verbose_name='图标alt名称')
    icon_collection_url = models.CharField(max_length=64, null=False, verbose_name='图标链接')
    icon_collection_img = models.ImageField(upload_to="photo/icon/", verbose_name='产品样式照片')
    icon_collection_add_personnel = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default="",
                                                      verbose_name='添加人员')
    icon_collection_add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    icon_collection_change_time = models.DateTimeField(auto_now=True, verbose_name='更改时间')
    remarks = models.CharField(max_length=5000, null=False, verbose_name='备注')

    def __str__(self):
        return self.icon_collection_name


class FooterBlog(models.Model):
    footer_blog_number = models.ForeignKey(Blog, on_delete=models.CASCADE, default="", verbose_name='博客ID')
    footer_blog_add_personnel = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default="",
                                                  verbose_name='添加人员')
    footer_blog_add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    footer_blog_change_time = models.DateTimeField(auto_now=True, verbose_name='更改时间')
    remarks = models.CharField(max_length=5000, null=False, verbose_name='备注')


class WebInfo(models.Model):
    contact_name = models.CharField(max_length=32, null=False, verbose_name='联系名称')
    contact_content = models.CharField(max_length=256, null=False, verbose_name='联系内容')
    add_personnel = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default="",
                                      verbose_name='添加人员')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    change_time = models.DateTimeField(auto_now=True, verbose_name='更改时间')
    remarks = models.CharField(max_length=5000, null=False, verbose_name='备注')


class FooterInfo(models.Model):
    footer_info_name = models.CharField(max_length=32, null=False, verbose_name='信息名称')
    footer_info_content = models.CharField(max_length=32, null=False, verbose_name='信息内容')
    footer_info_url = models.CharField(max_length=32, null=False, verbose_name='信息URL')
    add_personnel = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default="",
                                      verbose_name='添加人员')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    change_time = models.DateTimeField(auto_now=True, verbose_name='更改时间')
    remarks = models.CharField(max_length=5000, null=False, verbose_name='备注')


class FooterPopular(models.Model):
    footer_popular_name = models.CharField(max_length=32, null=False, verbose_name='信息名称')
    footer_popular_content = models.CharField(max_length=32, null=False, verbose_name='信息内容')
    footer_popular_url = models.CharField(max_length=32, null=False, verbose_name='信息URL')
    add_personnel = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default="",
                                      verbose_name='添加人员')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    change_time = models.DateTimeField(auto_now=True, verbose_name='更改时间')
    remarks = models.CharField(max_length=5000, null=False, verbose_name='备注')
