# -*- coding: UTF-8 -*-

"""
author: somenothing
e-mail: w98987@126.com
"""

from scripts.main import Check

username = ''  # 用户名（学号）
password = ''  # 密码
latitude = 30.564365  # 纬度
longitude = 104.007195  # 经度

path = '.\chromedriver\chromedriver.exe'

x = Check(user=username, passwd=password, lat=latitude, long=longitude, path=path)
x.main()