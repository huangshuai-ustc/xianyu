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
url = 'https://www3.somersetwestandtaunton.gov.uk/asp/webpages/plan/plapplookup.asp'

data, summaries, statuses, addresses,dates_validated, refs, applicationTypes, fromDates, toDates, urls = [],[],[],[],[],[],[],[],[],[]
appnums = []

def get_data(Application_Type):
    start_time = ['01/05/2013', '01/05/2014', '01/05/2015', '01/05/2016', '01/05/2017', '01/05/2018', '01/05/2019',
                  '01/05/2020', '01/05/2021', '01/05/2022']
    end_time = ['30/04/2014', '30/04/2015', '30/04/2016', '30/04/2017', '30/04/2018', '30/04/2019', '30/04/2020',
                '30/04/2021', '30/04/2022', '30/04/2023']
    for i in range(len(start_time)):
        driver.get(url)
        driver.find_element(By.CSS_SELECTOR, '#proposal').send_keys(Application_Type)  # 这里是Description Keyword输入框
        # s1 = Select(driver.find_element(By.ID, 'caseType'))  # 这里是Application Type下拉单选框
        # s1.select_by_visible_text(Application_Type)
        start_date = driver.find_element(By.CSS_SELECTOR, '#regdate1')  # 开始日期输入框
        start_date.click()  # 清空输入框内容
        start = start_time[i]
        start_date.send_keys(start)  # 发送开始时间
        end_date = driver.find_element(By.CSS_SELECTOR, '#regdate2')  # 结束日期输入框
        end_date.click()  # 清空输入框内容
        end = end_time[i]
        end_date.send_keys(end)  # 发送结束时间
        ##driver.find_element(By.CSS_SELECTOR,'#advancedSearchForm > div.buttons > input.button.primary.recaptcha-submit').click()  # 点击搜索
        driver.find_element(By.CSS_SELECTOR,
                            '#primary > form > div > input.SWTbutton').click()  # 点击搜索

        time.sleep(2)

        ##先检查是否是”没有搜索结果“或者“搜索结果太多”

        element_large = driver.find_elements(By.CSS_SELECTOR,
                                               "#pa > div:nth-child(4) > div.content > div.messagebox.errors > ul > li")
        if element_large:
            print(f"{Application_Type}，year: {start} 至 {end}，too much information")
            continue  # 或者执行其他操作

        no_elements = driver.find_elements(By.CSS_SELECTOR,
                                             "#pa > div:nth-child(4) > div.content > div.messagebox > ul > li")
        if no_elements:
            print(f"{Application_Type}，year: {start} 至 {end}，no result")
            continue  # 或者执行其他操作



        try:
            number = driver.find_element(By.CSS_SELECTOR, '#searchResultsContainer > p.pager.top > span.showing').text
            number = int(number.split('of ')[-1])
        except:
            number = 0

        def get_a_page_data():
            try:
                driver.find_element(By.CSS_SELECTOR, '#primary > form > input.SWTbutton').click()
            except:pass
            appnum = driver.find_elements(By.CSS_SELECTOR, '#primary > table > tbody > tr.zsubheader > td:nth-child(1)')
            for _ in appnum:
                appnums.append(_.text)
            summary = driver.find_elements(By.CSS_SELECTOR, '#primary > table > tbody > tr:nth-child(4) > td')
            for _ in summary:
                summaries.append(_.text)

            status = driver.find_elements(By.CSS_SELECTOR, '#primary > table > tbody > tr:nth-child(5) > td')
            for _ in status:
                statuses.append(_.text)
            date = driver.find_elements(By.CSS_SELECTOR, '#primary > table > tbody > tr.zsubheader > td.zAlignRight')
            for _ in date:
                dates_validated.append(_.text)
            for _ in range(len(appnums)):
                applicationTypes.append(Application_Type)
                fromDates.append(start)
                toDates.append(end)
                urls.append(url)
                time.sleep(1)

        get_a_page_data()
        # if number != 0:
        #     for _ in range(int((number - 1) / 10)):
        #         get_a_page_data()
        #         driver.find_element(By.CLASS_NAME, 'next').click()
        # else:
        #     pass
    ##dates deleted temporally
    data = [summaries, appnums, dates_validated, statuses, applicationTypes, fromDates, toDates, urls]
    df = pd.DataFrame(data).T
    header = ['summary', 'appnum', 'validated_data', 'status', 'applicationType', 'fromdate', 'todate', 'url']
    df.to_excel('{}.xlsx'.format(Application_Type), index=False, header=header)


if __name__ == '__main__':
    Application_Type = 'conversion'
    get_data(Application_Type)
