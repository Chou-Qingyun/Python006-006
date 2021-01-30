from django.db import models
# Create your models here.


class Type(models.Model):
    # 图书or电影
    # id = models.AutoField(primary_key=True) # Django会自动创建，并设置为主键
    name = models.CharField(max_length=20)


class Name(models.Model):
    # 作品名称和作者（主演）
    # id 自动创建
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    stars = models.CharField(max_length=5)
