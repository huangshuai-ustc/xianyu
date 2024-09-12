import time
import pandas as pd
from selenium import webdriver  # 调用浏览器驱动器
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


webdriver_path = r"D:\Download\IdmDownload\chromedriver-win64\chromedriver.exe"
user_data_dir = r"--user-data-dir=C:\\Users\\fjwyz\\AppData\\Local\\Google\\Chrome\\User Data"
option = webdriver.ChromeOptions()
# options.add_argument ( "--headless") # 开启无界面模式
option.add_argument(user_data_dir)
service = Service(executable_path=webdriver_path)
driver = webdriver.Chrome(service=service, options=option)
url = 'https://www.findmyaddress.co.uk/search'

driver.get(url)
driver.find_element(By.CSS_SELECTOR, '#fulladdress').send_keys('30 Sandacre Road, Manchester, M23 1AF')
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, '#ui-id-2').click()
try:
    info = driver.find_element(By.CSS_SELECTOR, '#popup-address-panel > table > tbody > tr:nth-child(1) > td').text
except:
    info = 'not found'
print(info)
