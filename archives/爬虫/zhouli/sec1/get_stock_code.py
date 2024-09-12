xx = []
with open('stock_code.txt', 'r') as f:
    x = f.readlines()
for i in x:
    xx.append(i.strip())

# print(xx)
