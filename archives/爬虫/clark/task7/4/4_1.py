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
url = 'https://pa.shropshire.gov.uk/online-applications/search.do?action=advanced'

data, summaries, statuses, addresses,dates_validated, refs, applicationTypes, fromDates, toDates, urls = [],[],[],[],[],[],[],[],[],[]
decisions = []

def get_data(Application_Type):
    start_time = ['01/05/2013', '01/05/2014', '01/05/2015', '01/05/2016', '01/05/2017', '01/05/2018', '01/05/2019',
                  '01/05/2020', '01/05/2021', '01/05/2022']
    end_time = ['30/04/2014', '30/04/2015', '30/04/2016', '30/04/2017', '30/04/2018', '30/04/2019', '30/04/2020',
                '30/04/2021', '30/04/2022', '30/04/2023']
    for i in range(len(start_time)):
        driver.get(url)
        #driver.find_element(By.CSS_SELECTOR, '#description').send_keys('conversion')  # 这里是Description Keyword输入框
        s1 = Select(driver.find_element(By.ID, 'caseType'))  # 这里是Application Type下拉单选框
        s1.select_by_visible_text(Application_Type)
        start_date = driver.find_element(By.CSS_SELECTOR, '#applicationValidatedStart')  # 开始日期输入框
        start_date.click()  # 清空输入框内容
        start = start_time[i]
        start_date.send_keys(start)  # 发送开始时间
        end_date = driver.find_element(By.CSS_SELECTOR, '#applicationValidatedEnd')  # 结束日期输入框
        end_date.click()  # 清空输入框内容
        end = end_time[i]
        end_date.send_keys(end)  # 发送结束时间
        ##driver.find_element(By.CSS_SELECTOR,'#advancedSearchForm > div.buttons > input.button.primary.recaptcha-submit').click()  # 点击搜索
        driver.find_element(By.CSS_SELECTOR,
                            '#advancedSearchForm > div.buttons > input.button.primary').click()  # 点击搜索

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
            all_datas = driver.find_elements(By.CSS_SELECTOR, '#searchresults > li')
            for _ in all_datas:
                all_data = _.text.split('\n')
                summary = all_data[0]
                link = driver.find_element(By.LINK_TEXT, summary).get_attribute('href')
                address = all_data[1]
                Status = all_data[2].split(' | ')[2].split(': ')[-1]
                date_validated = all_data[2].split(' | ')[1].split(': ')[-1]
                ref = all_data[2].split(' | ')[0].split(': ')[-1]

                # Add new information here
                summaries.append(summary)
                addresses.append(address)
                statuses.append(Status)
                dates_validated.append(date_validated)
                refs.append(ref)
                applicationTypes.append(Application_Type)
                fromDates.append(start)
                toDates.append(end)
                urls.append(link)
                time.sleep(1)

        get_a_page_data()
        if number != 0:
            for _ in range(int((number - 1) / 10)):
                get_a_page_data()
                driver.find_element(By.CLASS_NAME, 'next').click()

        else:
            pass
    for _ in urls:
        driver.get(_)
        decision = driver.find_element(By.CSS_SELECTOR, '#simpleDetailsTable > tbody > tr:nth-child(8) > td').text
        decisions.append(decision)
        time.sleep(1)
        ##dates deleted temporally
    data = [summaries, addresses, refs, dates_validated, statuses, applicationTypes, fromDates, toDates, urls, decisions]
    df = pd.DataFrame(data).T
    header = ['summary', 'address', 'ref', 'validated_data', 'status', 'applicationType', 'fromdate', 'todate', 'url', 'decision']
    df.to_excel('{}.xlsx'.format(Application_Type), index=False, header=header)


if __name__ == '__main__':
    Application_Type = 'Prior App from Agricultural to Dwellings'
    get_data(Application_Type)
