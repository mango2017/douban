from selenium import webdriver

# 抓取猫眼正在热映的电影
url = "https://maoyan.com/?utm_source=meituanweb"

browser = webdriver.Chrome()
browser.get(url)
browser.implicitly_wait(10)

movie_list = browser.find_elements_by_xpath("//div[@class='movie-grid']/div[1]//dl[@class='movie-list']/dd")
print(len(movie_list))
