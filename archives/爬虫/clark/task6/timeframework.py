from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

        Application_Number = driver.find_element(By.CSS_SELECTOR, '#searchresults > li:nth-child(1) > p.metaInfo').text.split('|')[0]
        for _ in Application_Number:
            Application_Numbers.append(_.text)
        Location = driver.find_element(By.CSS_SELECTOR, '#searchresults > li:nth-child(1) > p.address').text
        for _ in Location:
            Locations.append(_.text)
        Proposal = driver.find_element(By.CSS_SELECTOR, '#searchresults > li:nth-child(1) > a').text
        for _ in Proposal:
            Proposals.append(_.text)

        if not Application_Numbers:  # If no application numbers were found
            return False
        return True

    user_data_dir = r"--user-data-dir=/Users/denghong_ucl2022/Library/Application Support/Google/Chrome/Profile 1"
    option = webdriver.ChromeOptions()
    option.add_argument("--disable-blink-features=AutomationControlled")
    option.add_argument(user_data_dir)
    driver = webdriver.Chrome(options=option)
    url = 'https://plan.wychavon.gov.uk/Search/Advanced'

    start_period = datetime(2013, 5, 1)
    end_period = datetime(2023, 4, 30)
    current_start_date = start_period

    all_data = []

    while current_start_date < end_period:
        current_end_date = min(current_start_date + timedelta(days=365), end_period)

        driver.get(url)
        driver.find_element(By.CSS_SELECTOR, '#SearchPlanning').click()
        s1 = Select(driver.find_element(By.CSS_SELECTOR, '#ApplicationType'))
        s1.select_by_visible_text(ApplicationType)
        start_date_element = driver.find_element(By.CSS_SELECTOR, '#DateReceivedFrom')
        start_date_element.click()
        start_date_element.send_keys(current_start_date.strftime('%d/%m/%Y'))
        end_date_element = driver.find_element(By.CSS_SELECTOR, '#DateReceivedTo')
        end_date_element.click()
        end_date_element.send_keys(current_end_date.strftime('%d/%m/%Y'))
        driver.find_element(By.CSS_SELECTOR, '#submitBtn').click()
        time.sleep(2)

        Application_Numbers, Locations, Proposals = [], [], []

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

    if all_data:
        df = pd.DataFrame(all_data, columns=['Application_Numbers', 'Locations', 'Proposals'])
        df.to_excel('{}.xlsx'.format(ApplicationType), index=False)
        print("Data collection complete and saved to {}.xlsx".format(ApplicationType))
    else:
        print("No data found for the specified period and application type.")

    driver.quit()


if __name__ == '__main__':
    ApplicationType = 'GPMAE - Commercial, Business and Services uses to Dwellinghouses'
    get_some_data(ApplicationType)

