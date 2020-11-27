#参考https://www.pythonf.cn/read/102528 即可成功
#打开浏览器
from selenium import  webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.close()

#