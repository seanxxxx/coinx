from django.shortcuts import render
from public import dbUtil, robot_fun
import yaml
from public import robot_fun

from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
# Create your views here.

#登录地址
loginUrl = 'http://dev.zetafin.cn:22005/auth/login/test'

#挂单地址
orderUrl = 'http://dev.zetafin.cn:22004/ctc/order'

#撤单地址
cancel_order = 'http://dev.zetafin.cn:22004/ctc/order/cancel/test'

def index(request):
    f = open('config/ctcdb.yaml')
    data = yaml.load(f)
    a1 = dbUtil.execute(data['btc_usdt'][0])
    a2 = dbUtil.execute(data['btc_usdt'][1])
    a3 = dbUtil.execute(data['btc_usdt'][2])
    a4 = dbUtil.execute(data['btc_usdt'][3])

    b1 = dbUtil.execute(data['eth_usdt'][0])
    b2 = dbUtil.execute(data['eth_usdt'][1])
    b3 = dbUtil.execute(data['eth_usdt'][2])
    b4 = dbUtil.execute(data['eth_usdt'][3])

    c1 = dbUtil.execute(data['bch_usdt'][0])
    c2 = dbUtil.execute(data['bch_usdt'][1])
    c3 = dbUtil.execute(data['bch_usdt'][2])
    c4 = dbUtil.execute(data['bch_usdt'][3])

    d1 = dbUtil.execute(data['ltc_usdt'][0])
    d2 = dbUtil.execute(data['ltc_usdt'][1])
    d3 = dbUtil.execute(data['ltc_usdt'][2])
    d4 = dbUtil.execute(data['ltc_usdt'][3])

    e1 = dbUtil.execute(data['eth_btc'][0])
    e2 = dbUtil.execute(data['eth_btc'][1])
    e3 = dbUtil.execute(data['eth_btc'][2])
    e4 = dbUtil.execute(data['eth_btc'][3])

    f1 = dbUtil.execute(data['bch_btc'][0])
    f2 = dbUtil.execute(data['bch_btc'][1])
    f3 = dbUtil.execute(data['bch_btc'][2])
    f4 = dbUtil.execute(data['bch_btc'][3])

    g1 = dbUtil.execute(data['ltc_btc'][0])
    g2 = dbUtil.execute(data['ltc_btc'][1])
    g3 = dbUtil.execute(data['ltc_btc'][2])
    g4 = dbUtil.execute(data['ltc_btc'][3])

    h1 = dbUtil.execute(data['ltc_eth'][0])
    h2 = dbUtil.execute(data['ltc_eth'][1])
    h3 = dbUtil.execute(data['ltc_eth'][2])
    h4 = dbUtil.execute(data['ltc_eth'][3])

    return render(request,'index.html',{'a1':round(a1[0][0],6),
                                        'a2':round(a2[0][0],6),
                                        'a3':round(a3[0][0],6),
                                        # 'a4':round(a4[0][0],6),
                                        'b1': round(b1[0][0], 6),
                                        'b2': round(b2[0][0], 6),
                                        'b3': round(b3[0][0], 6),
                                        # 'b4': round(b4[0][0], 6),
                                        'c1': round(c1[0][0], 6),
                                        'c2': round(c2[0][0], 6),
                                        'c3': round(c3[0][0], 6),
                                        # 'c4': round(c4[0][0], 6),
                                        'd1': round(d1[0][0], 6),
                                        'd2': round(d2[0][0], 6),
                                        'd3': round(d3[0][0], 6),
                                        # 'd4': round(d4[0][0], 6),
                                        'e1': round(e1[0][0], 6),
                                        'e2': round(e2[0][0], 6),
                                        'e3': round(e3[0][0], 6),
                                        # 'e4': round(e4[0][0], 6),
                                        'f1': round(f1[0][0], 6),
                                        'f2': round(f2[0][0], 6),
                                        'f3': round(f3[0][0], 6),
                                        # 'f4': round(f4[0][0], 6),
                                        'g1': round(g1[0][0], 6),
                                        'g2': round(g2[0][0], 6),
                                        'g3': round(g3[0][0], 6),
                                        # 'g4': round(g4[0][0], 6),
                                        'h1': round(h1[0][0], 6),
                                        'h2': round(h2[0][0], 6),
                                        'h3': round(h3[0][0], 6),
                                        # 'h4': round(h4[0][0], 6),
                                        })

#访问订单处理页面
def order(request):
    return render(request,'order.html')

#挂单
def takeOrder(request):

    email = request.POST.get('inputEmail')
    password = request.POST.get('inputPassword')
    orderType = request.POST.get('inputBS')
    price = request.POST.get('inputPrice')
    count = request.POST.get('inputCount')

    if email != '' and password != '' and orderUrl != '' and price != '' and count != '':
        token = robot_fun.get_access_token(loginUrl, email, password)
        robot_fun.takeOrder(orderType,price,count,orderUrl,token)
        return render(request,
                      'order.html',
                      {'msg': '挂单成功!',
                       'email': email.split('@')[0],
                       'orderType': orderType,
                       'price': price,
                       'count': count})
    else:
        return render(request,'order.html',{'msg':'请填写完整!'})

#撤单
def cancelOrder(request):

    email = request.POST.get('email')
    password = request.POST.get('password')
    orderId = request.POST.get('orderId')
    remark = request.POST.get('remark')

    if email != '' and password != '' and orderId != '' and remark != '':
        token = robot_fun.get_access_token(loginUrl, email, password)
        robot_fun.cancelOrder(cancel_order,orderId,remark,token)
        return render(request,
                      'order.html',
                      {'cancelmsg': '撤单成功!'})
    else:
        return render(request,'order.html',{'cancelmsg':'请填写完整!'})
