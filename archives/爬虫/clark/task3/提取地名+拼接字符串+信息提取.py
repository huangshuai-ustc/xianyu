from selenium import webdriver  # 调用浏览器驱动器
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
from selenium.common.exceptions import NoSuchElementException  # Importing the exception
import os  # 判断文件存在

user_data_dir = r"--user-data-dir=C:\\Users\\fjwyz\\AppData\\Local\\Google\\Chrome\\User Data"
option = webdriver.ChromeOptions()
option.add_argument("--disable-blink-features=AutomationControlled")
option.add_argument(user_data_dir)
driver = webdriver.Chrome(options=option)
time.sleep(10)

quyu_elements = []
sub_quyu = []
url_list = []
result = []

#####获取大的区域比如南山区
def get_quyu():  # Added driver as a parameter
    url = "https://shenzhen.anjuke.com/community/"  ## url="https://shenzhen.anjuke.com/community/"
    driver.get(url)
    time.sleep(30)
    ##大致看了标签有限是2-14
    for i in range(1, 14):
        try:
            element_list = driver.find_element(By.CSS_SELECTOR, f'#__layout > div > section > section.filter > div.filter-wrap.filter-region > section > div > ul > li:nth-child({i}) > a').get_attribute('href')
            # 使用正则表达式提取yanqing部分
            match = re.search(r'/community/([^/]+)/', element_list)
            if match:
                quyu_elements.append(match.group(1))
        except NoSuchElementException:
            break
    print(quyu_elements)
    return quyu_elements

###继续获取下面的区域标签
def get_sub_quyu(quyu_elements):
##这里只选前三个测试
    quyu_elements_2 = quyu_elements[:3]
    for quyu in quyu_elements_2:
        url_quyu = f"https://shenzhen.anjuke.com/community/{quyu}/"
        driver.get(url_quyu)
        time.sleep(10)
        elements_sub_list = driver.find_elements(By.CSS_SELECTOR, '#__layout > div > section > section.filter > div.filter-wrap.filter-region > section > div > div.region-childs > li > a')
        for element in elements_sub_list:
# Get href attribute of each anchor tag
            href_value = element.get_attribute('href')
# Extract the required part from href using regex
            match = re.search(r'/community/([^/]+)/', href_value)
            if match:
                sub_quyu.append(match.group(1))
    print(sub_quyu)
    return sub_quyu

###生成交错网址
def cross_over(sub_quyu):
    for d in sub_quyu:
        p_list = ['m272', 'm273', 'm274', 'm275', 'm276', 'm277', 'm278']
        a_list = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6']
        for m in p_list:
            for a in a_list:
                 url_l = 'https://shenzhen.anjuke.com/community/{}/{}-{}/'.format(d, m, a)
                 url_list.append(url_l)
    return url_list
####

##基于网址list
def get_data(url_list):
    for url in url_list:
        driver.get(url)
        time.sleep(3)
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
                    data_element_jg_0000 = driver.find_element(By.CSS_SELECTOR,
                                                               '#__layout > div > div.props-main.w-1170 > div:nth-child(2) > div > h1').text  # 这里提取的是小区名字
                    data_element_jg_000 = driver.find_element(By.CSS_SELECTOR,
                                                              '#_#__layout > div > div.props-main.w-1170 > div:nth-child(2) > div > p').text  # 这里提取的是小区位置
                    data_element_jg_00 = driver.find_element(By.CSS_SELECTOR,
                                                             '#__layout > div > div.props-main.w-1170 > div.props-body > div.props-right > div.maininfo > div.house-price > div > span.average').text  # 这里提取的是average价格

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
                        [data_element_jg_0000,data_element_jg_000,data_element_jg_00, data_element_wy_01, data_element_qs_02, data_element_jg_03,
                         data_element_nx_04,
                         data_element_hs_05, data_element_jm_06, data_element_rj_07, data_element_lh_08,
                         data_element_jl_09,
                         data_element_sq_10, data_element_gn_11, data_element_gd_12, data_element_tc_13,
                         data_element_wy_14,
                         data_element_cq_15, data_element_cq_16, data_element_cq_17, data_element_cq_18,
                         data_element_cq_19])
                    driver.back()
                except:
                    pass



def is_next_page_available():
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, '#__layout > div > section > section.list-main > section > div.pagination.page-bar > a.next.next-active')
        return next_button is not None
    except:
        return False






if __name__ =='__main__':

    quyu_elements = get_quyu()
    get_sub_quyu(quyu_elements)
    url_list = cross_over(sub_quyu)
    quyu = 'quyu.xlsx'
    wangzhi = 'wangzhi.csv'
    df = pd.DataFrame(
        {
            "Sub_Area": sub_quyu
        }
    )

    df.to_excel(quyu, index=False, header=True)

    df1 = pd.DataFrame(
        {
            '网址': url_list
        }
    )
    df1.to_csv(wangzhi, mode='w', index=False, header=True, encoding='utf_8_sig')



    ##首先获取第一页数据
    get_data(url_list)
    ##检查是否还有下一页，并且继续获取数据
    while is_next_page_available():
        try:
            driver.find_element(By.CSS_SELECTOR,
                                '#__layout > div > section > section.list-main > section > div.pagination.page-bar > a.next.next-active').click()
            get_data(url_list)
        except:
            break

    headers = ['小区名字', "小区位置", "价格", "物业类型", "权属类型", "竣工时间", "产权年限",
               "总户数", "总建筑面积", "容积率", "绿化率", "建筑类型", "所属商圈", "统一供暖",
               "供水供电", "停车位", "物业费", "停车费", "车位管理费", "物业公司", "小区地址", "开发商"]


    df2 = pd.DataFrame(result, columns=headers)

    # 保存为CSV
    df2.to_csv('output.csv', index=False, encoding='utf-8')
