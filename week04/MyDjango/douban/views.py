from django.shortcuts import render
from django.http import HttpResponse
import requests
from fake_useragent import UserAgent
from lxml import etree
import re
from .models import Movie, Comment

# Create your views here.
def index(request):
    movie_info = Movie.objects.all()[:1]
    id = movie_info[0].id
    comments = Comment.objects.all()[:20]

    for comment in comments:
        print(comment.comment_info)
    return HttpResponse('index')

def scrapy(request):
    ua = UserAgent(verify_ssl=False)
    headers = {
        'User-Agent': ua.random
    }
    url = 'https://movie.douban.com/subject/30458949/comments?status=P'
    r = requests.get(url, headers=headers)
    html = etree.HTML(r.text)
    # 获取电影名称和封面

    movie_cover = html.xpath('//div[@class="movie-pic"]//img[1]/@src')
    movie_name = html.xpath('//div[@id="content"]/h1/text()')

    movie = Movie(name=movie_name[0].strip(), cover=movie_cover[0])
    movie.save()
    movie_id = movie.id

    comments = html.xpath('//div[@class="comment-item "]')
    for comment in comments:
        avatar = comment.xpath('./div[@class="avatar"]//img[1]/@src')
        account = comment.xpath('./div[@class="avatar"]/a[1]/@title')
        content = comment.xpath('./div[@class="comment"]/p/span/text()')
        star_res = comment.xpath('./div[@class="comment"]/h3/span[@class="comment-info"]/span[@class]')
        res = re.search(r"allstar(\d{2})", star_res[0].values()[0])
        star = res.group(1)
        comment = Comment(content=content[0].strip(), star=star, comment_info=account[0].strip(), avatar=avatar[0], movie_id=movie_id)
        comment.save()

    return HttpResponse('ok')