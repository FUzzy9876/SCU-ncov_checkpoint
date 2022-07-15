# 如何安装？

### 1. 克隆本项目到本地
```shell
git clone https://github.com/somenothing/SCU-ncov_checkpoint.git
 ```
### 2. 配置环境
* Python >= 3.10
    * configparser 库
    * selenium 库
    * pymysql 库
* Chrome (推荐) / 其他浏览器 及 对应的 driver
* MySQL 数据库

    结构：
    |id|username|password|statue|wechat (可选)|
    |-|-|-|-|-|
    |a.i.|学号|密码|非0值|微信通知的用户名|

### 3. 运行
```shell
python run.py
```