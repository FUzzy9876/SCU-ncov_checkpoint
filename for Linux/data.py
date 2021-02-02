import pymysql


def get_data():
    host = 'localhost'  # 数据库地址，如果为本地ip则无需更改
    user = 'root'  # 数据库用户名
    passwd = 'Wmz20020703!'  # 数据库密码
    name = 'python'  # 数据库名称
    try:  # 连接数据库
        db = pymysql.connect(host=host, user=user, passwd=passwd, db=name, charset='utf8')
    except Exception as error:
        print('Failed to connect to database!\n', error)
        return None
    cursor = db.cursor()
    sql = "SELECT * FROM ncov"  # 读取数据表
    cursor.execute(sql)
    results = cursor.fetchall()
    all_data = []
    for row in results:
        number = row[0]
        username = row[1]
        password = row[2]
        p = '*' * len(password)
        latitude = row[3]
        longitude = row[4]
        print('get data: %s - username: %s ,password: %s ,lat: %s ,long: %s '
              % (number, username, p, latitude, longitude))
        all_data.append(row)
    db.close()
    return all_data
