# 提示信息
print('-' * 50)
print('\n')
print('\t\t欢迎来到订单信息管理系统！')
print('\n')

# 循环做以下工作直到用户输入5自动退出
while True:
    # 提示语句
    print('-' * 50)
    print('\n')
    print('\tmenu:')
    print('\n')
    print('\t1、添加订单')
    print('\t2、显示订单')
    print('\t3、编辑订单')
    print('\t4、删除订单')
    print('\t5、退出系统')
    print('\n')
    print('\t请输入你的操作：')
    print('-' * 50)
    # choice为用户自行选择的操作数
    # choice需为int形式的整数
    choice = int(input('请选择你的操作：'))
    # 判断choice是不是int型
    if not isinstance(choice, int):
        # 若不是
        while not isinstance(choice, int):
            # 循环让用户输入直到是int为止
            try:
                choice = int(input('必须输入数字：'))
            except ValueError as ve:
                pass

    # 如果choice为1做添加订单操作
    if choice == 1:
        # 获取订单号
        order_id = input('请输入订单ID：')
        # 获取订单类型
        order_type = input('请输入订单类型：')
        # 获取订单内容
        context = input('请输入订单内容：')
        # 获取成本价格
        # 成本价格需为float形式的数
        cost = float(input('请输入成本价格：'))
        # 判断cost是不是float型
        if not isinstance(cost, float):
            # 若不是
            while not isinstance(cost, float):
                # 循环让用户输入直到是float为止
                try:
                    cost = float(input('必须输入数字：'))
                except ValueError as ve:
                    pass

        # 获取售价
        # 售价需为float形式的数
        price = float(input('请输入售价：'))
        # 判断price是不是float型
        if not isinstance(price, float):
            # 若不是
            while not isinstance(price, float):
                # 循环让用户输入直到是float为止
                try:
                    price = float(input('必须输入数字：'))
                except ValueError as ve:
                    pass

        # 获取当前时间
        time = input('请输入当前时间')
        # 以追加的方式写入order.txt文件
        with open('order.txt', 'a+', encoding='utf-8') as f:
            # 按指定格式写入文件
            f.write('\n订单ID：{},订单类型：{},订单内容：{},成本价格：{},售价：{}，利润：{}'
                    .format(order_id, order_type, context, cost, price, price - cost))
            # 成功写入输入提示添加成功
            print('添加成功')

    # 如果choice为2做显示订单信息操作
    elif choice == 2:
        # 按行读取文件内容
        with open('order.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        print('-' * 50)
        # 按行输出文件内容
        for i in lines:
            print(i)
        print('-' * 50)

    # 如果choice为3做编辑订单信息操作
    elif choice == 3:
        # 按行读取文件内容
        with open('order.txt', 'r', encoding='utf-8') as f1:
            lines = f1.readlines()
        # 输出先有的订单
        print('现有订单')
        for i in lines:
            print(i)
        # 输入要编辑的订单ID
        order_id = input('请输入要编辑的订单ID：')
        # 输入你想更改的订单信息
        change = input('请输入你想更改的订单信息：')
        # 输入你想改成的订单信息
        changed = input('请输入你想改成的订单信息：')
        # 打开一个新的文件覆盖原始文件
        with open('order.txt', 'w', encoding='utf-8') as f2:
            # 遍历每一行
            for i in lines:
                # 判断如果订单ID与文件内相同则更改想更改的部分
                i = i.split(',')
                i = i[0]
                i = i.split('：')
                i = i[-1]
                if order_id != i:
                    f2.write(i.replace(change, changed))
                # 否则不做更改直接写入
                else:
                    f2.write(i)

    # 如果choice为4做删除订单信息操作
    elif choice == 4:
        # 获取想删除的订单ID
        order_id = input('你想删除的订单ID：')
        # 按行读取文件内容
        with open('order.txt', 'r', encoding='utf-8') as f1:
            lines = f1.readlines()
        # 打开一个新文件
        with open('order.txt', 'w', encoding='utf-8') as f2:
            n = 0
            # 遍历旧文件内容
            for i in lines:
                # 判断如果订单ID找不到就直接写入
                i = i.split(',')
                i = i[0]
                i = i.split('：')
                i = i[-1]
                if order_id != i:
                    # 写入基数加一
                    n = n + 1
                    f2.write(i)
            # 判断如果写入计数不等于原来的文件行数则删除成功
            if n != len(lines):
                print('删除ID为{}的订单信息成功！'.format(order_id))
            # 判断如果写入计数等于原来的文件行数则没发现订单信息
            elif n == len(lines):
                print('未发现ID为{}的订单信息'.format(order_id))

    # 如果choice为5做退出系统操作
    elif choice == 5:
        print('感谢您使用本系统。')
        break
