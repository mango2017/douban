from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get("https://www.damai.cn/") #大麦网

cookie_1 = {"name":"cna","value":"5D1OGNFK+3cCAa+g0gfViClH"}
cookie_2 = {"name":"t","value":"e4d3b369962d1ffe45a1d847f0c9c0b7"}
cookie_3 = {"name":"damai.cn_nickName","value":"%E9%BA%A6%E5%AD%906vnJS"}
cookie_4 = {"name":"munb","value":"3954636087"}
cookie_5 = {"name":"UM_distinctid","value":"17646331b3c6ac-09d935b745f781-c791039-384000-17646331b3d8de"}
cookie_6 = {"name":"cn_7415364c9dab5n09ff68_dplus","value":"%7B%22distinct_id%22%3A%20%2217646331b3c6ac-09d935b745f781-c791039-384000-17646331b3d8de%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201607495525%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201607495525%2C%22initial_view_time%22%3A%20%221607493812%22%2C%22initial_referrer%22%3A%20%22https%3A%2F%2Fpassport.damai.cn%2Flogin%3Fru%3Dhttps%3A%2F%2Fpassport.damai.cn%2Faccountinfo%2Fmyinfo%22%2C%22initial_referrer_domain%22%3A%20%22passport.damai.cn%22%7D"}
cookie_7 = {"name":"XSRF-TOKEN","value":"d6578be8-967c-47e5-b7f4-123e33a055e8"}
cookie_8 = {"name":"xlly_s","value":"1"}
cookie_9 = {"name":"_samesite_flag_","value":"true"}
cookie_10 = {"name":"cookie2","value":"1d8a024ac07b670103c3865226320531"}
cookie_11 = {"name":"_tb_token_","value":"e7e568405b45e"}
cookie_12 = {"name":"_hvn_login","value":"18"}
cookie_13 = {"name":"csg","value":"3a5f986a"}
cookie_14 = {"name":"damai.cn_user","value":"wtpZsxcJTvQ4elIrU51+u6UMawUSEIor5jnEmRqj9RCWa2KECZIHVYfV8dx2IUOEGxb2+Rjuqig="}
cookie_15 = {"name":"damai.cn_user_new","value":"wtpZsxcJTvQ4elIrU51%2Bu6UMawUSEIor5jnEmRqj9RCWa2KECZIHVYfV8dx2IUOEGxb2%2BRjuqig%3D"}
cookie_16 = {"name":"h5token","value":"759c57feca30424ca8adc128641dd506_1_1"}
cookie_17 = {"name":"damai_cn_user","value":"wtpZsxcJTvQ4elIrU51%2Bu6UMawUSEIor5jnEmRqj9RCWa2KECZIHVYfV8dx2IUOEGxb2%2BRjuqig%3D"}
cookie_18 = {"name":"loginkey","value":"759c57feca30424ca8adc128641dd506_1_1"}
cookie_19 = {"name":"user_id","value":"103185543"}
cookie_20 = {"name":"_m_h5_tk","value":"0920ad08b6393e1b56003b64b3b6651c_1607666771599"}
cookie_21 = {"name":"_m_h5_tk_enc","value":"34b0f2bf93ce295c5b176f5eb181c7a7"}
cookie_22 = {"name":"x_hm_tuid","value":"kZe7lLhL7IFlhMu376A9ZnIULXYY6/kIR4tM8TF3c5EO2xky2aRO93Os2F3iuB/Z"}
cookie_23 = {"name":"tfstk","value":"ca1ABwOHMuq0FmTR8teoCa0cTG4hZPav4qTx6yJ-1TfSHIGOikfh95IQhnovwzC.."}
cookie_24 = {"name":"l","value":"eBMVrWHHO6PFQMKtBOfZlurza77TJIRAguPzaNbMiOCP9U5p5uP1WZJqr0Y9CnGVhstBR3uKcXmBBeYBqoxHavVy51xKbYkmn"}
cookie_25 = {"name":"isg","value":"BIqKY-994RYBEG3BuC2fWfMv23Asew7VQeJucxTDD11oxyuB_gsA5RT11zMbN4Zt"}





time.sleep(5)
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
driver.add_cookie(cookie_23)
driver.add_cookie(cookie_24)
driver.add_cookie(cookie_25)
driver.get("https://www.damai.cn/")
