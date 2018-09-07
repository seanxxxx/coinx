# -*- coding:utf-8 -*-
from DjangoWebPro.APITest.backup import trade_fun

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

n1=0
n2=0
n3=0
n4=0
n5=0
n6=0
n7=0
n8=0
n9=0
n10=0

m1=0
m2=0
m3=0
m4=0
m5=0
m6=0
m7=0
m8=0
m9=0
m10=0

uplist = trade_fun.increment_price(price - price_offset, add_range)
print(uplist)

downlist = trade_fun.decrement_price(price + price_offset, minus_range)
print(downlist)

for i in range(1,100000):
    number = trade_fun.get_random_addprice(price - price_offset, add_range, addrate)

    if number>uplist[0] and number<uplist[1]:
        n1 += 1
    if number>uplist[1] and number<uplist[2]:
        n2 += 1
    if number>uplist[2] and number<uplist[3]:
        n3 += 1
    if number>uplist[3] and number<uplist[4]:
        n4 += 1
    if number>uplist[4] and number<uplist[5]:
        n5 += 1
    if number>uplist[5] and number<uplist[6]:
        n6 += 1
    if number>uplist[6] and number<uplist[7]:
        n7 += 1
    if number>uplist[7] and number<uplist[8]:
        n8 += 1
    if number>uplist[8] and number<uplist[9]:
        n9 += 1
    if number>uplist[9] and number<uplist[10]:
        n10 += 1

print("####################################")

for i in range(1,100000):
    number = trade_fun.get_random_minusprice(price + price_offset, minus_range, minusrate)

    if number>downlist[1] and number<downlist[0]:
        m1 += 1
    if number>downlist[2] and number<downlist[1]:
        m2 += 1
    if number>downlist[3] and number<downlist[2]:
        m3 += 1
    if number>downlist[4] and number<downlist[3]:
        m4 += 1
    if number>downlist[5] and number<downlist[4]:
        m5 += 1
    if number>downlist[6] and number<downlist[5]:
        m6 += 1
    if number>downlist[7] and number<downlist[6]:
        m7 += 1
    if number>downlist[8] and number<downlist[7]:
        m8 += 1
    if number>downlist[9] and number<downlist[8]:
        m9 += 1
    if number>downlist[10] and number<downlist[9]:
        m10 += 1

print(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10)
print(m1,m2,m3,m4,m5,m6,m7,m8,m9,m10)