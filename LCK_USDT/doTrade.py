import numpy
from LCK_USDT import robot_fun
import time
import yaml
import random

f = open('config/basic_cfg.yaml')
data = yaml.load(f)

url_login = data['loginUrl']

url_order = data['orderUrl']

btc_usdt_url = data['btc_usdt_url']

tester01 = data['count']['tester01']
password1 = data['count']['password1']

tester02 = data['count']['tester02']
password2 = data['count']['password2']

token01 = robot_fun.get_access_token(url_login, tester01, password1)
token02 = robot_fun.get_access_token(url_login, tester02, password1)

tradePairCode = 'lck_usdt'

while 1:
    try:
        btc_usdt_lastprice = float(robot_fun.getMarketPrice(btc_usdt_url))
    except Exception as e:
        continue

    nowTime = time.time()

    for i in range(1,1000000):
        count1 = round(random.uniform(0.001, data['tradePair']['btc_usdtMaxCount']), 6)
        req1 = robot_fun.order_buy(tester01, btc_usdt_lastprice, url_order, token01, tradePairCode, count1)
        #设置等待时间
        if round(nowTime) % random.randint(1, i + 2):
            time.sleep(random.uniform(0, 5))
        else:
            time.sleep(numpy.random.random(5)[random.randint(0, 4)] + 0.5)

        count2 = round(random.uniform(0.001, data['tradePair']['btc_usdtMaxCount']), 6)
        req2 = robot_fun.order_sell(tester02, btc_usdt_lastprice, url_order, token02, tradePairCode, count2)
        # 设置等待时间
        if round(nowTime) % random.randint(1, i + 2):
            time.sleep(random.uniform(0, 5))
        else:
            time.sleep(numpy.random.random(5)[random.randint(0, 4)] + 0.5)

        if req1.json()['msg'] == 'AccessToken已过期':
            robot_fun.get_access_token(url_login, tester01, password1)

        if req2.json()['msg'] == 'AccessToken已过期':
            robot_fun.get_access_token(url_login, tester02, password2)

        # 30秒后跳出循环重新获取最新交易价格
        runTime = time.time()
        if ((runTime - nowTime) > 60):
            break

