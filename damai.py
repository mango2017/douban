from selenium import webdriver
import os
import time
import json
# wd = webdriver.Chrome()
# wd.get("https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F")
# wd.switch_to.frame("alibaba-login-box")  #进入iframe
# wd.find_element_by_id("fm-login-id").send_keys("15002449401")
# wd.find_element_by_id("fm-login-password").send_keys("qq13889303016")


def browser_initial():
    """"
    进行浏览器初始化
    """
    global  browser
    os.chdir('E:\\pythonwork')
    browser = webdriver.Chrome()
    log_url = 'https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F'
    return log_url, browser


def get_cookies(log_url, browser):
    """
    获取cookies保存至本地
    """
    browser.get(log_url)
    time.sleep(15)  # 进行扫码
    dictCookies = browser.get_cookies()  # 获取list的cookies
    print(dictCookies)
    jsonCookies = json.dumps(dictCookies)  # 转换成字符串保存

    with open('damai_cookies.txt', 'w') as f:
        f.write(jsonCookies)
    print('cookies保存成功！')
    # 保存成功之后，访问 网页
    browser  = get_browser()
    # log_damai(browser)

def get_browser():
    """"
        浏览器初始化,并打开大麦网购票界面（未登录状态）
        """
    os.chdir('E:\\pythonwork')
    # browser = webdriver.Chrome()
    browser.get(
        'https://detail.damai.cn/item.htm?spm=a2oeg.search_category.0.0.8778f91as7xLdc&id=610870234751&clicktitle=2020%E5%BC%A0%E6%9D%B0%E3%80%8C%E6%9C%AA%C2%B7LIVE%E3%80%8D%E5%B7%A1%E5%9B%9E%E6%BC%94%E5%94%B1%E4%BC%9A%20%E5%90%88%E8%82%A5%E7%AB%99')
    # return browser


def log_damai(browser):
    """
    从本地读取cookies并刷新页面,成为已登录状态
    """
    with open('damai_cookies.txt', 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())

    # 往browser里添加cookies
    for cookie in listCookies:
        cookie_dict = {
            'domain': '.damai.cn',
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            "expires": '',
            'path': '/',
            'httpOnly': False,
            'HostOnly': False,
            'Secure': False
        }
        browser.add_cookie(cookie_dict)
    browser.refresh()  # 刷新网页,cookies才成功


if __name__ == "__main__":
    tur = browser_initial()
    get_cookies(tur[0], tur[1])