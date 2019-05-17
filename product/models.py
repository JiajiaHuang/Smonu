from django.contrib.postgres.forms import JSONField
from django.db import models

# Create your models here.
from user.models import UserProfile


class Products(models.Model):
    product_number = models.CharField(max_length=16, null=False, verbose_name='产品编号')
    product_name = models.CharField(max_length=64, null=False, verbose_name='产品名称')
    product_current_price = models.FloatField(null=False, verbose_name='产品现价')
    product_original_price = models.FloatField(null=False, verbose_name='产品原价')
    product_property = models.IntegerField(null=False, verbose_name='产品类别')
    product_add_personnel = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default="",
                                              verbose_name='产品添加人员')
    product_add_time = models.DateTimeField(auto_now_add=True, verbose_name='产品添加时间')
    product_change_time = models.DateTimeField(auto_now=True, verbose_name='产品更改时间')
    product_description = models.TextField(max_length=1000000, verbose_name=u"产品介绍内容")
    product_introduction = models.TextField(max_length=1000, verbose_name=u"产品简介内容")
    product_video = models.BooleanField(default=False, verbose_name=u"产品视频存在")
    Remarks = models.CharField(max_length=5000, null=False, verbose_name='备注')

    def __str__(self):
        return self.product_name

    class Meta:
        # ordering 用来指定文章排序，
        ordering = ['-product_add_time']


def get_file_path(instance, filename):
    return 'file/document/%s/%s/%s' % (
        instance.product_style_product_number.product_number, instance.product_style_attributes, filename)


class ProductStyle(models.Model):
    product_style_number = models.CharField(max_length=16, null=False, verbose_name='产品样式编号')
    product_style_product_number = models.ForeignKey(Products, on_delete=models.CASCADE, default="",
                                                     verbose_name='产品编号')
    product_style_name = models.CharField(max_length=64, null=False, verbose_name='产品样式名称')
    product_style_attributes = models.CharField(max_length=16, null=False, verbose_name='产品样式属性')
    product_style_img = models.ImageField(upload_to=get_file_path, verbose_name='产品样式照片')
    product_style_amount = models.IntegerField(default=1, null=False, verbose_name='产品样式数量')
    product_add_personnel = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default="",
                                              verbose_name='产品添加人员')
    product_add_time = models.DateTimeField(auto_now_add=True, verbose_name='产品添加时间')
    product_change_time = models.DateTimeField(auto_now=True, verbose_name='产品更改时间')
    remarks = models.CharField(max_length=5000, null=False, verbose_name='备注')

    def __str__(self):
        return self.product_style_name

    class Meta:
        # ordering 用来指定文章排序，
        ordering = ['-product_add_time']


class ProductVideo(models.Model):
    product_video_product_number = models.ForeignKey(Products, on_delete=models.CASCADE, default="",
                                                     verbose_name='产品编号')
    product_video_name = models.CharField(max_length=64, null=False, verbose_name='产品视频名称')
    product_video_url = models.CharField(max_length=64, null=False, verbose_name='产品视频链接')
    product_add_personnel = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default="",
                                              verbose_name='产品添加人员')
    product_add_time = models.DateTimeField(auto_now_add=True, verbose_name='产品添加时间')
    product_change_time = models.DateTimeField(auto_now=True, verbose_name='产品更改时间')
    remarks = models.CharField(max_length=5000, null=False, verbose_name='备注')

    def __str__(self):
        return self.product_video_name

    class Meta:
        # ordering 用来指定文章排序，
        ordering = ['-product_add_time']


class ProductStylePicture(models.Model):
    product_style_picture_product_number = models.ForeignKey(ProductStyle, on_delete=models.CASCADE, default="",
                                                             verbose_name='产品样式编号')
    product_style_picture_name = models.CharField(max_length=64, null=False, verbose_name='产品样式图片名称')
    product_style_picture_url = models.ImageField(upload_to=get_file_path, verbose_name='产品样式照片')
    product_add_personnel = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default="",
                                              verbose_name='产品添加人员')
    product_add_time = models.DateTimeField(auto_now_add=True, verbose_name='产品添加时间')
    product_change_time = models.DateTimeField(auto_now=True, verbose_name='产品更改时间')
    remarks = models.CharField(max_length=5000, null=False, verbose_name='备注')

    def __str__(self):
        return self.product_style_picture_name

    class Meta:
        # ordering 用来指定文章排序，
        ordering = ['-product_add_time']


class ProductAttributeSpecs(models.Model):
    product_picture_product_number = models.ForeignKey(Products, on_delete=models.CASCADE, default="",
                                                       verbose_name='产品编号')
    product_attrinute = JSONField(db_index=True, verbose_name='产品属性规格')
    product_add_personnel = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default="",
                                              verbose_name='产品添加人员')
    product_add_time = models.DateTimeField(auto_now_add=True, verbose_name='产品添加时间')
    product_change_time = models.DateTimeField(auto_now=True, verbose_name='产品更改时间')
    remarks = models.CharField(max_length=5000, null=False, verbose_name='备注')

    def __str__(self):
        return self.product_picture_product_number.product_name

    class Meta:
        # ordering 用来指定文章排序，
        ordering = ['-product_add_time']


class ProductPicture(models.Model):
    product_picture_product_number = models.ForeignKey(Products, on_delete=models.CASCADE, default="",
                                                       verbose_name='产品编号')
    product_picture_name = models.CharField(max_length=64, null=False, verbose_name='产品图片名称')
    product_picture_url = models.CharField(max_length=64, null=False, verbose_name='产品图片链接')
    product_add_personnel = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default="",
                                              verbose_name='产品添加人员')
    product_add_time = models.DateTimeField(auto_now_add=True, verbose_name='产品添加时间')
    product_change_time = models.DateTimeField(auto_now=True, verbose_name='产品更改时间')
    remarks = models.CharField(max_length=5000, null=False, verbose_name='备注')

    def __str__(self):
        return self.product_picture_name

    class Meta:
        # ordering 用来指定文章排序，
        ordering = ['-product_add_time']


class ProductNew(models.Model):
    product_new = models.ForeignKey(Products, on_delete=models.CASCADE, default="", verbose_name='产品编号')
    product_add_personnel = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default="", null=True,
                                              verbose_name='产品添加人员')
    product_add_time = models.DateTimeField(auto_now_add=True, verbose_name='产品添加时间')
    product_change_time = models.DateTimeField(auto_now=True, verbose_name='产品更改时间')
    remarks = models.CharField(max_length=5000, null=False, verbose_name='备注')

    def __str__(self):
        return self.product_new

    class Meta:
        # ordering 用来指定文章排序，
        ordering = ['-product_add_time']
