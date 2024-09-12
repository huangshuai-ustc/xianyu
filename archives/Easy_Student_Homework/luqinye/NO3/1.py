import requests


url = 'https://www.tongji.edu.cn/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6)'}  # 请求头
r = requests.get(url, headers=headers).content.decode("utf-8")  # 发送requests请求
print(r)
