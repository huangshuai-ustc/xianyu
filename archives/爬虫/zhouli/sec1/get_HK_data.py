from selenium import webdriver  # 调用浏览器驱动器
from selenium.webdriver.common.by import By
import pandas as pd
import re
import time
from openpyxl import load_workbook
from get_stock_code import xx

data = []


def get_data(stock_code, i):
    print(stock_code)
    try:
        option = webdriver.ChromeOptions()
        # option.add_argument('headless')
        option.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=option)
        driver.get('http://stockpage.10jqka.com.cn/{}/company/'.format(stock_code))
        # time.sleep(1)
        stock_name = driver.find_element(By.CSS_SELECTOR, 'body > div.m_header > h1 > a').text.split('\n')[0]
        driver.switch_to.frame('data-ifm')  # 括号内填入iframe的id或name标记值均可
        company_name = driver.find_element(By.CSS_SELECTOR,
                                           '#basic > div.bd > table > tbody > tr:nth-child(1) > td:nth-child(1) > span').text
        regedit_where = driver.find_element(By.CSS_SELECTOR,
                                            '#basic > div.bd > table > tbody > tr:nth-child(1) > td:nth-child(2) > span > a').text
        industry = driver.find_element(By.CSS_SELECTOR,
                                       '#basic > div.bd > table > tbody > tr:nth-child(2) > td:nth-child(2) > span').text
        product_name = driver.find_element(By.CSS_SELECTOR,
                                           '#basic > div.bd > table > tbody > tr:nth-child(4) > td > span').text
        times = driver.find_element(By.CSS_SELECTOR,
                                    '#basic > div.bd > table > tbody > tr:nth-child(3) > td:nth-child(1) > span').text
        employee = driver.find_element(By.CSS_SELECTOR,
                                       '#basic > div.bd > table > tbody > tr:nth-child(5) > td:nth-child(3) > span').text
        main = driver.find_element(By.CSS_SELECTOR,
                                   '#basic > div.bd > table > tbody > tr:nth-child(4) > td > span').text
        where = driver.find_element(By.CSS_SELECTOR,
                                    '#basic > div.bd > table > tbody > tr:nth-child(8) > td > span > a').text
        company_profile = driver.find_element(By.CSS_SELECTOR,
                                              '#basic > div.bd > table > tbody > tr:nth-child(9) > td > div > p').text
        driver.get('http://stockpage.10jqka.com.cn/{}/finance/'.format(stock_code))
        driver.switch_to.frame('data-ifm')
        driver.find_element(By.CSS_SELECTOR, '#timeSelect > div > div > s').click()
        driver.find_element(By.CSS_SELECTOR, '#timeSelect > div > ul > li:nth-child(2) > a').click()
        net_profits = driver.find_element(By.CSS_SELECTOR,  # 营业收入
                                          '#cwzbTable > div.scroll_container > div > div.data_tbody > table.tbody > tbody > tr.on').text
        net_profit5 = net_profits.split(' ')[:5]
        gross_profits = driver.find_element(By.CSS_SELECTOR,  # 毛利
                                            '#cwzbTable > div.scroll_container > div > div.data_tbody > table.tbody > tbody > tr:nth-child(7)').text
        gross_profit5 = gross_profits.split(' ')[:5]
        asset_liability_ratios = driver.find_element(By.CSS_SELECTOR,  # 资产负债率
                                                     '#cwzbTable > div.scroll_container > div > div.data_tbody > table.tbody > tbody > tr:nth-child(14)').text
        asset_liability_ratio5 = asset_liability_ratios.split(' ')[:5]
        operating_margins = driver.find_element(By.CSS_SELECTOR,  # 营业利润率
                                                '#cwzbTable > div.scroll_container > div > div.data_tbody > table.tbody > tbody > tr.on').text
        operating_margin5 = operating_margins.split(' ')[:5]
        return [i + 1, stock_name, stock_code, industry, employee, product_name, company_profile, where, main, times,
                gross_profit5[0], gross_profit5[1], gross_profit5[2], gross_profit5[3], gross_profit5[4], net_profit5[0],
                net_profit5[1], net_profit5[2], net_profit5[3], net_profit5[4], operating_margin5[0],
                operating_margin5[1], operating_margin5[2], operating_margin5[3], operating_margin5[4],
                asset_liability_ratio5[0], asset_liability_ratio5[1], asset_liability_ratio5[2],
                asset_liability_ratio5[3], asset_liability_ratio5[4], where]
    except Exception as e:
        print(e)


# c = ['HK2337', 'HK0189']
c = ['HK2337', 'HK0438', 'HK0189', 'HK0968', 'HK0757', 'HK3899']
for i in range(len(c)):
    datas = get_data(c[i], i)
    if datas:
        data.append(datas)
df = pd.DataFrame(data)
f = open('y.csv', 'a+b')
df.to_csv(f, header=['序号', '股票名称', '股票代码', '行业', '员工人数', '产品', '简介', '办公地址', '主营业务', '成立时间',
                     '2022年毛利', '2021年毛利', '2020年毛利', '2019年毛利', '2018年毛利', '2022年营业收入', '2021年营业收入',
                     '2020年营业收入', '2019年营业收入', '2018年营业收入', '2022年营业利润率', '2021年营业利润率', '2020年营业利润率',
                     '2019年营业利润率', '2018年营业利润率', '2022年资产负债率', '2021年资产负债率', '2020年资产负债率',
                     '2019年资产负债率', '2018年资产负债率', '工作地点'], index=False)
df.to_csv(f, header=False, index=False)
