import time
import pandas as pd
from selenium import webdriver  # 调用浏览器驱动器
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException

webdriver_path = r"D:\Download\IdmDownload\chromedriver-win64\chromedriver.exe"
user_data_dir = r"--user-data-dir=C:\\Users\\fjwyz\\AppData\\Local\\Google\\Chrome\\User Data"
option = webdriver.ChromeOptions()
# options.add_argument ( "--headless") # 开启无界面模式
option.add_argument(user_data_dir)
service = Service(executable_path=webdriver_path)
driver = webdriver.Chrome(service=service, options=option)
df = pd.read_excel('Prior Approval Change of Use.xlsx')
url_list = df['url'].tolist()
decisions = []
for _ in url_list:
    driver.get(_)
    time.sleep(1)
    try:
        decision = driver.find_element(By.CSS_SELECTOR, '#simpleDetailsTable > tbody > tr:nth-child(8) > td').text
        decisions.append(decision)
    except:
        decisions.append('not found')
df['decision'] = decisions
df.to_excel('Prior Approval Change of Use.xlsx', index=False)

