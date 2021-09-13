# -*- coding: UTF-8 -*-
import sys
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import scripts.verification as ver


class Check:
    def __init__(self, user, passwd, path, lat=30.564365, long=104.007195):
        self.target = 'https://wfw.scu.edu.cn/ncov/wap/default/index'  # 微服务地址
        self.username = str(user)  # 用户名
        self.password = str(passwd)  # 密码
        self.lat = lat  # 纬度
        self.long = long  # 经度
        self.path = path

    def main(self):
        print('\npreparing...')
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(self.path, options=chrome_options)
        print('starting...')
        statue = 0
        while True:
            browser.delete_all_cookies()  # 清空cookie
            browser.get(self.target)
            try:  # 切换为账号密码登录
                browser.switch_to.frame('loginIframe')  # 切换frame
                switch_element = WebDriverWait(browser, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div/div[3]'))
                )
                switch_element.click()
            except Exception as error:
                print('network wrong...\n', error)
            input_elements = browser.find_elements_by_tag_name('input')
            username_element, password_element, verification_element = input_elements
            username_element.send_keys(self.username)  # 填用户名
            password_element.send_keys(self.password)  # 填密码
            time.sleep(0.5)
            browser.find_element_by_class_name('van-field__button').screenshot('captcha.png')
            verification = ver.main('captcha.png')
            print('verification code:' + verification)
            verification_element.send_keys(verification)
            browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[3]/button').click()  # 点击登录
            time.sleep(1)  # 等待跳转
            statue += 1
            if browser.current_url == self.target:
                break
            print('verification code / username / password wrong!')
            if statue == 3:
                print('请检查账号密码，或稍后再试！')
                browser.quit()
                sys.exit()
            time.sleep(5)

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
                EC.element_to_be_clickable((By.NAME, 'area'))
            )
            area_element.click()
        except Exception as error:
            print('get location wrong...\n', error)
        time.sleep(1)  # 等待位置信息
        browser.find_element_by_xpath('/html/body/div[1]/div/div/section/div[5]/div/a').click()  # 提交信息
        try:
            ok_element = WebDriverWait(browser, 3).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[2]/div[2]'))  # 提交按钮
            )
            ok_element.click()
            print(self.username, 'success!')
            WebDriverWait(browser, 3).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div[1]'))  # 成功对话框标题
            )
            title_success = browser.find_element_by_xpath('/html/body/div[5]/div/div[1]').get_attribute("innerHTML")
            print('From website:', title_success)
        except:
            info = browser.find_element_by_class_name('wapat-title').get_attribute('innerHTML')
            print('From website |', self.username, ':', info)
        browser.quit()


if __name__ == '__main__':
    x = Check()
    x.main()
