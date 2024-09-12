import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置selenium的一些属性，对selenium进行伪装，防止被服务器认出
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument("--disable-blink-features=AutomationControlled")
chrome = Chrome(options=option)

fs = open('专利信息.csv', 'w', encoding='utf-8')


def getCompanies():
    with open('data.txt', 'r', encoding='utf-8') as f:
        comList = [item.strip('\n') for item in f.readlines()]
    return comList


def getKeyWords():
    wordList = []
    with open('自定义关键词.txt', 'r', encoding='utf-8') as f:
        txtList = [item.strip('\n') for item in f.readlines()]
    for i in txtList:
        if i == '':
            continue
        else:
            i = i.strip()
            wordList.append(i)
    return " OR ".join(wordList)


# 模拟登录
def login(url):
    # 获取登录页面
    chrome.get(url)
    print('进入登录页面，请手工完成登录，登录完毕请回控制台输入任意字符继续')
    time.sleep(1)
    # 点击账号登录
    checkbox = chrome.find_element(By.XPATH, '//div[@id="tab-EMAIL_PASSWORD"]')
    print(checkbox)
    checkbox.click()
    # 找到账户密码的交互接口并进行输入
    user_name = chrome.find_element(By.XPATH, '//input[@type="text"]')
    # 输入手机号
    user_name.send_keys('18521778679')
    # 找到账户密码的交互接口并进行输入
    user_pass = chrome.find_element(By.XPATH, '//input[@type="password"]')
    # 输入手机号
    user_pass.send_keys('18521778679mfh')
    # 点击登录
    loginbox = chrome.find_element(By.XPATH,
                                   '//button[@class="el-button login-panel__submit el-button--primary el-button--large"]')
    loginbox.click()
    # 此处需要滑动滑块
    input()


def parse():
    time.sleep(3)
    print('进入parse函数！')
    comList = getCompanies()
    # 读取关键词自定义文件
    keyword = getKeyWords()
    print(keyword)
    # 自定义时间
    start = "20220101"
    end = "20221231"
    # 考虑专利号
    IPC = "G05B13/02 0R G05B13/04 OR G05B15/00 OR G05B15/02 OR G05B19/418 OR G05B19/042 OR G06E1/00 OR G06E3/00 OR G06F3/01 OR G06F3/02 OR G06F3/023 OR G06F3/027 OR G06F3/03 OR G06F3/033 OR G06F3/0338 OR G06F3/0346 OR G06F3/0354 OR G06F3/0362 OR G06F3/037 OR G06F3/038 OR G06F3/039 OR G06F3/041 OR G06F3/042 OR G06F3/043 OR G06F3/044 OR G06F3/045 OR G06F3/046 OR G06F3/047 OR G06F3/048 OR G06F3/0481 OR G06F3/04812 OR G06F3/04815 OR G06F3/04817 OR G06F3/0482 OR G06F3/0483 OR G06F3/0484 OR G06F3/04842 OR G06F3/04845 OR G06F3/04847 OR G06F3/0485 OR G06F3/04855 OR G06F3/0486 OR G06F3/0487 OR G06F3/0488 OR G06F3/04883 OR G06F3/04886 OR G06F3/0489 OR G06F3/14 OR G06F3/15 OR G06F9/44 OR G06F9/50 OR G06F9/54 OR G06F15/18 OR G06F15/00 OR G06F17/00 OR G06F17/20 OR G06F17/28 OR G06F17/30 OR G06F17/50 OR G06G7/00 OR G06J1/00 OR G06K9 OR G06K11 OR G06N3/00 OR G06N3/02 OR G06N3/04 OR G06N3/08 OR G06N3/10 OR G06N3/12 OR G06N5/00 OR G06N5/02 OR G06N5/04 OR G06N7/00 OR G06N7/02 OR G06N7/04 OR G06N7/06 OR G06N7/08 OR G06N99/00 OR G06Q10 OR G06Q30 OR G06Q50/04 OR G06Q90 OR G06T7 OR G06T11/80 OR G06T13 OR G06T15 OR G06T17/00 OR G06T17/05 OR G06T17/10 OR G06T17/20 OR G06T17/30 OR G06T19/00 OR G06T19/20 OR G08G1/0962 OR G08G1/0965 OR G08G1/0967 OR G08G1/0968 OR G08G1/0969 OR G10L13/027 OR G10L15 OR G10L17 OR G10L25/00 OR G10L25/63 OR G10L25/66 OR G16H"
    key_input = chrome.find_element(By.XPATH,
                                    "//div[@class='editor-container div-textarea editor-container--show-error']")
    for company in comList:
        # key = "ALL_AN:({}) AND APD:[{} TO {}] AND IPC:({}) AND TA:({})".format(company, start, end, IPC, keyword)
        key = "ALL_AN:({}) AND APD:[{} TO {}] AND IPC:({})".format(company, start, end, IPC)
        # key = "ALL_AN:({}) AND ISD:[{} TO {}] AND TA:({})", company, start, end,keyword)
        #key = "ALL_AN:({}) AND ISD:[{} TO {}]".format(company, start, end)
        # 输入查询条件
        key_input.clear()
        key_input.send_keys(key)
        # print(key)
        if len(key) >= 1500:
            print('当前检索式长度：{}，适当去除一些关键词！！！'.format(len(key)))
            return
        time.sleep(3)
        try:
            res = WebDriverWait(chrome, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//span[contains(@class,'text-them') and @style!='display:none']"))
            )
            print(f"{company},{res.text}")
            fs.write(f"{company},{res.text}\n")
        except Exception as e:
            print(f"Error for {company}: {e}")
            print(f"{company},0")
            fs.write(f"{company},0\n")
'''
        try:
            res = WebDriverWait(chrome, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//span[contains(@class,'text-them') and @style!='display:none']"))
            )
            print(f"{company},{res.text}")
            fs.write(f"{company},{res.text}\n")
        finally:
            print(f"{company},0")
            fs.write(f"{company},0\n")
'''

if __name__ == '__main__':
    login('https://account.zhihuiya.com/#/')
    parse()
