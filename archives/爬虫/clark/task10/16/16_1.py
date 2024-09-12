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
url = 'https://plantech.centralbedfordshire.gov.uk/PLANTECH/DCWebPages/acolnetcgi.gov?ACTION=UNWRAP&RIPNAME=Root.pgesearch'
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
        # driver.find_element(By.CSS_SELECTOR, '#AdvancedSearchTab').click()
        s1 = Select(driver.find_element(By.CSS_SELECTOR, '#apptype'))  # 这里是Application Type下拉单选框
        s1.select_by_visible_text(Application_Type)
        # driver.find_element(By.CSS_SELECTOR, '#proposal').send_keys(Application_Type)
        # driver.find_element(By.CSS_SELECTOR, '#txtProposal').send_keys('use as')
        # driver.find_element(By.CSS_SELECTOR, '#rbRange').click()
        start_date = driver.find_element(By.CSS_SELECTOR, '#dcndate1')  # 开始日期输入框
        start_date.clear()  # 清空输入框内容
        start = start_time[i]
        start_date.send_keys(start)  # 发送开始时间
        end_date = driver.find_element(By.CSS_SELECTOR, '#dcndate2')  # 结束日期输入框
        end_date.clear()  # 清空输入框内容
        end = end_time[i]
        end_date.send_keys(end)  # 发送结束时间
        driver.find_element(By.CSS_SELECTOR, '#contentcol > table:nth-child(11) > tbody > tr > td > input[type=submit]').click()  # 点击搜索
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
            number = driver.find_element(By.CSS_SELECTOR, '#contentcol > table.pagetitle > tbody > tr > td').text
            number = int(number.split('of ')[-1].split()[0])
        except:
            number = 0

        def get_a_page_data():
            names = driver.find_elements(By.CSS_SELECTOR, '#contentcol > table > tbody > tr:nth-child(1) > td > a')
            dates_validates = driver.find_elements(By.CSS_SELECTOR, '#contentcol > table > tbody > tr:nth-child(3) > td')
            addresss = driver.find_elements(By.CSS_SELECTOR, '#contentcol > table > tbody > tr:nth-child(5) > td')
            decisionss = driver.find_elements(By.CSS_SELECTOR, '#contentcol > table > tbody > tr:nth-child(9) > td')
            refss = driver.find_elements(By.CSS_SELECTOR, '#contentcol > table > tbody > tr:nth-child(7) > td')
            # print(len(names))
            # print(len(dates_validates))
            # print(len(addresss))
            # print(len(decisionss))
            # print(len(refss))
            for _ in range(len(decisionss)):
                name = names[_+1].text
                print(name)
                link = driver.find_element(By.LINK_TEXT, name).get_attribute('href')
                address = addresss[_].text
                decision = decisionss[_].text
                ref = refss[_].text
                date_validated = dates_validates[_+1].text
                # Add new information here
                appnums.append(name.replace(' (click for more details)', ''))
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
            for _ in range(int((number - 1) / 10)):
                if _ == 0:
                    get_a_page_data()
                    driver.find_element(By.ID, 'lnkPageNext').click()
                else:
                    time.sleep(2)
                    get_a_page_data()
                    driver.find_element(By.ID, 'lnkPageNext').click()
        else:
            pass

    data = [appnums, addresses, decisions, refs, dates_validated, applicationTypes, fromDates, toDates, urls]
    df = pd.DataFrame(data).T
    header = ['name', 'address', 'decision', 'Proposal', 'validated_data', 'applicationType', 'fromdate', 'todate', 'url']
    df.to_excel('./{}.xlsx'.format(Application_Type.replace('/', '')), index=False, header=header)


if __name__ == '__main__':
    Application_Type = 'P. Approval Light Industrial to Dwelling'
    Application_Types = ('P. Approval Light Industrial to Dwelling OR P.Approval from Agricultural to Dwelling OR '
                         'P.Approval from Shop/Bank to Dwellings OR P.Notif. Agricultural to Dwelling OR P.Notif. '
                         'Amusements/Casinos to Dwelling OR P.Notif. Comm (Class E) to Dwellinghouse OR P.Notif. '
                         'Light Industrial to Dwelling OR P.Notif. Offices to Dwelling OR P.Notif. Retail/Takeaway to '
                         'Dwelling OR P.Notif. Shop/Bank to Dwellings OR PA from Storage/Distribution to Dwelling OR '
                         'Prior Approval Offices to Dwelling')
    # get_data(Application_Type)
    for i in Application_Types.split(' OR ')[2:]:
        get_data(i)
