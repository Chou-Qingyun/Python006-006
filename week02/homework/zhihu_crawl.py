import requests
from fake_useragent import UserAgent
from time import sleep
from lxml import etree

i = 0


def get_zhihu_json(url):
    """需要先完成登录之后，拿到get请求的include值"""
    global i
    ua = UserAgent(verify_ssl=False)
    header = {"User-Agent": ua.random}

    response = requests.get(url, headers=header)
    data_json = response.json()
    for value in data_json['data']:
        i = i + 1
        if i == 1:
            mode = 'w'
        else:
            mode = 'a'
        with open('answer.txt', mode) as f:
            f.write(f'第{i}-用户名：{value["author"]["name"]}\n\r')
            f.write(f'答案：{value["content"]}\n\r')


if __name__ == '__main__':
    inclue = input('请输入登录后get请求的include的值：')
    urls = tuple(f'https://www.zhihu.com/api/v4/questions/429820088/answers?include={inclue}&limit=5&offset={ page * 5}' for page in range(5))
    for url in urls:
        get_zhihu_json(url)
        sleep(5)