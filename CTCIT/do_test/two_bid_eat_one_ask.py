#-*- coding: UTF-8 -*-

import unittest, logging, random

import time

from CTCIT.cfg import get_basic_cfg
from CTCIT.public import robot_fun
from CTCIT.util import ctcdbUtil
from CTCIT.cfg import get_ctcdb

class TestTwoBidEatOneAskTrade(unittest.TestCase):
    """模拟深度->挂2个价格的Bid->吃Ask（Ask一价全部交易）测试"""

    @classmethod
    def setUpClass(cls):
        print("This setUpClass() method only called once.")

    @classmethod
    def tearDownClass(cls):
        print("This tearDownClass() method only called once too.")

    def setUp(self):
        """开始执行，重置数据"""
        ctcdbUtil.execute(get_ctcdb.setDB)
        ctcdbUtil.execute(get_ctcdb.resetCount[0])
        ctcdbUtil.execute(get_ctcdb.resetCount[1])
        ctcdbUtil.execute(get_ctcdb.resetCount[2])
        ctcdbUtil.execute(get_ctcdb.cancel_order[0])

    def tearDown(self):
        """执行完毕，重置数据"""
        ctcdbUtil.execute(get_ctcdb.setDB)
        ctcdbUtil.execute(get_ctcdb.resetCount[0])
        ctcdbUtil.execute(get_ctcdb.resetCount[1])
        ctcdbUtil.execute(get_ctcdb.resetCount[2])
        ctcdbUtil.execute(get_ctcdb.cancel_order[0])

    def twoBidEatOneAsk(self):
        """tester01申报2个ask，吃掉test02申报的全部bid一价"""
        ask_price_list = []
        bid_price_list = []
        ask_count_list = []
        bid_count_list = []

        ask_price = robot_fun.getAskPrice(ask_price_list)
        bid_price = robot_fun.getBidPrice(bid_price_list)
        ask_count = robot_fun.getBtcCount(ask_count_list)
        bid_count = robot_fun.getBtcCount(bid_count_list)

        #生成深度数据
        tester01_token = robot_fun.get_access_token(get_basic_cfg.loginUrl,
                                                    get_basic_cfg.tester01,
                                                    get_basic_cfg.password)

        tester02_token = robot_fun.get_access_token(get_basic_cfg.loginUrl,
                                                    get_basic_cfg.tester02,
                                                    get_basic_cfg.password)
        bid_amount = 0

        ask_order = {}
        bid_order = {}

        for i in range(0,5):
            ask_req = robot_fun.takeOrder('sell',
                                          ask_price[i],
                                          ask_count[i],
                                          get_basic_cfg.orderUrl,
                                          tester01_token)
            bid_req = robot_fun.takeOrder('buy',
                                          bid_price[i],
                                          bid_count[i],
                                          get_basic_cfg.orderUrl,
                                          tester02_token)

            ask_order[ask_price[i]] = ask_count[i]
            bid_order[bid_price[i]] = bid_count[i]

            bid_amount = bid_amount + bid_price[i] * bid_count[i]

        sorted_ask_prices = sorted(ask_order.keys())
        sorted_bid_prices = sorted(bid_order.keys())

        ask_1_price = sorted_ask_prices[0]
        ask_2_price = sorted_ask_prices[1]
        ask_3_price = sorted_ask_prices[2]
        ask_4_price = sorted_ask_prices[3]
        ask_5_price = sorted_ask_prices[4]

        ask_1_count = ask_order[ask_1_price]
        ask_2_count = ask_order[ask_2_price]
        ask_3_count = ask_order[ask_3_price]
        ask_4_count = ask_order[ask_4_price]
        ask_5_count = ask_order[ask_5_price]

        bid_1_price = sorted_bid_prices[0]
        bid_2_price = sorted_bid_prices[1]
        bid_3_price = sorted_bid_prices[2]
        bid_4_price = sorted_bid_prices[3]
        bid_5_price = sorted_bid_prices[4]

        bid_1_count = bid_order[bid_1_price]
        bid_2_count = bid_order[bid_2_price]
        bid_3_count = bid_order[bid_3_price]
        bid_4_count = bid_order[bid_4_price]
        bid_5_count = bid_order[bid_5_price]

        print("*******当前深度图*******")
        print("--------------------------------------")
        print("----------#price#----------#count#----")
        print("    |***%f***|***%f***|" % (ask_5_price, ask_5_count))
        print("    |***%f***|***%f***|" % (ask_4_price, ask_4_count))
        print("ASK |***%f***|***%f***|" % (ask_3_price, ask_3_count))
        print("    |***%f***|***%f***|" % (ask_2_price, ask_2_count))
        print("    |***%f***|***%f***|" % (ask_1_price, ask_1_count))
        print("———————————————————————————————————————")
        print("    |***%f***|***%f***|" % (bid_5_price, bid_5_count))
        print("    |***%f***|***%f***|" % (bid_4_price, bid_4_count))
        print("BID |***%f***|***%f***|" % (bid_3_price, bid_3_count))
        print("    |***%f***|***%f***|" % (bid_2_price, bid_2_count))
        print("    |***%f***|***%f***|" % (bid_1_price, bid_1_count))
        print("--------------------------------------")
        print("--------------------------------------")

        #第一次挂卖单的总数量
        ask_count_amount = round(robot_fun.getListSum(ask_count),3)

        # bid价格进行排序（由大到小）
        # bid_price.sort()
        # bid_price.reverse()

        #挂两个价格的Bid，价格小于卖二大于卖一
        deal_price_1 = round(random.uniform(ask_1_price, ask_2_price), 2)
        deal_price_2 = round(random.uniform(ask_1_price, ask_2_price), 2)
        deal_count_1 = round(random.uniform(0.001, ask_1_count), 3)
        deal_count_2 = round(ask_1_count - deal_count_1, 3)

        time.sleep(3)

        bid_req_1 = robot_fun.takeOrder('buy',
                                        deal_price_1,
                                        deal_count_1,
                                        get_basic_cfg.orderUrl,
                                        tester02_token)

        bid_req_2 = robot_fun.takeOrder('buy',
                                        deal_price_2,
                                        deal_count_2,
                                        get_basic_cfg.orderUrl,
                                        tester02_token)
        time.sleep(3)

        print("\n")
        print("Ask申报1 价格:%f 数量:%f"%(deal_price_1,deal_count_1))
        print("\n")
        print("Ask申报2 价格:%f 数量:%f"%(deal_price_2,deal_count_2))

        userId_1 = bid_req_1.json()['data']['id']
        trade_order_id_1 = robot_fun.getTradeOrderId(userId_1)
        sqlstr1 = "select close_code,close_msg from trade_order where id = %s" % trade_order_id_1

        userId_2 = bid_req_2.json()['data']['id']
        trade_order_id_2 = robot_fun.getTradeOrderId(userId_2)
        sqlstr2 = "select close_code,close_msg from trade_order where id = %s" % trade_order_id_2

        data1 = ctcdbUtil.execute(sqlstr1)
        data2 = ctcdbUtil.execute(sqlstr2)

        self.assertEqual(data1[0][0], 8001, msg="验证订单状态是否正确")
        self.assertEqual(data1[0][1], '撮合成功完成', msg="验证关闭消息是否正确")

        self.assertEqual(data2[0][0], 8001, msg="验证订单状态是否正确")
        self.assertEqual(data2[0][1], '撮合成功完成', msg="验证关闭消息是否正确")

        #获取挂单吃单手续费
        rate = robot_fun.getRate()
        maker_rate = rate[0]
        taker_rate = rate[1]

        #交易总价
        deal_amount = round(ask_1_price * ask_1_count,5)
        print("\n")
        print("交易总价:",deal_amount)
        print("\n")

        maker_change_amount = deal_amount - deal_amount * maker_rate
        taker_change_amount = ask_1_count - ask_1_count * taker_rate

        tester01_available_BTC = round(100 - ask_count_amount,3)

        tester01_reserved_BTC = round(ask_count_amount - ask_1_count,3)

        tester01_available_USDT = round(1000000 + maker_change_amount,8)

        tester02_available_BTC = round(100 + taker_change_amount,8)

        tester02_available_USDT = round(1000000 - bid_amount - deal_price_1 * deal_count_1 - deal_price_2 * deal_count_2 + (deal_price_1 - ask_1_price) * deal_count_1 + (deal_price_2 - ask_1_price) * deal_count_2,5)

        tester02_reserved_USDT = round(bid_amount,5)

        print("tester01可用btc:",tester01_available_BTC)
        print("tester01冻结btc:",tester01_reserved_BTC)
        print("tester01可用usdt:",tester01_available_USDT)
        print("tester02可用btc:",tester02_available_BTC)
        print("tester02可用usdt:",tester02_available_USDT)
        print("tester02冻结usdt:",tester02_reserved_USDT)

        tester01_BTC = ctcdbUtil.execute(get_ctcdb.search_tester01_money[0])
        tester01_USDT = ctcdbUtil.execute(get_ctcdb.search_tester01_money[1])
        tester02_BTC = ctcdbUtil.execute(get_ctcdb.search_tester02_money[0])
        tester02_USDT = ctcdbUtil.execute(get_ctcdb.search_tester02_money[1])

        self.assertEqual(float(tester01_BTC[0][0]), tester01_available_BTC, msg='验证tester01BTC的可用余额')
        self.assertEqual(float(tester01_BTC[0][1]), tester01_reserved_BTC, msg='验证tester01BTC的冻结数额')
        self.assertEqual(float(tester01_USDT[0][0]), tester01_available_USDT, msg='验证tester01USDT的可用余额')
        self.assertEqual(float(tester02_BTC[0][0]), tester02_available_BTC, msg='验证tester02BTC的可用余额')
        self.assertEqual(float(tester02_USDT[0][0]), tester02_available_USDT, msg='验证tester02USDT的可用余额')
        self.assertEqual(float(tester02_USDT[0][1]), tester02_reserved_USDT, msg='验证tester02USDT的冻结数额')

        print("\n")
        print("测试用例说明:")
        print("1.用户1挂5个ask，用户2挂5个bid，形成深度图")
        print("2.用户2挂一个bid（价格小于ask二价大于ask一价，数量小于ask一价数量），吃掉部分ask一价")
        print("3.用户2挂一个bid（价格小于ask二价大于ask一价，数量等于剩余ask一价数量），吃掉剩余ask一价")
        print("4.验证后面两次挂bid的订单状态")
        print("5.验证用户1和用户2的各货币金额")

if __name__ == '__main__':
    unittest.main()