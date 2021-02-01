SCU-ncov_checkpoint
====
四川大学微服务健康每日报 自动打卡
----

## 更新日志：
### 最近更新：2021年2月1日
* 添加服务器版本，现在可以在服务器上创建计划任务实现自动打卡。
* 修复部分bug。

### 2021年1月30日
* 打包项目为.exe文件，无需python环境运行，但仍需下载对应版本的chromedriver放于tools文件夹。
* 新增功能：批量打卡 <br> 可以将多个账号密码储存在本地，运行run.exe文件批量打卡。

# 免责声明：
## 本项目仅供学习交流使用，请勿用于其他用途！
## 根据《教育部公安厅关于进一步做好新型冠状病毒感染的肺炎疫情“日报告、零报告”工作的通知》、《中华人民共和国传染病防疫法》、《中华人民共和国治安管理处罚法》等，请需要打卡的同学于每天中午12:00前通过“健康每日报”功能进行每日健康打卡，在填写过程中确认真实无误，若有任何问题，请及时与辅导员联系！

# 隐私声明：
## 您输入的所有数据（包括但不限于学号、密码、地理位置信息）均储存在您的计算机上，仅用于微服务身份认证，不会以任何形式泄露！

# 本项目可实现：
* 使用账号密码自动登录
  * 无需提供cookies，无需担心cookies失效问题
  * 可实现批量打卡
* 继承上次打卡数据，自动填报
  * 无需获取post表单中uid、id等信息
* 根据提供的经纬度信息虚拟获取位置
  * 解决部分设备或浏览器无定位功能的问题

# 使用方法：
## 以应用程序运行：
确保有chrome浏览器，并[在此](http://npm.taobao.org/mirrors/chromedriver/)下载对应版本的chromedriver <br>
将chromedriver.exe放入tools目录 <br>
运行run.exe文件，首次运行请先添加用户

## 以python文件运行：
确保有chrome浏览器，并[在此](http://npm.taobao.org/mirrors/chromedriver/)下载对应版本的chromedriver <br>
将chromedriver.exe放入tools目录 <br>
更改ncov.py中学号、密码、纬度、经度信息
```
python ncov.py
```

## 在服务器上运行：
#### 环境
python3.8+ [教程](https://www.cnblogs.com/somenothing/p/14355971.html) <br>
chrome & chromedriver [教程](https://www.cnblogs.com/somenothing/p/14356004.html) <br>
selenium库 [教程](https://www.cnblogs.com/somenothing/p/14356017.html) <br>
#### 运行
下载for Linux目录中的ncov.py
运行

# 开发 & 更新：
author: Aaron <br>
e-mail: w98987@126.com <br>
wechat official account: 化院学生从不学化学 <br>
使用python - selenium开发 <br>
持续更新，可通过邮箱或微信公众号后台反馈问题、提出建议、催更 <br>
#### 请留下star，谢谢！
