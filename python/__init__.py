# info = {'name':'哈哈哈','height':'180cm'}
# info['height'] = '175cm'
# print(info)


# letter = '''刘总：
#    '您好！'
#    "您发的货我们已经收到，明天就把余款付清。"
#
#                祝： 商祺。
#                小徐
#                2016-06-12'''
#
# hello = '''hi
#         fjdskjfs
#         '''
#
# print(hello)

# letter = "hello!"
# print(letter[-1])
# print(len(letter))
# print(letter[1:4])
# print(letter[-3:-1])

# def func(arg1,arg2,arg3):
#     print(arg1)
#     print(arg2)
#     print(arg3)
#
# func(arg2="hi",arg1="hello",arg3="word")

# a=[1,2,3,4,"hello",[7,8,9]]
# print(a[-1][2])
# a[-1][2] = 10
# print(a)
# a[1:4]=[6,6,6]
# print(a)
# print(a[-6])

# a=(1,)
# print(a)

# a="hello world"
# # a[0]="g"
# # print(a)

# x,y=(1,2)
# print(x,y)

# print(1==1)
# print('1'=='1')
# print(1!=2)

# def registerUser():
#     phone = input("输入手机号")
#     if len(phone)>11:
#         print("输入错误")
#     elif not phone.isdigit():
#         print("输入的手机号码不是数字")
#     elif not phone.startswith("1"):
#         print("输入错误，手机号码必须以1开头")
#     else:
#         print("输入正确")
#     print("函数结束")
# registerUser()


# var1=[1,2,3,4,5,6,7]
# var1.reverse()
# print(var1)

# print('我们今天不去上学，我们去踢足球'.count('我们'))
#
# str1 = '我们今天不去上学，我们去贴足球'
# pos1 = str1.find('我们')
# print(pos1)
#
# pos2 = str1.find('我们',5)
# print(pos2)

# str1 = '小张：79 | 小李：88 | 小赵：83'
# pos1 = str1.split('|')
# print(pos1[1])
# salary = '''
# 小王
# 小李
# 小醋
# '''
# print(salary.splitlines())

# a = "|".join([
#     '小张：79 ',
#     '小李：88',
#     '小赵：86'
# ])
# print(a)

# print('    小李: 888    ' .strip())
# print('    小李: 888    ' .lstrip())
# print('    小李: 888    ' .rstrip())

# str1 = "我们今天不去上学，我们去踢足球"
# str2 = str1.replace('我们','他们')
# print(str1)
# print(str2)


# str1 = "字符串的倒序"
# reverse = str1[::-1]
# print(reverse)

# a=[1,2,3,'hello']
# a.append('你好')
# print(a)
#
# a.append([7,8])
# print(a)
#
# a.insert(0,'你好')
# print(a)
#
# b = a.pop(3)
# print(a)
# print(b)
# a.remove('你好')
# print(a)
# a.reverse()
# print(a)
# print(a.index(1))
# str = [7,9,3,2]
# str.sort()
# print(str)

# salary = input('请输入薪资')
# tax = int(salary)*25/100
# taxStr = str(tax)
#
# aftertax = int(salary)*75/100
# aftertax = str(aftertax)
# salary = str(salary)
# print('税前薪资是'+salary+'元，缴税：'+taxStr + '元，税后薪资是：'+aftertax)

# print('税前工资 %010d'%1000)
# sarlay = 1000
# print(f'工资{sarlay:x}')

# path='c:\\windows\\temp'
# print(path)

# command = input('请输入命令')
# while command != 'exit':
#     print(f'输入的命令是{command}')
#     command = input('请输入命令')

# for n in range(50,101,5):
#     print(n)
#
# studentAges = ['小王:17', '小赵:16', '小李:18', '小孙:16', '小徐:18']
# for index,student in enumerate(studentAges):
#     # print(index)
#     if int(student.split(':')[-1])>17:
#         print(index)


# list1 = [1,2,3,4,5,6]
# list2 = [num**3 for num in list1]
# print(list2)

# list1 = ['关羽','张飞','赵云','马超','黄忠']
# list2 = ['典韦','许褚','张辽','夏侯惇','夏侯渊']
#
# for member1 in list1:
#     for member2 in list2:
#         print(f'{member1} 大战 {member2}')

# print('你好'.encode('utf8'))
# print('你好'.encode('gbk'))

# print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf8'))
# w会覆盖 a是追加
# f = open('tmp.txt','a',encoding='utf8')
# f.write('白月黑羽再次祝大家 ：good luck\n')
# f.close()

# f = open('tmp.txt','r',encoding='utf8')
# content = f.read()
# f.close()
# name = content.split('：')[0]
# print(name)

# f = open('tmp.txt')
# tmp = f.read(3)
# print(tmp)
#
# tmp = f.read(3)
# print(tmp)
#
# tmp = f.read()
# print(tmp)
# f.close()

# f = open('tmp.txt')
# linlist = f.readlines()
# f.close()
# for line in linlist:
#     print(line)

# def savetofile(memberlist,avgfee):
#     with open('record.txt','a',encoding='utf8') as f:
#         recordList = [f'{member}:{avgfee}' for member in memberlist]
#         f.write('|'.join(recordList)+'\n')