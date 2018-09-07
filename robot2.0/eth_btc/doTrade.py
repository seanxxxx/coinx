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
eth_btc_url = data['eth_btc_url']

#撤单地址
url_cancel_order = data['cancelOrder']

#用户账号密码

robot03 = data['count']['robot03']
password1 = data['count']['password1']

robot04 = data['count']['robot04']
password2 = data['count']['password2']

token01 = data['count']['token03']
token02 = data['count']['token04']

tradePairCode = 'ETH_BTC'

while 1:
    try:
        eth_btc_lastprice = float(robot_fun.getMarketPrice(eth_btc_url))

    except Exception as e:
        continue

    nowTime = time.time()

    for i in range(1,10000):

        count1 = round(random.uniform(0.001, data['tradePair']['eth_btcMaxCount']), 3)
        req1 = robot_fun.order_buy(robot03, eth_btc_lastprice, url_order, token01, tradePairCode, count1)

        count2 = round(random.uniform(0.001, data['tradePair']['eth_btcMaxCount']), 3)
        req2 = robot_fun.order_sell(robot04, eth_btc_lastprice, url_order, token02, tradePairCode, count2)

        #设置等待时间
        if round(nowTime) % random.randint(1, i + 2):
            time.sleep(random.uniform(3, 5))
        else:
            time.sleep(random.randint(3, 6))

        #30秒后跳出循环重新获取最新交易价格
        runTime = time.time()
        if ((runTime - nowTime) > 60):
            req_cancel_1 = robot_fun.cancelOrderWithTradePair(url_cancel_order,tradePairCode,token01)
            req_cancel_2 = robot_fun.cancelOrderWithTradePair(url_cancel_order,tradePairCode,token02)

            print req_cancel_1.text
            print req_cancel_2.text

            break

