# -*- coding:utf-8 -*-
import random,requests
import logging
from CTCIT.cfg import get_ctcdb
from CTCIT.util import ctcdbUtil

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='ctc.log',
                    filemode='w')

# 定义一个Handler打印INFO及以上级别的日志到sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# 设置日志打印格式
#format='%(asctime)s - %(levelname)s: %(message)s'
formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
console.setFormatter(formatter)
# 将定义好的console日志handler添加到root logger
logging.getLogger('').addHandler(console)

#以中心价格随机获取区间价格
def getPrice(lastPrice):
    minusNum = lastPrice-lastPrice*random.uniform(0.0001,0.001)
    addNum = lastPrice+lastPrice*random.uniform(0.0001,0.001)
    price = round(random.uniform(minusNum,addNum),2)
    logging.info("当前获取的价格区间是:[%f,%f]" % (minusNum,addNum))
    return price

#获取Bitstamp的最新成交价
def getLastPrice(url):
    req = requests.post(url)
    lastPrice = req.json()['last']
    logging.info("----------------------------------------------------------------")
    logging.info("********** 当前Bitstamp的BTC/USD交易价格为:【%s】**********" %lastPrice)
    logging.info("----------------------------------------------------------------")

    return lastPrice

#获取用户token
def get_access_token(url_login,email,password):
    headers = {"content-type": "application/json"}
    login_data = {"email": email, "password": password}
    login_request = requests.post(url_login, headers=headers, json=login_data)
    access_token = login_request.json()['data']['access_token']
    # logging.info("access_token:"+access_token)
    # print(login_request.text)
    return access_token

#挂买单
def order_buy(email,price,url_order,access_token):
    price = getPrice(price)
    count = round(random.uniform(0.001,5.000),6)
    chip_order_headers = {"content-type":"application/json","access_token":access_token}
    order_data = {
        "direction":"B",
        "orderType":'100',
        "price":price,
        "count":count,
        "tradePairCode":"btc_usdt"
    }
    buy_request = requests.post(url_order, headers=chip_order_headers, json=order_data)

    #print(up_buy_request.text)
    logging.info("用户:%s 挂买单的价格:%s 挂买单的数量:%s"
                 % (email.split('@')[0],price,count)+" 状态:"+buy_request.json()['msg'])
    return buy_request

#挂卖单
def order_sell(email,price,url_order,access_token):
    price = getPrice(price)
    count = round(random.uniform(0.001,5.000),6)
    chip_order_headers = {"content-type":"application/json","access_token":access_token}
    order_data = {
        "direction":"S",
        "orderType":'100',
        "price":price,
        "count":count,
        "tradePairCode":"btc_usdt"
    }
    sell_request = requests.post(url_order, headers=chip_order_headers, json=order_data)

    #print(up_buy_request.text)
    logging.info("用户:%s 挂卖单的价格:%s 挂卖单的数量:%s"
                 % (email.split('@')[0],price,count)+" 状态:"+sell_request.json()['msg'])
    return sell_request

#挂单
def takeOrder(orderType,price,count,url_order,access_token):
    chip_order_headers = {"content-type":"application/json","access_token":access_token}
    order_data = {
        "direction":orderType,
        "orderType":'200',
        "price":price,
        "count":count,
        "tradePairCode":"btc_usdt"
    }
    request = requests.post(url_order, headers=chip_order_headers, json=order_data)
    return request

#挂市价单
def takeMarketOrder(orderType,price,count,url_order,access_token):
    chip_order_headers = {"content-type":"application/json","access_token":access_token}
    order_data = {
        "direction":orderType,
        "orderType":'100',
        "price":price,
        "count":count,
        "tradePairCode":"btc_usdt"
    }
    request = requests.post(url_order, headers=chip_order_headers, json=order_data)
    return request

#批量挂买
def batchBuyOrder(price,count,url_order,access_token):
    return

#批量挂卖单
def batchSellOrder(price,count,url_order,access_token):
    return

#撤单
def cancelOrder(url_cancel,orderId,remark,access_token):
    cancel_headers = {"content-type":"application/json","access_token":access_token}
    order_data = {
        "orderId":orderId,
        "remark":remark
    }
    cancel_request = requests.post(url_cancel, headers=cancel_headers, json=order_data)
    return cancel_request

#随机获取大于7000的价格
def getAskPrice(list):
    for i in range(0, 5):
        list.append(round(random.uniform(7000, 7100), 2))
    #list.sort()
    #list.reverse()
    return list

#随机获取小于7000的价格
def getBidPrice(list):
    for i in range(0, 5):
        list.append(round(random.uniform(6900, 7000), 2))
    #list.sort()
    #list.reverse()
    return list

#随机获取BTC数量
def getBtcCount(list):
    for i in range(0, 5):
        list.append(round(random.uniform(0.001, 5), 3))
    #list.sort()
    #list.reverse()
    return list

#获取挂单吃单手续费
def getRate():
    data = ctcdbUtil.execute(get_ctcdb.get_rate[0])
    maker_rate = data[0][0]
    taker_rate = data[0][1]
    return maker_rate,taker_rate

#获取列表和
def getListSum(list):
    sum = 0.0
    for i in range(5):
        sum = sum + list[i]
    return sum

#形成深度图

#用户的订单id转换成数据库的trade_order_id
def getTradeOrderId(userId):
    userId = str(userId)

    if ord(userId[0]) > ord('9'):
        len_offset = 10 + ord(userId[0]) - ord('A')
    else:
        len_offset = ord(userId[0]) - ord('0')

    lenth = userId.__len__() - len_offset

    return userId[1:lenth][::-1]