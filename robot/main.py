# -*- coding: UTF-8 -*-

# # import os
# lsit=['python bch_btc/doTrade.py',
# 'python bch_usdt/doTrade.py',
# 'python btc_usdt/doTrade.py',
# 'python eth_btc/doTrade.py',
# 'python eth_usdt/doTrade.py',
# 'python ltc_btc/doTrade.py',
# 'python ltc_eth/doTrade.py',
# 'python ltc_usdt/doTrade.py',
# 'python xrp_btc/doTrade.py',
# 'python xrp_eth/doTrade.py',
# 'python xrp_usdt/doTrade.py']
#
#
# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# import threading
# import time
#
# import datetime
# import os
# import threading
#
#
# def execCmd(cmd):
#     try:
#         print("命令%s开始运行%s" % (cmd, datetime.datetime.now()))
#         os.system(cmd)
#         print("命令%s结束运行%s" % (cmd, datetime.datetime.now()))
#     except Exception, e:
#         print '%s\t 运行失败,失败原因\r\n%s' % (cmd, e)
#
# if __name__ == '__main__':
#     # 需要执行的命令列表
#     cmds = lsit
#
#     # 线程池
#     threads = []
#
# print("程序开始运行%s" % datetime.datetime.now())
#
# for cmd in cmds:
#     th = threading.Thread(target=execCmd, args=(cmd,))
#     th.start()
#     threads.append(th)
#
# # 等待线程运行完毕
# for th in threads:
#     th.join()
#
# print("程序结束运行%s" % datetime.datetime.now())