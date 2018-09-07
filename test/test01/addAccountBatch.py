import unittest, logging, random,time
#根据customer_id控制range范围,(开始id，结束id+1)
from test.test01 import ctcdbUtil

for i in range (185,285):
    print("开始批量添加货币......")

    add_usdt_sql = "INSERT INTO trade_account (coin_symbol, available_balance, reserved_balance, customer_id, status, created_at, updated_at) VALUE ('USDT', 0, 0, %d, 100, '2000-01-01 00:00:00', '2000-01-01 00:00:00');" % i
    add_btc_sql = "INSERT INTO trade_account (coin_symbol, available_balance, reserved_balance, customer_id, status, created_at, updated_at) VALUE ('BTC', 0, 0, %d, 100, '2000-01-01 00:00:00', '2000-01-01 00:00:00');" % i
    add_eth_sql = "INSERT INTO trade_account (coin_symbol, available_balance, reserved_balance, customer_id, status, created_at, updated_at) VALUE ('ETH', 0, 0, %d, 100, '2000-01-01 00:00:00', '2000-01-01 00:00:00');" % i
    add_ltc_sql = "INSERT INTO trade_account (coin_symbol, available_balance, reserved_balance, customer_id, status, created_at, updated_at) VALUE ('LTC', 0, 0, %d, 100, '2000-01-01 00:00:00', '2000-01-01 00:00:00');" % i

    ctcdbUtil.execute(add_usdt_sql)
    ctcdbUtil.execute(add_btc_sql)
    ctcdbUtil.execute(add_eth_sql)
    ctcdbUtil.execute(add_ltc_sql)

