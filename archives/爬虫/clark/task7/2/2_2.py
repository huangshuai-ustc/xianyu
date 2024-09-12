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
url = 'https://planning.runnymede.gov.uk/Northgate/PlanningExplorer/GeneralSearch.aspx'
##dates deleted temporally
data, summaries, statuses, addresses, dates_validated, refs, applicationTypes, fromDates, toDates, urls, appnums = [], [], [], [], [], [], [], [], [], [], []


def get_data(Application_Type,Description):
    start_time = ['01/05/2013']
    end_time = ['30/04/2023']
    for i in range(len(start_time)):
        driver.get(url)
        ##driver.find_element(By.CSS_SELECTOR, '#description').send_keys('conversion')  # 这里是Description Keyword输入框
        ##driver.find_element(By.CSS_SELECTOR, '#reference').send_keys('COU')  # 这里是Description Keyword输入框
        ##click
        # driver.find_element(By.CSS_SELECTOR, '#Planning applications').click()  # 点击搜索
        s1 = Select(driver.find_element(By.ID, 'cboApplicationTypeCode'))  # 这里是Application Type下拉单选框
        s1.select_by_visible_text(Application_Type)
        driver.find_element(By.CSS_SELECTOR, '#txtProposal').send_keys(Description)
        driver.find_element(By.CSS_SELECTOR, '#rbRange').click()
        start_date = driver.find_element(By.CSS_SELECTOR, '#dateStart')  # 开始日期输入框
        start_date.click()  # 清空输入框内容
        start = start_time[i]
        start_date.send_keys(start)  # 发送开始时间
        end_date = driver.find_element(By.CSS_SELECTOR, '#dateEnd')  # 结束日期输入框
        end_date.click()  # 清空输入框内容
        end = end_time[i]
        end_date.send_keys(end)  # 发送结束时间
        driver.find_element(By.CSS_SELECTOR,
                            '#csbtnSearch').click()  # 点击搜索
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
            number = driver.find_element(By.CSS_SELECTOR, '#lblPagePosition').text
            number = int(number.split('of ')[-1])
        except:
            number = 0

        def get_a_page_data():
            all_datas = driver.find_elements(By.CSS_SELECTOR,
                                             '#pagewrapper > div.row > div > div.middle > div > table > tbody > tr > td')
            for _ in range(int(len(all_datas) / 6)):
                appnum = all_datas[6 * _].text
                link = driver.find_element(By.LINK_TEXT, appnum).get_attribute('href')
                address = all_datas[6 * _ + 1].text
                summary = all_datas[6 * _ + 2].text

                ##3_2
                Status = all_datas[6 * _ + 3].text
                date_validated = all_datas[6 * _ + 4].text
                ref = all_datas[6 * _ + 5].text

                # Add new information here
                appnums.append(appnum)
                summaries.append(summary)
                addresses.append(address)
                statuses.append(Status)
                dates_validated.append(date_validated)
                refs.append(ref)
                applicationTypes.append(Application_Type)
                fromDates.append('01/05/2013')
                toDates.append('30/04/2023')
                urls.append(link)

        get_a_page_data()
        if number != 0:
            for _ in range(int((number - 1) / 10)):
                if _ == 0:
                    get_a_page_data()
                    driver.find_element(By.CLASS_NAME, 'noborder').click()
                else:
                    get_a_page_data()
                    driver.find_elements(By.CLASS_NAME, 'noborder')[2].click()
        else:
            pass
    ##dates deleted temporally
    data = [summaries, addresses, refs, dates_validated, statuses, applicationTypes, fromDates, toDates, urls]
    df = pd.DataFrame(data).T
    header = ['summary', 'address', 'decision', 'validated_data', 'status', 'applicationType', 'fromdate', 'todate', 'url']
    df.to_excel('{}_{}.xlsx'.format(Application_Type, Description), index=False, header=header)
    ##df.to_excel('filename.xlsx'.format(Application_Type), index=False, header=header)


if __name__ == '__main__':
    Application_Type = 'Full Planning Permission'
    Description = 'use as'
    get_data(Application_Type, Description)
