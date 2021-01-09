import requests

# 同一个 Session实例发出的所有请求之间保持cookie
s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456')
r = s.get("http://httpbin.org/cookies")

print(r.text)

# 会话可以使用上下文管理器
# with requests.Session() as s:
#     s.get("http://httpbin.org/cookies/set/sessioncookie/123456789")