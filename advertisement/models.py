from django.db import models

# Create your models here.
from product.models import Products
from user.models import UserProfile


class IndexNotice(models.Model):
    """
    首页通知：
    """
    index_notice_number = models.CharField(max_length=32, null=False, verbose_name='通知编号')
    index_notice_content = models.CharField(max_length=255, null=False, verbose_name='通知内容')
    index_notice_particular = models.BooleanField(default=False, null=False, verbose_name='通知特别')
    index_notice_add_personnel = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default="",
                                                   verbose_name='博客添加人员')
    index_notice_add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    index_notice_change_time = models.DateTimeField(auto_now=True, verbose_name='更改时间')
    remarks = models.CharField(max_length=5000, null=False, verbose_name='备注')

    # 重载为了打印自定义的字符串
    def __unicode__(self):
        return self.index_notice_content

    def __str__(self):
        return "IndexNotice Class"


class IndexCarousel(models.Model):
    """
    首页轮播图
    """
    index_carousel_number = models.CharField(max_length=32, null=False, verbose_name='首页轮播编号')
    index_carousel_product_number = models.ForeignKey(Products, on_delete=models.CASCADE, default="",
                                                      verbose_name='首页轮播编号')
    index_carousel_grade = models.IntegerField(max_length=2, null=False, verbose_name='首页轮播标志号')
    index_carousel_personnel = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default="",
                                                 verbose_name='添加人员')
    index_carousel_add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    index_carousel_change_time = models.DateTimeField(auto_now=True, verbose_name='更改时间')
    remarks = models.CharField(max_length=5000, null=False, verbose_name='备注')

    # 重载为了打印自定义的字符串
    def __unicode__(self):
        return self.index_carousel_number

    def __str__(self):
        return "IndexNotice Class"


class ShowVideo(models.Model):
    show_video_number = models.CharField(max_length=32, null=False, verbose_name='视频编号')
    show_video_position_name = models.CharField(max_length=32, null=False, verbose_name='视频位置名称')
    show_video_url = models.CharField(max_length=64, null=False, verbose_name='视频链接')
    show_video_url_name = models.CharField(max_length=64, null=False, verbose_name='视频名称')
    show_video_personnel = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default="",
                                             verbose_name='添加人员')
    index_carousel_add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    index_carousel_change_time = models.DateTimeField(auto_now=True, verbose_name='更改时间')
    remarks = models.CharField(max_length=5000, null=False, verbose_name='备注')

    # 重载为了打印自定义的字符串
    def __unicode__(self):
        return self.show_video_url_name

    def __str__(self):
        return "ShowVideo Class"


class SocialSites(models.Model):
    social_site_number = models.CharField(max_length=32, null=False, verbose_name='社交网站编号')
    social_site_url = models.CharField(max_length=32, null=False, verbose_name='社交网站链接')
    social_site_url_name = models.CharField(max_length=32, null=False, verbose_name='社交网站链接名称')
    social_site_name = models.CharField(max_length=32, null=False, verbose_name='社交网站用户名称')
    social_site_icon = models.CharField(max_length=255, null=False, verbose_name='社交网站图标')
    show_video_personnel = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default="",
                                             verbose_name='添加人员')
    index_carousel_add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    index_carousel_change_time = models.DateTimeField(auto_now=True, verbose_name='更改时间')
    remarks = models.CharField(max_length=5000, null=False, verbose_name='备注')
