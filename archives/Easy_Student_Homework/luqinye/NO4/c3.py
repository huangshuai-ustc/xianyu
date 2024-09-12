import requests
from bs4 import BeautifulSoup
import pandas as pd
from b3 import urls

f = open("result_ansi.csv", "a", encoding="utf-8")

def get_result(i):
    url = 'http://www.tianqihoubao.com' + i
    print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    div = soup.find_all("div", attrs={"class": "wdetail"})[0]
    table = div.find_all("table", attrs={"class": "b"})[0]
    td = table.find_all("td")
    tianqi = []
    for i in range(len(td)):
        x = td[i].text.replace("\n", "").replace("\r", "").replace(" ", "")
        tianqi.append(x)
    last_result = [tianqi[i:i + 4] for i in range(0, len(tianqi), 4)]
    del (last_result[0])
    df = pd.DataFrame(last_result)
    df.to_csv(f, header=False, index=False)


if __name__ == '__main__':
    for i in urls[108:]:
        get_result(i)
