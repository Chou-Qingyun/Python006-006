from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField("电影名称", max_length=50)
    cover = models.CharField("电影封面", max_length=100)

class Comment(models.Model):
    content = models.TextField("短评内容", blank=False)
    star = models.SmallIntegerField("星级", blank=False)
    comment_info = models.CharField('用户名', max_length=50)
    avatar = models.CharField('头像', max_length=200)
    movie_id = models.IntegerField("电影id", blank=False)

