from django.db import models

# Create your models here.
from user.models import PersonalProfile, UserProfile


class Blog(models.Model):
    blog_number = models.CharField(max_length=32, null=False, verbose_name='博客编号')
    blog_url_name = models.CharField(max_length=1024, null=False, verbose_name='博客URL名称')
    blog_property_name = models.CharField(max_length=1024, null=False, verbose_name='博客属性')

    blog_title = models.CharField(max_length=1024, null=False, verbose_name='博客标题')
    blog_text = models.TextField(max_length=1000000, verbose_name=u"博客内容")
    blog_add_personnel = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default="", verbose_name='博客添加人员')
    blog_add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    blog_change_time = models.DateTimeField(auto_now=True, verbose_name='更改时间')
    remarks = models.CharField(max_length=5000, null=False, verbose_name='备注')

    def __str__(self):
        return self.blog_title

    class Meta:
        # ordering 用来指定文章排序，
        ordering = ['-blog_add_time']


class BlogProperty(models.Model):
    blog_property_number = models.CharField(max_length=32, null=False, verbose_name='博客属性编号')
    blog_property_name = models.CharField(max_length=1024, null=False, verbose_name='博客属性名称')
    blog_property_url = models.CharField(max_length=32, null=False, verbose_name='博客属性编号')
    blog_property_subclass = models.BooleanField(default=False, verbose_name='是否只为子类')
    blog_property_add_personnel = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default="", verbose_name='博客添加人员')
    blog_add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    blog_change_time = models.DateTimeField(auto_now=True, verbose_name='更改时间')
    remarks = models.CharField(max_length=5000, null=False, verbose_name='备注')

    def __str__(self):
        return self.blog_property_name

    class Meta:
        # ordering 用来指定文章排序，
        ordering = ['-blog_add_time']


