import requests
import random
import yaml
from DjangoWebPro.APITest import robot_fun
from DjangoWebPro.APITest import dbUtil

# f = open('config/basic_cfg.yaml')
# data = yaml.load(f)
# headers = {"content-type": "application/json"}
# login_request = requests.post('https://api.bitmart.com/ticker/', headers=headers, json='eth_usdt')
# # price = login_request.json()['new_24h']
# print(login_request)
# print(login_request)
# req = requests.get('https://api.bitmart.com/ticker/eth_usdt')
# print(req.text)
# print(req.json()['new_24h'])

sql = 'insert into coin (name,price) values ("btc",7000);'

dbUtil.execute(sql)

# test1 = data['count']['tester01']
# test2 = data['count']['tester02']
#
# print(data['tradePair']['tradePairCode'])
# print(type(data['tradePair']['tradeMaxCount']))

# #登录地址
# url_login = data['loginUrl']
#
# #挂单地址
# url_order = data['orderUrl']
#
# #撤单地址
# cancel_order = data['cancelOrder']
#
# #获取最新交易价格的地址
# price_url = data['priceUrl']

def chip_order_buy(price,count,url_order,access_token):
    chip_order_headers = {"content-type":"application/json","access_token":access_token}
    order_data = {
        "direction":"B",
        "orderType":'100',
        "price":price,
        "count":count,
        "tradePairCode":"btc_usdt"
    }
    buy_request = requests.post(url_order, headers=chip_order_headers, json=order_data)
    print(buy_request.text)
    return buy_request

def chip_order_sell(price,count,url_order,access_token):
    chip_order_headers = {"content-type":"application/json","access_token":access_token}
    order_data = {
        "direction":"S",
        "orderType":"100",
        "price":price,
        "count":count,
        "tradePairCode":"btc_usdt"
    }
    sell_request = requests.post(url_order, headers=chip_order_headers, json=order_data)
    print(sell_request.text)
    return sell_request

def batchBuyOrder(email,password,url_login,pl,cl,url_order):
    access_token = robot_fun.get_access_token(url_login, email, password)
    chip_order_headers = {"content-type":"application/json","access_token":access_token}
    amount = 0
    for i in range(0,5):
        amount = amount + pl[i] * cl[i]
        order_data = {
            "direction":"B",
            "orderType":'100',
            "price":pl[i],
            "count":cl[i],
            "tradePairCode":"btc_usdt"
        }
        buy_request = requests.post(url_order, headers=chip_order_headers, json=order_data)
    print("批量挂买单：", buy_request.json()['msg'])

def batchSellOrder(email,password,url_login,pl,cl,url_order):
    access_token = robot_fun.get_access_token(url_login, email, password)
    chip_order_headers = {"content-type":"application/json","access_token":access_token}
    amount = 0
    for i in range(0,5):
        amount = amount + pl[i]*cl[i]
        order_data = {
            "direction":"S",
            "orderType":'100',
            "price":pl[i],
            "count":cl[i],
            "tradePairCode":"btc_usdt"
        }
        sell_request = requests.post(url_order, headers=chip_order_headers, json=order_data)
    print("批量挂卖单：",sell_request.json()['msg'])

def batchBuyOrder(email,password,url_login,pl,cl,url_order):
    access_token = robot_fun.get_access_token(url_login, email, password)
    chip_order_headers = {"content-type":"application/json","access_token":access_token}
    amount = 0
    for i in range(0,5):
        amount = amount + pl[i] * cl[i]
        order_data = {
            "direction":"B",
            "orderType":'200',
            "price":pl[i],
            "count":cl[i],
            "tradePairCode":"BTC_ETH"
        }
        buy_request = requests.post(url_order, headers=chip_order_headers, json=order_data)
    print("批量挂买单：", buy_request.json()['msg'])

def batchSellOrder(email,password,url_login,pl,cl,url_order):
    access_token = robot_fun.get_access_token(url_login, email, password)
    chip_order_headers = {"content-type":"application/json","access_token":access_token}
    amount = 0
    for i in range(0,5):
        amount = amount + pl[i]*cl[i]
        order_data = {
            "direction":"S",
            "orderType":'200',
            "price":pl[i],
            "count":cl[i],
            "tradePairCode":"BTC_ETH"
        }
        sell_request = requests.post(url_order, headers=chip_order_headers, json=order_data)
    print("批量挂卖单：",sell_request.json()['msg'])

#调试代码
# batchBuyOrder(test2,password,url_login,buyPriceList,buyCountList,url_order)
# batchSellOrder(test1,password,url_login,sellPriceList,sellCountList,url_order)

# token = robot_fun.get_access_token(url_login,email2,password)
# req = robot_fun.cancelOrder(cancel_order,1024,'wtf',token)
# print(req)
#
# token = robot_fun.get_access_token(url_login,'xuxuan@lanlingdai.net','123456')
# print(token)