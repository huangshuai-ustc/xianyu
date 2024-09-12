import time
import pandas as pd
from selenium import webdriver  # 调用浏览器驱动器
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select


def get_data():
    time.sleep(1)
    Application_Number = driver.find_elements(By.CSS_SELECTOR,
                                              '#results > div > div > div.results > div > table > tbody > tr > td:nth-child(1)')
    for _ in Application_Number:
        Application_Numbers.append(_.text)
    Location = driver.find_elements(By.CSS_SELECTOR,
                                    '#results > div > div > div.results > div > table > tbody > tr > td:nth-child(2)')
    for _ in Location:
        Locations.append(_.text)
    Proposal = driver.find_elements(By.CSS_SELECTOR,
                                    '#results > div > div > div.results > div > table > tbody > tr > td:nth-child(3)')
    for _ in Proposal:
        Proposals.append(_.text)


webdriver_path = r"D:\Download\IdmDownload\msedgedriver.exe"
user_data_dir = r"--user-data-dir=C:\Users\fjwyz\AppData\Local\Microsoft\Edge\User Data"
option = webdriver.EdgeOptions()
option.add_argument("--disable-blink-features=AutomationControlled")
option.add_argument(user_data_dir)
service = Service(executable_path=webdriver_path)
driver = webdriver.Edge(service=service, options=option)
url = 'https://plan.wychavon.gov.uk/Search/Advanced'
driver.get(url)
# Click - Wychavon
driver.find_element(By.CSS_SELECTOR, '#SearchPlanning').click()  # 点击搜索
# driver.find_element(By.CSS_SELECTOR, '#description').send_keys('xxx')  # Description Keyword
s1 = Select(driver.find_element(By.CSS_SELECTOR, '#ApplicationType'))  # Application Type下
s1.select_by_visible_text('GPDQ - agricultural to C3 dwellinghouse')
start_date = driver.find_element(By.CSS_SELECTOR, '#DateReceivedFrom')  # 开始日期输入框
start_date.click()  # 清空输入框内容
start_date.send_keys('01/05/2013')  # 发送开始时间
end_date = driver.find_element(By.CSS_SELECTOR, '#DateReceivedTo')  # 结束日期输入框
end_date.click()  # 清空输入框内容
end_date.send_keys('30/04/2023')  # 发送结束时间
driver.find_element(By.CSS_SELECTOR, '#submitBtn').click()  # 点击搜索
time.sleep(2)
data = []
Application_Numbers, Locations, Proposals, Application_Valid_Dates = [], [], [], []
result_number = driver.find_element(By.CSS_SELECTOR, '#results > div > div > div.pager > div > ul > li:nth-child(13) > a').text
get_data()
for i in range(int(result_number)-1):
    time.sleep(0.5)
    bu = driver.find_element(By.CSS_SELECTOR, '#results > div > div > div.pager > div > ul > li:nth-child(14) > a')
    bu.click()
    time.sleep(0.5)
    get_data()
for i in Application_Numbers:
    driver.get("https://plan.wychavon.gov.uk/Planning/Display/"+i)
    time.sleep(0.5)
    try:
        date = driver.find_element(By.CSS_SELECTOR,
                                   '#MainDetails > table:nth-child(3) > tbody > tr:nth-child(3) > td:nth-child(2)').text
    except:
        date = 'not found'
    Application_Valid_Dates.append(date)

data = [Proposals, Locations, Application_Numbers, Application_Valid_Dates]
# Converting list to DataFrame
df = pd.DataFrame(data).T
# Saving DataFrame to Excel
header = ['Proposals', 'Locations', 'Application_Numbers', 'Application_Valid_Dates']
df.to_excel('collected_data.xlsx', index=False, header=header)
print("Data collection complete and saved to collected_data.xlsx")



