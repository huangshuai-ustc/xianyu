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
file_name = 'Change of Use_change of use.xlsx'
df = pd.read_excel(file_name)
urls = df['url'].to_list()
decisions = []
for i in trange(len(urls)):
    driver.get(urls[i])
    try:
        decision = driver.find_element(By.CSS_SELECTOR, '#Template > div > div.main > div > div:nth-child(4) > div > div > div:nth-child(8) > ul > li:nth-child(1) > div').text
    except:
        decision = ''
    decisions.append(decision.split()[-1])
    time.sleep(2)

df['validated_data'] = decisions
df.to_excel(file_name, index=False)
