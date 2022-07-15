# -*- coding: UTF-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from . import verification as ver


def screenshot(browser):
    width = browser.execute_script("return document.documentElement.scrollWidth")
    height = browser.execute_script("return document.documentElement.scrollHeight")
    print(width,height)
    browser.set_window_size(width, height)
    time.sleep(0.5)
    browser.save_screenshot('pic.png')


class Check:
    def __init__(self, user, passwd, path='', lat=30.564365, long=104.007195):
        self.target = 'https://wfw.scu.edu.cn/ncov/wap/default/index'  # 微服务地址
        self.username = str(user)  # 用户名
        self.password = str(passwd)  # 密码
        self.lat = lat  # 纬度
        self.long = long  # 经度
        self.path = path

    def main(self, api, secret):
        head = '(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), self.username)'
        print('[%s] (%s) preparing...' % eval(head))
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        browser = webdriver.Chrome(executable_path="/usr/bin/chromedriver", chrome_options=chrome_options)
        print('[%s] (%s) starting...' % eval(head))
        statue = 0
        while True:  # 获取验证码登录
            browser.delete_all_cookies()  # 清空cookie
            browser.get(self.target)
            try:  # 切换为账号密码登录
                browser.switch_to.frame('loginIframe')  # 切换frame
                switch_element = WebDriverWait(browser, 10).until(
                    ec.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div/div[3]'))
                )
                switch_element.click()
            except Exception as error:
                print('[%s] (%s) [!ERROR!] Network wrong: \n' % eval(head), error)
                return -1  # 异常启动
            input_elements = browser.find_elements_by_tag_name('input')
            username_element, password_element, verification_element = input_elements
            username_element.send_keys(self.username)  # 填用户名
            password_element.send_keys(self.password)  # 填密码
            time.sleep(0.5)
            browser.find_element_by_class_name('van-field__button').screenshot('captcha.png')
            verification = ver.main('captcha.png', api, secret)
            print('[%s] (%s) verification code: ' % eval(head) + verification, end=' --- ')
            verification_element.send_keys(verification)
            browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[3]/button').click()  # 点击登录
            time.sleep(0.5)  # 等待跳转
            statue += 1
            if browser.current_url == self.target:
                print('correct')
                break
            print('wrong')
            if statue == 50:
                print('[%s] (%s) 请检查账号密码，或稍后再试！' % eval(head))
                browser.quit()
                return 1  # 超时返回值
            time.sleep(3)
        
        # 2022-05-15修复，解决弹窗问题
        WebDriverWait(browser, 5).until(
            ec.presence_of_element_located((By.CLASS_NAME, 'wapat-btn.wapat-btn-ok'))
        )
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, '.wapat-btn.wapat-btn-ok').click()  # 点击对话框
        

        browser.execute_cdp_cmd(
            "Browser.grantPermissions",  # 授权地理位置信息
            {
                "origin": "https://wfw.scu.edu.cn/",
                "permissions": ["geolocation"]
            },
        )
        browser.execute_cdp_cmd(
            "Emulation.setGeolocationOverride",  # 虚拟位置
            {
                "latitude": self.lat,
                "longitude": self.long,
                "accuracy": 50,
            },
        )
        try:  # 提交位置信息
            area_element = WebDriverWait(browser, 10).until(
                ec.element_to_be_clickable((By.NAME, 'area'))
            )
            area_element.click()
        except Exception as error:
            print('[%s] (%s) [!ERROR!] Get location wrong: \n' % eval(head), error)
            return 2  # 位置错误返回
        time.sleep(1)  # 等待位置信息
        # screenshot(browser)
        browser.find_element(By.CSS_SELECTOR, 'div.footers > a').click()  # 提交信息
        time.sleep(0.5)
        # screenshot(browser)
        try:
            ok_element = WebDriverWait(browser, 3).until(
                ec.element_to_be_clickable((By.CLASS_NAME, 'wapcf-btn.wapcf-btn-ok'))  # 提交按钮
            )
            ok_element.click()
            WebDriverWait(browser, 3).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div[1]'))  # 成功对话框标题
            )
            title_success = browser.find_element_by_xpath('/html/body/div[5]/div/div[1]').get_attribute("innerHTML")
            print('[%s] (%s) Success!' % eval(head))
            print('[%s] (%s) From website: ' % eval(head), title_success)
            browser.quit()
            return 0  # 正确返回
        except Exception:
            info = browser.find_element_by_class_name('wapat-title').get_attribute('innerHTML')
            print('[%s] (%s) From website: ' % eval(head), info)
            browser.quit()
            return info  # 不明信息返回


def begin(value, keys):
    x = Check(user=value['username'], passwd=value['password'])
    r = x.main(keys[0], keys[1])
    return r
