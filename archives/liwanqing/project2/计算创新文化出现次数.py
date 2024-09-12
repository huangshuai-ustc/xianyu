import os
import re
from tqdm import tqdm
from collections import Counter
import pandas as pd

# 关键词列表
keywords = [
    "一流", "不断进步", "互动式", "促进", "创一流", "创作力", "创塑", "创想", "创想力", "创新",
    "创新力", "创新性", "创构", "创造", "创造力", "创造性", "创造性地", "创造才能", "创造精神", "创造者",
    "勇敢", "勇毅", "卓越", "博采", "发明创造", "变革时代", "塑造", "多方位", "完美", "实时",
    "开拓性", "心勇", "性能优越", "想象力", "才华", "斗志", "新创建", "新创意", "易于控制", "智造力",
    "更优越", "更新换代", "极效", "模块化", "灵活化", "热爱", "爱岗", "独创性", "眼光", "睿智",
    "科学园区", "科技时代", "突破性", "精毅", "缔造", "编造", "自尊", "自弘", "自强", "自豪",
    "至荣", "致邦", "英勇", "超前发展", "超越", "跨越", "转变观念", "革命性", "革新", "颠覆性",
    "首创", "骄傲", "高傲", "高性益", "高性能", "高效", "高精度", "高集成度"
]


# 定义函数计算关键词出现次数
def count_keywords_in_file(file_path, keywords):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        keyword_counts = Counter({keyword: content.count(keyword) for keyword in keywords})
    return keyword_counts


# 定义文件夹路径
folder_path = "./0123制造业管理层分析"
output_folder = "./创新性企业文化计算"
result = []
# 遍历文件夹
for file in tqdm(os.listdir(folder_path)):
    if file.endswith(".txt"):
        file_path = os.path.join(folder_path, file)
        year = re.search(r"_\d{4}", file).group()[1:]  # 从文件名获取年份
        stock_code = file.split("_")[0]  # 从文件名获取证券代码
        keyword_counts = count_keywords_in_file(file_path, keywords)
        total_count = sum(keyword_counts.values())  # 关键词总次数
        result.append([stock_code, year, total_count])

        # 将结果保存到DataFrame中
        # df = pd.DataFrame({"证券代码": [stock_code], "关键词出现次数": [total_count]})

        # 检查输出文件夹是否存在，不存在则创建
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # 保存结果到Excel
        # output_file = os.path.join(output_folder, f"output_{year}.xlsx")
df = pd.DataFrame(result)
df.to_excel('output_file.xlsx', header=["证券代码", '年份', "关键词出现次数"], index=False)
# with pd.ExcelWriter(output_file, mode='w', engine='openpyxl', if_sheet_exists='replace') as writer:
#     df.to_excel(writer, index=False)

# 代码运行完成提示
print("关键词统计完成并已保存到对应Excel文件中。")
