import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Clock:
    def __init__(self, u, p, a, o):
        self.target = 'https://wfw.scu.edu.cn/ncov/wap/default/index'  # 微服务地址
        self.username = str(u)
        self.password = str(p)
        self.lat = int(a)
        self.long = int(o)

    def main(self):
        print('preparing...')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)
        print('working on %s...' % self.username)
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
            browser.quit()
            return 'fail'
        input_element = browser.find_elements_by_tag_name('input')
        username_element, password_element = input_element[0], input_element[1]
        username_element.send_keys(self.username)  # 填用户名
        password_element.send_keys(self.password)  # 填密码
        browser.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[3]/button').click()  # 点击登录
        time.sleep(1)  # 等待跳转
        if browser.current_url != 'https://wfw.scu.edu.cn/ncov/wap/default/index':  # 检测登录是否成功
            browser.quit()
            print('\n', self.username, ': wrong username or password!')
            return 'fail'
        browser.execute_cdp_cmd(
            "Browser.grantPermissions",
            {
                "origin": "https://wfw.scu.edu.cn/",
                "permissions": ["geolocation"]
            },
        )
        browser.execute_cdp_cmd(
            "Emulation.setGeolocationOverride",
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
            browser.quit()
            return 'fail'
        time.sleep(2)  # 等待位置信息
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
        except Exception as error:
            info = browser.find_element_by_class_name('wapat-title').get_attribute('innerHTML')
            print(self.username, ':', info)
            browser.quit()
            return 'already'
        browser.quit()
        return 'success'
