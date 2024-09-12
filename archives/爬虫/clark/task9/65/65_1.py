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
data, summaries, statuses, addresses, dates_validated, refs, applicationTypes, fromDates, toDates, urls, appnums = [], [], [], [], [], [], [], [], [], [], []


def get_data(Application_Type):
    start_time = ['01/05/2013']
    end_time = ['30/04/2023']
    for i in range(len(start_time)):
        driver.get(url)
        # driver.find_element(By.CSS_SELECTOR, '#\33 80\:0__item').click()
        # s1 = Select(driver.find_element(By.CSS_SELECTOR, '#\35 24\:0'))  # 这里是Application Type下拉单选框
        # s1.select_by_visible_text(Application_Type)
        driver.find_element(By.CSS_SELECTOR, '#proposal').send_keys(Application_Type)
        # driver.find_element(By.CSS_SELECTOR, '#txtProposal').send_keys('use as')
        # driver.find_element(By.CSS_SELECTOR, '#rbRange').click()
        start_date = driver.find_element(By.CSS_SELECTOR, '#regdate1')  # 开始日期输入框
        start_date.clear()  # 清空输入框内容
        start = start_time[i]
        start_date.send_keys(start)  # 发送开始时间
        end_date = driver.find_element(By.CSS_SELECTOR, '#regdate2')  # 结束日期输入框
        end_date.clear()  # 清空输入框内容
        end = end_time[i]
        end_date.send_keys(end)  # 发送结束时间
        driver.find_element(By.CSS_SELECTOR, '#primary > form > div > input.SWTbutton').click()  # 点击搜索
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, '#primary > form > input.SWTbutton').click()
        time.sleep(10000)


        # element_large = driver.find_elements(By.CSS_SELECTOR,
        #                                      "#pa > div:nth-child(4) > div.content > div.messagebox.errors > ul > li")
        # if element_large:
        #     print(f"{Application_Type}，year: {start} 至 {end}，too much information")
        #     continue  # 或者执行其他操作
        #
        # no_elements = driver.find_elements(By.CSS_SELECTOR,
        #                                    "#pa > div:nth-child(4) > div.content > div.messagebox > ul > li")
        # if no_elements:
        #     print(f"{Application_Type}，year: {start} 至 {end}，no result")
        #     continue  # 或者执行其他操作

        try:
            # number = driver.find_element(By.CSS_SELECTOR, '#primary > p').text
            # number = int(number.split('of ')[-1])
            number = 0
        except:
            number = 0

        def get_a_page_data():
            names = driver.find_elements(By.CSS_SELECTOR, '#primary > table > tbody > tr.zsubheader > td:nth-child(1)')
            dates_validates = driver.find_elements(By.CSS_SELECTOR, '#primary > table > tbody > tr.zsubheader > td.zAlignRight')
            addresss = driver.find_elements(By.CSS_SELECTOR, '#primary > table > tbody > tr:nth-child(2) > td:nth-child(1)')
            decisions = driver.find_elements(By.CSS_SELECTOR, '#primary > table > tbody > tr:nth-child(5) > td')
            refss = driver.find_elements(By.CSS_SELECTOR, '#primary > table > tbody > tr:nth-child(4) > td')
            for _ in range(len(names)):
                name = names[_].text
                print(name)
                link = driver.find_element(By.LINK_TEXT, name).get_attribute('href')
                address = addresss[_].text
                ref = decisions[_].text
                date_validated = dates_validates[_].text.split(' ')[-1]
                # Add new information here
                appnums.append(name.split(': ')[-1])
                # summaries.append(summary)
                addresses.append(address)
                # statuses.append(Status)
                dates_validated.append(date_validated)
                refs.append(ref)
                applicationTypes.append(Application_Type)
                fromDates.append(start)
                toDates.append(end)
                urls.append(link)

        get_a_page_data()
        if number != 0:
            for _ in range(int((number - 1) / 10)):
                if _ == 0:
                    get_a_page_data()
                    driver.find_element(By.CLASS_NAME, 'next').click()
                else:
                    get_a_page_data()
                    driver.find_element(By.CLASS_NAME, 'next').click()
        else:
            pass

    data = [appnums, addresses, refs, dates_validated, applicationTypes, fromDates, toDates, urls]
    df = pd.DataFrame(data).T
    header = ['name', 'address', 'decision', 'validated_data', 'applicationType', 'fromdate', 'todate', 'url']
    df.to_excel('./{}.xlsx'.format(Application_Type), index=False, header=header)


if __name__ == '__main__':
    Application_Type = 'Office to resi'
    a = ["Office to resi OR Office to dwelling OR Office to C3 OR B1 to resi OR B1  to dwelling OR B1 to C3 Shop to "
         "resi OR Shop to dwelling OR Shop to C3 OR Retail to Resi OR Retail to dwelling OR Retail to C3 A1 to resi "
         "OR A1 to dwelling OR A1 to C3 OR A2 to resi OR A2 to dwelling OR A2 to C3 industrial to resi OR industrial "
         "to dwelling OR industrial to C3 storage to resi OR storage to dwelling OR storage to C3 B8 to resi OR B8 to "
         "dwelling OR B8 to C3 sui generis to resi OR sui generis to dwelling OR sui generis to C3 agricult to resi "
         "OR agricult to dwelling OR agricult to C3"]
    for i in a[0].split(' OR '):
        get_data(i)
