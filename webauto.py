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


# wd = webdriver.Chrome()
# # 设置最大等待时长为 10秒
# wd.implicitly_wait(10)
# wd.get("https://www.baidu.com")
# element = wd.find_element_by_id('kw')
# element.send_keys('白月黑雨\n')
# # sleep(2)
# element = wd.find_element_by_id("1")
# print(element.get_attribute("srcid"))
# print(element.get_attribute('outerHTML'))
# print(element.get_attribute('innerHTML'))
#
# wd.quit()




wd = webdriver.Chrome()
# 设置最大等待时长为 10秒

# wd.get("http://cdn1.python3.vip/files/selenium/sample1.html")
# element = wd.find_element_by_css_selector(".animal")
# print(element.get_attribute("outerHTML"))

# elements = wd.find_elements_by_css_selector("span")
# for element in elements:
#     print(element.get_attribute("outerHTML"))

# element = wd.find_element_by_css_selector("#searchtext")
# print(element.get_attribute('outerHTML'))
# 
# wd.quit()


# wd.get("http://cdn1.python3.vip/files/selenium/sample1.html")
# # elements = wd.find_elements_by_css_selector("#container > div ")
# elements = wd.find_elements_by_css_selector("#container  span ")
# for element in elements:
#     print(element.get_attribute("outerHTML"))
# wd.quit()


# wd.get("http://cdn1.python3.vip/files/selenium/sample2.html")
# wd.switch_to.frame("frame1")
# elements = wd.find_elements_by_css_selector(".plant")
# for element in elements:
#     print(element.get_attribute("outerHTML"))
# wd.switch_to.default_content()
# wd.find_element_by_id('outerbutton').click()
# wd.quit()


wd.get('http://cdn1.python3.vip/files/selenium/sample3.html')
link = wd.find_element_by_tag_name("a")
link.click()
mainWindow = wd.current_window_handle
for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if 'Bing' in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break
print(wd.title)
wd.find_element_by_id("sb_form_q").send_keys("白月黑雨")
wd.switch_to.window(mainWindow)