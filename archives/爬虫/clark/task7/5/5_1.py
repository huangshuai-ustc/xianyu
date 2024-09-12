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
url = 'https://planning.southderbyshire.gov.uk/'

data, summaries, statuses, addresses,dates_validated, refs, applicationTypes, fromDates, toDates, urls = [],[],[],[],[],[],[],[],[],[]


def get_data(Proposal_key_word):
    start_time = ['01/05/2013']
    end_time = ['30/04/2014']
    for i in range(len(start_time)):
        driver.get(url)
        #driver.find_element(By.CSS_SELECTOR, '#description').send_keys('conversion')  # 这里是Description Keyword输入框
        driver.find_element(By.CSS_SELECTOR, '#Mainpage_txtProposal').send_keys(Proposal_key_word)
        s1 = Select(driver.find_element(By.CSS_SELECTOR, '#Mainpage_FromDay'))  # 这里是Application Type下拉单选框
        s1.select_by_visible_text('01')
        s2 = Select(driver.find_element(By.CSS_SELECTOR, '#Mainpage_FromMonth'))  # 这里是Application Type下拉单选框
        s2.select_by_visible_text('May')
        s3 = Select(driver.find_element(By.CSS_SELECTOR, '#Mainpage_FromYear'))  # 这里是Application Type下拉单选框
        s3.select_by_visible_text('2013')
        s4 = Select(driver.find_element(By.CSS_SELECTOR, '#Mainpage_ToDay'))  # 这里是Application Type下拉单选框
        s4.select_by_visible_text('30')
        s5 = Select(driver.find_element(By.CSS_SELECTOR, '#Mainpage_ToMonth'))  # 这里是Application Type下拉单选框
        s5.select_by_visible_text('Apr')
        s6 = Select(driver.find_element(By.CSS_SELECTOR, '#Mainpage_ToYear'))  # 这里是Application Type下拉单选框
        s6.select_by_visible_text('2023')
        ##driver.find_element(By.CSS_SELECTOR,'#advancedSearchForm > div.buttons > input.button.primary.recaptcha-submit').click()  # 点击搜索
        driver.find_element(By.CSS_SELECTOR,'#Mainpage_cmdSearch').click()  # 点击搜索

        time.sleep(2)

        ##先检查是否是”没有搜索结果“或者“搜索结果太多”

        element_large = driver.find_elements(By.CSS_SELECTOR,
                                               "#pa > div:nth-child(4) > div.content > div.messagebox.errors > ul > li")
        if element_large:
            print(f"{Application_Type}，year: too much information")
            continue  # 或者执行其他操作

        no_elements = driver.find_elements(By.CSS_SELECTOR,
                                             "#pa > div:nth-child(4) > div.content > div.messagebox > ul > li")
        if no_elements:
            print(f"{Application_Type}，year: no result")
            continue  # 或者执行其他操作



        try:
            number = driver.find_element(By.CSS_SELECTOR, '#searchResultsContainer > p.pager.top > span.showing').text
            number = int(number.split('of ')[-1])
        except:
            number = 0

        def get_a_page_data():
            all_datas = driver.find_elements(By.CSS_SELECTOR, '#Mainpage_gridMain > tbody > tr > td')
            print(len(all_datas))
            print(all_datas[1].text)
            print(all_datas[2].text)
            print(all_datas[3].text)
            for _ in all_datas:
                all_data = _.text.split('\n')
                summary = all_data[0]
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
                fromDates.append('01/05/2013')
                toDates.append('30/04/2023')
                urls.append(url)
                time.sleep(1)

        get_a_page_data()
        if number != 0:
            for _ in range(int((number - 1) / 10)):
                get_a_page_data()
                driver.find_element(By.CLASS_NAME, 'next').click()

        else:
            pass
    ##dates deleted temporally
    data = [summaries, addresses, refs, dates_validated, statuses, applicationTypes, fromDates, toDates, urls]
    df = pd.DataFrame(data).T
    header = ['summary', 'address', 'ref', 'validated_data', 'status', 'applicationType', 'fromdate', 'todate', 'url']
    df.to_excel('{}.xlsx'.format(Application_Type), index=False, header=header)


if __name__ == '__main__':
    Application_Type = 'prior notification'
    get_data(Application_Type)
