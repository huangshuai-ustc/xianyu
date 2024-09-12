import time

from selenium import webdriver  # 调用浏览器驱动器
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd

webdriver_path = r"D:\Download\IdmDownload\chromedriver-win64\chromedriver.exe"
user_data_dir = r"--user-data-dir=C:\\Users\\fjwyz\\AppData\\Local\\Google\\Chrome\\User Data"
option = webdriver.ChromeOptions()
option.add_argument(user_data_dir)
service = Service(executable_path=webdriver_path)
driver = webdriver.Chrome(service=service, options=option)

with open('3.txt', 'r', encoding='utf-8') as f:
    links = f.readlines()
datas = []
for link in links:
    time.sleep(2)
    driver.get(link.strip().split(' ')[1])
    try:
        industry = driver.find_element(By.CSS_SELECTOR,
                                       '#page-root > div.page-container.relative > div > div.layout_company-header__C4hcj > div.layout_company-header-main__nuikF > div.layout_company-header-right__oIUZw > div.index_company-header-content__Ayzr2 > div.index_detail__JSmQM > div.index_detail-content__RCnTr > div.detail-item.index_detail-item-third__ukvtr > div:nth-child(1) > span.index_detail-text__Ac9Py.index_detail-tooltips__5QOeW').text
    except:
        industry = '未找到相关信息'
    try:
        scale = driver.find_element(By.CSS_SELECTOR,
                                    '#page-root > div.page-container.relative > div > div.layout_company-header__C4hcj > div.layout_company-header-main__nuikF > div.layout_company-header-right__oIUZw > div.index_company-header-content__Ayzr2 > div.index_detail__JSmQM > div.index_detail-content__RCnTr > div.detail-item.index_detail-item-third__ukvtr > div:nth-child(2) > span.index_detail-text__Ac9Py').text
    except:
        scale = '未找到相关信息'
    try:
        people = driver.find_element(By.CSS_SELECTOR,
                                     '#page-root > div.page-container.relative > div > div.layout_company-header__C4hcj > div.layout_company-header-main__nuikF > div.layout_company-header-right__oIUZw > div.index_company-header-content__Ayzr2 > div.index_detail__JSmQM > div.index_detail-content__RCnTr > div.detail-item.index_detail-item-third__ukvtr > div:nth-child(3) > span.index_detail-text__Ac9Py').text
    except:
        people = '未找到相关信息'
    try:
        income = driver.find_element(By.CSS_SELECTOR,
                                     '#page-root > div.page-container.relative > div > div.layout_company-header__C4hcj > div.layout_company-header-main__nuikF > div.layout_company-header-right__oIUZw > div.index_company-header-content__Ayzr2 > div.index_detail__JSmQM > div.index_detail-content__RCnTr > div.detail-item.index_detail-item-third__ukvtr > div:nth-child(4) > span.index_detail-text__Ac9Py.index_detail-tooltips__5QOeW > span').text
    except:
        income = '未找到相关信息'
    try:
        profit = driver.find_element(By.CSS_SELECTOR,
                                     '#page-root > div.page-container.relative > div > div.layout_company-header__C4hcj > div.layout_company-header-main__nuikF > div.layout_company-header-right__oIUZw > div.index_company-header-content__Ayzr2 > div.index_detail__JSmQM > div.index_detail-content__RCnTr > div.detail-item.index_detail-item-third__ukvtr > div:nth-child(5) > span.index_detail-text__Ac9Py.index_detail-tooltips__5QOeW > span').text
    except:
        profit = '未找到相关信息'
    data = [link.strip().split(' ')[0], industry, scale, people, income, profit]
    datas.append(data)
df = pd.DataFrame(datas)
df.to_excel('1.xlsx', header=['company', 'industry', 'scale', 'people', 'income', 'profit'], index=False)
