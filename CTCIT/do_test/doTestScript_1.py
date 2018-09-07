# -*- coding: utf-8 -*-
import unittest
from CTCIT.do_test.ask_bid_order import TestAskBidOrder
from CTCIT.do_test.cancel_order import TestCancelOrder
from CTCIT.public.HTMLTestRunner import HTMLTestRunner
from CTCIT.do_test.ask_eat_part import TestAskEatBidTrade
from CTCIT.do_test.ask_eat_all import TestAskEatBidAllTrade
from CTCIT.do_test.ask_eat_allpart import TestAskEatBidAllPartTrade
from CTCIT.do_test.ask_eat_upwall import TestAskEatupWallTrade
from CTCIT.do_test.bid_eat_part import TestBidEatAskTrade
from CTCIT.do_test.bid_eat_all import TestBidEatAskAllTrade
from CTCIT.do_test.bid_eat_allpart import TestBidEatAskAllPartTrade
from CTCIT.do_test.bid_eat_upwall import TestBidEatupWallTrade
from CTCIT.do_test.two_ask_eat_one_bid import TestTwoAskEatOneBidTrade
from CTCIT.do_test.two_bid_eat_one_ask import TestTwoBidEatOneAskTrade
from CTCIT.do_test.ask_eat_bid_cancelbid import TestAskEatBidCancelBidTrade
from CTCIT.do_test.bid_eat_ask_cancelask import TestBidEatAskCancelAskTrade
from CTCIT.do_test.ask_eat_bid_cancelask import TestAskEatBidCancelAskTrade
from CTCIT.do_test.bid_eat_ask_cancelbid import TestBidEatAskCancelBidTrade

if __name__ == '__main__':

    suite = unittest.TestSuite()

    # test_ask_bid_order = [TestAskBidOrder("askOrder"),
                          # TestAskBidOrder("bidOrder"),
                          # TestAskBidOrder("askBatchOrder"),
                          # TestAskBidOrder("bidBatchOrder")]

    # test_cancel_order = [TestCancelOrder("cancelAskOrder"),
    #                      TestCancelOrder("cancelBidOrder")]

    test_ask_eat_part_trade = [TestAskEatBidTrade("takePart")]
    # test_ask_eat_all_trade = [TestAskEatBidAllTrade("takeAll")]
    # test_ask_eat_all_part_trade = [TestAskEatBidAllPartTrade("takeAllPart")]
    # test_ask_eat_upwall = [TestAskEatupWallTrade("takeAllupWall")]
    test_bid_eat_part_trade = [TestBidEatAskTrade("takePart")]
    # test_bid_eat_all_trade = [TestBidEatAskAllTrade("takeAll")]
    # test_bid_eat_all_part_trade = [TestBidEatAskAllPartTrade("takeAllPart")]
    # test_bid_eat_upwall = [TestBidEatupWallTrade("takeAllupWall")]
    # test_two_ask_eat_one_bid = [TestTwoAskEatOneBidTrade("twoAskEatOnebid")]
    # test_two_bid_eat_one_ask = [TestTwoBidEatOneAskTrade("twoBidEatOneAsk")]
    # test_ask_eat_bid_cancelbid = [TestAskEatBidCancelBidTrade("askBidCancelBid")]
    # test_bid_eat_ask_cancelask = [TestBidEatAskCancelAskTrade("bidAskCancelAsk")]
    # test_ask_eat_bid_cancelask = [TestAskEatBidCancelAskTrade("askBidCancelAsk")]
    # test_bid_eat_ask_cancelbid = [TestBidEatAskCancelBidTrade("bidAskCancelBid")]


    # suite.addTests(test_ask_bid_order)
    # suite.addTests(test_cancel_order)
    suite.addTests(test_ask_eat_part_trade)
    # suite.addTests(test_ask_eat_all_trade)
    # suite.addTests(test_ask_eat_all_part_trade)
    # suite.addTests(test_ask_eat_upwall)
    suite.addTests(test_bid_eat_part_trade)
    # suite.addTests(test_bid_eat_all_trade)
    # suite.addTests(test_bid_eat_all_part_trade)
    # suite.addTests(test_bid_eat_upwall)
    # suite.addTests(test_two_ask_eat_one_bid)
    # suite.addTests(test_two_bid_eat_one_ask)
    # suite.addTests(test_ask_eat_bid_cancelbid)
    # suite.addTests(test_bid_eat_ask_cancelask)
    # suite.addTests(test_ask_eat_bid_cancelask)
    # suite.addTests(test_bid_eat_ask_cancelbid)

    with open('HTMLReport.html', 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='数字货币交易系统测试报告',
                                description='该报告使用HTMLTestRunner输出',
                                verbosity=2
                                )
        runner.run(suite)