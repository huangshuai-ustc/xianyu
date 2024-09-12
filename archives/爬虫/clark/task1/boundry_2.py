import json
import pandas as pd
import requests
import os

def geocode_and_get_aoiid(excel_file, amap_api_key):
    # 读取Excel文件
    df = pd.read_excel(excel_file)

    # 定义高德API的URL
    amap_api_url_geocode = "https://restapi.amap.com/v3/geocode/geo?parameters"
    amap_api_url_place = "https://restapi.amap.com/v5/place/text?parameters"

    # 获取第19列的数据
    addresses = df.iloc[:, 18]  # 假设第19列是索引为18的列
    df.iloc[:, 18] = "深圳市" + addresses  # 让地址的指向性更强

    # 初始化新的列来存储地理坐标和AOI ID
    df["地理坐标"] = ""
    df["aoiid"] = ""

    # 遍历地址列表，并获取地理坐标和AOI ID
    for index, address in enumerate(addresses):
        # 发送逆地理编码请求
        params_geocode = {
            "key": amap_api_key,
            "address": "深圳市" + address,  # 在地址前添加"深圳市"
        }

        response_geocode = requests.get(amap_api_url_geocode, params=params_geocode)
        data_geocode = response_geocode.json()

        if response_geocode.status_code == 200:
            print("逆地理编码响应数据：", data_geocode)
        else:
            print("逆地理编码请求失败，状态码：", response_geocode.status_code)
            continue

        # 提取地理坐标
        if data_geocode["status"] == "1" and "geocodes" in data_geocode:
            geocode = data_geocode["geocodes"][0]
            location = geocode["location"]

            df.at[index, "地理坐标"] = location

        # 发送关键词搜索请求以获取AOI ID
        params_place = {
            "key": amap_api_key,
            "keywords": "深圳市" + address,  # 在地址前添加"深圳市"
        }

        response_place = requests.get(amap_api_url_place, params=params_place)
        data_place = response_place.json()

        if response_place.status_code == 200:
            print("关键词搜索响应数据：", data_place)
        else:
            print("关键词搜索请求失败，状态码：", response_place.status_code)
            continue

        # 提取AOI ID
        if data_place["status"] == "1" and "pois" in data_place:
            poi = data_place["pois"][0]
            poi_id = poi["id"]
            df.at[index, "aoiid"] = poi_id

    # 保存更新后的Excel文件
    # 获取当前脚本所在的文件夹路径
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 构建保存文件的完整路径
    output_excel_file = os.path.join(script_dir, "output_excel_file.xlsx")

    # 将数据保存到Excel文件
    df.to_excel(output_excel_file, index=False)

    print("逆地理编码和获取AOI ID完成，结果已保存到Excel文件。")

# 使用示例
excel_file_path = "xiaoqu_shenzhen_5_ceshi.xlsx"
amap_api_key = "cc6d29d9cdba914a194d111d40ddc95f"
geocode_and_get_aoiid(excel_file_path, amap_api_key)