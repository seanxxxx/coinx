# -*- coding: utf-8 -*-

import unittest
from untest01 import TestMathFunc
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':

    suite = unittest.TestSuite()

    tests = [TestMathFunc("test_add"),
             TestMathFunc("test_minus"),
             TestMathFunc("test_divide"),
             TestMathFunc("test_multi")]

    suite.addTests(tests)

    with open('HTMLReport.html', 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='数字货币交易系统测试报告',
                                description='generated by HTMLTestRunner.',
                                verbosity=2
                                )
        runner.run(suite)