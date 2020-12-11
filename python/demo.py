from selenium import webdriver

import time


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

#登录状态
cookie_1 = {"name":"BAIDUID","value":"7C01715B86E516AA57B927789FDD8C72:FG=1"}
cookie_2 = {"name":"BDUSS","value":"g1c2x0cWJwM0xqMW9TTFBiR0ZZOHM4Rm9xaWtCcHFvazhZOHV4UX52cWhidnBmRVFBQUFBJCQAAAAAAAAAAAEAAADtYPw1bWFuZ28yMDE4OAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKHh0l-h4dJfRG"}

time.sleep(5)
driver.add_cookie(cookie_1)
driver.add_cookie(cookie_2)
driver.get("https://www.baidu.com")