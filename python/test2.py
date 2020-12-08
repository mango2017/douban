class BenzCar:
    brand = '奔驰'
    country = '德国'

    @staticmethod
    def pressHorn():
        print('嘟嘟....')


    def __init__(self,color,engineSN):
        self.color = color
        self.engineSN = engineSN

    def changeColor(self,newColor):
        self.color = newColor


class Benz2018(BenzCar):
    price = 88000
    model = 'Benz2018'


    def __init__(self,color,engineSN,weight):
        BenzCar.__init__(self,color,engineSN)
        self.weight = weight
        self.oilweight= 0

    def fillOil(self,oildAdded):
        self.oilweight += oildAdded
        self.weight += oildAdded


car2 = Benz2018('blue','1111111',1500)
print(car2.oilweight)
print(car2.weight)

car2.fillOil(50)
print(car2.oilweight)
print(car2.weight)