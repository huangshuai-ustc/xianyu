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
file_name = 'Full Planning_use as.xlsx' # change
df = pd.read_excel(file_name)
urls = df['url'].to_list()
decisions, proposals, dates = [], [], []
for i in trange(len(urls)):
    driver.get(urls[i])
    try:
        statues = driver.find_element(By.ID, 'ApplicationStatuslist')
        statu = statues.find_element(By.CLASS_NAME, 'selected').text
    except:
        statu = ''
    proposals.append(statu)
    time.sleep(0.5)

df['statu'] = proposals
df.to_excel(file_name, index=False)
