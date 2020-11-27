from selenium import webdriver

# 抓取猫眼正在热映的电影
url = "https://maoyan.com/?utm_source=meituanweb"

browser = webdriver.Chrome()
browser.get(url)
browser.implicitly_wait(10)

movie_list = browser.find_elements_by_xpath("//div[@class='movie-grid']/div[1]//dl[@class='movie-list']/dd")
print(type(movie_list))
for key,m_item in enumerate(movie_list):
    movie_item = {}
    movie_name = browser.find_elements_by_xpath("//div[@class='movie-grid']/div[1]//dl[@class='movie-list']/dd//div[contains(@class,'movie-title')]")  #获取电影名字
    movie_item['movie_name'] = movie_name[key].text

    # movie_item['movie_href'] = "https://maoyan.com" + browser.find_elements_by_xpath("//div[@class='movie-grid']/div[1]//dl[@class='movie-list']/dd//div[@class='movie-item']/a/@href")
    movie_href = browser.find_elements_by_xpath("//div[@class='movie-grid']/div[1]//dl[@class='movie-list']/dd//div[@class='movie-item']/a")
    movie_item['movie_href'] = movie_href[key].get_attribute('href')
    maoyan_movie_detail_page = browser.get(movie_item['movie_href'])   #进入电影详情页面
    movie_detail = browser.find_elements_by_xpath("//div[@class='mod-content']/span")
    movie_item['movie_detail'] = movie_detail[0].text
    movie_score = browser.find_elements_by_xpath("//span[@class='index-left info-num ']//span[@class='stonefont']")
    movie_item['movie_score'] = movie_score[key].text
    print(movie_score[key].text)
    browser.back()


    # movie_item['movie_name'] = movie_name.text
    #
    # try:
    #



        # score_2 = m_item.find_elements_by_xpath("//div[@class='movie-grid']/div[1]//dl[@class='movie-list']/dd//div[@class='movie-score']/i[2]")
    # except Exception as error:
    #     print("none")
    # if score_1 and score_2:
    #     movie_item['movie_score'] = score_1[key].text + score_2[key].text
    # else:
    #     movie_item['movie_score'] = 0
        # print(score_1[key].text)

    # print(score_2[key].text)

    # movie_item['movie_href'] = "https://maoyan.com" + m_item.find_elements_by_xpath(
    # #     ".//div[@class='movie-item']/a/@href").extract_first()
    # print(movie_name[key].text)
    # print(movie_item)

    # https: // maoyan.com / films / 1228788


    # browser.execute_script("arguments[0].click();", movie_name)
    # col = browser.find_elements_by_xpath("//div[@class='mod-content']/span")
    # print(col)
