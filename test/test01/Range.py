#!/usr/bin/python
# -*- coding: UTF-8 -*-

fo = open("/Users/xuanxu/Desktop/a.txt", "r")
while True:
    content = fo.readline()
    print(content)
    if content == '':
        break
    content = content.strip().split()
fo.close()