SCU-ncov_checkpoint
====


# 免责声明：
## 本项目仅供学习交流使用，请勿用于其他用途！
## 根据《教育部公安厅关于进一步做好新型冠状病毒感染的肺炎疫情“日报告、零报告”工作的通知》、《中华人民共和国传染病防疫法》、《中华人民共和国治安管理处罚法》等，请需要打卡的同学于每天中午12:00前通过“健康每日报”功能进行每日健康打卡，在填写过程中确认真实无误，若有任何问题，请及时与辅导员联系！

# 本项目可实现：
* 使用账号密码自动登录
  * 无需提供cookies，无需担心cookies失效问题
  * 可实现批量打卡（开发中）
* 继承上次打卡数据，自动填报
  * 无需获取post表单中uid、id等信息
* 根据提供的经纬度信息虚拟获取位置
  * 解决部分设备或浏览器无定位功能的问题

# 使用方法：
确保有chrome浏览器，并[在此](http://npm.taobao.org/mirrors/chromedriver/)下载对应版本的chromedriver <br>
将chromedriver.exe放入tools目录 <br>
更改ncov.py中学号、密码、纬度、经度信息
```
python ncov.py
```

# 开发 & 更新：
author: Aaron <br>
e-mail: w98987@126.com <br>
wechat official account: 化院学生从不学化学 <br>
使用python - selenium开发 <br>
持续更新，可通过邮箱或微信公众号后台反馈问题、提出建议、催更 <br>
#### 请留下star，谢谢！
