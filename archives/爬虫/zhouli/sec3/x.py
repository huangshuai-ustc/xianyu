f1 = open('1.txt', 'r', encoding='utf-8')
name = f1.readlines()
f2 = open('2.txt', 'r', encoding='utf-8')
link = f2.readlines()
f3 = open('3.txt', 'w', encoding='utf-8')
for i, j in zip(name, link):
    f3.write(i.strip() + ' ' + j)
