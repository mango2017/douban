import time

# 定义一个装饰器函数
def sayLocal(func):
    def wrapper2():
        curTime = func()
        return f'当地时间： {curTime}'
    return wrapper2

def getXXXTime():
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())

# 装饰 getXXXTime
getXXXTime = sayLocal(getXXXTime)

print (getXXXTime())