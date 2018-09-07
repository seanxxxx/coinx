# -*- coding:utf-8 -*-
import yaml

basic_cfg_file = open('../cfg/basic_cfg.yaml')
data_basic = yaml.load(basic_cfg_file)

#登录地址
loginUrl = data_basic['loginUrl']

#挂单地址
orderUrl = data_basic['orderUrl']

#撤单地址
cancelOrderUrl = data_basic['cancelOrderUrl']

#用户账号密码
tester01 = data_basic['count']['tester01']
tester02 = data_basic['count']['tester02']
tester03 = data_basic['count']['tester03']
tester04 = data_basic['count']['tester04']
xuxuan = data_basic['count']['xuxuan']
password = data_basic['count']['password']