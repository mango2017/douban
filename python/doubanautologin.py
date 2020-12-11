from selenium import webdriver

import time

#这种登录方式就是 先在浏览器登录 然后拿到cookie 手动赋值进行携带登录
driver = webdriver.Chrome()
driver.get("https://www.douban.com/") #豆瓣

cookie_1 = {"name":"bid","value":"joEr7Pec4GI"}
cookie_2 = {"name":"douban-fav-remind","value":"1"}
cookie_3 = {"name":"__yadk_uid","value":"ZDwchmY5uU9wgxhcb76IqPjwbgSsBwhq"}
cookie_4 = {"name":"__gads","value":"ID=7c68d90099c55b9b-2279e050c4c400fd:T=1605503840:RT=1605503840:S=ALNI_MbHIz1wmfZZ9KWfHZHOnWbbP5UW6A"}
cookie_5 = {"name":"viewed","value":"30147778"}
cookie_6 = {"name":"gr_user_id","value":"e8058689-163b-4678-8c9d-d8c5ca7b17c1"}
cookie_7 = {"name":"_vwo_uuid_v2","value":"DB487462ECB43D637F1A032797FB0CCE9|5d005848148ba556f266a651b0303aa6"}
cookie_8 = {"name":"ll","value":"118123"}
cookie_9 = {"name":"__utmc","value":"30149280"}
cookie_10 = {"name":"_pk_ref.100001.8cb4","value":"%5B%22%22%2C%22%22%2C1607664001%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DX4Zy9_ahj7t1b1pWbEgFP0-TqK3PK0Kh0MADWXe0Q7P4URxTeI7BBaF7HnoLiYXy%26wd%3D%26eqid%3D949737c600084662000000035fd3017c%22%5D"}
cookie_11 = {"name":"_pk_ses.100001.8cb4","value":"*"}
cookie_12 = {"name":"__utma","value":"30149280.992248413.1591583651.1607654482.1607664003.16"}
cookie_13 = {"name":"__utmz","value":"30149280.1607664003.16.11.utmcsr=baidu|utmccn=(organic)|utmcmd=organic"}
cookie_14 = {"name":"__utmt","value":"1"}
cookie_15 = {"name":"dbcl2","value":"187832993:Xg2QoPhMzks"}
cookie_16 = {"name":"ck","value":"ctHS"}
cookie_17 = {"name":"_pk_id.100001.8cb4","value":"654a3dd1dfa4a05f.1591583650.12.1607664094.1607654482."}
cookie_18 = {"name":"ap_v","value":"0,6.0"}
cookie_19 = {"name":"push_noty_num","value":"0"}
cookie_20 = {"name":"push_doumail_num","value":"0"}
cookie_21 = {"name":"__utmv","value":"30149280.18783"}
cookie_22 = {"name":"__utmb","value":"30149280.5.10.1607664003"}


time.sleep(1)
driver.add_cookie(cookie_1)
driver.add_cookie(cookie_2)
driver.add_cookie(cookie_3)
driver.add_cookie(cookie_4)
driver.add_cookie(cookie_5)
driver.add_cookie(cookie_6)
driver.add_cookie(cookie_7)
driver.add_cookie(cookie_8)
driver.add_cookie(cookie_9)
driver.add_cookie(cookie_10)
driver.add_cookie(cookie_11)
driver.add_cookie(cookie_12)
driver.add_cookie(cookie_13)
driver.add_cookie(cookie_14)
driver.add_cookie(cookie_15)
driver.add_cookie(cookie_16)
driver.add_cookie(cookie_17)
driver.add_cookie(cookie_18)
driver.add_cookie(cookie_19)
driver.add_cookie(cookie_20)
driver.add_cookie(cookie_21)
driver.add_cookie(cookie_22)

driver.get("https://www.douban.com/")


# 点击文本
floderurls  = driver.find_elements_by_xpath("//div[@class='mod']/ul/li[@class='rec_topics'][1]/a")
floderurls[0].click()
time.sleep(2)
driver.close()