import unittest, logging, random,time

import datetime
import requests
import redis

# from performance.public import ctcdbUtil

# for i in range (10):
#     print("开始批量新建账号......")
#     account_name = "test%d@lanlingdai.net" % (i+1)
#
#     add_sql = "INSERT INTO customer (type, mobile, password, email, full_name, gender, dob, nric_no, country_code, register_channel_code, register_channel_name, register_platform, invite_code, fullface_pic, contact_first_name, contact_first_relation, contact_first_phone, contact_second_name, contact_second_relation, contact_second_phone, google_secret, device_bind_status, blacklisted, locked, unlock_code, credit_score, credit_level, credited_at, created_at, updated_at) VALUES (300, '13800000000', '3e6c7d141e32189c917761138b026b74', '%s', NULL, NULL, NULL, NULL, NULL, '', '', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, '2018-04-03 10:46:45', '2018-05-16 09:57:11');" % account_name
#
#     ctcdbUtil.execute(add_sql)

# getId = ctcdbUtil.execute_select("created_at","2018-04-12 12:04:32")
# print(getId)

# 根据customer_id控制range范围,(开始id，结束id+1)
# for i in range(185, 285):
#     print("开始批量添加货币......")
#
#     add_usdt_sql = "INSERT INTO trade_account (coin_symbol, available_balance, reserved_balance, customer_id, status, created_at, updated_at) VALUE ('USDT', 0, 0, %d, 100, '2000-01-01 00:00:00', '2000-01-01 00:00:00');" % i
#     add_btc_sql = "INSERT INTO trade_account (coin_symbol, available_balance, reserved_balance, customer_id, status, created_at, updated_at) VALUE ('BTC', 0, 0, %d, 100, '2000-01-01 00:00:00', '2000-01-01 00:00:00');" % i
#     add_eth_sql = "INSERT INTO trade_account (coin_symbol, available_balance, reserved_balance, customer_id, status, created_at, updated_at) VALUE ('ETH', 0, 0, %d, 100, '2000-01-01 00:00:00', '2000-01-01 00:00:00');" % i
#     add_ltc_sql = "INSERT INTO trade_account (coin_symbol, available_balance, reserved_balance, customer_id, status, created_at, updated_at) VALUE ('LTC', 0, 0, %d, 100, '2000-01-01 00:00:00', '2000-01-01 00:00:00');" % i
#
#     ctcdbUtil.execute(add_usdt_sql)
#     ctcdbUtil.execute(add_btc_sql)
#     ctcdbUtil.execute(add_eth_sql)
#     ctcdbUtil.execute(add_ltc_sql)
# url = "http://coinx.zetafin.cn/api/ctc/exchange/refresh?tradePair=BTC_USDT"
# url_login = 'http://dev.zetafin.cn:22004/ctc/exchange/refresh'
# headers = {"content-type": "application/json"}
# trade_pair_code = {"trade_pair_code":"BTC_USDT"}
# request = requests.get(url)
# access_token = login_request.json()['data']['access_token']
# logging.info("access_token:"+access_token)
# print(login_request.text)

# print(request.text)


# REDIS_DB_INDEX = env("REDIS_DB_INDEX", 7)
#
# REDIS_HOST = env("REDIS_HOST", "dev.zetafin.cn")
#
# REDIS_PORT = env("REDIS_PORT", 6379)
#
# REDIS_CONNECTION_TIMEOUT = env("REDIS_CONNECTION_TIMEOUT", 1000)
#
# REDIS_AUTH_PASSWORD = {"REDIS_AUTH_PASSWORD", "Lld@123456"}

redis_config = {
    "host": "dev.zetafin.cn",
    "password": "Lld@123456",
    "port": 6379,
    "db": 7
}
# redis连接对象
redis_conn = redis.Redis(**redis_config)
btc_usd = redis_conn.get("CQ__huobi_ExRate_coin_LTC-USD")
print("获取的BTC_USD价格：",btc_usd)
print("获取的BTC_CNY价格：",btc_usd)

t = time.time()

end = int(round(t * 1000))
beg = end - 30000000

print(beg)
print(end)

