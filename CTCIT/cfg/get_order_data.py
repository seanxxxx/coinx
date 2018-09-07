#-*- coding: UTF-8 -*-

import yaml

get_order_data = open('../cfg/order.yaml')
order_data = yaml.load(get_order_data)

#ask价格列表
ask_price = order_data['ask_price']

#bid价格列表
bid_price = order_data['bid_price']

#ask数量列表
ask_count = order_data['ask_count']

#bid数量列表
bid_count = order_data['bid_count']