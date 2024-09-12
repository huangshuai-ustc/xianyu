import requests
import time
import pandas as pd
from bs4 import BeautifulSoup


url = 'https://shanghai.8684.cn/line2'
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Cookie': 'JSESSIONID=48304F9E8D55A9F2F8ACC14B7EC5A02D; wbf__voiceplg-is=false; tongue=1',
    'Host': 'shanghai.8684.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"'
}
r = requests.get(url=url, headers=header)
soup = BeautifulSoup(r.text, 'lxml')
a = soup.find(attrs={'class': "list clearfix"})
links = a.find_all('a')
result = []
for link in links:
    href = link.get('href')
    title = link.get('title')
    url = 'https://shanghai.8684.cn' + href
    print(url)
    r = requests.get(url=url, headers=header)
    soup = BeautifulSoup(r.text, 'lxml')
    li = soup.find(attrs={'class': 'bus-lzlist mb15'})
    UpStation = [i.text for i in li.find_all('a')]
    DownStation = UpStation[::-1]
    Numbers = len(UpStation)
    result.append([title, UpStation, DownStation, Numbers])
    time.sleep(0.3)
df_result = pd.DataFrame(result)
df_result.to_csv('results.csv', header=['BusLine', 'UpStations', 'DownStations', 'Numbers'], index=False)
