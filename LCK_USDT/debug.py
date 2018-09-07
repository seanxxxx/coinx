import random
from LCK_USDT import robot_fun

price = robot_fun.getMarketPrice('https://www.bitstamp.net/api/ticker/')
price2 = float(price) / 7000.0
print("price2:",price2)
print(random.uniform(7000.0,7500.0))

def getPrice(lastPrice):
    minusNum = (lastPrice-lastPrice*random.uniform(0.0001,0.001))/7000.0
    addNum = (lastPrice+lastPrice*random.uniform(0.0001,0.001))/7000.0
    price = round(random.uniform(minusNum,addNum),2)
    print("当前获取的价格区间是:[%f,%f]" % (minusNum,addNum))
    return price


