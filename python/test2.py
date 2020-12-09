# class BenzCar:
#     brand = '奔驰'
#     country = '德国'
#
#     @staticmethod
#     def pressHorn():
#         print('嘟嘟....')
#
#
#     def __init__(self,color,engineSN):
#         self.color = color
#         self.engineSN = engineSN
#
#     def changeColor(self,newColor):
#         self.color = newColor
#
#
# class Benz2018(BenzCar):
#     price = 88000
#     model = 'Benz2018'
#
#
#     def __init__(self,color,engineSN,weight):
#         BenzCar.__init__(self,color,engineSN)
#         self.weight = weight
#         self.oilweight= 0
#
#     def fillOil(self,oildAdded):
#         self.oilweight += oildAdded
#         self.weight += oildAdded
#
#
# car2 = Benz2018('blue','1111111',1500)
# print(car2.oilweight)
# print(car2.weight)
#
# car2.fillOil(50)
# print(car2.oilweight)
# print(car2.weight)
#
# print(car2.price)
# car1 = BenzCar('red','222222222')
# print(car1.color)


# ----------------------------------------------------


# class Tire:
#     def __init__(self,size,createDate):
#         self.size = size
#         self.createDate = createDate
#
#
# class BenzCar:
#     brand = '奔驰'
#     country = '德国'
#
#     def __init__(self,color,engineSN,tires):
#         self.color = color
#         self.engineSN = engineSN
#         self.tires = tires
#
# tires = [Tire(20,'20201515') for i in range(4)]
# # print(tires)
#
# car  = BenzCar('red','222222',tires)


# --------------------------------------
# a = 100/0
# print(a)
#
# dict1 = {1:1}
# print(dict1[2])

# while True:
#     miles = input('请输入英里数')
#     km = int(miles) * 1.609344
#     print(f'等于{km}公里')


# while True:
#     try:
#         miles = input('请输入英里数')
#         km = int(miles) * 1.609
#         print(f'等于{km}公里')
#     except ValueError:
#         print('输入非法字符')

# import traceback  #打印异常
# while True:
#     try:
#         100/0
#     except Exception as e:
#         print(traceback.format_exc())

# import traceback
# class InvalidCharError(Exception):
#     pass
#
# # 异常对象，代表电话号码非中国号码
# class NotChinaTelError(Exception):
#     pass
#
#
# def register():
#     tel = input('请注册您的电话号码:')
#
#     # 如果有非数字字符
#     if not tel.isdigit():
#         raise InvalidCharError
#
#     # 如果不是以86开头，则不是中国号码
#     if not tel.startswith('86'):
#         raise NotChinaTelError
#
#     return tel
#
#
# try:
#     ret = register()
# except InvalidCharError:
#     print('电话号码中有错误的字符',traceback.format_exc())
# except NotChinaTelError:
#     print('非中国手机号码',traceback.format_exc())


def level_3():
    print('进入level_3')
    a = [0]
    b = a[0]
    print('离开level_3')
def level_2():
    print('进入level_2')
    level_3()
    print('离开level_2')
def level_1():
    print('进入level_1')
    level_2()
    print('离开level_1')


level_1()
print('程序正常退出')
