import time
import json
import requests
from scripts.config import read_config, write_config

head = 'time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())'


def get_token(force=0):
    token_conf = read_config('Wechat')
    corpid, corpsecret = token_conf['corpid'], token_conf['Secret']
    if force == 0 and token_conf['token'] != '123456' and int(time.time()) + 300 < int(token_conf['valid_time']):
        token = token_conf['token']
        print('[%s] (Wechat) 已从本地缓存中读取token!' % eval(head))
    else:
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (corpid, corpsecret)
        token_result = requests.get(url).json()
        if token_result['errcode'] != 0:
            print('[%s] (Wechat) [Warning] 无法获取最新的token，可能导致微信消息推送失败!\n建议：检查企业微信各项参数是否正确。\n'
                  % eval(head), token_result['errcode'], ' | ', token_result['errmsg'])
            return 0
        token = token_result['access_token']
        valid_time = int(time.time()) + int(token_result['expires_in'])
        try:
            write_config('Wechat', 'token', str(token))
            write_config('Wechat', 'valid_time', str(valid_time))
            print('[%s] (Wechat) 已重新获取token并成功写入本地缓存!' % eval(head))
        except Exception as error:
            print('[%s] (Wechat) [Warning] 无法将token写入缓存文件\n建议：检查配置文件是否正确。\n' % eval(head), error)
    return token


def send_message(text: str, user: str, token=get_token()):
    if token == 0:
        print('[%s] (Wechat) [!ERROR!] token获取失败!\n建议：检查企业微信各项参数是否正确，或稍后再试。' % eval(head))
        return 1
    url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % token
    data = {
        'touser': user,
        'msgtype': 'text',
        'agentid': 1000002,
        'text': {
            'content': text
        },
        'safe': 0,
        'enable_id_trans': 0,
        'enable_duplicate_check': 0,
        'duplicate_check_interval': 1800
    }
    try:
        message_result = requests.post(url, json.dumps(data)).json()
        if message_result['errcode'] != 0:
            print('[%s] (Wechat) [!ERROR!] 微信消息推送失败!\n建议：检查企业微信各项参数是否正确。\n' % eval(head),
                  message_result['errcode'], ' | ', message_result['errmsg'])
            return 2
        print('[%s] (Wechat) 已成功发送微信消息!' % eval(head))
    except Exception as error:
        print('[%s] (Wechat) [!ERROR!] 微信消息推送失败!\n建议：检查企业微信各项参数是否正确，网络连接是否正常。\n' % eval(head), error)
        return -1
    return 0
