#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Time: 2020/11/10 2:47 下午
# Author: K
import json

#
# j = '{\"minUnit\":0.1,\"count\":10,\"enabled\":1,\"yy_time\":\"2020-11-10T17:35\"}'
# data = json.loads(j)
# yy_time = data.get('yy_time')
# yy_time = yy_time.replace('T',' ')
# print(yy_time)
# # ts = time.strptime(yy_time, "%Y-%m-%d %H:%M:%S")


# print(ts)
import time


dt = "2017-09-20T22:28"
a = 12
if a:
    print(a)

exit()
dt = dt.replace('T', ' ')
timeArray = time.strptime(dt, "%Y-%m-%d %H:%M")

print(timeArray)
timestamp = int(time.mktime(timeArray))
print(timestamp)

print(int(time.time()))

exit()
# 转换为时间数组
timeArray = time.strptime(dt, "%Y-%m-%d %H%M%S")
# 转换为时间戳
timestamp = time.mktime(timeArray)

print(timeArray)
print(timestamp)
