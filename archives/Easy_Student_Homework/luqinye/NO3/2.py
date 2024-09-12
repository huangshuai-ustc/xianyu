import requests
from bs4 import BeautifulSoup
from html.py import html2


def get_text(url):
    # 请求地址
    # url = 'https://www.lemonde.fr/idees/article/2023/04/03/guerre-en-ukraine-l-effort-militaire-de-la-france-n-est-pas-a-la-hauteur-de-ses-moyens_6168085_3232.html'
    # 用户代理

    headers = {
        "authority": "www.lemonde.fr",
        "method": "GET",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cookie": "euconsent-v2=CPpv0QAPpv0QAFzABBFRC8CsAP_AAH_AAAqIJTNf_X__b3_v-_7___t0eY1f9_7__-0zjhfdt-8N3f_X_L8X_2M7vF36tr4KuR4ku3bBIUdtHPncTVmx6olVrzPsbk2cr7NKJ_Pkmnsbe2dYGH9_n9_z_ZKZ7___f__7_______________________________________________________________________-8EmwCTDVuIAuxLHAm2jCKBECMKwkKoFABRQDC0QGEDq4KdlcBPrCJAAgFAEYEQIcAUYMAgAAAgCQiICQI8EAgAIgEAAIAFQiEABGwCCgAsBAIABQDQsUYoAhAkIMiIiKUwICJEgoJ7KhBKD_Q0whDrLACg0f8VCAiUAIVgRCQsHIcESAl4skCzFG-QAjACgFEqFagk9NAAA; lmd_consent=%7B%22userId%22%3A%223635a00f-0f43-424e-a8fc-4cb03246a5dc%22%2C%22timestamp%22%3A%221680709111.687987654%22%2C%22version%22%3A1%2C%22cmpId%22%3A371%2C%22displayMode%22%3A%22cookiewall%22%2C%22purposes%22%3A%7B%22analytics%22%3Atrue%2C%22ads%22%3Atrue%2C%22personalization%22%3Atrue%2C%22mediaPlatforms%22%3Atrue%2C%22social%22%3Atrue%7D%7D; atauthority=%7B%22name%22%3A%22atauthority%22%2C%22val%22%3A%7B%22authority_name%22%3A%22default%22%2C%22visitor_mode%22%3A%22optin%22%7D%2C%22options%22%3A%7B%22end%22%3A%222024-05-06T15%3A38%3A33.443Z%22%2C%22path%22%3A%22%2F%22%7D%7D; lmd_sso_twipe=%7B%22token%22%3A%22jms7e6MPZSi%2BBBLkjeNehEg9xcsntFbxxf5vjYZr2mk%3D%22%7D; lmd_a_s=skpeFS3ltnUntQM%2BplZuR2F7HPhZ4Ipv7b3Iq6LtInbae2LEB4qBtmyQlTKf6Zn8; lmd_a_ld=khKkSli6cgrAFgbT95hRfr4DOkcGROfPqEIkrwwH%2Fgg%3D; lmd_a_sp=skpeFS3ltnUntQM%2BplZuR2F7HPhZ4Ipv7b3Iq6LtInbae2LEB4qBtmyQlTKf6Zn8; lmd_a_m=jms7e6MPZSi%2BBBLkjeNehEg9xcsntFbxxf5vjYZr2mk%3D; lmd_a_c=1; lmd_ab=YQjCbhDutdKiTJrvVwoBZF1Re1JI3L3TMCoEe7zvXsqa%2F5td9PvhEM3FyS5Sr8BW8%2FHgy9tpu1k5%2FS%2BSAzDzQoPRRN0%3D; lmd_cap=_tvwjn0u17; user_session=vthfi9g2tgj9tljdn9uca1lohn",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62"
    }
    r = requests.get(url, headers=headers)
    # print(r.text)
    soup = BeautifulSoup(r.text, "lxml")  # 转换成beautifulsoup
    p = soup.find_all('p', attrs={"class": "article__paragraph"})  # 定位到滚动新闻处
    title = soup.find_all('h1', attrs={"class": "article__title article__title--opinion"})[0].text  # 定位到滚动新闻处
    # print(title)
    f = open("d:/Output/fr/{}.txt".format(title), "w", encoding="utf-8")
    text = [p[i].text for i in range(len(p))]
    for i in range(len(text)):
        f.writelines(text[i])
# for i in range(len(h2)):
#     title = h2[i].find_all("h2", attrs={"class": "post__live-container--title post__space-node"})[0].text
#     text = h2[i].find_all("p", attrs={"class": "post__live-container--answer-text post__space-node"})
#     if text:
#         f.writelines(title+"\n")
#         f.writelines("\t"+text[0].text+"\n")
# f = open("d:/1.txt", "w", encoding="utf-8")
# for i in range(len(span)):
#     if span[i]:
#         f.writelines("\t"+span[i][0].text+"\n")
