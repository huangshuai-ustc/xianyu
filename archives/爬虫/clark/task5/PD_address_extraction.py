import time
import pandas as pd
from selenium import webdriver  # 调用浏览器驱动器
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

webdriver_path = r"D:\Download\IdmDownload\chromedriver-win64\chromedriver.exe"
user_data_dir = r"--user-data-dir=C:\\Users\\fjwyz\\AppData\\Local\\Google\\Chrome\\User Data"
option = webdriver.ChromeOptions()
option.add_argument("--disable-blink-features=AutomationControlled")
option.add_argument(user_data_dir)
service = Service(executable_path=webdriver_path)
driver = webdriver.Chrome(service=service, options=option)
url = 'https://plan.wychavon.gov.uk/Search/Advanced'

driver.get(url)
##Click - Wychavon
driver.find_element(By.CSS_SELECTOR, '#SearchPlanning').click()  # 点击搜索
##driver.find_element(By.CSS_SELECTOR, '#description').send_keys('xxx')  # Description Keyword
s1 = Select(driver.find_element(By.CSS_SELECTOR, '#ApplicationType'))  # Application Type下
s1.select_by_visible_text('GPDQ - agricultural to C3 dwellinghouse')
start_date = driver.find_element(By.CSS_SELECTOR, '#DateReceivedFrom')  # 开始日期输入框
start_date.click()  # 清空输入框内容
start_date.send_keys('01/05/2013')  # 发送开始时间
end_date = driver.find_element(By.CSS_SELECTOR, '#DateReceivedTo')  # 结束日期输入框
end_date.click()  # 清空输入框内容
end_date.send_keys('30/04/2023')  # 发送结束时间
driver.find_element(By.CSS_SELECTOR,
                    '#submitBtn').click()  # 点击搜索
time.sleep(2)
data = []


def navigate_to_next_page():
    try:
        next_button = driver.find_element(By.CSS_SELECTOR,
                                          '#results > div > div > div.pager > div > ul > li:nth-child(14) > a')
        next_button.click()
        return True
    except Exception as e:
        print("Last page reached or error navigating to next page:", e)
        return False


page = 1
while True:
    for i in range(1, 11):  # Corrected loop to iterate through numbers 1 to 10

        try:
            summary_selector = f'#results > div > div > div.results > div > table > tbody > tr:nth-child({i}) > td:nth-child(3)'
            summary = driver.find_element(By.CSS_SELECTOR, summary_selector).text
        except:
            summary = 'not found'
        try:
            address_selector = f'#results > div > div > div.results > div > table > tbody > tr:nth-child({i}) > td:nth-child(2)'
            address = driver.find_element(By.CSS_SELECTOR, address_selector).text
        except:
            address = 'not found'
        try:
            number_selector = f'#results > div > div > div.results > div > table > tbody > tr:nth-child({i}) > td:nth-child(1) > strong > a'
            number = driver.find_element(By.CSS_SELECTOR, number_selector).text
        except:
            number = 'not found'
        try:
            number_selector = f'#results > div > div > div.results > div > table > tbody > tr:nth-child({i}) > td:nth-child(1) > strong > a'
            driver.find_element(By.CSS_SELECTOR, number_selector).click()
            date_selector = '#MainDetails > table:nth-child(3) > tbody > tr:nth-child(3) > td:nth-child(2) > font > font'
            date = driver.find_element(By.CSS_SELECTOR, date_selector).text
            if '?' in date:
                driver.find_element(By.CSS_SELECTOR, '#searchresults > li:nth-child(1) > a').click()
                time.sleep(1)
                driver.find_element(By.ID, 'tab_documents').click()
                date = driver.find_element(By.CSS_SELECTOR,
                                           '#Documents > tbody > tr:nth-child(7) > td:nth-child(2)').text
        except:
            date = 'not found'

        data.append({
            'Summary': summary,
            'Address': address,
            'Number': number,
            'Date': date
        })
        if i < 10:
            driver.back()
            time.sleep(1)

    if not navigate_to_next_page():
        break  # Exit loop if no next page
    page += 1
    time.sleep(2)  # Adjust based on your page's response time

# Converting list to DataFrame
df = pd.DataFrame(data)
# Saving DataFrame to Excel
df.to_excel('collected_data.xlsx', index=False)
print("Data collection complete and saved to collected_data.xlsx")
