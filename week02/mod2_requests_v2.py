from pathlib import *
import sys
import requests

url = "https://movie.douban.com/top250"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"
header = {"user-agent": user_agent}

try: 
    response = requests.get(url, headers=header)
except requests.exceptions.ConnectTimeout as e:
    print(f"请求超时{e}")
    sys.exit(1)

# print(response.text)

path = Path(__file__)

path_parent = path.resolve().parent
# 建立新的目录
html_path = path_parent.joinpath('html')

if not html_path.is_dir():
    Path.mkdir(html_path)
    # Path(html_path).mkdir(mode=0o777)

page = html_path.joinpath('double.html')

# 上下文管理
try:
    with open(page, 'w', encoding='utf-8') as f:
        f.write(response.text)
except FileNotFoundError as e:
    print(f"文件无法打开：{e}")
except IOError as e:
    print(f"文件读写错误： {e}")
except Exception as e:
    print(e)