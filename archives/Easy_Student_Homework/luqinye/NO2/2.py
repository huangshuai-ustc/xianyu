import csv
import jieba

f = open('D:/luqinye.txt')  # 打开文件,open(file,mode,encoding)函数格式，示例open(file,mode=‘w’,encoding=‘utf-8’)
f1 = open("d:/sorted.txt", "w",encoding="utf-8")
f2 = open("d:/result_ansi.csv", "w", newline="",encoding="utf-8")
articleText = f.read()  # 读取文件，该方法返回一个字符串
f.close()  # 关闭文件
wordList = jieba.lcut(articleText)  # 用jieba.lcut()方法分中文词汇，并将所有词汇存放在列表wordList中
dic = {}  # 创建一个字典
for word in wordList:  # 将列表中的词汇写进词典
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] += 1
swd = sorted(list(dic.items()), key=lambda lst: lst[1], reverse=True)  # list(dic.items())将字典转化为列表并排序
for kword, times in swd:  # 做循环输出关键词及次数
    # 判断关键词，如果不是列表中的字符则屏幕输出
    if kword not in ["，", "。", "：", "、", "！", "？", "；", "》", "《", "“", "”", "的", "我", "是", "在", "里"]:
        f1.write(kword + "\t" + str(times) + "\n")  # 将结果输出到txt文件
        csv.writer(f2).writerow([kword, times])  # 将结果输出到csv文件
        print(kword, times)  # 输出一行结果看看
