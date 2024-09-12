import requests

urls = []
for i in range(2021, 2023):
    for j in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
        urls.append('http://www.tianqihoubao.com/lishi/shanghai/month/' + str(i) + j + '.html')
print(urls)

for url in urls:
    r = requests.get(url)
    filename = url.split('/')[-1].split('.')[0]
    f = open('./html/{}天气.txt'.format(filename), 'wt', encoding='utf-8')
    f.write(r.text)
    f.close()
    print('写入' + filename + '天气成功！')
