from selenium import webdriver  # 调用浏览器驱动器
from selenium.webdriver.common.by import By
import pandas as pd
import re
import time
from get_stock_code import xx

data = []


def get_data(stock_code, i):
    print(stock_code)
    try:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=option)
        driver.get('http://stockpage.10jqka.com.cn/{}/holder/'.format(stock_code))
        # time.sleep(1)
        driver.switch_to.frame('dataifm')  # 括号内填入iframe的id或name标记值均可
        try:
            holders = driver.find_elements(By.CLASS_NAME, 'tl')
        except:
            holders = '无法查找到该字段信息'
        try:
            ctrl = [i.text for i in holders if '实际控制人' in i.text][0]  # 实际控制人
        except:
            ctrl = '无法查找到该字段信息'
        driver.get('http://stockpage.10jqka.com.cn/{}/company/'.format(stock_code))
        # time.sleep(1)
        try:
            name = driver.find_element(By.CSS_SELECTOR, '#stockNamePlace').text
        except:
            name = '无法查找到该字段信息'
        try:
            stock = re.sub('\d{6}', '', name)
        except:
            stock = '无法查找到该字段信息'
        try:
            code = re.findall('\d{6}', name)[0]
        except:
            code = '无法查找到该字段信息'
        driver.switch_to.frame('dataifm')  # 括号内填入iframe的id或name标记值均可
        try:
            industry = driver.find_element(By.XPATH, '//*[@id="detail"]/div[2]/table/tbody/tr[2]/td[2]/span').text
        except:
            industry = '无法查找到该字段信息'
        try:
            employee = driver.find_element(By.CSS_SELECTOR,
                                           '#detail > div.bd > div > table > tbody > tr:nth-child(7) > td:nth-child(3) > span').text
        except:
            employee = '无法查找到该字段信息'
        try:
            product_name = driver.find_element(By.CSS_SELECTOR,
                                               '#detail > div.bd > div > table > tbody > tr.product_name > td > span > span').text
        except:
            product_name = '无法查找到该字段信息'
        try:
            company_profile = driver.find_element(By.CSS_SELECTOR,
                                                  '#detail > div.bd > div > table > tbody > tr.intro > td > p').text
        except:
            company_profile = '无法查找到该字段信息'
        try:
            where = driver.find_element(By.CSS_SELECTOR,
                                        '#detail > div.bd > div > table > tbody > tr:nth-child(9) > td > span').text
        except:
            where = '无法查找到该字段信息'
        try:
            main = driver.find_element(By.CSS_SELECTOR,
                                       '#detail > div.bd > div > table > tbody > tr:nth-child(1) > td > span').text
        except:
            main = '无法查找到该字段信息'
        try:
            times = driver.find_element(By.CSS_SELECTOR,
                                        '#publish > div.bd.pr > table > tbody > tr:nth-child(1) > td:nth-child(1) '
                                        '> span').text
        except:
            times = '无法查找到该字段信息'
        driver.get('http://stockpage.10jqka.com.cn/{}/finance/'.format(stock_code))
        # time.sleep(1)
        driver.switch_to.frame('dataifm')  # 括号内填入iframe的id或name标记值均可
        driver.find_element(By.CSS_SELECTOR, '#cwzbTable > div.scroll_container > ul > li:nth-child(2)').click()
        try:
            net_profits = driver.find_element(By.XPATH,
                                              '//*[@id="cwzbTable"]/div[1]/div[1]/div[4]/div/table[2]/tbody/tr[2]')
        except:
            net_profits = '无法查找到该字段信息'
        try:
            net_profit5 = []
            for _ in net_profits.text.split(' ')[:5]:
                if _[-1] == '亿':
                    net_profit5.append(str(float(_.split('亿')[0]) * 100000000))
                elif _[-1] == '万':
                    net_profit5.append(str(float(_.split('万')[0]) * 10000))
                else:
                    net_profit5.append(_)
        except:
            net_profit5 = ['无法查找到该字段信息', '无法查找到该字段信息', '无法查找到该字段信息', '无法查找到该字段信息', '无法查找到该字段信息']
        try:
            gross_revenues = driver.find_element(By.XPATH,
                                                 '//*[@id="cwzbTable"]/div[1]/div[1]/div[4]/div/table[2]/tbody/tr[6]')
        except:
            gross_revenues = '无法查找到该字段信息'
        try:
            gross_revenue5 = []
            for _ in gross_revenues.text.split(' ')[:5]:
                if _[-1] == '亿':
                    gross_revenue5.append(str(float(_.split('亿')[0]) * 100000000))
                elif _[-1] == '万':
                    gross_revenue5.append(str(float(_.split('万')[0]) * 10000))
                else:
                    gross_revenue5.append(_)
        except:
            gross_revenue5 = ['无法查找到该字段信息', '无法查找到该字段信息', '无法查找到该字段信息', '无法查找到该字段信息', '无法查找到该字段信息']
        try:
            asset_liability_ratios = driver.find_element(By.XPATH,
                                                         '//*[@id="cwzbTable"]/div[1]/div[1]/div[4]/div/table['
                                                         '2]/tbody/tr[29]')
        except:
            asset_liability_ratios = '无法查找到该字段信息'
        try:
            asset_liability_ratio5 = asset_liability_ratios.text.split(' ')[:5]
        except:
            asset_liability_ratio5 = ['无法查找到该字段信息', '无法查找到该字段信息', '无法查找到该字段信息', '无法查找到该字段信息', '无法查找到该字段信息']

        return [i + 1, name, code, industry, employee, product_name, company_profile, where, main, ctrl, times,
                net_profit5[0], net_profit5[1], net_profit5[2], net_profit5[3], net_profit5[4],
                gross_revenue5[0], gross_revenue5[1], gross_revenue5[2], gross_revenue5[3], gross_revenue5[4],
                asset_liability_ratio5[0], asset_liability_ratio5[1], asset_liability_ratio5[2],
                asset_liability_ratio5[3], asset_liability_ratio5[4], where]
    except Exception as e:
        print(e)

c = ['600367', '871447']
for i in range(len(xx)):
    datas = get_data(xx[i], i)
    if datas:
        data.append(datas)
df = pd.DataFrame(data)
print(df)
f = open('m.xlsx', 'wb')
df.to_excel(f, header=['序号', '股票名称', '股票代码', '行业', '员工人数', '产品', '简介', '办公地址', '主营业务',
                       '实际控制人及股权', '成立时间', '2022年净利润', '2021年净利润', '2020年净利润', '2019年净利润',
                       '2018年净利润', '2022年营业收入', '2021年营业收入', '2020年营业收入', '2019年营业收入',
                       '2018年营业收入', '2022年资产负债率', '2021年资产负债率', '2020年资产负债率', '2019年资产负债率',
                       '2018年资产负债率', '工作地点'], index=False)
