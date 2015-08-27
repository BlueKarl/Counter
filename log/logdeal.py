#coding:utf-8

import time
import logging
from log import celeryconnect, redisconnect

app = celeryconnect()
rds = redisconnect()

@app.task
def logcount(msg):
    main_key = "%s-%s-%s" % (msg['name'], msg['entrypoint'], msg['date'])
    timestamp = time.mktime(time.strptime(msg['datetime'], '%Y-%m-%d %H:%M:%S'))
    logging.info(main_key)
    rds.hincrby(main_key, timestamp, 1)
