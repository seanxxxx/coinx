#-*- coding: UTF-8 -*-

import unittest, logging, random
from CTCIT.cfg import get_basic_cfg
from CTCIT.public import robot_fun
from CTCIT.util import ctcdbUtil
from CTCIT.cfg import get_ctcdb

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='ctc.log',
                    filemode='w')

# 定义一个Handler打印INFO及以上级别的日志到sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# 设置日志打印格式
# format='%(asctime)s - %(levelname)s: %(message)s'
formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
console.setFormatter(formatter)
# 将定义好的console日志handler添加到root logger
logging.getLogger('').addHandler(console)


class TestAskBidOrder(unittest.TestCase):
    """用户挂单测试"""

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

    def askOrder(self):
        """tester01挂卖单"""
        ask_price = round(random.uniform(6900, 7100), 2)
        ask_count = round(random.uniform(0.001, 5.000), 3)
        token = robot_fun.get_access_token(get_basic_cfg.loginUrl,
                                           get_basic_cfg.tester01,
                                           get_basic_cfg.password)
        req = robot_fun.takeOrder('sell', ask_price, ask_count, get_basic_cfg.orderUrl, token)
        print(req)
        data = ctcdbUtil.execute(get_ctcdb.search_tester01_money[0])
        self.assertEqual(float(data[0][0]), round((100.000-ask_count),3), msg='验证BTC可用余额')
        self.assertEqual(float(data[0][1]), round(ask_count,3), msg='验证BTC冻结金额')
        self.assertEqual(req.json()['msg'], 'success', msg='验证挂卖单是否成功')
        order_id = req.json()['data']['id']
        print("订单id：%d\n订单price：%f\n订单数量：%f" % (order_id, ask_price, ask_count))

        print("\n")
        print("测试用例说明:")
        print("1.用户申报一个Ask单")
        print("2.验证BTC可用余额")
        print("3.验证BTC冻结金额")
        print("4.验证挂单请求返回的msg")

    def bidOrder(self):
        """tester02挂买单"""
        bid_price = round(random.uniform(6900, 7100), 2)
        bid_count = round(random.uniform(0.001, 5.000), 3)
        token = robot_fun.get_access_token(get_basic_cfg.loginUrl,
                                           get_basic_cfg.tester02,
                                           get_basic_cfg.password)
        req = robot_fun.takeOrder('buy', bid_price, bid_count, get_basic_cfg.orderUrl, token)
        data = ctcdbUtil.execute(get_ctcdb.search_tester02_money[1])
        self.assertEqual(float(data[0][0]), round((1000000.00000-bid_price*bid_count),5), msg='验证USDT可用余额')
        self.assertEqual(float(data[0][1]), round(bid_price*bid_count,5), msg='验证USDT冻结数额')
        self.assertEqual(req.json()['msg'], 'success', msg='验证挂买单是否成功')
        order_id = req.json()['data']['id']
        print("订单id：%d\n订单price：%f\n订单数量：%f" % (order_id, bid_price, bid_count))

        print("\n")
        print("测试用例说明:")
        print("1.用户申报一个Bid单")
        print("2.验证BTC可用余额")
        print("3.验证BTC冻结金额")
        print("4.验证挂单请求返回的msg")

    def askBatchOrder(self):
        """tester01批量挂卖单"""
        token = robot_fun.get_access_token(get_basic_cfg.loginUrl,
                                           get_basic_cfg.tester01,
                                           get_basic_cfg.password)
        count_amount = 0
        USDT_amount = 0
        for i in range(10):
            ask_price = round(random.uniform(6900, 7100), 2)
            ask_count = round(random.uniform(0.001, 5.000), 3)
            req = robot_fun.takeOrder('sell',
                                      ask_price,
                                      ask_count,
                                      get_basic_cfg.orderUrl,
                                      token)
            self.assertEqual(req.json()['msg'], 'success', msg='验证挂买单是否成功')
            USDT_amount = float(USDT_amount + ask_price*ask_count)
            count_amount = float(count_amount + ask_count)
            order_id = req.json()['data']['id']
            print("订单id：%d\n订单price：%f\n订单数量：%f" % (order_id, ask_price, ask_count))
        data = ctcdbUtil.execute(get_ctcdb.search_tester01_money[0])
        self.assertEqual(float(data[0][0]), round((100.000-count_amount),3), msg='验证BTC可用余额')
        self.assertEqual(float(data[0][1]), round(count_amount,3), msg='验证BTC冻结数额')

        print("\n")
        print("测试用例说明:")
        print("1.用户申报10个Ask单")
        print("2.验证BTC可用余额")
        print("3.验证BTC冻结金额")
        print("4.验证挂单请求返回的msg")

    def bidBatchOrder(self):
        """tester02批量挂买单"""
        token = robot_fun.get_access_token(get_basic_cfg.loginUrl,
                                           get_basic_cfg.tester02,
                                           get_basic_cfg.password)
        count_amount = 0
        USDT_amount = 0
        for i in range(10):
            bid_price = round(random.uniform(6900, 7100), 2)
            bid_count = round(random.uniform(0.001, 5.000), 3)
            req = robot_fun.takeOrder('buy',
                                      bid_price,
                                      bid_count,
                                      get_basic_cfg.orderUrl,
                                      token)
            self.assertEqual(req.json()['msg'], 'success', msg='验证挂买单是否成功')
            USDT_amount = USDT_amount + bid_price*bid_count
            count_amount = count_amount + bid_count
            order_id = req.json()['data']['id']
            print("订单id：%d\n订单price：%f\n订单数量：%f" % (order_id, bid_price, bid_count))
        data = ctcdbUtil.execute(get_ctcdb.search_tester02_money[1])
        self.assertEqual(float(data[0][0]), round((1000000.00000-USDT_amount),5), msg='验证USDT可用余额')
        self.assertEqual(float(data[0][1]), round(USDT_amount,5), msg='验证USDT冻结数额')

        print("\n")
        print("测试用例说明:")
        print("1.用户申报10个Bid单")
        print("2.验证BTC可用余额")
        print("3.验证BTC冻结金额")
        print("4.验证挂单请求返回的msg")

if __name__ == '__main__':
    unittest.main()
