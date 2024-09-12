from bs4 import BeautifulSoup

# 假设html_content包含了您的HTML代码
html_content = """
<a class="index_alink__zcia5 link-click" href="https://www.tianyancha.com/company/3200941879" target="_blank"><span><em>天合光能（宿迁）科技有限公司</em></span></a>
"""

# 使用Beautiful Soup解析HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 找到<a>标签
a_tag = soup.find('a', class_='index_alink__zcia5 link-click')

# 提取href属性的内容
href_content = a_tag['href']

# 打印结果
print(href_content)
