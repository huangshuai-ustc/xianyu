import time
import pandas as pd
from selenium import webdriver  # 调用浏览器驱动器
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

webdriver_path = r"D:\Download\IdmDownload\chromedriver-win64\chromedriver.exe"
user_data_dir = r"--user-data-dir=C:\\Users\\fjwyz\\AppData\\Local\\Google\\Chrome\\User Data"
option = webdriver.ChromeOptions()
# options.add_argument ( "--headless") # 开启无界面模式
option.add_argument(user_data_dir)
service = Service(executable_path=webdriver_path)
driver = webdriver.Chrome(service=service, options=option)
url = 'https://pa.manchester.gov.uk/online-applications/search.do?action=advanced&searchType=Application'

driver.get(url)
# driver.find_element(By.CSS_SELECTOR, '#description').send_keys('xxx')  # 这里是Description Keyword输入框
s1 = Select(driver.find_element(By.ID, 'caseType'))  # 这里是Application Type下拉单选框
s1.select_by_visible_text('Prior approval - agricultual to dwelling')
start_date = driver.find_element(By.CSS_SELECTOR, '#applicationValidatedStart')  # 开始日期输入框
start_date.click()  # 清空输入框内容
start_date.send_keys('01/05/2013')  # 发送开始时间
end_date = driver.find_element(By.CSS_SELECTOR, '#applicationValidatedEnd')  # 结束日期输入框
end_date.click()  # 清空输入框内容
end_date.send_keys('01/01/2023')  # 发送结束时间
driver.find_element(By.CSS_SELECTOR,
                    '#advancedSearchForm > div.buttons > input.button.primary.recaptcha-submit').click()  # 点击搜索
time.sleep(2)
try:
    summary = driver.find_elements(By.CSS_SELECTOR, '#searchresults > li:nth-child(1) > a')
except:
    summary = 'not found'
try:
    address = driver.find_elements(By.CSS_SELECTOR, '#searchresults > li:nth-child(1) > p.address')
except:
    address = 'not found'
# try:
#     number = driver.find_element(By.CSS_SELECTOR, '').text
# except:
#     number = 'not found'
dates = []
try:
    date = driver.find_elements(By.CSS_SELECTOR, '#searchresults > li:nth-child(1) > p.metaInfo')
    for i in range(len(date)):
        if '?' in date[i].text:
            driver.find_element(By.CSS_SELECTOR, '#searchresults > li:nth-child(1) > a').click()
            time.sleep(1)
            driver.find_element(By.ID, 'tab_documents').click()
            dates[i] = driver.find_element(By.CSS_SELECTOR, '#Documents > tbody > tr:nth-child(7) > td:nth-child(2)').text
            driver.back()
except:
    date = 'not found'
for i in range(len(date)):
    print(summary[i].text)
    print(address[i].text)
    # print(number)
    print(date[i].text)
