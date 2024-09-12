import os
import time

from selenium import webdriver  # 调用浏览器驱动器
from selenium.webdriver.common.by import By
import re
import requests


def download_pdf(url, stack_code):
    os.makedirs('./报告/{}'.format(stack_code))
    option = webdriver.ChromeOptions()
    # option.add_argument('headless')
    option.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=option)
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@id="prodType"]').send_keys(stack_code)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="keyWord"]').send_keys('年年度报告')
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="filterButton"]').click()
    time.sleep(1)
    filename1 = driver.find_element(By.XPATH, '//*[@id="txt"]/table/tbody/tr[2]/td[3]').text
    filename2 = driver.find_element(By.XPATH, '//*[@id="txt"]/table/tbody/tr[3]/td[3]').text
    filename3 = driver.find_element(By.XPATH, '//*[@id="txt"]/table/tbody/tr[4]/td[3]').text
    filename4 = driver.find_element(By.XPATH, '//*[@id="txt"]/table/tbody/tr[5]/td[3]').text
    filename5 = driver.find_element(By.XPATH, '//*[@id="txt"]/table/tbody/tr[6]/td[3]').text
    filename6 = driver.find_element(By.XPATH, '//*[@id="txt"]/table/tbody/tr[7]/td[3]').text
    filename = [filename1, filename2, filename3, filename4, filename5, filename6]
    url1 = driver.find_element(By.XPATH, '//*[@id="txt"]/table/tbody/tr[2]/td[3]').get_attribute('onclick')
    url2 = driver.find_element(By.XPATH, '//*[@id="txt"]/table/tbody/tr[3]/td[3]').get_attribute('onclick')
    url3 = driver.find_element(By.XPATH, '//*[@id="txt"]/table/tbody/tr[4]/td[3]').get_attribute('onclick')
    url4 = driver.find_element(By.XPATH, '//*[@id="txt"]/table/tbody/tr[5]/td[3]').get_attribute('onclick')
    url5 = driver.find_element(By.XPATH, '//*[@id="txt"]/table/tbody/tr[6]/td[3]').get_attribute('onclick')
    url6 = driver.find_element(By.XPATH, '//*[@id="txt"]/table/tbody/tr[7]/td[3]').get_attribute('onclick')
    url_compile = re.compile("http:.*\.pdf")
    results = [url_compile.findall(url1)[0], url_compile.findall(url2)[0], url_compile.findall(url3)[0],
               url_compile.findall(url4)[0], url_compile.findall(url5)[0], url_compile.findall(url6)[0]]
    for i in range(len(results)):
        r = requests.get(results[i])
        with open('./报告/{}/{}.pdf'.format(stack_code, filename[i]), 'wb') as f:
            f.write(r.content)


shanghai = 'http://eid.csrc.gov.cn/101111/index_f.html'
shenzhen = 'http://eid.csrc.gov.cn/101811/index_f.html'
code = ['600463', '600848', '601512']
for _ in code:
    if _[0:2] == '60' or _[0:2] == '900':
        try:
            download_pdf(shanghai, _)
        except Exception as e:
            print('该股票代码找不到对应报告')
    elif _[0:3] == '000' or _[0:3] == '002' or _[0:3] == '300' or _[0:3] == '200':
        try:
            download_pdf(shenzhen, _)
        except Exception as e:
            print('该股票代码找不到对应报告')

