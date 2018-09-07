# -*- coding:utf-8 -*-
import random,requests,logging

import time

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='ctc.log',
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


url_kline = "http://dev.zetafin.cn:22004//ctc/kline/list"
url_depth = "http://dev.zetafin.cn:22004//ctc/depth"
url_list = "http://dev.zetafin.cn:22004//ctc/trade/list"
url_statistics = "http://dev.zetafin.cn:22004//ctc/trade/statistic"

headers = {"content-type": "application/json"}

data = {
  "pageIndex": 1,
  "pageSize": 10,
  "tradePairdCode": "BTC_USDT"
}

request = requests.post(url_list, headers=headers, json=data)

print(request.text)




