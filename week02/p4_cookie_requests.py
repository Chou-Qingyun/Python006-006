import time
import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
headers = {
    'User-Agent': ua.random,
    'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony'
}

s = requests.Session()
# 会话对象：在同一个 Session 实例发出的所有请求之间保持 cookie,
# 期间使用urllib3的connection pooling 功能。
# 向同一主机发送多个请求，底层的TCP连接将会被重用，从而带来显著的性能提升。
login_url = 'https://accounts.douban.com/j/mobile/login/basic'
form_data = {
    "ck": '',
    "remember": "true",
    "name": '',
    "password": ''
}

response = s.post(login_url, data=form_data, headers=headers)

# 登陆后可以进行后续的请求
# url2 = "https://accounts.douban.com/passport/setting"
#
# response2 = s.get(url2, headers=headers)
# response3 = newsession.get(url3, headers=headers, cookies = s.cookies)
#
# with open('profile.html', 'w+') as f:
#     f.write(response2.txt)
