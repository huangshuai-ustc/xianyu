import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('./1-2.xlsx')

df_nko, df_in, df_indo, df_jp = df[df['国家'] == '朝鲜'], df[df['国家'] == '印度'], df[df['国家'] == '印度尼西亚'], df[df['国家'] == '日本']
df_ma, df_mong, df_fe, df_si = df[df['国家'] == '马来西亚'], df[df['国家'] == '蒙古'], df[df['国家'] == '菲律宾'], df[df['国家'] == '新加坡']
df_sko, df_th, df_eu, df_eng = df[df['国家'] == '韩国'], df[df['国家'] == '泰国'], df[df['国家'] == '欧洲'], df[df['国家'] == '英国']
df_ge, df_fr, df_it, df_he = df[df['国家'] == '德国'], df[df['国家'] == '法国'], df[df['国家'] == '意大利'], df[df['国家'] == '荷兰']
df_pu, df_swe, df_swi, df_ru = df[df['国家'] == '葡萄牙'], df[df['国家'] == '瑞典'], df[df['国家'] == '瑞士'], df[df['国家'] == '俄罗斯']
df_nam, df_ca, df_am, df_oc = df[df['国家'] == '北美洲'], df[df['国家'] == '加拿大'], df[df['国家'] == '美国'], df[df['国家'] == '大洋洲及太平洋地区']
df_as, df_nsi = df[df['国家'] == '澳大利亚'], df[df['国家'] == '新西兰']
x = df_nko['年份']
y1, y2, y3, y4 = df_nko['x1'], df_in['x1'], df_indo['x1'], df_jp['x1']
y5, y6, y7, y8 = df_ma['x1'], df_mong['x1'], df_fe['x1'], df_si['x1']
y9, y10, y11, y12 = df_sko['x1'], df_th['x1'], df_eu['x1'], df_eng['x1']
y13, y14, y15, y16 = df_ge['x1'], df_fr['x1'], df_it['x1'], df_he['x1']
y17, y18, y19, y20 = df_pu['x1'], df_swe['x1'], df_swi['x1'], df_ru['x1']
y21, y22, y23, y24 = df_nam['x1'], df_ca['x1'], df_am['x1'], df_oc['x1']
y25, y26 = df_as['x1'], df_nsi['x1']
colors = sns.color_palette("hls", 26)
plt.plot(x, y1, label='朝鲜',color=colors[0])
plt.plot(x, y2, label='印度',color=colors[1])
plt.plot(x, y3, label='印度尼西亚',color=colors[2])
plt.plot(x, y4, label='日本',color=colors[3])
plt.plot(x, y5, label='马来西亚',color=colors[4])
plt.plot(x, y6, label='蒙古',color=colors[5])
plt.plot(x, y7, label='菲律宾',color=colors[6])
plt.plot(x, y8, label='新加坡',color=colors[7])
plt.plot(x, y9, label='韩国',color=colors[8])
plt.plot(x, y10, label='泰国',color=colors[9])
plt.plot(x, y11, label='欧洲',color=colors[10])
plt.plot(x, y12, label='英国',color=colors[11])
plt.plot(x, y13, label='德国',color=colors[12])
plt.plot(x, y14, label='法国',color=colors[13])
plt.plot(x, y15, label='意大利',color=colors[14])
plt.plot(x, y16, label='荷兰',color=colors[15])
plt.plot(x, y17, label='葡萄牙',color=colors[16])
plt.plot(x, y18, label='意瑞典',color=colors[17])
plt.plot(x, y19, label='瑞士',color=colors[18])
plt.plot(x, y20, label='俄罗斯',color=colors[19])
plt.plot(x, y21, label='北美洲',color=colors[20])
plt.plot(x, y22, label='加拿大',color=colors[21])
plt.plot(x, y23, label='美国',color=colors[22])
plt.plot(x, y24, label='大洋洲及太平洋地区',color=colors[23])
plt.plot(x, y25, label='澳大利亚',color=colors[24])
plt.plot(x, y26, label='新西兰',color=colors[25])
plt.legend(bbox_to_anchor=(1.0, 1.0))#图例
plt.scatter(x, y1, label='朝鲜',color=colors[0])
plt.scatter(x, y2, label='印度',color=colors[1])
plt.scatter(x, y3, label='印度尼西亚',color=colors[2])
plt.scatter(x, y4, label='日本',color=colors[3])
plt.scatter(x, y5, label='马来西亚',color=colors[4])
plt.scatter(x, y6, label='蒙古',color=colors[5])
plt.scatter(x, y7, label='菲律宾',color=colors[6])
plt.scatter(x, y8, label='新加坡',color=colors[7])
plt.scatter(x, y9, label='韩国',color=colors[8])
plt.scatter(x, y10, label='泰国',color=colors[9])
plt.scatter(x, y11, label='欧洲',color=colors[10])
plt.scatter(x, y12, label='英国',color=colors[11])
plt.scatter(x, y13, label='德国',color=colors[12])
plt.scatter(x, y14, label='法国',color=colors[13])
plt.scatter(x, y15, label='意大利',color=colors[14])
plt.scatter(x, y16, label='荷兰',color=colors[15])
plt.scatter(x, y17, label='葡萄牙',color=colors[16])
plt.scatter(x, y18, label='意瑞典',color=colors[17])
plt.scatter(x, y19, label='瑞士',color=colors[18])
plt.scatter(x, y20, label='俄罗斯',color=colors[19])
plt.scatter(x, y21, label='北美洲',color=colors[20])
plt.scatter(x, y22, label='加拿大',color=colors[21])
plt.scatter(x, y23, label='美国',color=colors[22])
plt.scatter(x, y24, label='大洋洲及太平洋地区',color=colors[23])
plt.scatter(x, y25, label='澳大利亚',color=colors[24])
plt.scatter(x, y26, label='新西兰',color=colors[25])
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlabel("年份", fontdict={'size': 16})
plt.ylabel("客源地GDP/亿", fontdict={'size': 16})
plt.title("2013-2018年间来川旅游国家或地区客源地GDP折线图", fontdict={'size': 18})
plt.show()
