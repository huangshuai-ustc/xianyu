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
company = ' OR '.join(df.iloc[:, 0].tolist()[:10])
start = "20220101"
end = "20221231"
IPC = ""
url = 'https://analytics.zhihuiya.com/search/input/field'
driver.get('https://analytics.zhihuiya.com/search/input/field')
time.sleep(1)
# 点击代码搜索按钮
driver.find_element(By.CSS_SELECTOR,
                    'body > div.analytics-website > div.analytics-website__body > div > div.search-app.master-nav-wrap-container.master-nav-open > div > div.analytics-search-module__field.search-responsive-content > div > div.afs-right > div.advance-search-form__preview.advance-search-form__preview-fixed > div > div.afsr-search-result > div.es-preview__append > div > div:nth-child(1) > div').click()
# 点击清除按钮
driver.find_element(By.CSS_SELECTOR,
                    'body > div.analytics-website > div.analytics-website__body > div > div.search-app.master-nav-wrap-container.master-nav-open > div > div.analytics-search-module__field.search-responsive-content > div > div > div.advance-command-search__action > button.common-search-button.common-search-button__clear').click()
time.sleep(1)
# 获取输入框
key_input = driver.find_element(By.XPATH, "//div[@class='editor-container div-textarea editor-container--show-error']")
# 发送关键字
key = "ALL_AN:({}) AND APD:[{} TO {}]".format(company, start, end)
key_input.send_keys(key)
time.sleep(3)
# 获取搜索到的文献数量
number = driver.find_element(By.CSS_SELECTOR,
                             'body > div.analytics-website > div.analytics-website__body > div > div.search-app.master-nav-wrap-container.master-nav-open > div > div.analytics-search-module__field.search-responsive-content > div > div > div.preview-container.search-preview > p:nth-child(1) > span.text-them').text
# 点击搜索
driver.find_element(By.CSS_SELECTOR,
                    'body > div.analytics-website > div.analytics-website__body > div > div.search-app.master-nav-wrap-container.master-nav-open > div > div.analytics-search-module__field.search-responsive-content > div > div > div.advance-command-search__action > button.common-search-button.common-search-button__search').click()
time.sleep(3)
# 点击导出按钮
driver.find_element(By.CSS_SELECTOR,
                    'body > div.analytics-website > div.analytics-website__body > div > div.snap-patent-result.master-nav-wrap-container.browser-name--chrome.browser-version--120.browser-os--windows.master-nav-open > div.sidebar-table > div.sidebar-table__right > div:nth-child(1) > div > div.srfb__row.srfb__row__top > div.srfb__row-right > div:nth-child(1) > button > svg > use').click()
time.sleep(3)
# 获取当前drive页面信息
handles = driver.window_handles
# 切换到第二个页面
driver.switch_to.window(handles[1])
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,
                    'body > div.analytics-website > div.wrapper > div > div.export-content-wrapper > div > div.export-content-left > div.export-templates-wrapper.section > div.export-content-config > div.field-language-selector > div.field-language-selector-right > div.common-select-wrapper > div.el-select.common-select > div.el-input.el-input--suffix > input').click()
driver.find_element(By.CSS_SELECTOR,
                    'body > div.el-select-dropdown.el-popper.is-multiple.common-select-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li.el-select-dropdown__item.selected').click()
driver.find_element(By.CSS_SELECTOR,
                    'body > div.el-select-dropdown.el-popper.is-multiple.common-select-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1)').click()
driver.find_element(By.CSS_SELECTOR,
                    'body > div.analytics-website > div.wrapper > div > div.section-submit > div > button').click()
time.sleep(60)
