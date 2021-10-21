import time

from scripts import config
from scripts import mysql
from scripts.main import begin
from scripts import message


def ncov():
    database = config.read_config('Database')
    match database:
        case -1:
            return 0.1
        case 1:
            return 0.2
        case _:
            data = mysql.connect_db(database)
    match data:
        case -1:
            return 1.1
        case 1:
            return 1.2
        case _:
            pass
    keys = tuple(config.read_config('BaiduOCR').values())
    for value in data:
        result = begin(value, keys)
        if result == 0:
            text = '%s今日健康打卡已完成！' % value['username']
        else:
            text = '注意：今日健康打卡未成功，程序会在12点前再次运行确保完成打卡，请实时关注！\n错误信息：\n' + str(result)
        message.send_message(text, value['wechat'])


if __name__ == '__main__':
    r = ncov()
    print(r)
    print('程序正常退出')
