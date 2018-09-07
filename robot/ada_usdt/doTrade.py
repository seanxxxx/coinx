import numpy
import ada_usdt.robot_fun
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
ada_usdt_url = data['coinmarket'] + str(2010) + '/?convert=usdt'

#用户账号密码

tester01 = data['count']['tester01']
password1 = data['count']['password1']

tester02 = data['count']['tester02']
password2 = data['count']['password2']

token01 = ada_usdt.robot_fun.get_access_token(url_login, tester01, password1)
token02 = ada_usdt.robot_fun.get_access_token(url_login, tester02, password1)

tradePairCode = 'ada_usdt'

while 1:
    try:
        ada_usdt_lastprice = float(ada_usdt.robot_fun.getMarketPrice(ada_usdt_url))
        sql = "insert into coin (name,price) values ('ada',%f);" % ada_usdt_lastprice
        config.dbUtil.execute(sql)

    except Exception as e:
        continue

    nowTime = time.time()

    for i in range(1,1000000):
        count1 = round(random.uniform(0.001, data['tradePair']['ada_usdtMaxCount']), 2)
        req1 = ada_usdt.robot_fun.order_buy(tester01, ada_usdt_lastprice, url_order, token01, tradePairCode, count1)
        #设置等待时间
        if round(nowTime) % random.randint(1, i + 2):
            time.sleep(random.uniform(0, 5))
        else:
            time.sleep(numpy.random.random(5)[random.randint(0, 4)] + 0.5)

        count2 = round(random.uniform(0.001, data['tradePair']['ada_usdtMaxCount']), 2)
        req2 = ada_usdt.robot_fun.order_sell(tester02, ada_usdt_lastprice, url_order, token02, tradePairCode, count2)
        #设置等待时间
        if round(nowTime) % random.randint(1, i + 2):
            time.sleep(random.uniform(0, 5))
        else:
            time.sleep(numpy.random.random(5)[random.randint(0, 4)] + 0.5)

        if req1.json()['msg'] == 'AccessToken已过期':
            ada_usdt.robot_fun.get_access_token(url_login, tester01, password1)

        if req2.json()['msg'] == 'AccessToken已过期':
            ada_usdt.robot_fun.get_access_token(url_login, tester02, password2)

        #30秒后跳出循环重新获取最新交易价格
        runTime = time.time()
        if ((runTime - nowTime) > 60):
            break

