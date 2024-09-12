import pandas as pd
import os
from senti_c import SentenceSentimentClassification
from opencc import OpenCC

os.chdir('./Data')

file_path = './Laotan Pickled Cabbage.xlsx'  # 替换为你的Excel文件路径
sheet_name = 'Tiktok'  # 替换为你的工作表名称
df = pd.read_excel(file_path, sheet_name=sheet_name)
data = df['comment content'].tolist()
cc = OpenCC('s2t')
sentence_classifier = SentenceSentimentClassification(logging_level="info")
test_data = [cc.convert(str(i)) for i in data]
result = sentence_classifier.predict(test_data, run_split=True, aggregate_strategy=False)
df['senti'] = result['Preds']

with pd.ExcelWriter(file_path, mode='a', engine='openpyxl') as writer:
    wb = writer.book  # openpyxl.workbook.workbook.Workbook 获取所有sheet
    wb.remove(wb[sheet_name])  # 删除需要覆盖的sheet
    df.to_excel(writer, sheet_name=sheet_name, index=False)
