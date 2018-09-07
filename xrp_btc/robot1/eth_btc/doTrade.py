#-*- coding: UTF-8 -*-
import numpy
import robot_fun
import time
import yaml
import random
import os

dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path=os.path.join(dir,"config","basic_cfg.yaml")
f = open(config_path)
data = yaml.load(f)

#登录地址
url_login = data['loginUrl']

#挂单地址
url_order = data['orderUrl']

#获取最新交易价格
eth_btc_url = data['coinmarket'] + str(1027) + '/?convert=btc'

#用户账号密码

robot09 = data['count']['robot09']
password1 = data['count']['password1']

robot10 = data['count']['robot10']
password2 = data['count']['password2']

token01 = robot_fun.get_access_token(url_login, robot09, password1)
token02 = robot_fun.get_access_token(url_login, robot10, password1)

tradePairCode = 'eth_btc'

while 1:
    try:
        eth_btc_lastprice = float(robot_fun.getMarketPrice(eth_btc_url))

    except Exception as e:
        continue

    nowTime = time.time()

    for i in range(1,1000000):
        count1 = round(random.uniform(0.001, data['tradePair']['eth_btcMaxCount']), 6)
        req1 = robot_fun.order_buy(robot09, eth_btc_lastprice, url_order, token01, tradePairCode, count1)
        #设置等待时间
        if round(nowTime) % random.randint(1, i + 2):
            time.sleep(random.uniform(0, 5))
        else:
            time.sleep(numpy.random.random(5)[random.randint(0, 4)] + 0.5)

        count2 = round(random.uniform(0.001, data['tradePair']['eth_btcMaxCount']), 6)
        req2 = robot_fun.order_sell(robot10, eth_btc_lastprice, url_order, token02, tradePairCode, count2)
        #设置等待时间
        if round(nowTime) % random.randint(1, i + 2):
            time.sleep(random.uniform(0, 5))
        else:
            time.sleep(numpy.random.random(5)[random.randint(0, 4)] + 0.5)

        if req1.json()['msg'] == u'AccessToken已过期':
            robot_fun.get_access_token(url_login, robot09, password1)

        if req2.json()['msg'] == u'AccessToken已过期':
            robot_fun.get_access_token(url_login, robot10, password2)

        #30秒后跳出循环重新获取最新交易价格
        runTime = time.time()
        if ((runTime - nowTime) > 60):
            break

