from django.shortcuts import render
from django.http import HttpResponse
import requests
from fake_useragent import UserAgent
from lxml import etree
import re
from .models import Movie, Comment
from django.shortcuts import render

# Create your views here.
def index(request):
    movie_info = Movie.objects.all()[:10]

    return render(request, 'douban/index.html', locals())


# 电影热评
def comment(request, **param):
    movie_id = param['id']
    movie = Movie.objects.get(id=movie_id)
    list = Comment.objects.filter(movie_id=movie_id)
    sort = 0
    keyword = ''
    try:
        if request.GET['keyword']:
            keyword = request.GET['keyword'].strip()
            list = list.filter(content__icontains=keyword)
        if int(request.GET['sort']) == 1:
            sort = 1
            list = list.filter(star__gte=30)
    except (KeyError):
        num = list.count()
        return render(request, 'douban/comment.html', locals())
    num = list.count()
    return render(request, 'douban/comment.html', locals())

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