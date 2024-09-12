import pandas as pd
import numpy as np


df = pd.read_excel('./1-2.xlsx')
number_of_inbound_tourists = df['入境旅游游客人数/万人'].apply(lambda x: np.log(x))
df = df.iloc[:, 2:]
for i in list(df.iloc[:, 2:].columns):
    Max = np.max(df[i])
    Min = np.min(df[i])
    df[i] = (df[i] - Min) / (Max - Min)

df.to_excel('./1-1.xlsx',index=False)
print(df)
