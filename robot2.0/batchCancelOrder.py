#-*- coding: UTF-8 -*-

import requests

#撤单地址
url_cancelOrder = 'http://www.luckybi.io/api/ctc/order/cancel/ETH_USDT'
#url_cancelOrder = 'http://dev.zetafin.cn:22004/ctc/order/cancel/ETH_BTC'

def getTradeOrderId(userId):
    userId = str(userId)

    if ord(userId[0]) > ord('9'):
        len_offset = 10 + ord(userId[0]) - ord('A')
    else:
        len_offset = ord(userId[0]) - ord('0')

    lenth = userId.__len__() - len_offset

    return userId[1:lenth][::-1]

def cancelOrder(url_cancel,orderId,remark,access_token):
    cancel_headers = {"content-type":"application/json","access_token":access_token}
    order_data = {
        "orderId":orderId,
        "remark":remark
    }
    cancel_request = requests.post(url_cancel, headers=cancel_headers, json=order_data)
    return cancel_request

def cancelOrderWithTradePair(url_cancel,access_token):
    cancel_headers = {"content-type":"application/json","access_token":access_token}
    cancel_request = requests.get(url_cancel, headers=cancel_headers)
    return cancel_request

def changeId(userId,orderId):

    size = 12

    uid = str(userId)

    oid = str(orderId)

    uidLen = uid.__len__()

    oidLen = oid.__len__()

    cutUidLen = size - oidLen - 1

    snChars = [0] * 12

    if cutUidLen < 10:
        initChar = '0'
    else:
        initChar = 'A'

    if cutUidLen > 9:
        cutUidLen = cutUidLen - 10

    snChars[0] = (str(int(initChar) + cutUidLen))

    beginIndex = size - uidLen

    for i in range(beginIndex,beginIndex + uidLen):
        if i - beginIndex >= oidLen:
            snChars[i] = '0'
        else:
            snChars[i] = oid[i - beginIndex]

    for i in range(1,oidLen + 1):
        if i < size:
            snChars[i] = oid[oidLen - i]

    gapLen = size - (1 + oidLen + uidLen)
    if gapLen > 0:
        beginIndex = 1 + oidLen
        for i in range(beginIndex,beginIndex + gapLen):
            snChars[i] = '0'

    return str(''.join(snChars))

userId = 105

token = '6468922b-8d7d-464b-a589-81aa211bebc5'

fo = open("/Users/xuanxu/Desktop/a.txt", "r")

while True:
    content = fo.readline()
    if content == '':
        break
    content = content.strip()
    orderId = changeId(userId, content)
    #cancelRep = cancelOrder(url_cancelOrder, orderId, '深度撤单', token)
    cancelRep = cancelOrderWithTradePair(url_cancelOrder ,token)
    print cancelRep.text
    break
fo.close()
