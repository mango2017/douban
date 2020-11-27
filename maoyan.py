from selenium import webdriver

# 抓取猫眼正在热映的电影
url = "https://maoyan.com/?utm_source=meituanweb"

browser = webdriver.Chrome()
browser.get(url)
browser.implicitly_wait(10)

