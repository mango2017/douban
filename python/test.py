# def pressHorn():
#     print('嘟嘟....')
#
# benzCar = {
#     'brand': '奔驰',
#     'country': '德国',
#     'price': 300000,
#     'pressHorn': pressHorn  # 字典对象的值可以是一个函数对象
# }
#
# benzCar['pressHorn']()
class BenzCar:
    brand = '奔驰'
    country = '德国'

    @staticmethod
    def pressHorn():
        print('嘟嘟...')

    def __init__(self,color,engineSN):
        self.color = color
        self.engineSN = engineSN
        # self.brand = "heihei"

class Benz2016(BenzCar):
    price = 1000
    model = 'Benz2016'


class Benz2018(BenzCar):
    price = 20000
    model = 'Benz2018'

car1 = Benz2016('red','1222222')
car2 = Benz2018('blue','22233333')

print(car1.color)
print(car1.price)
# BenzCar.pressHorn()

# car1 = BenzCar()
# car2 = BenzCar()
# print(car1)
# print(car2)
# print(car1.brand)
# car1.pressHorn()
# for i in range(5):
#     print(i)

# car1 = BenzCar('red','1234')
# print(car1.color)
# print(car1.brand)
# print(car1.pressHorn())
# print("------------------")
# car2 = BenzCar('green','1234')
# print(car2.color)
# print(car2.brand)
#
# print(car2.pressHorn())
# c1 = BenzCar('red','1234')
# print(BenzCar.brand)
# print(c1.brand)