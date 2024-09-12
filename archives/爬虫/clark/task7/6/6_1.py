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
url = 'https://southhams.planning-register.co.uk/Search/Advanced'

data, summaries, statuses, addresses, dates_validated, refs, applicationTypes, fromDates, toDates, urls = [], [], [], [], [], [], [], [], [], []
Application_Numbers, Locations, Proposals, Statuses = [], [], [], []


def get_data(Application_Type):
    start_time = ['01/05/2013']
    end_time = ['30/04/2023']
    for i in range(len(start_time)):
        driver.get(url)
        driver.find_element(By.CSS_SELECTOR, '#SearchPlanning').click()
        s1 = Select(driver.find_element(By.ID, 'ApplicationType'))  # 这里是Application Type下拉单选框
        s1.select_by_visible_text(Application_Type)
        start_date = driver.find_element(By.CSS_SELECTOR, '#DateReceivedFrom')  # 开始日期输入框
        start_date.click()  # 清空输入框内容
        start = start_time[i]
        start_date.send_keys(start)  # 发送开始时间
        end_date = driver.find_element(By.CSS_SELECTOR, '#DateReceivedTo')  # 结束日期输入框
        end_date.click()  # 清空输入框内容
        end = end_time[i]
        end_date.send_keys(end)  # 发送结束时间
        ##driver.find_element(By.CSS_SELECTOR,'#advancedSearchForm > div.buttons > input.button.primary.recaptcha-submit').click()  # 点击搜索
        driver.find_element(By.CSS_SELECTOR, '#submitBtn').click()  # 点击搜索

        time.sleep(2)

        ##先检查是否是”没有搜索结果“或者“搜索结果太多”
        try:

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
        except:
            pass

        try:
            number = driver.find_element(By.CSS_SELECTOR,
                                         '#ModuleButtons > ul.background2.controls.controls-row.hidden-phone > li > a > p').text
            number = int(number.split('(')[-1].split(')')[0])
        except:
            number = 0

        def get_a_page_data():
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
            Status = driver.find_elements(By.CSS_SELECTOR,
                                          '#results > div > div > div.results > div > table > tbody > tr > td:nth-child(4)')
            for _ in Status:
                Statuses.append(_.text)
            time.sleep(3)

        get_a_page_data()
        if number != 0:
            t = int((number - 1) / 10)
            for _ in range(t):
                if t > 10:
                    get_a_page_data()
                    driver.find_element(By.CSS_SELECTOR,
                                        '#results > div > div > div.pager > div > ul > li:nth-child(14) > a').click()
                else:
                    get_a_page_data()
                    driver.find_element(By.CSS_SELECTOR,
                                        '#results > div > div > div.pager > div > ul > li:nth-child({}) > a'.format(
                                            t + 3)).click()
        else:
            pass
    ##dates deleted temporally
    data = [Application_Numbers, Proposals, Locations, statuses]
    df = pd.DataFrame(data).T
    df['applicationType'] = Application_Type
    df['fromDates'] = '01/05/2013'
    df['toDates'] = '30/04/2023'
    df['url'] = url
    header = ['appnum', 'Proposal', 'Location', 'status', 'applicationType', 'fromdate', 'todate', 'url']
    df.to_excel('{}.xlsx'.format(Application_Type.replace('/', '')), index=False, header=header)


if __name__ == '__main__':
    Application_Type = 'Change of Use'
    get_data(Application_Type)
