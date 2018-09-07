import numpy
import eth_btc.robot_fun
import time
import yaml
import random
import config.dbUtil

f = open('config/basic_cfg.yaml')
data = yaml.load(f)

#登录地址
url_login = data['loginUrl']

#挂单地址
url_order = data['orderUrl']

#获取最新交易价格
eth_btc_url = data['coinmarket'] + str(1027) + '/?convert=btc'

#用户账号密码

tester01 = data['count']['tester01']
password1 = data['count']['password1']

tester02 = data['count']['tester02']
password2 = data['count']['password2']

token01 = eth_btc.robot_fun.get_access_token(url_login, tester01, password1)
token02 = eth_btc.robot_fun.get_access_token(url_login, tester02, password1)

tradePairCode = 'eth_btc'

while 1:
    try:
        eth_btc_lastprice = float(eth_btc.robot_fun.getMarketPrice(eth_btc_url))
        sql = "insert into coin (name,price) values ('eth',%f);" % eth_btc_lastprice
        config.dbUtil.execute(sql)

    except Exception as e:
        continue

    nowTime = time.time()

    for i in range(1,1000000):
        count1 = round(random.uniform(0.001, data['tradePair']['eth_btcMaxCount']), 6)
        req1 = eth_btc.robot_fun.order_buy(tester01, eth_btc_lastprice, url_order, token01, tradePairCode, count1)
        #设置等待时间
        if round(nowTime) % random.randint(1, i + 2):
            time.sleep(random.uniform(0, 5))
        else:
            time.sleep(numpy.random.random(5)[random.randint(0, 4)] + 0.5)

        count2 = round(random.uniform(0.001, data['tradePair']['eth_btcMaxCount']), 6)
        req2 = eth_btc.robot_fun.order_sell(tester02, eth_btc_lastprice, url_order, token02, tradePairCode, count2)
        #设置等待时间
        if round(nowTime) % random.randint(1, i + 2):
            time.sleep(random.uniform(0, 5))
        else:
            time.sleep(numpy.random.random(5)[random.randint(0, 4)] + 0.5)

        if req1.json()['msg'] == 'AccessToken已过期':
            eth_btc.robot_fun.get_access_token(url_login, tester01, password1)

        if req2.json()['msg'] == 'AccessToken已过期':
            eth_btc.robot_fun.get_access_token(url_login, tester02, password2)

        #30秒后跳出循环重新获取最新交易价格
        runTime = time.time()
        if ((runTime - nowTime) > 60):
            break

