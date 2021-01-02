import requests

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"

myurl = "https://movie.douban.com/top250"
header = {'user-agent': user_agent}

response = requests.get(myurl, headers=header)

print(response.text)

print(f"返回的状态码： {response.status_code}")
