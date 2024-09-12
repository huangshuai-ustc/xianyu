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
url = 'https://planning.wealden.gov.uk/advsearch.aspx'
data, summaries, statuses, addresses, dates_validated, refs, applicationTypes, fromDates, toDates, urls, appnums = [], [], [], [], [], [], [], [], [], [], []
proposals = []

def get_data(Application_Type):
    start_time = ['01/05/2013']
    end_time = ['30/04/2023']
    for i in range(len(start_time)):
        driver.get(url)
        time.sleep(5)
        try:
            driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_btnAccept').click()
        except:
            pass
        # driver.find_element(By.CSS_SELECTOR, '#\33 80\:0__item').click()
        s1 = Select(driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_ddlPS2Category'))  # 这里是Application Type下拉单选框
        s1.select_by_visible_text(Application_Type)
        # driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_txtAppNumber').send_keys(Application_Type)
        # driver.find_element(By.CSS_SELECTOR, '#txtProposal').send_keys('use as')
        # driver.find_element(By.CSS_SELECTOR, '#rbRange').click()
        start_date = driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_txtDateReceivedFrom')  # 开始日期输入框
        start_date.clear()  # 清空输入框内容
        start = start_time[i]
        start_date.send_keys(start)  # 发送开始时间
        end_date = driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_txtDateReceivedTo')  # 结束日期输入框
        end_date.clear()  # 清空输入框内容
        end = end_time[i]
        end_date.send_keys(end)  # 发送结束时间
        driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_Button1').click()  # 点击搜索
        time.sleep(5)
        # driver.find_element(By.CSS_SELECTOR, '#primary > form > input.SWTbutton').click()


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
            number = driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_lvResults_RadDataPager1 > div:nth-child(4)').text
            number = int(number.split('of ')[-1])
        except:
            number = 0
        def get_a_page_data():
            time.sleep(3)
            all_datas = driver.find_elements(By.CLASS_NAME, 'emphasise-area')
            # names = driver.find_elements(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_lvResults_ctrl0_hypDisplayRecord')
            # dates_validates = driver.find_elements(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_lvResults_ctrl0_plabldpanel > p:nth-child(4)')
            # addresss = driver.find_elements(By.CSS_SELECTOR, '#news_results_list > div > p:nth-child(3)')
            # decisions = driver.find_elements(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_lvResults_ctrl1_plabldpanel > p:nth-child(2)')
            # proposal = driver.find_elements(By.CSS_SELECTOR, '#news_results_list > div > p:nth-child(5)')
            # refss = driver.find_elements(By.CSS_SELECTOR, '#primary > table > tbody > tr:nth-child(4) > td')
            # print(len(all_datas))
            for _ in range(len(all_datas)-2):
                datas = all_datas[_+1].text.split('\n')
                print(datas[0])
                link = driver.find_element(By.LINK_TEXT, datas[0]).get_attribute('href')
                address = datas[2]
                try:
                    ref = datas[6]
                except:
                    ref = 'N/A'
                try:
                    date_validated = datas[8]
                except:
                    date_validated = 'N/A'
                try:
                    proposal = datas[4]
                except:
                    proposal = 'N/A'
                # Add new information here
                appnums.append(datas[0])
                proposals.append(proposal)
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
            for _ in range(int(number - 1)):
                get_a_page_data()
                driver.find_element(By.CLASS_NAME, 'rdpPageNext').click()
        else:
            pass

    data = [appnums, addresses, refs, proposals, dates_validated, applicationTypes, fromDates, toDates, urls]
    df = pd.DataFrame(data).T
    header = ['name', 'address', 'decision', 'proposal', 'validated_data', 'applicationType', 'fromdate', 'todate', 'url']
    df.to_excel('./{}.xlsx'.format(Application_Type), index=False, header=header)


if __name__ == '__main__':
    Application_Type = 'Change of Use'
    get_data(Application_Type)
    # a = ["PD Change of use from Offices to Dwellings OR PD Change of use from Agricultural to Dwellings OR PD Change "
    #      "of use from A1, A2, A5, Betting Office, Pay Day Loan Shop, Launderette to single Dwelling OR PD Change of "
    #      "use from Light Industrial to Residential Use"]
    # for i in a[0].split(' OR '):
    #     get_data(i)
