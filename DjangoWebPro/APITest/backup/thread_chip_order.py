from DjangoWebPro.APITest.backup import trade_fun
import threading


#登录地址
url_login = 'http://dev.zetafin.cn:22005/auth/login'
#挂单地址
url_order = 'http://dev.zetafin.cn:22004/ctc/order'
#用户账号密码
user1 = 'zhoujiayi@lanlingdai.net'
password1 = '123456'

user2 = 'xuxuan@lanlingdai.net'
password2 = '123456'

#递增趋势比例
addrate = [3,5,47,10,20,30,70,500,500,500]
#递减趋势比例
minusrate = [3,5,47,10,20,30,70,500,500,500]
#交易价格
price = 7000
#价格递增率
add_range = 0.015
#价格递减率
minus_range = 0.015
#设置偏移量
price_offset = 100

# #递增趋势比例
# addrate = [3,5,7,9,10,17,23,50,300,50]
# #递减趋势比例
# minusrate = [1,7,9,10,17,23,25,50,300,50]
# #交易价格
# price = 7000
# #价格递增率
# add_range = 0.015
# #价格递减率
# minus_range = 0.015
# #设置偏移量
# price_offset = 100

def user_chip_order(email,password):
    access_token = trade_fun.get_access_token(url_login, email, password)
    #两个账号分别执行买卖挂单，根据偏移量进行撮合
    while 1:
        if email == 'zhoujiayi@lanlingdai.net':
            cobu_re = trade_fun.chip_order_buy_up(email.split('@')[0], price - price_offset, add_range, addrate, url_order, access_token)
            cobd_re = trade_fun.chip_order_buy_down(email.split('@')[0], price + price_offset, minus_range, minusrate, url_order, access_token)
            if cobd_re.json()['msg'] == 'AccessToken已过期':
                access_token = trade_fun.get_access_token(url_login, email, password)
        if email == 'xuxuan@lanlingdai.net':
            cosd_re = trade_fun.chip_order_sell_down(email.split('@')[0], price + price_offset, minus_range, minusrate, url_order, access_token)
            cosu_re = trade_fun.chip_order_sell_up(email.split('@')[0], price - price_offset, add_range, addrate, url_order, access_token)
            if cosu_re.json()['msg'] == 'AccessToken已过期':
                access_token = trade_fun.get_access_token(url_login, email, password)


#     #每个账号执行四种价格区间的买卖挂单
# def user_chip_order(email,password):
#     access_token = trade_fun.get_access_token(url_login, email, password)
#     while 1:
#         logging.info("******** 当前用户: %s ********" % email)
#         cobu_re = trade_fun.chip_order_buy_up(email.split('@')[0],price-price_offset, add_range, addrate, url_order, access_token)
#         cosu_re = trade_fun.chip_order_sell_up(email.split('@')[0],price-price_offset, add_range,addrate,url_order,access_token)
#         cobd_re = trade_fun.chip_order_buy_down(email.split('@')[0],price+price_offset, minus_range, minusrate, url_order, access_token)
#         cosd_re = trade_fun.chip_order_sell_down(email.split('@')[0],price+price_offset, minus_range, minusrate, url_order, access_token)
#
#         #重新获取token
#         if cosd_re.json()['msg'] == 'AccessToken已过期':
#             access_token = trade_fun.get_access_token(url_login,email,password)
#         #time.sleep(1)

user1_threading = threading.Thread(target=user_chip_order,
                                   args=(user1, password1))

user2_threading = threading.Thread(target=user_chip_order,
                                   args=(user2, password2))

user1_threading.start()
user2_threading.start()

user1_threading.join()
user2_threading.join()