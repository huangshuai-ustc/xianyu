import wordcloud
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

f = open('d:/sorted.txt', 'r')  # 打开文件
word = f.read()  # 读取文件
f.close()  # 关闭文件
image = np.array(Image.open("C:/Users/fjwyz/Desktop/1.png"))  # 打开图像并转化为数字矩阵
font = "D:/Data/Fonts/Aa方萌.ttf"  # 指定字体格式文件路径
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
myWordcloud = wordcloud.WordCloud(scale=5,
                                  font_path=font,  # 设置字体
                                  mask=image,  # 设置造型背景
                                  background_color='white',  # 设置背景色
                                  max_words=100,  # 设置最大词数
                                  max_font_size=60,  # 字体最大值
                                  min_font_size=8,  # 字体最小值
                                  random_state=20)  # 随机数
myWordcloud.generate(word)  # 产生词云
plt.imshow(myWordcloud)  # 图像处理
plt.axis("off")  # 隐藏坐标
plt.show()  # 显示图像
myWordcloud.to_file('d:/result.jpg')  # 生成一个jpg格式的图像文件
