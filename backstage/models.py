from django.db import models


# Create your models here.

class VisitorInfo(models.Model):
    visitor_info_number = models.CharField(max_length=32, null=False, verbose_name='访客编号')
    visitor_info_ip = models.CharField(max_length=32, null=False, verbose_name='访客IP')
    visitor_info_url = models.CharField(max_length=32, null=False, verbose_name='访客URL')
    visitor_info_device = models.CharField(max_length=32, null=False, verbose_name='访客设备')
    visitor_info_browser = models.CharField(max_length=32, null=False, verbose_name='访客浏览器')
    visitor_info_country = models.CharField(max_length=32, null=False, verbose_name='访客国家')
    visitor_info_source = models.CharField(max_length=32, null=False, verbose_name='访客来源')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    remarks = models.CharField(max_length=5000, null=False, verbose_name='备注')





