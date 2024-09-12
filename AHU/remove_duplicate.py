import pandas as pd
zone = 'xxxx'
df = pd.read_csv('{}.csv'.format(zone))
df = df.drop_duplicates()
df.to_csv('{}.csv'.format(zone), index=False)
