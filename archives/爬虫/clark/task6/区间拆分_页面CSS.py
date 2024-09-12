from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
from datetime import datetime, timedelta
from selenium.common.exceptions import NoSuchElementException


def get_some_data(ApplicationType):
    def get_data():
        time.sleep(1)
        Application_Numbers.clear()
        Locations.clear()
        Proposals.clear()
        ##针对现在页面的形式修改CSS选择器
        try:
            all_datas = driver.find_elements(By.CSS_SELECTOR, '#searchresults > li')
        except:
            all_datas = 'not found'
        for i in range(len(all_datas)):
            x = all_datas[i].text.split('\n')
            Application_Number = x[0]
            Location = x[1]
            Proposal = x[2].split(' | ')[1].split(': ')[-1]
        if not Application_Numbers:  # If no application numbers were found
            return False
        return True

    webdriver_path = r"D:\Download\IdmDownload\chromedriver-win64\chromedriver.exe"
    user_data_dir = r"--user-data-dir=C:\\Users\\fjwyz\\AppData\\Local\\Google\\Chrome\\User Data"
    option = webdriver.ChromeOptions()
    # options.add_argument ( "--headless") # 开启无界面模式
    option.add_argument(user_data_dir)
    service = Service(executable_path=webdriver_path)
    driver = webdriver.Chrome(service=service, options=option)
    url = 'https://pa.westlancs.gov.uk/online-applications/search.do?action=advanced'

    start_period = datetime(2013, 5, 1)
    end_period = datetime(2023, 4, 30)
    current_start_date = start_period

    all_data = []

    while current_start_date < end_period:
        current_end_date = min(current_start_date + timedelta(days=365), end_period)

        driver.get(url)
        #####这个条件暂时不用了，因为这个网页没有这个按钮了
        #driver.find_element(By.CSS_SELECTOR, '#SearchPlanning').click()
        s1 = Select(driver.find_element(By.ID, 'caseType'))
        ###application type 选择“ Planning permission"
        s1.select_by_visible_text(ApplicationType)
        ###新增条件“Description word”这一栏输入“ change of use“
        #####以上是这一次的搜索条件，仅仅包括指定application type和关键字


        ###时间上，需要拆分。注意一下，有课程出现没有的情况，所以我感觉是否需要先判断存不存在我需要的元素，没有就跳进下一个小区间。查看无内容的页面情况可以搜索一个未来时间段。
        start_date_element = driver.find_element(By.CSS_SELECTOR, '#applicationValidatedStart')
        start_date_element.click()
        start_date_element.send_keys(current_start_date.strftime('%d/%m/%Y'))
        end_date_element = driver.find_element(By.CSS_SELECTOR, '#applicationValidatedEnd')
        end_date_element.click()
        end_date_element.send_keys(current_end_date.strftime('%d/%m/%Y'))
        driver.find_element(By.CSS_SELECTOR, '#advancedSearchForm > div.buttons > input.button.primary.recaptcha-submit').click()
        time.sleep(2)
        ##感谢内页的解决方案，但是现在这一阶段我先舍弃了
        Application_Numbers, Locations, Proposals = [], [], []

        ##新加的判断页数的条件，少于1就是1
        try:
            result_number = int(driver.find_element(By.CSS_SELECTOR,
                                                    '#results > div > div > div.pager > div > ul > li:nth-child(13) > a').text)
        except NoSuchElementException:
            result_number = 1

        if get_data() and result_number > 1:
            for i in range(result_number - 1):
                time.sleep(0.5)
                bu = driver.find_element(By.CSS_SELECTOR,
                                         '#results > div > div > div.pager > div > ul > li:nth-child(14) > a')
                bu.click()
                time.sleep(0.5)
                get_data()

        for a, l, p in zip(Application_Numbers, Locations, Proposals):
            all_data.append([a, l, p])

        current_start_date = current_end_date + timedelta(days=1)

    ##完成每一个区间搜索后把数据储存。
    if all_data:
        df = pd.DataFrame(all_data, columns=['Application_Numbers', 'Locations', 'Proposals'])
        df.to_excel('{}.xlsx'.format(ApplicationType), index=False)
        print("Data collection complete and saved to {}.xlsx".format(ApplicationType))
    else:
        print("No data found for the specified period and application type.")

    driver.quit()


if __name__ == '__main__':
    ApplicationType = 'Change of Use'
    get_some_data(ApplicationType)

