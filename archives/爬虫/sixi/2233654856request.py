# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    ElementClickInterceptedException
)

# 新版本的Selenium使用Service对象来指定ChromeDriver的路径
webdriver_path = r"D:\Download\IdmDownload\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=webdriver_path)
driver = webdriver.Chrome(service=service)

# 打开登录页面
driver.get('https://www.boardvitals.com/users/sign_in')

# 设置显式等待
wait = WebDriverWait(driver, 10)

# 定位邮箱和密码输入框并输入凭据
email_input = wait.until(EC.visibility_of_element_located((By.ID, 'ua-username')))
email_input.send_keys('daizq3@gmail.com')

password_input = wait.until(EC.visibility_of_element_located((By.ID, 'ua-password')))
password_input.send_keys('Qs8928322!')

# 点击登录按钮
login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ua-submit')))
login_button.click()

# 等待登录完成，以确保“Review”按钮可点击
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Review')]"))).click()

# 如果"Review Questions"是在新页面加载后出现的，应该在这里加入对应的显式等待
review_questions_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Review Questions')]")))
review_questions_button.click()

import pandas as pd
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# 定位并点击"Questions List"按钮
try:
    # 使用按钮的类名定位Questions List按钮
    questions_list_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'drawer-trigger')))
    questions_list_button.click()
except TimeoutException:
    print("The 'Questions List' button could not be found on the page.")

scrollable_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".scrollable")))

# 在循环开始前初始化last_category_text为None
last_category_text = None

# 初始收集可见的Category信息
categories = []

# 收集所有类wenj别
new_categories_collected = True
while new_categories_collected:
    new_categories_collected = False
    current_category_elements = scrollable_element.find_elements(By.CSS_SELECTOR,
                                                                 "div.col.text-break.col-2.d-none.d-sm-block > span")

    # 如果这是第一次循环或者新的类别被发现，则更新last_category_text
    if last_category_text is None or new_categories_collected:
        last_category_text = current_category_elements[-1].text.strip() if current_category_elements else ""

    for element in current_category_elements:
        category_text = element.text.strip()
        if category_text not in categories:
            categories.append(category_text)
            new_categories_collected = True

    # 如果有新的类别被添加，则滚动可滚动元素
    if new_categories_collected:
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_element)
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element(By.CSS_SELECTOR,
                                               "div.col.text-break.col-2.d-none.d-sm-block > span:last-child").text.strip() != last_category_text
        )

        # 现在再次获取类别元素，并更新last_category_text
        new_category_elements = scrollable_element.find_elements(By.CSS_SELECTOR,
                                                                 "div.col.text-break.col-2.d-none.d-sm-block > span")
        new_last_category_text = new_category_elements[-1].text.strip() if new_category_elements else ""

        # 如果新获取的最后一个类别文本与之前的不同，则说明有新类别被加载
        if new_last_category_text != last_category_text:
            new_categories_collected = True
            last_category_text = new_last_category_text  # 更新最后一个类别的文本以便于下一次比较

# 收集完分类信息后点击返回主页面的按钮
try:
    back_to_main_page_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'drawer-trigger')))
    driver.execute_script("arguments[0].click();", back_to_main_page_button)
except TimeoutException:
    print("The 'Questions List' button could not be found or is not clickable.")
except ElementClickInterceptedException:
    print("Element click was intercepted by another element, trying JavaScript click.")

driver.find_element(By.CSS_SELECTOR, "#App > main > button").click()
time.sleep(3)
subjects = []
for i in range(28):
    subject = driver.find_element(By.CSS_SELECTOR, "#App > main > div.QuestionListDrawer.shown > div > div > div "
                                                    "> div.position-relative.columns-container.scrollable > "
                                                    "div:nth-child({}) > "
                                                    "div.col.text-break.col-2.d-none.d-sm-block > span".format(i+1)).text
    subjects.append(subject)
# 初始化问题和答案的列表
driver.find_element(By.CSS_SELECTOR, "#App > main > button").click()
questions_with_answers = []

# 独立地收集28个问题和答案
for i in range(28):
    try:
        # 获取问题文本
        question_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".wysiwyg.question-name.mb-3")))
        question_text = question_element.text
        print(f"Collecting question {i + 1}: {question_text}")

        # 获取所有答案文本和答案标记
        answer_labels = driver.find_elements(By.CSS_SELECTOR, ".answer-index")
        answer_texts = driver.find_elements(By.CSS_SELECTOR, ".wysiwyg.answer-name")

        # 获取正确答案的文本
        correct_answer_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".question-correct-answer.d-flex.flex-row")))
        # 分割并清洗文本以提取正确答案字母
        correct_answer_text = correct_answer_element.text.split("Correct Answer: ")[-1].strip()

        # 提取正确答案的首字母
        correct_answer_letter = correct_answer_text.split('.')[0].strip()

        # 获取难度等级的文本
        difficulty_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".difficulty-level-value.mt-1")))
        difficulty_level = difficulty_element.text

        # 组合答案标记和答案文本
        combined_answers = []
        for label, text in zip(answer_labels, answer_texts):
            label_text = label.text.strip()  # 去除可能的空格
            if not label_text.endswith('.'):  # 如果label_text不以点号结尾
                label_text += '.'  # 添加点号
            combined_answer = f"{label_text} {text.text.strip()}"  # 去除答案文本的可能空格，并组合
            combined_answers.append(combined_answer)

        # 将问题、答案、正确答案字母和难度等级组合成一个字典
        question_with_answer_info = {
            'Question': question_text,
            'Answers': ' | '.join(combined_answers),
            'Correct Answer': correct_answer_text,
            'Correct Answer Letter': correct_answer_letter,  # 添加正确答案字母
            'Category': subjects[i]
        }

        # 添加字典到列表
        questions_with_answers.append(question_with_answer_info)

        # 点击“下一页”按钮，前往下一个问题
        next_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "next-button")))
        next_button.click()


    except Exception as e:
        print(f"An error occurred: {e}")

    # 关闭浏览器
driver.quit()

# 如果收集到问题和答案，则保存到Excel文件
if questions_with_answers:
    df = pd.DataFrame(questions_with_answers)
    df.to_excel('questions_with_answers.xlsx', index=False)
    print("Questions and answers have been saved to Excel file.")
else:
    print("No questions or answers were collected.")
