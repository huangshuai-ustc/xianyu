import requests
import re
from bs4 import BeautifulSoup

url = 'https://so.gushiwen.cn/shiwenv_3aed26d1fa99.aspx'  # 古诗词网址
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6)'}  # 请求头
r = requests.get(url, headers=headers)  # 发送requests请求
soup = BeautifulSoup(r.text, "lxml")  # 转换成beautifulsoup对象
poem = soup.find_all('div', attrs={"class": "contson"}, id="contson3aed26d1fa99")[0].text  # 定位到古诗词所在的位置并取出古诗词
# 对得到的文本清洗
poem = poem.replace("\r", "").replace("                    ", "").replace(" \n                ", "").replace("\n", "")
poem = re.split(r"\(.{5,15}\)", poem)  # 继续清洗
del (poem[-1])  # 继续清洗
with open("d:/luqinye.txt", "w") as f:  # 打开待写入的文件（d盘）
    f.writelines(poem)  # 写入古诗词
# with open("./22255040121.txt", "w") as f: #打开待写入的文件（当前文件夹）
#     f.writelines(poem)    #写入古诗词
print(poem)  # 输出一下看看
