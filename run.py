# -*- coding: UTF-8 -*-

"""
author: somenothing
e-mail: admin@somenothing.top
"""

import pymysql

from scripts.main import Check


latitude = 30.564365  # 纬度
longitude = 104.007195  # 经度

path = '.\chromedriver\chromedriver.exe'


db = pymysql.connect(host="localhost",user="",password="",database="")
cursor = db.cursor()

sql = "SELECT * FROM user"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
except:
    print ("Error: unable to fetch data")
print('success to fetch data')
for row in results:
    username = row[2]  # 学号对应
    password = row[3]  # 密码对应位置
    statue = row[4]  # 等待后续更新
    x = Check(user=username, passwd=password, lat=latitude, long=longitude, path=path)
    x.main()


db.close()

'''
开发备用
username = ''  # 用户名（学号）
password = ''  # 密码
'''