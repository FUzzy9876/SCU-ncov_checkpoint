import time
from configparser import ConfigParser

head = 'time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())'


def read_config(section: str):
    """读取配置文件"""
    cfg = ConfigParser()
    try:
        cfg.read('config.ini')
    except Exception as error:
        print('[%s] (config) [!ERROR!] 未找到配置文件!\n建议：重新按照文档配置环境。\n' % head, error)
        return -1
    try:
        result = cfg[section]
    except Exception as error:
        print('[%s] (config) [!ERROR!] 配置文件读取失败!\n建议：恢复配置文件默认值。\n' % head, error)
        return 1
    return result


def write_config(section: str, item: str, value):
    cfg = ConfigParser()
    try:
        cfg.read('config.ini')
    except Exception as error:
        print('[%s] (config) [!ERROR!] 未找到配置文件!\n建议：重新按照文档配置环境。\n' % head, error)
        return -1
    cfg[section][item] = value
    with open('config.ini', 'w', encoding='utf-8') as file:
        cfg.write(file)  # 数据写入配置文件
