import time

from CTCIT.public import robot_fun
import random
import decimal
from CTCIT.cfg import get_basic_cfg

print("############################################################ ")
#
# ask_price_list = []
# bid_price_list = []
# ask_count_list = []
# bid_count_list = []
#
# ask_price = robot_fun.getAskPrice(ask_price_list)
# bid_price = robot_fun.getBidPrice(bid_price_list)
# ask_count = robot_fun.getBtcCount(ask_count_list)
# bid_count = robot_fun.getBtcCount(bid_count_list)
#
# tester03_token = robot_fun.get_access_token(get_basic_cfg.loginUrl,
#                                             get_basic_cfg.tester03,
#                                             get_basic_cfg.password)
#
# tester04_token = robot_fun.get_access_token(get_basic_cfg.loginUrl,
#                                             get_basic_cfg.tester04,
#                                             get_basic_cfg.password)
#
# print(ask_price, ask_count, bid_price, bid_count)
#
# for i in range(0, 5):
#     ask_req = robot_fun.takeOrder('S',
#                                   ask_price_list[i],
#                                   ask_count_list[i],
#                                   get_basic_cfg.orderUrl,
#                                   tester03_token)
#     print(ask_req.text)
#     bid_req = robot_fun.takeOrder('B',
#                                   bid_price_list[i],
#                                   bid_count_list[i],
#                                   get_basic_cfg.orderUrl,
#                                   tester04_token)
#     print(bid_req.text)
#
#     print(ask_req.json()['data']['id'])
#     print(bid_req.json()['data']['id'])
# 获取bid一价的申报价格和数量
# bid_first_price = max(bid_price)
# bid_first_count = bid_count[bid_price.index(max(bid_price))]

# bid价格进行排序（由大到小）
# bid_price.sort()
# bid_price.reverse()

# time.sleep(3)
# # 挂ask并吃bid一价的一部分（价格小于bid一价，数量小于bid一价数量）
# deal_price = round(random.uniform(6900, bid_first_price), 2)
# deal_count = round(random.uniform(0.001, bid_first_count), 3)
#
# tester01_token = robot_fun.get_access_token(get_basic_cfg.loginUrl,
#                                             get_basic_cfg.tester03,
#                                             get_basic_cfg.password)
# tester01_req = robot_fun.takeOrder('S',
#                               7000,
#                               1.0001,
#                               get_basic_cfg.orderUrl,
#                               tester01_token)
# print(tester01_req.text)
# rate = robot_fun.getRate()
# maker_rate = rate[0]
# taker_rate = rate[1]
#
# print(maker_rate,taker_rate)

str = '596103200023'

robot_fun.getTradeOrderId(str)

# if str[0] > '9':
#     lenth = len_offset = 10 + ord(str[0]) - ord('A')
# else:
#     print("small")
#     print(ord(str[0]))
#     len_offset = int(ord(str[0])) - ord('0')
#     print(len_offset)
#
#     lenth = str.__len__() - len_offset
#     print(lenth)
#
# print(str[1:lenth][::-1])
# print(ord(str[0]))
# print(10 + ord(str[0]) - ord('A'))


