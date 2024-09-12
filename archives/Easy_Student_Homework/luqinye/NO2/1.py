import requests
import re
from bs4 import BeautifulSoup

url = 'https://hanyu.baidu.com/shici/detail?from=kg1&highlight=&pid=19051ffdf85065b36b918eff8d4221f2&srcid=51369'  # 古诗词网址
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6)'}  # 请求头
r = requests.get(url, headers=headers)  # 发送requests请求
soup = BeautifulSoup(r.text, "lxml")  # 转换成beautifulsoup对象
# print(soup)
poem = soup.find_all('div', attrs={"class": "poem-detail-main-text"})[0].text  # 定位到古诗词所在的位置并取出古诗词
# 对得到的文本清洗
poem = poem.replace("  　　", "")
poem = re.sub(r"\(.*\)", "",poem)  # 继续清洗
with open("d:/luqinye.txt", "w",encoding="utf-8") as f:  # 打开待写入的文件
    f.writelines(poem)  # 写入散文
print(poem)  # 输出一下看看
