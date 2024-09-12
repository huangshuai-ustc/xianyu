import time
from tqdm import trange
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
file_name = 'PN-COU Ag building to Dwelling.xlsx' # change 
df = pd.read_excel(file_name)
urls = df['url'].to_list()
decisions, statues, dates, typs = [], [], [], []
for i in trange(len(urls)):
    driver.get(urls[i])
    # try:
    #     decision = driver.find_element(By.CSS_SELECTOR, '#MainDetails > table:nth-child(1) > tbody > tr:nth-child(4) > td:nth-child(2)').text
    # except:
    #     decision = ''
    try:
        statu = driver.find_element(By.CSS_SELECTOR, '#MainDetails > table:nth-child(1) > tbody > tr:nth-child(5) > td:nth-child(2)').text
    except:
        statu = ''
    try:
        date = driver.find_element(By.CSS_SELECTOR, '#MainDetails > table:nth-child(3) > tbody > tr:nth-child(3) > td:nth-child(2)').text
    except:
        date = ''
    try:
        typ = driver.find_element(By.CSS_SELECTOR, '#MainDetails > table:nth-child(1) > tbody > tr:nth-child(6) > td:nth-child(2)').text
    except:
        typ = ''
    # decisions.append(decision)
    statues.append(statu)
    dates.append(date)
    typs.append(typ)
    time.sleep(2)
# df['decision'] = decisions
df['statu'] = statues
df['validated_data'] = dates
df['applicationType'] = typs
df.to_excel(file_name, index=False)
