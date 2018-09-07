#-*- coding: UTF-8 -*-

import unittest, logging, random
from CTCIT.cfg import get_basic_cfg
from CTCIT.public import robot_fun
from CTCIT.util import ctcdbUtil
from CTCIT.cfg import get_ctcdb

class TestCancelOrder(unittest.TestCase):
    """用户撤单测试"""

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

    def cancelAskOrder(self):
        """撤销tester01卖单"""
        ask_price = round(random.uniform(6900, 7100), 2)
        ask_count = round(random.uniform(0.001, 5.000), 3)
        token = robot_fun.get_access_token(get_basic_cfg.loginUrl,
                                           get_basic_cfg.tester01,
                                           get_basic_cfg.password)
        ask_req = robot_fun.takeOrder('sell', ask_price, ask_count, get_basic_cfg.orderUrl, token)
        #time.sleep(3)
        userId = ask_req.json()['data']['id']
        order_id = robot_fun.getTradeOrderId(userId)

        cancel_req = robot_fun.cancelOrder(get_basic_cfg.cancelOrderUrl,
                                           order_id,
                                           "remark",
                                           token)
        sqlstr = "select status from trade_order where id = %s" %order_id
        data = ctcdbUtil.execute(sqlstr)
        self.assertEqual(data[0][0],9000,msg="验证订单状态是否正确")
        self.assertEqual(cancel_req.json()['msg'],'success',msg="验证是否撤单成功")
        print("订单id：%s\n订单price：%f\n订单数量：%f"%(order_id,ask_price,ask_count))

        print("\n")
        print("测试用例说明:")
        print("1.用户1申报1个Ask单")
        print("2.用户1撤单")
        print("3.验证订单状态和返回的msg")

    def cancelBidOrder(self):
        """撤销tester02买单"""
        bid_price = round(random.uniform(6900, 7100), 2)
        bid_count = round(random.uniform(0.001, 5.000), 3)
        token = robot_fun.get_access_token(get_basic_cfg.loginUrl,
                                           get_basic_cfg.tester02,
                                           get_basic_cfg.password)
        bid_req = robot_fun.takeOrder('buy', bid_price, bid_count, get_basic_cfg.orderUrl, token)
        #time.sleep(3)
        userId = bid_req.json()['data']['id']
        order_id = robot_fun.getTradeOrderId(userId)
        cancel_req = robot_fun.cancelOrder(get_basic_cfg.cancelOrderUrl,
                                           order_id,
                                           "remark",
                                           token)
        sqlstr = "select status from trade_order where id = %s" % order_id
        data = ctcdbUtil.execute(sqlstr)
        self.assertEqual(data[0][0], 9000, msg="验证订单状态是否正确")
        self.assertEqual(cancel_req.json()['msg'], 'success', msg="验证是否撤单成功")
        print("订单id：%s\n订单price：%f\n订单数量：%f" % (order_id, bid_price, bid_count))

        print("\n")
        print("测试用例说明:")
        print("1.用户2申报1个bid单")
        print("2.用户2撤单")
        print("3.验证订单状态和返回的msg")

if __name__ == '__main__':
    unittest.main()