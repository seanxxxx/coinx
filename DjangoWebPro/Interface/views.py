from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from DjangoWebPro.APITest import robot_fun
import logging
# Create your views here.

#登录地址
loginUrl = 'http://dev.zetafin.cn:22005/auth/login/test'

#挂单地址
orderUrl = 'http://dev.zetafin.cn:22004/ctc/order'

#撤单地址
cancel_order = 'http://dev.zetafin.cn:22004/ctc/order/cancel/test'

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='coinx.log',
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

def login_action(request):
    return -1

def index(request):
    return render(request,'index.html')

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
