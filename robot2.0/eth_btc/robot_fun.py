# -*- coding:utf-8 -*-
import random,requests
import logging
from retrying import retry

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='coinx.log',
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
    price = round(random.uniform(minusNum,addNum),6)
    #logging.info("当前获取的价格区间是:[%f,%f]" % (minusNum,addNum))
    return price

#获取最新成交价
@retry
def getMarketPrice(url):
    req = requests.get(url)
    lastPrice = req.json()['data']['quotes']['BTC']['price']
    logging.info("----------------------------------------------------------------")
    logging.info(u"********** 当前ETH/BTC市场交易价格为:【%s】**********" %lastPrice)
    logging.info("----------------------------------------------------------------")
    return lastPrice

#获取用户token
@retry
def get_access_token(url_login,email,password):
    headers = {"content-type": "application/json"}
    login_data = {"email": email, "password": password}
    login_request = requests.post(url_login, headers=headers, json=login_data)
    access_token = login_request.json()['data']['access_token']
    # logging.info("access_token:"+access_token)
    # print(login_request.text)
    return access_token

#挂买单
@retry
def order_buy(email,price,url_order,access_token,tradePairCode,count):
    price = getPrice(price)

    chip_order_headers = {"content-type":"application/json","access_token":access_token}
    order_data = {
        "direction":"buy",
        "orderType":'100',
        "price":price,
        "count":count,
        "tradePairCode":tradePairCode
    }
    buy_request = requests.post(url_order, headers=chip_order_headers, json=order_data)

    #print(up_buy_request.text)
    logging.info(u"交易币对: %s  用户:%s 挂【买】单的价格:%s 挂【买】单的数量:%s"
                 % (tradePairCode.upper(),email.split('@')[0],price,count)+u" 状态:"+buy_request.json()['msg'])
    return buy_request

#挂卖单
@retry
def order_sell(email,price,url_order,access_token,tradePairCode,count):
    price = getPrice(price)

    chip_order_headers = {"content-type":"application/json","access_token":access_token}
    order_data = {
        "direction":"sell",
        "orderType":'100',
        "price":price,
        "count":count,
        "tradePairCode":tradePairCode
    }
    sell_request = requests.post(url_order, headers=chip_order_headers, json=order_data)

    logging.info(u"交易币对: %s  用户:%s 挂【卖】单的价格:%s 挂【卖】单的数量:%s"
                 % (tradePairCode.upper(),email.split('@')[0],price,count)+u" 状态:"+sell_request.json()['msg'])
    return sell_request

#挂单
@retry
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

#撤单
@retry
def cancelOrder(url_cancel,orderId,remark,access_token):
    cancel_headers = {"content-type":"application/json","access_token":access_token}
    order_data = {
        "orderId":orderId,
        "remark":remark
    }
    cancel_request = requests.post(url_cancel, headers=cancel_headers, json=order_data)
    return cancel_request

def batchBuyOrder(price,count,url_order,access_token):
    return

def batchSellOrder(price,count,url_order,access_token):
    return

#用户的订单id转换成数据库的trade_order_id
def getTradeOrderId(userId):
    userId = str(userId)

    if ord(userId[0]) > ord('9'):
        len_offset = 10 + ord(userId[0]) - ord('A')
    else:
        len_offset = ord(userId[0]) - ord('0')

    lenth = userId.__len__() - len_offset

    return userId[1:lenth][::-1]

#数据库的trade_order_id转换成用户的订单id
def getTradeOrderId(userId):
    userId = str(userId)

    if ord(userId[0]) > ord('9'):
        len_offset = 10 + ord(userId[0]) - ord('A')
    else:
        len_offset = ord(userId[0]) - ord('0')

    lenth = userId.__len__() - len_offset

    return userId[1:lenth][::-1]

#批量撤单接口
def cancelOrderWithTradePair(url_cancel,trade_pair_code,access_token):
    url = url_cancel + '/' + trade_pair_code
    print url
    cancel_headers = {"content-type":"application/json","access_token":access_token}
    cancel_request = requests.get(url, headers=cancel_headers)
    return cancel_request