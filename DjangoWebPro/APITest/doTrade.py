import numpy
import DjangoWebPro.APITest.robot_fun
import time
import yaml
import random

f = open('config/basic_cfg.yaml')
data = yaml.load(f)

#登录地址
url_login = data['loginUrl']

#挂单地址
url_order = data['orderUrl']

#获取最新交易价格
btc_usdt_url = data['btc_usdt_url']

#用户账号密码

tester01 = data['count']['tester01']
password1 = data['count']['password1']

tester02 = data['count']['tester02']
password2 = data['count']['password2']

token01 = DjangoWebPro.APITest.robot_fun.get_access_token(url_login, tester01, password1)
token02 = DjangoWebPro.APITest.robot_fun.get_access_token(url_login, tester02, password1)

tradePairCode = 'btc_usdt'

while 1:
    try:
        btc_usdt_lastprice = float(DjangoWebPro.APITest.robot_fun.getBtcUsdtPrice(btc_usdt_url))
    except Exception as e:
        continue

    nowTime = time.time()

    for i in range(1,1000000):

        req1 = DjangoWebPro.APITest.robot_fun.order_buy(tester01, btc_usdt_lastprice, url_order, token01, tradePairCode)
        #设置等待时间
        if round(nowTime) % random.randint(1, i + 2):
            time.sleep(random.uniform(0, 5))
        else:
            time.sleep(numpy.random.random(5)[random.randint(0, 4)] + 0.5)

        req2 = DjangoWebPro.APITest.robot_fun.order_sell(tester02, btc_usdt_lastprice, url_order, token02, tradePairCode)
        #设置等待时间
        if round(nowTime) % random.randint(1, i + 2):
            time.sleep(random.uniform(0, 5))
        else:
            time.sleep(numpy.random.random(5)[random.randint(0, 4)] + 0.5)

        if req1.json()['msg'] == 'AccessToken已过期':
            DjangoWebPro.APITest.robot_fun.get_access_token(url_login, tester01, password1)

        if req2.json()['msg'] == 'AccessToken已过期':
            DjangoWebPro.APITest.robot_fun.get_access_token(url_login, tester02, password2)

        #30秒后跳出循环重新获取最新交易价格
        runTime = time.time()
        if ((runTime - nowTime) > 30):
            break

