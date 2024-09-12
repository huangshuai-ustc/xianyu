import pandas as pd


df = pd.read_csv('y.csv')
list1 = ['2022年净利润', '2021年净利润', '2020年净利润', '2019年净利润', '2018年净利润', '2022年营业收入', '2021年营业收入',
         '2020年营业收入', '2019年营业收入', '2018年营业收入', '2022年资产负债率', '2021年资产负债率', '2020年资产负债率',
         '2019年资产负债率', '2018年资产负债率']
for x in list1:
    print(df[x])
    for i in range(len(df[x].values)):
        if df[x].values[i][-1] == '万':
            df[x].values[i] = round(float(df[x].values[i].split('万')[0]) / 10000, 2)
        elif df[x].values[i][-1] == '亿':
            df[x].values[i] = float(df[x].values[i].split('亿')[0])
        else:
            pass
df.to_csv('y.csv', index=False)

