import pandas as pd
import os
from zhconv import convert
from senti_c import SentenceSentimentClassification

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "1,2,3,6"
# print(os.listdir())
os.chdir('./Data')

file_path = './Pre-packaged Food-.xlsx'  # 替换为你的Excel文件路径
sheet_name = 'Tiktok'  # 替换为你的工作表名称
df = pd.read_excel(file_path, sheet_name=sheet_name)
data = df['comment content'].tolist()
text_data = [convert(str(i), 'zh-tw') for i in data]
sentence_classifier = SentenceSentimentClassification(logging_level="info")
result = sentence_classifier.predict(text_data, run_split=True, aggregate_strategy=False)
df['senti'] = result['Preds']

with pd.ExcelWriter(file_path, mode='a', engine='openpyxl') as writer:
    wb = writer.book  # openpyxl.workbook.workbook.Workbook 获取所有sheet
    wb.remove(wb[sheet_name])  # 删除需要覆盖的sheet
    df.to_excel(writer, sheet_name=sheet_name, index=False)
