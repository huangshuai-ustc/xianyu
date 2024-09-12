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
url = 'https://secure.telford.gov.uk/planningsearch/'
data, summaries, statuses, addresses, dates_validated, refs, applicationTypes, fromDates, toDates, urls, appnums = [], [], [], [], [], [], [], [], [], [], []
decisions = []

def get_data(Application_Type):
    start_time = ['01-05-2013']
    end_time = ['30-04-2023']
    for i in range(len(start_time)):
        driver.get(url)
        # driver.find_element(By.CSS_SELECTOR, '#AdvancedSearchTab').click()
        s1 = Select(driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_ddlPlanningapplicationtype'))  # 这里是Application Type下拉单选框
        s1.select_by_visible_text(Application_Type)
        # driver.find_element(By.CSS_SELECTOR, '#proposal').send_keys(Application_Type)
        # driver.find_element(By.CSS_SELECTOR, '#txtProposal').send_keys('use as')
        # driver.find_element(By.CSS_SELECTOR, '#rbRange').click()
        start_date = driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_DCdatefrom')  # 开始日期输入框
        start_date.clear()  # 清空输入框内容
        start = start_time[i]
        start_date.send_keys(start)  # 发送开始时间
        end_date = driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_DCdateto')  # 结束日期输入框
        end_date.clear()  # 清空输入框内容
        end = end_time[i]
        end_date.send_keys(end)  # 发送结束时间
        driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_btnSearchPlanningDetails').click()  # 点击搜索
        # time.sleep(5)
        # driver.find_element(By.CSS_SELECTOR, '#primary > form > input.SWTbutton').click()
        time.sleep(3)

        for choice in range(3):
            driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_lbPlanning2ndLevel{}'.format(choice+1)).click()
            try:
                text = driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_gvResults > tbody > tr > td').text
                if text == 'Sorry no records were found - please modify your search.':
                    continue
            except:
                pass
            try:
                number = driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_gvResults > tbody > tr:nth-child(1) > td > div > div.left').text
                number = int(number.split('of ')[-1].split()[0])
            except:
                number = 0

            def get_a_page_data1():
                names = driver.find_elements(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_gvResults > tbody > tr > td:nth-child(1) > a')
                dates_validates = driver.find_elements(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_gvResults > tbody > tr > td:nth-child(2)')
                addresss = driver.find_elements(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_gvResults > tbody > tr > td:nth-child(3)')
                # decisionss = driver.find_elements(By.CSS_SELECTOR, '#contentcol > table > tbody > tr:nth-child(9) > td')
                refss = driver.find_elements(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_gvResults > tbody > tr > td:nth-child(4)')
                # print(len(names))
                # print(len(dates_validates))
                # print(len(addresss))
                # print(len(decisionss))
                # print(len(refss))
                for _ in range(len(names)):
                    name = names[_].text
                    print(name)
                    link = driver.find_element(By.LINK_TEXT, name).get_attribute('href')
                    address = addresss[_].text
                    # decision = decisionss[_].text
                    ref = refss[_].text
                    date_validated = dates_validates[_].text
                    # Add new information here
                    appnums.append(name)
                    refs.append(ref)
                    # summaries.append(summary)
                    addresses.append(address)
                    statuses.append('')
                    dates_validated.append(date_validated)
                    decisions.append('')
                    applicationTypes.append(Application_Type)
                    fromDates.append(start)
                    toDates.append(end)
                    urls.append(link)
            def get_a_page_data2():
                names = driver.find_elements(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_gvResults > tbody > tr > td:nth-child(1) > a')
                dates_validates = driver.find_elements(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_gvResults > tbody > tr > td:nth-child(2)')
                addresss = driver.find_elements(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_gvResults > tbody > tr > td:nth-child(3)')
                # decisionss = driver.find_elements(By.CSS_SELECTOR, '#contentcol > table > tbody > tr:nth-child(9) > td')
                refss = driver.find_elements(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_gvResults > tbody > tr > td:nth-child(4)')

                for _ in range(len(names)):
                    name = names[_].text
                    print(name)
                    link = driver.find_element(By.LINK_TEXT, name).get_attribute('href')
                    address = addresss[_].text
                    # decision = decisionss[_].text
                    ref = refss[_].text
                    date_validated = dates_validates[_].text
                    # Add new information here
                    appnums.append(name)
                    refs.append(ref)
                    # summaries.append(summary)
                    addresses.append(address)
                    statuses.append('')
                    dates_validated.append(date_validated)
                    decisions.append('')
                    applicationTypes.append(Application_Type)
                    fromDates.append(start)
                    toDates.append(end)
                    urls.append(link)
            def get_a_page_data3():
                names = driver.find_elements(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_gvResults > tbody > tr > td:nth-child(1) > a')
                dates_validates = driver.find_elements(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_gvResults > tbody > tr > td:nth-child(5)')
                addresss = driver.find_elements(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_gvResults > tbody > tr > td:nth-child(2)')
                decisionss = driver.find_elements(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_gvResults > tbody > tr > td:nth-child(4)')
                refss = driver.find_elements(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_gvResults > tbody > tr > td:nth-child(3)')
                for _ in range(len(names)):
                    name = names[_].text
                    print(name)
                    link = driver.find_element(By.LINK_TEXT, name).get_attribute('href')
                    address = addresss[_].text
                    decision = decisionss[_].text
                    ref = refss[_].text
                    date_validated = dates_validates[_].text
                    # Add new information here
                    appnums.append(name)
                    refs.append(ref)
                    # summaries.append(summary)
                    addresses.append(address)
                    statuses.append('')
                    dates_validated.append(date_validated)
                    decisions.append(decision)
                    applicationTypes.append(Application_Type)
                    fromDates.append(start)
                    toDates.append(end)
                    urls.append(link)

            if choice == 0:
                get_a_page_data1()
                if number != 0:
                    for _ in range(int((number - 1) / 10)):
                        if _ == 0:
                            get_a_page_data1()
                            driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_gvResults_ctl14_lbPagerTopNext').click()
                        else:
                            time.sleep(2)
                            get_a_page_data1()
                            driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_gvResults_ctl14_lbPagerTopNext').click()
                else:
                    pass
            elif choice == 1:
                get_a_page_data2()
                if number != 0:
                    for _ in range(int((number - 1) / 10)):
                        if _ == 0:
                            get_a_page_data2()
                            driver.find_element(By.ID,
                                                'ctl00_ContentPlaceHolder1_gvResults_ctl14_lbPagerTopNext').click()
                        else:
                            time.sleep(2)
                            get_a_page_data2()
                            driver.find_element(By.ID,
                                                'ctl00_ContentPlaceHolder1_gvResults_ctl14_lbPagerTopNext').click()
                else:
                    pass
            else:
                get_a_page_data3()
                if number != 0:
                    for _ in range(int((number - 1) / 10)):
                        if _ == 0:
                            get_a_page_data3()
                            driver.find_element(By.ID,
                                                'ctl00_ContentPlaceHolder1_gvResults_ctl14_lbPagerTopNext').click()
                        else:
                            time.sleep(2)
                            get_a_page_data3()
                            driver.find_element(By.ID,
                                                'ctl00_ContentPlaceHolder1_gvResults_ctl14_lbPagerTopNext').click()
                else:
                    pass

    data = [appnums, addresses, refs, statuses, decisions, dates_validated, applicationTypes, fromDates, toDates, urls]
    df = pd.DataFrame(data).T
    header = ['name', 'address', 'Proposal', 'statu', 'decisions', 'validated_date', 'applicationType', 'fromdate', 'todate', 'url']
    df.to_excel('./{}.xlsx'.format(Application_Type.replace('/', '')), index=False, header=header)


if __name__ == '__main__':
    Application_Type = 'Change Of Use (Prior Approval)'
    get_data(Application_Type)

