from selenium import webdriver  # 调用浏览器驱动器
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

user_data_dir = r"--user-data-dir=C:\\Users\\fjwyz\\AppData\\Local\\Google\\Chrome\\User Data"

with open('url.txt', 'r') as f:
    content = f.read().split('\n')


def get():
    result, x, need = [], [], []
    option = webdriver.ChromeOptions()
    option.add_argument("--disable-blink-features=AutomationControlled")
    option.add_argument(user_data_dir)
    driver = webdriver.Chrome(options=option)

    def get_data():
        for url in content[1500:2000]:
            driver.get(url)
            time.sleep(1.5)
            try:
                msg = driver.find_element(By.CSS_SELECTOR,
                                          '#__layout > div > section > section.list-main > section > section > span')
            except:
                msg = None
            if msg is None:
                for i in range(25):
                    try:
                        driver.find_element(By.CSS_SELECTOR,
                                        '#__layout > div > section > section.list-main > section > div.list-cell '
                                        '> a:nth-child({}) > div.li-info > div.li-title > div'.format(
                                            i + 1)).click()
                        try:
                            data_element_jg_00 = driver.find_element(By.CSS_SELECTOR,
                                                                 '#__layout > div > div.props-main.w-1170 > div.props-body > div.props-right > div.maininfo > div.house-price > div > span.average').text  # 这里提取的是average价格
                        except:
                            data_element_jg_00 = '暂无此项数据'
                        data_element_wy_01 = driver.find_element(By.CSS_SELECTOR,
                                                                 '#__layout > div > div.props-main.w-1170 > div.props-body > div.props-right > div.maininfo > div.info > div > div:nth-child(1) > div.hover > div.value.value_0').text  # 这里提取的是物业类型
                        data_element_qs_02 = driver.find_element(By.CSS_SELECTOR,
                                                                 '#__layout > div > div.props-main.w-1170 > div.props-body > div.props-right > div.maininfo > div.info > div > div:nth-child(2) > div.hover > div.value.value_1').text  # 这里提取的是权属类型
                        data_element_jg_03 = driver.find_element(By.CSS_SELECTOR,
                                                                 '#__layout > div > div.props-main.w-1170 > div.props-body > div.props-right > div.maininfo > div.info > div > div:nth-child(3) > div.hover > div.value.value_2').text  # 这里提取的是竣工时间
                        data_element_nx_04 = driver.find_element(By.CSS_SELECTOR,
                                                                 '#__layout > div > div.props-main.w-1170 > div.props-body > div.props-right > div.maininfo > div.info > div > div:nth-child(4) > div.hover > div.value.value_3').text  # 这里提取的是产权年限
                        data_element_hs_05 = driver.find_element(By.CSS_SELECTOR,
                                                                 '#__layout > div > div.props-main.w-1170 > div.props-body > div.props-right > div.maininfo > div.info > div > div:nth-child(5) > div.hover > div.value.value_4').text  # 这里提取的是总户数
                        data_element_jm_06 = driver.find_element(By.CSS_SELECTOR,
                                                                 '#__layout > div > div.props-main.w-1170 > div.props-body > div.props-right > div.maininfo > div.info > div > div:nth-child(6) > div.hover > div.value.value_5').text  # 这里提取的是总建筑面积
                        data_element_rj_07 = driver.find_element(By.CSS_SELECTOR,
                                                                 '#__layout > div > div.props-main.w-1170 > div.props-body > div.props-right > div.maininfo > div.info > div > div:nth-child(7) > div.hover > div.value.value_6').text  # 这里提取的是容积率
                        data_element_lh_08 = driver.find_element(By.CSS_SELECTOR,
                                                                 '#__layout > div > div.props-main.w-1170 > div.props-body > div.props-right > div.maininfo > div.info > div > div:nth-child(8) > div.hover > div.value.value_7').text  # 这里提取的是绿化率
                        data_element_jl_09 = driver.find_element(By.CSS_SELECTOR,
                                                                 '#__layout > div > div.props-main.w-1170 > div.props-body > div.props-right > div.maininfo > div.info > div > div:nth-child(9) > div.hover > div.value.value_8').text  # 这里提取的是建筑类型
                        data_element_sq_10 = driver.find_element(By.CSS_SELECTOR,
                                                                 '#__layout > div > div.props-main.w-1170 > div.props-body > div.props-right > div.maininfo > div.info > div > div:nth-child(10) > div.hover > div.value.value_9').text  # 这里提取的是所属商圈
                        data_element_gn_11 = driver.find_element(By.CSS_SELECTOR,
                                                                 '#__layout > div > div.props-main.w-1170 > div.props-body > div.props-right > div.maininfo > div.info > div > div:nth-child(11) > div.hover > div.value.value_10').text  # 这里提取的是统一供暖
                        data_element_gd_12 = driver.find_element(By.CSS_SELECTOR,
                                                                 '#__layout > div > div.props-main.w-1170 > div.props-body > div.props-right > div.maininfo > div.info > div > div:nth-child(12) > div.hover > div.value.value_11').text  # 这里提取的是供水供电
                        data_element_tc_13 = driver.find_element(By.CSS_SELECTOR,
                                                                 '#__layout > div > div.props-main.w-1170 > div.props-body > div.props-right > div.maininfo > div.info > div > div:nth-child(13) > div.hover > div.value.value_12').text  # 这里提取的是停车位
                        data_element_wy_14 = driver.find_element(By.CSS_SELECTOR,
                                                                 '#__layout > div > div.props-main.w-1170 > div.props-body > div.props-right > div.maininfo > div.info > div > div:nth-child(14) > div.hover > div.value.value_13').text  # 这里提取的是物业费
                        data_element_cq_15 = driver.find_element(By.CSS_SELECTOR,
                                                                 '#__layout > div > div.props-main.w-1170 > div.props-body > div.props-right > div.maininfo > div.info > div > div:nth-child(15) > div.value').text  # 这里提取的是停车费
                        data_element_cq_16 = driver.find_element(By.CSS_SELECTOR,
                                                                 '#__layout > div > div.props-main.w-1170 > div.props-body > div.props-right > div.maininfo > div.info > div > div:nth-child(16) > div.value').text  # 这里提取的是车位管理费
                        data_element_cq_17 = driver.find_element(By.CSS_SELECTOR,
                                                                 '#__layout > div > div.props-main.w-1170 > div.props-body > div.props-right > div.maininfo > div.info > div > div:nth-child(17) > div.value').text  # 这里提取的是物业公司
                        data_element_cq_18 = driver.find_element(By.CSS_SELECTOR,
                                                                 '#__layout > div > div.props-main.w-1170 > div.props-body > div.props-right > div.maininfo > div.info > div > div:nth-child(18) > div.value').text  # 这里提取的是小区地址
                        data_element_cq_19 = driver.find_element(By.CSS_SELECTOR,
                                                                 '#__layout > div > div.props-main.w-1170 > div.props-body > div.props-right > div.maininfo > div.info > div > div:nth-child(19) > div.value').text  # 这里提取的是开发商
                        result.append(
                            [data_element_jg_00, data_element_wy_01, data_element_qs_02, data_element_jg_03, data_element_nx_04,
                             data_element_hs_05, data_element_jm_06, data_element_rj_07, data_element_lh_08, data_element_jl_09,
                             data_element_sq_10, data_element_gn_11, data_element_gd_12, data_element_tc_13, data_element_wy_14,
                             data_element_cq_15, data_element_cq_16, data_element_cq_17, data_element_cq_18,
                             data_element_cq_19])
                        driver.back()
                    except:
                        pass
    get_data()
    for i in range(10):
        try:
            driver.find_element(By.CSS_SELECTOR, '#__layout > div > section > section.list-main > section > div.pagination.page-bar > a.next.next-active').click()
            get_data()
        except:
            pass

    df = pd.DataFrame(result)
    df.to_excel('./result.xlsx', 'a', index=False, header=False)


get()
