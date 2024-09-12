import jieba
import jieba.posseg as pseg
import pandas as pd
from matplotlib import pyplot as plt
from wordcloud import WordCloud
text = open('红楼梦.txt', 'r', encoding="utf-8").read()
text = text.split('\n')
name_list = open('红楼梦人名词库.txt', encoding='utf-8').read().split('\n')
list1, list2, list3 = [], [], []
for i in text:
    dict1 = dict([(x, 0) for x in name_list])
    for j in name_list:
        if j in i:
            dict1[j] += 1
    list1.append(dict1)
for i in range(len(list1)):
    my_dict = {key: value for key, value in list1[i].items() if value != 0}
    list2.append(my_dict)
for i in range(len(list2)):
    my_list = [x for x in list2 if x]
    list3.append(my_list)
keys_to_check = ['宝玉']
new_list = [d for d in list3[0] if set(keys_to_check) <= set(d.keys())]
result = {}
for d in new_list:
    for key, value in d.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
sorted_result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
name = [i for i in sorted_result.keys()][:12]
time = [i for i in sorted_result.values()][:12]
time[10] = time[10]+time[1]
name.remove('宝玉')
name.remove('黛玉')
time.remove(time[0])
time.remove(time[1])
result = dict(zip(name,time))
plt.figure(figsize=(10, 8), dpi=200)
font_path = "D:\\Data\\Fonts\\Aa方萌.ttf"
mask = plt.imread(r"枫叶.jpg")
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
wc = WordCloud(mask=mask, font_path=font_path, width=800, height=500, scale=2, mode="RGBA", background_color='white')
wc = wc.generate_from_frequencies(result)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.savefig("词云图2.png")
