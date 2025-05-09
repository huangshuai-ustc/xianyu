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
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument(user_data_dir)
service = Service(executable_path=webdriver_path)
driver = webdriver.Chrome(service=service, options=option)
df = pd.read_excel('1.xlsx')
company = df.iloc[:, 0].tolist()
numbers = []
start = "20220101"
end = "20221231"
IPC = ""
url = 'https://analytics.zhihuiya.com/search/input/field'
driver.get('https://analytics.zhihuiya.com/search/input/field')
time.sleep(1)
# 点击代码搜索按钮
driver.find_element(By.CSS_SELECTOR,
                    'body > div.analytics-website > div.analytics-website__body > div > div.search-app.master-nav-wrap-container.master-nav-open > div > div.analytics-search-module__field.search-responsive-content > div > div.afs-right > div.advance-search-form__preview.advance-search-form__preview-fixed > div > div.afsr-search-result > div.es-preview__append > div > div:nth-child(1) > div').click()
for i in company:
    print(i)
    # 点击清除按钮
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR,
                        'body > div.analytics-website > div.analytics-website__body > div > div.search-app.master-nav-wrap-container.master-nav-open > div > div.analytics-search-module__field.search-responsive-content > div > div > div.advance-command-search__action > button.common-search-button.common-search-button__clear').click()
    time.sleep(0.5)
    try:
        driver.find_element(By.CSS_SELECTOR,
                            'body > div.el-dialog__wrapper.patsnap-biz-dialog.clear-query-confirm__dialog > div > div.el-dialog__footer > div > button.patsnap-ui-button.patsnap-ui-button--small.patsnap-ui-button--danger').click()
    except:
        pass
    time.sleep(1)
    # 获取输入框
    key_input = driver.find_element(By.XPATH,
                                    "//div[@class='editor-container div-textarea editor-container--show-error']")
    # 发送关键字
    key = "ALL_AN:({})".format(i)
    key_input.send_keys(key)

    time.sleep(1)
    number = driver.find_element(By.CSS_SELECTOR,
                                 'body > div.analytics-website > div.analytics-website__body > div > div.search-app.master-nav-wrap-container.master-nav-open > div > div.analytics-search-module__field.search-responsive-content > div > div > div.preview-container.search-preview > p:nth-child(1) > span.text-them').text
    if number == '0':
        numbers.append(0)
        time.sleep(1)
    else:
        driver.find_element(By.CSS_SELECTOR,
                            'body > div.analytics-website > div.analytics-website__body > div > div.search-app.master-nav-wrap-container.master-nav-open > div > div.analytics-search-module__field.search-responsive-content > div > div > div.advance-command-search__action > button.common-search-button.common-search-button__search').click()
        time.sleep(3)
        # 获取搜索到的文献数量
        number = driver.find_element(By.CSS_SELECTOR,
                                     'body > div.analytics-website > div.analytics-website__body > div > div.snap-patent-result.master-nav-wrap-container.browser-name--chrome.browser-version--122.browser-os--windows.master-nav-open > div.sidebar-table > div.sidebar-table__right > div:nth-child(1) > div > div.srfb__row.srfb__row__top > div.srfb__row-left > div.srfb__row-column.srfb__quantity-info > button > span > b').text
        driver.back()
        numbers.append(number.replace(',', ''))
        time.sleep(1)
df['专利数量'] = numbers
df.to_excel('2.xlsx', index=False)
