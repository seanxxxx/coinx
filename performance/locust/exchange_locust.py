import json
import time
import datetime
import random

from locust import HttpLocust, TaskSet, task

class UserBehaviorExchange(TaskSet):

    def on_start(self):
        print('开始性能测试...')
        pass

#1表示一个Locust实例被挑选执行的权重
    @task(1)
    def kline(self):
        url_kline = "/ctc/kline/list"

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'}

        t = time.time()

        end = int(round(t * 1000))
        beg = end - 30000000

        pairList = ['BTC_USDT','ETH_USDT','ETH_BTC']
        tradePair = pairList[random.randint(0,2)]

        data = {
            "content-type": "application/json",
            "eosDateBeg": beg,
            "eosDateEnd": end,
            "pageIndex": 1,
            "pageSize": 500,
            "periodCode": "1min",
            "symbol": tradePair
        }

        response_kline = self.client.post(url_kline,data=json.dumps(data),headers=headers,name='K线图')
        print("K线接口数据---%s" % response_kline.json()['msg'])

    @task(12)
    def depListStat(self):
        pairList = ['BTC_USDT','ETH_USDT','ETH_BTC']
        tradePair = pairList[random.randint(0,2)]
        url_refresh= "/ctc/exchange/refresh"+"?tradePair="+tradePair
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'}

        response_refresh = self.client.get(url_refresh, headers=headers, name='深度数据')

        print("refresh接口数据---%s" % response_refresh.json()['msg'])

class WebsiteUserExchange(HttpLocust):
    weight = 1
    task_set = UserBehaviorExchange
    host = "http://www.luckybi.io/api"
    min_wait = 1700
    max_wait = 1800