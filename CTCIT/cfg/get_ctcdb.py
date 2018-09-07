#-*- coding: UTF-8 -*-

import yaml

get_ctcdb_file = open('../cfg/ctcdb.yaml')
data_ctcdb = yaml.load(get_ctcdb_file)

host = data_ctcdb['host']
user = data_ctcdb['user']
password = data_ctcdb['pwd']
db = data_ctcdb['db']
port = data_ctcdb['port']
charset = data_ctcdb['charset']

setDB = data_ctcdb['setDB']
resetCount = data_ctcdb['resetCount']
search_tester01_money = data_ctcdb['search_tester01_BTC&USDT']
search_tester02_money = data_ctcdb['search_tester02_BTC&USDT']
cancel_order = data_ctcdb['cancel_order']
get_rate = data_ctcdb['get_rate']