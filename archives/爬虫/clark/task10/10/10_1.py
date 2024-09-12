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
url = 'https://planningregister.crawley.gov.uk/Search/Advanced#AdvancedSearchTab'
data, summaries, statuses, addresses, dates_validated, refs, applicationTypes, fromDates, toDates, urls, appnums = [], [], [], [], [], [], [], [], [], [], []
decisions = []

def get_data(Application_Type):
    start_time = ['01/05/2013']
    end_time = ['30/04/2023']
    for i in range(len(start_time)):
        driver.get(url)
        try:
            driver.find_element(By.CSS_SELECTOR, '#agreeToDisclaimer').click()
        except:
            pass
        driver.find_element(By.CSS_SELECTOR, '#AdvancedSearchTab').click()
        s1 = Select(driver.find_element(By.CSS_SELECTOR, '#ApplicationType'))  # 这里是Application Type下拉单选框
        s1.select_by_visible_text(Application_Type)
        # driver.find_element(By.CSS_SELECTOR, '#proposal').send_keys(Application_Type)
        # driver.find_element(By.CSS_SELECTOR, '#txtProposal').send_keys('use as')
        # driver.find_element(By.CSS_SELECTOR, '#rbRange').click()
        start_date = driver.find_element(By.CSS_SELECTOR, '#DateIssuedFrom')  # 开始日期输入框
        start_date.clear()  # 清空输入框内容
        start = start_time[i]
        start_date.send_keys(start)  # 发送开始时间
        end_date = driver.find_element(By.CSS_SELECTOR, '#DateIssuedTo')  # 结束日期输入框
        end_date.clear()  # 清空输入框内容
        end = end_time[i]
        end_date.send_keys(end)  # 发送结束时间
        driver.find_element(By.CSS_SELECTOR, '#SearchRegisterButton').click()  # 点击搜索
        # time.sleep(5)
        # driver.find_element(By.CSS_SELECTOR, '#primary > form > input.SWTbutton').click()
        time.sleep(3)


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
            number = driver.find_element(By.CSS_SELECTOR, '#topOfContent > div.page-search-results > p:nth-child(2)').text
            number = int(number.split('of ')[-1].split()[0])
        except:
            number = 0

        def get_a_page_data():
            names = driver.find_elements(By.CSS_SELECTOR, '#topOfContent > div.page-search-results > div:nth-child(7) > div > div:nth-child(1) > div.col-xs-12.col-sm-3.col-sm-offset-1.results__application-no > div.results__data > a')
            dates_validates = driver.find_elements(By.CSS_SELECTOR, '#topOfContent > div.page-search-results > div:nth-child(7) > div > div:nth-child(1) > div.col-xs-12.col-sm-2')
            addresss = driver.find_elements(By.CSS_SELECTOR, '#topOfContent > div.page-search-results > div:nth-child(7) > div > div:nth-child(2) > dl > dd:nth-child(2)')
            decisionss = driver.find_elements(By.CSS_SELECTOR, '#topOfContent > div.page-search-results > div:nth-child(7) > div > div:nth-child(1) > div:nth-child(2)')
            refss = driver.find_elements(By.CSS_SELECTOR, '#topOfContent > div.page-search-results > div:nth-child(7) > div > div:nth-child(2) > dl > dd:nth-child(4)')
            for _ in range(len(names)):
                name = names[_].text
                print(name)
                link = driver.find_element(By.LINK_TEXT, name).get_attribute('href')
                address = addresss[_].text
                decision = decisionss[_].text
                ref = refss[_].text
                date_validated = dates_validates[_].text.split(' ')[-1]
                # Add new information here
                appnums.append(name.split(': ')[-1])
                refs.append(ref)
                # summaries.append(summary)
                addresses.append(address)
                # statuses.append(Status)
                dates_validated.append(date_validated)
                decisions.append(decision)
                applicationTypes.append(Application_Type)
                fromDates.append(start)
                toDates.append(end)
                urls.append(link)

        get_a_page_data()
        if number != 0:
            for _ in range(int((number - 1))):
                if _ == 0:
                    get_a_page_data()
                    driver.find_elements(By.CSS_SELECTOR, '#topOfContent > div.page-search-results > div.pager > div > nav > ul > li:nth-child(13) > a')[-1].click()
                else:
                    time.sleep(2)
                    get_a_page_data()
                    driver.find_elements(By.CSS_SELECTOR, '#topOfContent > div.page-search-results > div.pager > div > nav > ul > li:nth-child(13) > a')[-1].click()
        else:
            pass

    data = [appnums, addresses, decisions, refs, dates_validated, applicationTypes, fromDates, toDates, urls]
    df = pd.DataFrame(data).T
    header = ['name', 'address', 'decision', 'Proposal', 'validated_data', 'applicationType', 'fromdate', 'todate', 'url']
    df.to_excel('./{}.xlsx'.format(Application_Type), index=False, header=header)


if __name__ == '__main__':
    Application_Type = 'Prior Approval - Changes of use'
    get_data(Application_Type)
