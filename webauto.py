from selenium import webdriver
from time import sleep
# wd = webdriver.Chrome()
# wd.get("https://www.baidu.com")
# #根据id选择元素，返回的就是该元素对应的webelement对象
# element = wd.find_element_by_id("kw")  #查找id=kw的元素
# #通过webelement对象 就可以对页面元素进行操作了
# #比如输入字符串到这个输入框里
# # element.send_keys("php\n")
# element.send_keys("php")
# element2 = wd.find_element_by_id("su")
# element2.click()

# wd.get("http://cdn1.python3.vip/files/selenium/sample1.html")
# elements = wd.find_element_by_class_name("animal123")
# # for element in elements:
# print(elements.text)

# elements = wd.find_elements_by_tag_name("span")
# for element in elements:
#     print(element.text)

# element = wd.find_element_by_id("container")
# spans = element.find_elements_by_tag_name("span")
# for span in spans:
#     print(span.text)


wd = webdriver.Chrome()
# 设置最大等待时长为 10秒
wd.implicitly_wait(10)
wd.get("https://www.baidu.com")
element = wd.find_element_by_id('kw')
element.send_keys('白月黑雨\n')
# sleep(2)
element = wd.find_element_by_id("1")
print(element.get_attribute("srcid"))
print(element.get_attribute('outerHTML'))
print(element.get_attribute('innerHTML'))
wd.quit()