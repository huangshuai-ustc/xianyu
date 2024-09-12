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
file_name = 'Prior Approval.xlsx'
df = pd.read_excel(file_name)
urls = df['url'].to_list()
decisions, addresses = [], []
for i in trange(len(urls)):
    driver.get(urls[i])
    time.sleep(3)
    try:
        decision = driver.find_element(By.CSS_SELECTOR, '#applicationSummary > div > div > div > div > div:nth-child(1) > div > div > div:nth-child(15) > div.civicadetailtext.civica-appplancase-decisioncode').text
    except:
        decision = ''
    try:
        address = driver.find_element(By.CSS_SELECTOR, '#applicationSummary > div > div > div > div > div:nth-child(1) > div > div > div:nth-child(2) > div.civicadetailtext.civica-appplancase-premisesaddress').text
    except:
        address = ''
    addresses.append(address)
    decisions.append(decision)

df['address'] = addresses
df['decision'] = decisions
df.to_excel(file_name, index=False)
