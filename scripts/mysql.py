import time
import pymysql

head = 'time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())'


def connect_db(db_conf):
    host, user, password, database = tuple(db_conf.values())
    try:
        db = pymysql.connect(host=host, user=user, password=password, database=database)
    except Exception as error:
        print('[%s] (database) [!ERROR!] 数据库连接失败!\n建议：请检查账号密码和数据库名称是否正确，再重试。\n' % head, error)
        return -1
    cursor = db.cursor()
    sql = 'SELECT * FROM `ncov`'
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except Exception as error:
        print('[%s] (database) [!ERROR!] 数据库连接失败!\n建议：请检查数据库，再重试。\n' % head, error)
        return 1
    data = []
    num = 0
    for row in results:
        if row[3] == 0:
            continue
        num += 1
        data.append({'id': num, 'username': row[1], 'password': row[2], 'statue': row[3], 'wechat': row[4]})
    print('[%s] (database) 数据库连接成功!' % head)
    return data
