import requests,logging,random
import urllib.parse
import json
import time

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

#根据权重选取下标
def random_index(rate):
    start = 0
    random_num = random.randint(1,sum(rate))
    #print("random_num:",random_num)
    for index,item in enumerate(rate):
        start = start + item
        #print("index/",index,"/start:", start, "/item:", item)
        if random_num <= start:
            break
    return index

#获取递增的价格列表(1,2,3,4,5,6,7,8,9)
def increment_price(price,add_range):
    price_increment_list = []
    for i in range(0,11):
        price = price+price*(add_range/10)
        price_increment_list.append(price)
    return price_increment_list

#获取递减的价格列表(9,8,7,6,5,4,3,2,1)
def decrement_price(price,minus_range):
    price_decrement_list = []
    for i in range(0,11):
        price = price-price*(minus_range/10)
        price_decrement_list.append(price)
    return price_decrement_list

#获取随机递增价格
def get_random_addprice(price,add_range,rate):
    price_increment_list = increment_price(price, add_range)
    #logging.debug(price_increment_list)
    arr_increment_price = [
        round(random.uniform(price_increment_list[0],price_increment_list[1]),2),
        round(random.uniform(price_increment_list[1],price_increment_list[2]),2),
        round(random.uniform(price_increment_list[2],price_increment_list[3]),2),
        round(random.uniform(price_increment_list[3],price_increment_list[4]),2),
        round(random.uniform(price_increment_list[4],price_increment_list[5]),2),
        round(random.uniform(price_increment_list[5],price_increment_list[6]),2),
        round(random.uniform(price_increment_list[6],price_increment_list[7]),2),
        round(random.uniform(price_increment_list[7],price_increment_list[8]),2),
        round(random.uniform(price_increment_list[8],price_increment_list[9]),2),
        round(random.uniform(price_increment_list[9],price_increment_list[10]),2)
    ]
    logging.debug(arr_increment_price)
    return arr_increment_price[random_index(rate)]

#获取随机递减价格
def get_random_minusprice(price,minus_range,rate):
    price_decrement_list = decrement_price(price, minus_range)
    #logging.debug(price_decrement_list)
    arr_decrement_price = [
        round(random.uniform(price_decrement_list[0],price_decrement_list[1]),2),
        round(random.uniform(price_decrement_list[1],price_decrement_list[2]),2),
        round(random.uniform(price_decrement_list[2],price_decrement_list[3]),2),
        round(random.uniform(price_decrement_list[3],price_decrement_list[4]),2),
        round(random.uniform(price_decrement_list[4],price_decrement_list[5]),2),
        round(random.uniform(price_decrement_list[5],price_decrement_list[6]),2),
        round(random.uniform(price_decrement_list[6],price_decrement_list[7]),2),
        round(random.uniform(price_decrement_list[7],price_decrement_list[8]),2),
        round(random.uniform(price_decrement_list[8],price_decrement_list[9]),2),
        round(random.uniform(price_decrement_list[9],price_decrement_list[10]),2)
    ]
    logging.debug(arr_decrement_price)
    return arr_decrement_price[random_index(rate)]

#获取用户token
def get_access_token(url_login,email,password):
    headers = {"content-type": "application/json"}
    login_data = {"email": email, "password": password}
    login_request = requests.post(url_login, headers=headers, json=login_data)
    access_token = login_request.json()['data']['access_token']
    # logging.info("*****"+access_token)
    # print(login_request.text)
    return access_token

#挂买单(价格递增)
def chip_order_buy_up(username,price,add_range,addrate,url_order,access_token):
    buyprice = get_random_addprice(price,add_range,addrate)
    count = round(random.uniform(0.001,5.000),6)
    chip_order_headers = {"content-type":"application/json","access_token":access_token}
    order_data = {
        "direction":"B",
        "orderType":'100',
        "price":buyprice,
        "count":count,
        "tradePairCode":"btc_usdt"
    }
    up_buy_request = requests.post(url_order, headers=chip_order_headers, json=order_data)

    #print(up_buy_request.text)
    logging.info("用户:%s 挂买单的价格:%s 挂买单的数量:%s"
                 % (username,buyprice,count)+" 状态:"+up_buy_request.json()['msg'])
    return up_buy_request

#挂买单(价格递减)
def chip_order_buy_down(username,price,minus_range,minusrate,url_order,access_token):
    buyprice = get_random_minusprice(price,minus_range,minusrate)
    count = round(random.uniform(0.001,5.000),6)
    chip_order_headers = {"content-type":"application/json","access_token":access_token}
    order_data = {
        "direction":"B",
        "orderType":'100',
        "price":buyprice,
        "count":count,
        "tradePairCode":"btc_usdt"
    }
    down_buy_request = requests.post(url_order, headers=chip_order_headers, json=order_data)

    #print(down_buy_request.text)
    logging.info("用户:%s 挂买单的价格:%s 挂买单的数量:%s"
                 % (username,buyprice, count)+" 状态:"+down_buy_request.json()['msg'])
    return down_buy_request

#挂卖单(价格递增)
def chip_order_sell_up(username,price,add_range,addrate,url_order,access_token):
    sellprice = get_random_addprice(price,add_range,addrate)
    count = round(random.uniform(0.001,5.000),6)
    chip_order_headers = {"content-type":"application/json","access_token":access_token}
    order_data = {
        "direction":"S",
        "orderType":"100",
        "price":sellprice,
        "count":count,
        "tradePairCode":"btc_usdt"
    }
    up_sell_request = requests.post(url_order, headers=chip_order_headers, json=order_data)

    #print(up_sell_request.text)
    logging.info("用户:%s 挂卖单的价格:%s 挂卖单的数量:%s"
                 % (username,sellprice, count)+" 状态:"+up_sell_request.json()['msg'])
    return up_sell_request

#挂卖单(价格递减)
def chip_order_sell_down(username,price,minus_range,minusrate,url_order,access_token):
    sellprice = get_random_minusprice(price,minus_range,minusrate)
    count = round(random.uniform(0.001,5.000),6)
    chip_order_headers = {"content-type":"application/json","access_token":access_token}
    order_data = {
        "direction":"S",
        "orderType":"100",
        "price":sellprice,
        "count":count,
        "tradePairCode":"btc_usdt"
    }
    down_sell_request = requests.post(url_order, headers=chip_order_headers, json=order_data)

    #print(down_sell_request.text)
    logging.info("用户:%s 挂卖单的价格:%s 挂卖单的数量:%s"
                 % (username,sellprice, count)+" 状态:"+down_sell_request.json()['msg'])
    return down_sell_request

