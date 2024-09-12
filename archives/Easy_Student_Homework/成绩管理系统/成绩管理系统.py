grade_list = []


def insert():
    method = int(input("选择成绩导入方式（1、手动输入；2、文件读取）："))
    if method == 1:
        while True:
            name = input("请输入姓名：")
            if name == '结束':
                break
            sno = input("请输入学号：")
            if sno == '结束':
                break
            grade = input("请输入年级：")
            if grade == '结束':
                break
            try:
                sub1 = float(input("请输入科目1成绩："))
                if sub1 == '结束':
                    break
                if not isinstance(sub1, float):
                    while not isinstance(sub1, float):
                        try:
                            sub1 = float(input('必须输入数字：'))
                        except ValueError as ve:
                            pass
                sub2 = float(input("请输入科目2成绩："))
                if sub1 == '结束':
                    break
                if not isinstance(sub2, float):
                    while not isinstance(sub2, float):
                        try:
                            sub2 = float(input('必须输入数字：'))
                        except ValueError as ve:
                            pass
                sub3 = float(input("请输入科目3成绩："))
                if sub3 == '结束':
                    break
                if not isinstance(sub3, float):
                    while not isinstance(sub3, float):
                        try:
                            sub3 = float(input('必须输入数字：'))
                        except ValueError as ve:
                            pass
                info = {'姓名': name, '学号': sno, '年级': grade, '科目1': float(sub1), '科目2': float(sub2),
                        '科目3': float(sub3)}
                grade_list.append(info)
            except:
                print("你输入的成绩不是数字。")
    else:
        f = open('score.txt', 'r', encoding='utf-8')
        score = []
        for i in f.readlines():
            try:
                j = i.strip().split(' ')
                assert len(j) == 6
                score.append(j)
            except:
                print("格式错误", i)
        for _ in score:
            info = {'姓名': _[0], '学号': _[1], '年级': _[2], '科目1': float(_[3]), '科目2': float(_[4]),
                    '科目3': float(_[5])}
            grade_list.append(info)
    for i in grade_list:
        print(i)


def find():
    method = int(input("请输入查询方式：（1、查三科成绩；2、查单科成绩；3、查前三名姓名）"))
    if method == 1:
        name = input("请输入姓名：")
        sno = input("请输入学号：")
        for i in grade_list:
            if i['姓名'] == name and i['学号'] == sno:
                print("科目1成绩", i['科目1'], "科目2成绩", i['科目2'], "科目3成绩", i['科目3'])
            else:
                print("无相关信息。")
    if method == 2:
        name = input("请输入姓名：")
        sno = input("请输入学号：")
        sub = input("请输入某一科目：（科目1、科目2、科目3）")
        try:
            for i in grade_list:
                if i['姓名'] == name and i['学号'] == sno:
                    if sub in ['科目1', '科目2', '科目3']:
                        print(i[sub])
        except:
            print("无相关信息。")
    if method == 3:
        sub = input("请输入某一科目：（科目1、科目2、科目3）")
        try:
            grade_list.sort(key=lambda x: x[sub], reverse=True)
            if len(grade_list) >= 3:
                print(grade_list[0]['姓名'], grade_list[1]['姓名'], grade_list[2]['姓名'])
            else:
                for i in grade_list:
                    print(i['姓名'])
        except:
            print("请输入正确的科目。")


def change():
    name = input("请输入姓名：")
    sno = input("请输入学号：")
    sub = input("请输入某一科目：（科目1、科目2、科目3）")
    sub_score = int(input("请输入修改后的成绩："))
    for i in grade_list:
        if i['姓名'] == name and i['学号'] == sno:
            i[sub] = sub_score
        print(i)


if __name__ == '__main__':
    insert()
    print('-' * 50)
    find()
    print('-' * 50)
    change()
