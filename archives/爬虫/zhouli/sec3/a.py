# 基本包导入
import requests
import time
from bs4 import BeautifulSoup

url = 'http://suqian.gov.cn/cnsq/gbzfwj/202303/503a27463ab34342a0d82ad52e4c5d7f.shtml'
herder = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 '
                  'Safari/537.36 Edg/120.0.0.0',
    'Cookie': 'HWWAFSESID=34eab45ad5dcf6edab8; HWWAFSESTIME=1704963666963; csrfToken=WYwTwKAyWC_4kb4-R3waUJ3F; TYCID=f6d4ffc0b05f11ee8cee3395213947ec; sajssdk_2015_cross_new_user=1; bannerFlag=true; searchSessionId=1704965915.82172786; ssuid=585920458; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22311493483%22%2C%22first_id%22%3A%2218cf7c10c77478-05a3a4b2646ef8-4c657b58-1296000-18cf7c10c78480%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThjZjdjMTBjNzc0NzgtMDVhM2E0YjI2NDZlZjgtNGM2NTdiNTgtMTI5NjAwMC0xOGNmN2MxMGM3ODQ4MCIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjMxMTQ5MzQ4MyJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22311493483%22%7D%2C%22%24device_id%22%3A%2218cf7c10c77478-05a3a4b2646ef8-4c657b58-1296000-18cf7c10c78480%22%7D; tyc-user-info={%22state%22:%220%22%2C%22vipManager%22:%220%22%2C%22mobile%22:%2215305520142%22%2C%22userId%22:%22311493483%22}; tyc-user-info-save-time=1704967042540; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTMwNTUyMDE0MiIsImlhdCI6MTcwNDk2NzA0MSwiZXhwIjoxNzA3NTU5MDQxfQ.xQL-qSR3aXPmlS3G9nu8Ro0KfMrMFhpfV7Uh4qfo36Sy1-94JFvrS_q693I9nKLb2h7GI18p5JN0a3x8X8xvTQ; tyc-user-phone=%255B%252215305520142%2522%255D'
}
r = requests.get(url, headers=herder)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'lxml')
s = soup.find_all(attrs={'style': 'text-indent:2em;'})
comp = []
for i in s[1:]:
    comp.append(i.text.strip())
# print(comp)
# f = open('1.txt', 'w', encoding='utf-8')
# for _ in comp:
#     f.write(_)
#     f.write('\n')
link = []
for _ in comp:
    time.sleep(1)
    urls = 'https://www.tianyancha.com/search?key=' + _
    rs = requests.get(urls, headers=herder)
    rs.encoding = 'utf-8'
    soups = BeautifulSoup(rs.text, 'lxml')
    ss = soups.find('a', class_='index_alink__zcia5 link-click')['href']
    print(ss)
    link.append(ss)
ff = open('2.txt', 'w', encoding='utf-8')
for j, k in zip(link, comp):
    ff.write(j + k + '\n')
