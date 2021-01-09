import requests
from lxml import etree
from time import sleep


# 控制请求的频率，引入time模块

# 使用def定义请求的方法
def get_url_name(url):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

    headers = {'user-agent': ua}
    response = requests.get(url, headers=headers)

    selector = etree.HTML(response.text)
    # 电影名称
    film_name = selector.xpath('//div[@class="hd"]/a/span[1]/text()')

    # 电影链接
    film_link = selector.xpath('//div[@class="hd"]/a/@href')

    # 遍历对应关系字典
    film_info = dict(zip(film_name, film_link))

    for i in film_info:
        print(f'电影名称： {i} \t\t 电影链接: {film_info[i]}')


if __name__ == '__main__':
    # 生成包含所有页面的元祖
    urls = tuple(f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))

    for page in urls:
        get_url_name(page)
        sleep(5)
