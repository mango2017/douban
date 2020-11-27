import selenium
import time
from selenium import webdriver
from selenium.webdriver.support import  ui

#darius
#top

wait_time = 180
#1.用户输入
position = input("请输入您想查询的位置")
hero = input("请输入您想查询的英雄")

#2.构造网址
url=f'https://www.op.gg/champion/{hero}/statistics/{position}/matchup'

#3.打开浏览器
browser = webdriver.Chrome()
browser.get(url)
browser.implicitly_wait(10)

wait = ui.WebDriverWait(browser,wait_time)
try:
    wait.until(lambda driver:driver.find_elements_by_xpath("//div[@class='champion-matchup-list__champion']//span[1]"))
    buttons = browser.find_elements_by_xpath("//div[@class='champion-matchup-list__champion']//span[1]")
except Exception as error1:
    print(error1)
    buttons = browser.find_elements_by_xpath("//div[@class='champion-matchup-list__champion']//span[1]")
    time.sleep(10)


# some_botton = buttons[2]

#遍历每一个按钮节点
for button in buttons:
    #点击按钮
    browser.execute_script("arguments[0].click();",button)
    #寻找表格的最左列
    wait = ui.WebDriverWait(browser,wait_time)
    try:
        wait.until(lambda driver:driver.find_elements_by_xpath("//table[@class='champion-matchup-table']//td[1]"))
        col = browser.find_elements_by_xpath("//table[@class='champion-matchup-table']//td[1]")
    except Exception as error1:
        browser.execute_script("arguments[0].click();", button)
        col = browser.find_elements_by_xpath("//table[@class='champion-matchup-table']//td[1]")
        time.sleep(10)
    print(col)
    print(button.text,col[0].text,col[6].text)