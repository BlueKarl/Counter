#coding:utf-8

import json
from QPSmonitor import redisconnect

rds = redisconnect()

def search(args):
    date=[]
    number=[]
    data = rds.hgetall(args)
    sorteddata = sorted(data.keys())
    for key in sorteddata:
        date.append(float(key))
        number.append(data[key])
    return json.dumps(date), json.dumps(number)
