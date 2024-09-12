import time
import pandas as pd
from selenium import webdriver  # 调用浏览器驱动器
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

webdriver_path = r"D:\Download\IdmDownload\chromedriver-win64\chromedriver.exe"
user_data_dir = r"--user-data-dir=C:\\Users\\fjwyz\\AppData\\Local\\Google\\Chrome\\User Data"
option = webdriver.ChromeOptions()
# options.add_argument ( "--headless") # 开启无界面模式
option.add_argument(user_data_dir)
service = Service(executable_path=webdriver_path)
driver = webdriver.Chrome(service=service, options=option)
url = 'https://pa.westlancs.gov.uk/online-applications/search.do?action=advanced'



def get_data(Application_Type):
    data, summaries, addresses, dates, refs, status, fromdate, todate, Application_Types = [], [], [], [], [], [], [], [], []
    # start_time = ['01/05/2013', '01/05/2014', '01/05/2015', '01/05/2016', '01/05/2017', '01/05/2018', '01/05/2019',
    #               '01/05/2020', '01/05/2021', '01/05/2022']
    # end_time = ['30/04/2014', '30/04/2015', '30/04/2016', '30/04/2017', '30/04/2018', '30/04/2019', '30/04/2020',
    #             '30/04/2021', '30/04/2022', '30/04/2023']
    start_time = ['01/05/2013']
    end_time = ['30/04/2023']
    for i in range(len(start_time)):
        driver.get(url)
        # driver.find_element(By.CSS_SELECTOR, '#description').send_keys('xxx')  # 这里是Description Keyword输入框
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
        driver.find_element(By.CSS_SELECTOR,
                            '#advancedSearchForm > div.buttons > input.button.primary.recaptcha-submit').click()  # 点击搜索
        time.sleep(2)
        # 直接进入详情页解决方案
        try:
            driver.find_element(By.CSS_SELECTOR, '#tab_summary > span')
            continue
        except:
            pass
        # 未找到解决方案
        try:
            driver.find_element(By.CSS_SELECTOR, '#pa > div:nth-child(4) > div.content > div.messagebox > ul > li')
            continue
        except:
            pass

        try:
            number = driver.find_element(By.CSS_SELECTOR, '#searchResultsContainer > p.pager.top > span.showing').text
            number = int(number.split('of ')[-1])
        except:
            number = 0

        def get_a_page_data():
            all_datas = driver.find_elements(By.CSS_SELECTOR, '#searchresults > li')
            for _ in range(len(all_datas)):
                all_data = all_datas[_].text.split('\n')
                summary = all_data[0]
                address = all_data[1]
                date = all_data[2].split(' | ')[2].split(': ')[-1]
                ref = all_data[2].split(' | ')[0].split(': ')[-1]
                statu = all_data[2].split(' | ')[3].split(': ')[-1]
                fromdate.append(start)
                todate.append(end)
                summaries.append(summary)
                addresses.append(address)
                dates.append(date)
                refs.append(ref)
                status.append(statu)
                Application_Types.append(Application_Type)

        get_a_page_data()
        if number != 0:
            for _ in range(int((number - 1) / 10)):
                get_a_page_data()
                driver.find_element(By.CLASS_NAME, 'next').click()
        else:
            pass
    dataa = [summaries, addresses, refs, dates, status,Application_Types,fromdate,todate]

    df = pd.DataFrame(dataa).T
    df['url'] = url
    header = ['summary', 'address', 'ref', 'validated_date', 'status', 'applicationType','fromdate','todate','url']
    df.to_excel('{}.xlsx'.format(Application_Type), index=False, header=header)


if __name__ == '__main__':
    app_type = ['Additional Environmental Approval', 'Advertisement Consent', 'Approval of Reserved Matters',
                'Change of Use',
                'Conservation Area Consent', 'County Application', 'County Application (LDC)',
                'County Application (Scoping Opinion)',
                'County Application Reg.3', 'County Application Reg.4', 'County Matter (Minerals)',
                'County Matter Application',
                'Discharge of Condition(s)', 'Full Planning Application', 'Government Department Application',
                'Hazardous Substances Consent',
                'Hedgerow Removal Notice', 'Historical - Pre1990', 'Hybrid - Full & Outline Application',
                'Lawful Development Cert Listed Bldg)',
                'Lawful Development Cert. (existing)', 'Lawful Development Cert. (proposed)', 'Listed Building Consent',
                'Local Development Order',
                'Modif or Discharge of S106 obligations', 'Non Material Amendment (s96A)', 'Overhead Line Application',
                'Pavement Cafe Licence', 'Permission in Principle', 'Prior Approval - Part 18',
                'Prior Notification - Additional Storeys',
                'Outline Planning Application', 'Prior Notification - Agriculture',
                'Prior Notification - Change of Use', 'Prior Notification - Demolition',
                'Prior Notification - Telecommunications', 'Prior Notification-Extension of dwelling',
                'Prior Notification-Renewable Energy',
                'Rights of Way', 'Scoping Opinion (EIA)', 'Screening Opinion (EIA)', 'Test App Type',
                'West Lancs Application (Reg. 3)1992',
                'West Lancs Application (Reg. 4)', 'Works to Protected Trees', 'Works to Trees in Conservation Area']
    # x = [app_type[0], app_type[6], app_type[7], app_type[9], app_type[11], app_type[14], app_type[15], app_type[16],
    #      app_type[20], app_type[28], app_type[31], app_type[39], app_type[42], app_type[44]]
    y = [app_type[0], app_type[9], app_type[11], app_type[14], app_type[15], app_type[20],
         app_type[21], app_type[28], app_type[31], app_type[39], app_type[42], app_type[44]]
    for _ in y:
        get_data(_)
