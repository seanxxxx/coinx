# -*- coding:utf-8 -*-
import random,requests
import logging

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
    min = lastPrice-lastPrice*random.uniform(0.0001,0.001)
    max = lastPrice+lastPrice*random.uniform(0.0001,0.001)
    price = round(random.uniform(min,max),5)
    logging.info("当前获取的价格区间是:[%.5f,%.5f]" % (round(min,5),round(max,5)))
    return price

#获取最新成交价
def getMarketPrice(url):
    req = requests.get(url)
    lastPrice = req.json()['data']['quotes']['ETH']['price']
    logging.info("----------------------------------------------------------------")
    logging.info("********** 当前LTC/ETH市场交易价格为:【%s】**********" %lastPrice)
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
def order_buy(email,price,url_order,access_token,tradePairCode,count):
    price = getPrice(price)
    # count = 0
    # if tradePairCode == 'btc_usdt':
    #     count = round(random.uniform(0.001, data['tradePair']['btc_usdtMaxCount']), 3)
    # elif tradePairCode == 'eth_usdt':
    #     count = round(random.uniform(0.001, data['tradePair']['eth_usdtMaxCount']), 3)
    # elif tradePairCode == 'xrp_usdt':
    #     count = round(random.uniform(0.001, data['tradePair']['xrp_usdtMaxCount']), 3)
    # elif tradePairCode == 'bch_usdt':
    #     count = round(random.uniform(0.001, data['tradePair']['bch_usdtMaxCount']), 3)
    # elif tradePairCode == 'eos_usdt':
    #     count = round(random.uniform(0.001, data['tradePair']['eos_usdtMaxCount']), 3)
    # elif tradePairCode == 'ltc_usdt':
    #     count = round(random.uniform(0.001, data['tradePair']['ltc_usdtMaxCount']), 3)
    # elif tradePairCode == 'ada_usdt':
    #     count = round(random.uniform(0.001, data['tradePair']['ada_usdtMaxCount']), 3)
    # elif tradePairCode == 'xlm_usdt':
    #     count = round(random.uniform(0.001, data['tradePair']['xlm_usdtMaxCount']), 3)
    # elif tradePairCode == 'iota_usdt':
    #     count = round(random.uniform(0.001, data['tradePair']['iota_usdtMaxCount']), 3)
    # elif tradePairCode == 'eth_btc':
    #     count = round(random.uniform(0.001, data['tradePair']['eth_btcMaxCount']), 3)
    # elif tradePairCode == 'xrp_btc':
    #     count = round(random.uniform(0.001, data['tradePair']['xrp_btcMaxCount']), 3)
    # elif tradePairCode == 'bch_btc':
    #     count = round(random.uniform(0.001, data['tradePair']['bch_btcMaxCount']), 3)
    # elif tradePairCode == 'eos_btc':
    #     count = round(random.uniform(0.001, data['tradePair']['eos_btcMaxCount']), 3)
    # elif tradePairCode == 'ltc_btc':
    #     count = round(random.uniform(0.001, data['tradePair']['ltc_btcMaxCount']), 3)
    # elif tradePairCode == 'ada_btc':
    #     count = round(random.uniform(0.001, data['tradePair']['ada_btcMaxCount']), 3)
    # elif tradePairCode == 'xlm_btc':
    #     count = round(random.uniform(0.001, data['tradePair']['xlm_btcMaxCount']), 3)
    # elif tradePairCode == 'iota_btc':
    #     count = round(random.uniform(0.001, data['tradePair']['iota_btcMaxCount']), 3)
    # elif tradePairCode == 'xrp_eth':
    #     count = round(random.uniform(0.001, data['tradePair']['xrp_ethMaxCount']), 3)
    # elif tradePairCode == 'eos_eth':
    #     count = round(random.uniform(0.001, data['tradePair']['eos_ethMaxCount']), 3)
    # elif tradePairCode == 'ltc_eth':
    #     count = round(random.uniform(0.001, data['tradePair']['ltc_ethMaxCount']), 3)
    # elif tradePairCode == 'ada_eth':
    #     count = round(random.uniform(0.001, data['tradePair']['ada_ethMaxCount']), 3)
    # elif tradePairCode == 'xlm_eth':
    #     count = round(random.uniform(0.001, data['tradePair']['xlm_ethMaxCount']), 3)
    # elif tradePairCode == 'iota_eth':
    #     count = round(random.uniform(0.001, data['tradePair']['iota_ethMaxCount']), 3)

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
    logging.info("交易币对: %s  用户:%s 挂【买】单的价格:%s 挂【买】单的数量:%s"
                 % (tradePairCode.upper(),email.split('@')[0],price,count)+" 状态:"+buy_request.json()['msg'])
    return buy_request

#挂卖单
def order_sell(email,price,url_order,access_token,tradePairCode,count):
    price = getPrice(price)
    # count = 0
    # if tradePairCode == 'btc_usdt':
    #     count = round(random.uniform(0.001, data['tradePair']['btc_usdtMaxCount']), 3)
    # elif tradePairCode == 'eth_usdt':
    #     count = round(random.uniform(0.001, data['tradePair']['eth_usdtMaxCount']), 3)
    # elif tradePairCode == 'xrp_usdt':
    #     count = round(random.uniform(0.001, data['tradePair']['xrp_usdtMaxCount']), 3)
    # elif tradePairCode == 'bch_usdt':
    #     count = round(random.uniform(0.001, data['tradePair']['bch_usdtMaxCount']), 3)
    # elif tradePairCode == 'eos_usdt':
    #     count = round(random.uniform(0.001, data['tradePair']['eos_usdtMaxCount']), 3)
    # elif tradePairCode == 'ltc_usdt':
    #     count = round(random.uniform(0.001, data['tradePair']['ltc_usdtMaxCount']), 3)
    # elif tradePairCode == 'ada_usdt':
    #     count = round(random.uniform(0.001, data['tradePair']['ada_usdtMaxCount']), 3)
    # elif tradePairCode == 'xlm_usdt':
    #     count = round(random.uniform(0.001, data['tradePair']['xlm_usdtMaxCount']), 3)
    # elif tradePairCode == 'iota_usdt':
    #     count = round(random.uniform(0.001, data['tradePair']['iota_usdtMaxCount']), 3)
    # elif tradePairCode == 'eth_btc':
    #     count = round(random.uniform(0.001, data['tradePair']['eth_btcMaxCount']), 3)
    # elif tradePairCode == 'xrp_btc':
    #     count = round(random.uniform(0.001, data['tradePair']['xrp_btcMaxCount']), 3)
    # elif tradePairCode == 'bch_btc':
    #     count = round(random.uniform(0.001, data['tradePair']['bch_btcMaxCount']), 3)
    # elif tradePairCode == 'eos_btc':
    #     count = round(random.uniform(0.001, data['tradePair']['eos_btcMaxCount']), 3)
    # elif tradePairCode == 'ltc_btc':
    #     count = round(random.uniform(0.001, data['tradePair']['ltc_btcMaxCount']), 3)
    # elif tradePairCode == 'ada_btc':
    #     count = round(random.uniform(0.001, data['tradePair']['ada_btcMaxCount']), 3)
    # elif tradePairCode == 'xlm_btc':
    #     count = round(random.uniform(0.001, data['tradePair']['xlm_btcMaxCount']), 3)
    # elif tradePairCode == 'iota_btc':
    #     count = round(random.uniform(0.001, data['tradePair']['iota_btcMaxCount']), 3)
    # elif tradePairCode == 'xrp_eth':
    #     count = round(random.uniform(0.001, data['tradePair']['xrp_ethMaxCount']), 3)
    # elif tradePairCode == 'eos_eth':
    #     count = round(random.uniform(0.001, data['tradePair']['eos_ethMaxCount']), 3)
    # elif tradePairCode == 'ltc_eth':
    #     count = round(random.uniform(0.001, data['tradePair']['ltc_ethMaxCount']), 3)
    # elif tradePairCode == 'ada_eth':
    #     count = round(random.uniform(0.001, data['tradePair']['ada_ethMaxCount']), 3)
    # elif tradePairCode == 'xlm_eth':
    #     count = round(random.uniform(0.001, data['tradePair']['xlm_ethMaxCount']), 3)
    # elif tradePairCode == 'iota_eth':
    #     count = round(random.uniform(0.001, data['tradePair']['iota_ethMaxCount']), 3)

    chip_order_headers = {"content-type":"application/json","access_token":access_token}
    order_data = {
        "direction":"sell",
        "orderType":'100',
        "price":price,
        "count":count,
        "tradePairCode":tradePairCode
    }
    sell_request = requests.post(url_order, headers=chip_order_headers, json=order_data)

    #print(up_buy_request.text)
    logging.info("交易币对: %s  用户:%s 挂【卖】单的价格:%s 挂【卖】单的数量:%s"
                 % (tradePairCode.upper(),email.split('@')[0],price,count)+" 状态:"+sell_request.json()['msg'])
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

#撤单
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