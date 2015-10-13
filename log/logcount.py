#coding:utf-8

import sys
import json
import time
import redis
from log import config
from log.logdeal import logcount


def logsend(host, port):
    rds = redis.Redis(host=host, port=port)
    pub = rds.pubsub()
    pub.subscribe(config.SUBSCRIBE)
    while True:
        m = pub.get_message()
        if not m or not m.get('data'):
            continue
        data = str(m["data"])
        data_value = json.loads(data)
        if isinstance(data_value, dict):
            timestamp = time.mktime(time.strptime(data_value['datetime'], '%Y-%m-%d %H:%M:%S'))
            main_key = "%s-%s-%s" % (data_value['name'],data_value['entrypoint'], data_value['date'])
            logcount.delay(main_key, timestamp)
