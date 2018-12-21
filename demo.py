# -*- coding:utf8 -*-
from __future__ import unicode_literals
import requests
import itchat
import time
import datetime

def get_news():
    url = "http://open.iciba.com/dsapi"
    r = requests.get(url)
    contents = r.json()['content']
    note = r.json()['note']
    translation = r.json()['translation']
    return contents, note, translation

def send_news():
    friend_name = u'TN'
    your_name = u'最爱你的人'
    test = True
    try:
        # 登陆你的微信账号，会弹出网页二维码，扫描即可
        itchat.auto_login(hotReload=True)
        # 获取你对应的好友备注，这里的小明我只是举个例子
        # 改成你最心爱的人的名字。
        friend = 'filehelper'
        if not test:
            my_friend = itchat.search_friends(name=friend_name)
            # 获取对应名称的一串数字
            friend = my_friend[0]["UserName"]
        # 获取金山字典的内容
        new_arr = get_news()
        message1 = new_arr[0]
        message2 = new_arr[1]
        message3 = new_arr[2][5:]
        message4 = u"来自" + your_name
        # 发送消息
        itchat.send(message1, toUserName=friend)
        itchat.send(message2, toUserName=friend)
        itchat.send(message3, toUserName=friend)
        itchat.send(message4, toUserName=friend)
    except Exception as e:
        print(e)
        message4 = u"今天" + your_name + u"出现了 bug /(ㄒoㄒ)/~~"
        itchat.send(message4, toUserName=friend)

def run_task():
    print('run_task')
    send_news()

def timerfun(sched_timer):
    while True:
        now = datetime.datetime.utcnow()
        fnow = datetime.datetime.strftime(now, '%Y-%m-%dT%H:%M:%S')
        if fnow >= sched_timer:
            run_task()  

            sched_timer = datetime.datetime.strptime(sched_timer, '%Y-%m-%dT%H:%M:%S')
            # minutes days seconds
            sched_timer = datetime.datetime.strftime(sched_timer + datetime.timedelta(days=1), '%Y-%m-%dT%H:%M:%S')
        time.sleep(20)


if __name__ == '__main__':
    itchat.auto_login(hotReload=True, enableCmdQR=True)
    timerfun('2018-12-21T22:00:00')





