import os
import time
import pandas as pd
import urllib.request


def get_pic(zone, path, count):
    f = open('1.txt', 'a', encoding='utf-8')
    df = pd.read_csv('{}.csv'.format(zone))
    urls = df['url_c'].to_list()
    urls = list(set(urls))
    if not os.path.exists(path):
        os.makedirs(path)
    for url in urls[:]:
        try:
            urllib.request.urlretrieve(url, path + str(count).zfill(7) + "." + os.path.basename(url).split(".")[1])
            time.sleep(0.5)
            count += 1
        except:
            f.write(url + '\n')
        print(url)


if __name__ == '__main__':
    zone = 'shanghai'  # change
    path = "./pic/"  # change
    count = 0  # change
    get_pic(zone, path, count)
