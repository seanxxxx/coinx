# -*- coding:utf-8 -*-
import requests
import datetime
import time
import logging
import traceback
from retrying import retry

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='log.log',
                    filemode='w')

# 定义一个Handler打印INFO及以上级别的日志到sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# 设置日志打印格式
#format='%(asctime)s - %(levelname)s: %(message)s'
formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
console.setFormatter(formatter)
# 将定义好的console日志handler添加到root logger
logging.getLogger('').addHandler(console)

url='https://api.coinmarketcap.com/v2/ticker/1/?convert=usdt'
@retry
def getprice():
    while 1:
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            req = requests.get(url)
            res = req.json()['data']['quotes']['USDT']['price']
            info=u'%s返回值:%s'%(nowTime,res)
            logging.info(info)
        except Exception, e:
    # format_exc()返回字符串，print_exc()则直接给打印出来
            traceback.print_exc()
            logging.warning("exec failed, failed msg:" + traceback.format_exc())
        time.sleep(2)

getprice()