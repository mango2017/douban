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

while True:
    miles = input('请输入英里数')
    km = int(miles) * 1.609344
    print(f'等于{km}公里')