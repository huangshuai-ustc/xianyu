import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open("红楼梦.txt", encoding="utf-8") as f:
    text = f.read()
text = text.replace("\n", " ")
text_new = text.split()
name_list = open('红楼梦人名词库.txt', encoding='utf-8').read().split('\n')
df = pd.DataFrame(data=name_list, columns=['姓名'], index=None)
df['出现次数'] = df.apply(lambda x: len([k for k in text_new if x[u'姓名'] in k]), axis=1)
results = df.sort_values(by=['出现次数'], ascending=False)[:30]
result = dict(zip(results["姓名"], results["出现次数"]))
plt.figure(figsize=(10, 8), dpi=200)
font_path = "D:\\Data\\Fonts\\Aa方萌.ttf"
mask = plt.imread(r"枫叶.jpg")
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
wc = WordCloud(mask=mask, font_path=font_path, width=800, height=500, scale=2, mode="RGBA", background_color='white')
wc = wc.generate_from_frequencies(result)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.savefig("词云图1.png")
