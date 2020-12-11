# =============================================
# -*- coding: utf-8 -*-
# @Time    : 2020-02-06
# @Author  : KeyboArd
# @Blog    : www.wrpzkb.cn
# @FileName: bilibili_login.py
# @Software: PyCharm
# =============================================
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import random
from PIL import Image
USER_AGENT_LIST = [
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
        "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10",
        "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
        "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
        "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
        "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
        "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
        "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
        "Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00",
        "Opera/12.0(Windows NT 5.1;U;en)Presto/22.9.168 Version/12.00",
        "Mozilla/5.0 (Windows NT 5.1) Gecko/20100101 Firefox/14.0 Opera/12.0",
        "Opera/9.80 (Windows NT 6.1; WOW64; U; pt) Presto/2.10.229 Version/11.62",
        "Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.10.229 Version/11.62",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; de) Presto/2.9.168 Version/11.52",
        "Opera/9.80 (Windows NT 5.1; U; en) Presto/2.9.168 Version/11.51",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; de) Opera 11.51",
        "Opera/9.80 (X11; Linux x86_64; U; fr) Presto/2.9.168 Version/11.50",
        "Opera/9.80 (X11; Linux i686; U; hu) Presto/2.9.168 Version/11.50",
    ]

class bilibili_code():
    def init(self):
        """
        初始化变量
        :return:
        """
        global url, browser, username, password, wait

        url = 'https://passport.bilibili.com/login'

        path = r'G:\Python3\Scripts\chromedriver.exe'
        chrome_options = Options()
        user_agent = random.choice(USER_AGENT_LIST)
        #全屏
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('user-agent=%s'%user_agent)
       # chrome_options.add_argument(user_agent)
        chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors","enable-automation"])
        browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)

        username = '用户名'

        password = '密码'
        wait = WebDriverWait(browser, 20)

    def login(self):
        """
        输入帐号密码登录
        :return:
        """
        browser.get(url)

        user = wait.until(EC.presence_of_element_located((By.ID,'login-username')))

        passwd = wait.until(EC.presence_of_element_located((By.ID,'login-passwd')))

        user.send_keys(username)
        passwd.send_keys(password)

        login_btn = wait.until(EC.presence_of_element_located((By.XPATH,"//a[contains(@class,'btn-login')]")))
        ran_time = random.random() * 2
        print("随机睡眠时间: ",ran_time)
        time.sleep(ran_time)

        login_btn.click()


    def find_code(self):
        """
        查找 验证码图片
        :return:
        """
        #带有缺口的图片
        code_bg = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'canvas.geetest_canvas_bg.geetest_absolute'))
        )
        #需要滑动的图片
        code_slice = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'canvas.geetest_canvas_slice.geetest_absolute'))
        )
        #完整的图片
        code_fullbg = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'canvas.geetest_canvas_fullbg.geetest_fade.geetest_absolute'))
        )
        #隐藏验证码
        self.hide_element(code_slice)

        #保存带有缺口的验证码图片
        self.save_screenshot(code_bg,'bg')

        #显示需要滑动的验证码图片
        self.show_element(code_slice)

        #保存需要滑动的验证码图片
        self.save_screenshot(code_slice,"slice")

        #显示完整验证码图片
        self.show_element(code_fullbg)

        #保存完整验证码图片
        self.save_screenshot(code_fullbg,"full")


    def hide_element(self,element):
        """
        隐藏属性
        :return:
        """
        browser.execute_script("arguments[0].style=arguments[1]",element,"display:none;")

    def show_element(self,element):
        """
        显示属性
        :return:
        """
        browser.execute_script("arguments[0].style=arguments[1]",element,"display:block;")

    def save_screenshot(self,obj,name):
        """
        网页截图，获取验证码图片
        :param name:图片名字
        :return:截图对象
        """
        #obj 需要 截图的 位置  name 文件名称
        try:
            #save_screenshot 对整个网页进行截图
            pic_url = browser.save_screenshot('./bilibili.png')
            print("%s截图成功"%pic_url)
            left,top,right,bottom = obj.location['x'],obj.location['y'],obj.location['x'] + obj.size['width'],obj.location['y'] + obj.size['height']
            print('图：' + name)
            print('Left %s' % left)
            print('Top %s' % top)
            print('Right %s' % right)
            print('Bottom %s' % bottom)
            print('')
            # 在整个页面截图的基础上，根据位置信息，分别剪裁出三张验证码图片并保存
            im = Image.open('./bilibili.png')
            im = im.crop((left, top, right, bottom)) #对浏览器截图进行裁剪
            file_name = 'bili_' + name + '.png'
            im.save(file_name)
        except BaseException as msg:
            print("%s:截图失败"%msg)

    def slide(self):
        """
        :return:
        """
        distance = self.get_distance(Image.open('./bili_back.png'),Image.open('./bili_full.png'))
        print('计算偏移量：%s Px'% distance)
        trace = self.get_trace(distance - 5)
        self.move_to_gap(trace)
        time.sleep(3)

    def get_distance(self,bg_image,fullbg_image):
        """
        获取缺口偏移量
        :param bg_image:带缺口图片
        :param fullbg_image:不带缺口图片
        :return:
        """
        distance = 60
        for i in range(distance,fullbg_image.size[0]):
            for j in range(fullbg_image.size[1]):
                if not self.is_pixel_equal(fullbg_image,bg_image,i,j):
                    distance = i
                    return distance
        return distance

    def is_pixel_equal(self,bg_image,fullbg_image,x,y):
        """
        判断两个像素是否相同
        :param bg_image:带缺口图片
        :param fullbg_image:不带缺口图片
        :param x:位置x
        :param y:位置y
        :return:像素是否相同
        """
        #获得两章图片对应像素点的RGB数据
        bg_pixel = bg_image.load()[x,y]
        fullbg_pixel = fullbg_image.load()[x,y]
        #设定一个阈值，像素也许存在误差， 60作为容差范围
        threshold = 60
        #比较两张图 RGB 的 绝对值是否小于定义的阈值
        for i in range(0,3):
            if (abs(bg_pixel[i] - fullbg_pixel[i]<threshold)):
                return True
        # if (abs(bg_pixel[0] - fullbg_pixel[0] < threshold)and abs(bg_pixel[1] - fullbg_pixel[1] <threshold) and abs(bg_pixel[2] - fullbg_pixel[2] <threshold)):
            #return True
        return False

    #模拟人工拉动滑块
    def get_trace(self,distance):
        """
        根据偏移量获取移动轨迹
        :param distance:偏移量
        :return:滑动轨迹
        """
        trace = []
        # 设置加速距离为总距离的 4 /5
        mid = distance * (4 / 5)
        #设置当前位移， 初始速度、时间间隔
        current,v0 ,t = 0,0,0.1

        while current< distance:
            if current< mid:
                #加速度为正10
                a =10
            else:
                #减速度为负10
                a = -10
            #运用物理加速度位移相关公式  X=v0 * t+ 1/2 * a * t*t
            #a 加速度 X 位移 v0 初速度
            X = v0 * t +1/2 * a * t * t
            #当前时刻的速度
            v = v0 + a * t
            v0 =v
            current +=X
            #记录每个时间间隔移动的多少位移
            trace.append(round(X))
        return trace

    def move_to_gap(self,trace):
        """
        拖动滑块到缺口处
        :param trace:轨迹
        :return:
        """
        slider = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.geetest_slider_button')))
        ActionChains(browser).click_and_hold(slider).perform()

        for x in trace:
            ActionChains(browser).move_by_offset(xoffset=x,yoffset=0).perform()

        time.sleep(0.5)

        ActionChains(browser).release().perform()

    def crack(self):
        self.init()
        self.login()
        self.find_code()
        self.slide()

        success = browser.current_url
        if success == "https://www.bilibili.com/":
            print("登录成功")
            browser.close()
        else:
            self.crack()



if __name__ == '__main__':
    bi = bilibili_code()
    bi.crack()
