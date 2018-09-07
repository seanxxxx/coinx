import json
import logging
import random
import time
import datetime
import requests
from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    def on_start(self):
        pass

#1表示一个Locust实例被挑选执行的权重
    @task(4)
    def kline(self):
        url_kline = "/ctc/kline/list"

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'}
        beg = int(time.mktime(datetime.date.today().timetuple()))
        end = int(time.mktime(datetime.date.today().timetuple())) + 86399
        data = {
            "content-type": "application/json",
            "eosDateBeg": beg * 1000,
            "eosDateEnd": end * 1000,
            "pageIndex": 1,
            "pageSize": 500,
            "periodCode": "1min",
            "symbol": "BTC_USDT"
        }

        response = self.client.post(url_kline,data=json.dumps(data),headers=headers)
        print("K线接口数据---%s" % response.json()['msg'])

    @task(12)
    def depListStat(self):
        url_depth = "/ctc/depth"
        url_list = "/ctc/trade/list"
        url_statistics = "/ctc/trade/statistics"

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'}

        data_markdepth = {
            "pageIndex": 1,
            "pageSize": 50,
            "tradePairCode": "BTC_USDT"
        }

        data_list = {
            "pageIndex": 1,
            "pageSize": 10,
            "tradePairdCode": "BTC_USDT"
        }

        data_statistics = {
            "timeJump": 24,
            "tradePairCode": "BTC_USDT"
        }

        response_depth_1 = self.client.post(url_depth, data=json.dumps(data_markdepth), headers=headers)
        response_depth_2 = self.client.post(url_depth, data=json.dumps(data_markdepth), headers=headers)
        response_list = self.client.post(url_list, data=json.dumps(data_list), headers=headers)
        response_statistics = self.client.post(url_statistics, data=json.dumps(data_statistics), headers=headers)

        print("depth1数据---%s" % response_depth_1.json()['msg'])
        print("depth2数据---%s" % response_depth_2.json()['msg'])
        print("list数据---%s" % response_list.json()['msg'])
        print("statistics数据---%s" % response_statistics.json()['msg'])

    @staticmethod
    def get_token_1():
        url_login = 'http://dev.zetafin.cn:22005/auth/login/test'
        username = "tester01@lanlingdai.net"
        password = "123456Aa"
        headers = {"content-type": "application/json"}
        login_data = {"email": username, "password": password}
        login_request = requests.post(url_login, headers=headers, json=login_data)
        access_token = login_request.json()['data']['access_token']
        print("%s:请求/login接口" % username)
        print("token:" + access_token)
        return access_token

    @staticmethod
    def get_token_2():
        url_login = 'http://dev.zetafin.cn:22005/auth/login/test'
        username = "tester02@lanlingdai.net"
        password = "123456Aa"
        headers = {"content-type": "application/json"}
        login_data = {"email": username, "password": password}
        login_request = requests.post(url_login, headers=headers, json=login_data)
        access_token = login_request.json()['data']['access_token']
        print("%s:请求/login接口" % username)
        print("token:"+access_token)
        return access_token

    @task(3)
    def takeOrder_ask(self):
        url_order = '/ctc/order'
        access_token = self.get_token_1()
        price = round(random.uniform(7000.00,9000.00),2)
        count = round(random.uniform(0.001,5.000),3)
        chip_order_headers = {"content-type": "application/json", "access_token": access_token}
        order_data = {
            "direction": 'S',
            "orderType": '200',
            "price": price,
            "count": count,
            "tradePairCode": "btc_usdt"
        }
        request = self.client.post(url_order, headers=chip_order_headers, data=json.dumps(order_data))
        print("tester01挂卖单的价格:%s 挂卖单的数量:%s"
                     % (price, count) + " 状态:" + request.json()['msg'])

    @task(3)
    def takeOrder_buy(self):
        url_order = '/ctc/order'
        access_token = self.get_token_2()
        price = round(random.uniform(7000.00,9000.00),2)
        count = round(random.uniform(0.001,5.000),3)
        chip_order_headers = {"content-type": "application/json", "access_token": access_token}
        order_data = {
            "direction": 'B',
            "orderType": '200',
            "price": price,
            "count": count,
            "tradePairCode": "btc_usdt"
        }
        request = self.client.post(url_order, headers=chip_order_headers, data=json.dumps(order_data))
        print("tester02挂买单的价格:%s 挂买单的数量:%s"
                     % (price, count) + " 状态:" + request.json()['msg'])

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = "http://dev.zetafin.cn:22004"
    min_wait = 1800
    max_wait = 1900