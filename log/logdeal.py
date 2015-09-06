#coding:utf-8

from log import redisconnect, celeryconnect
from log import config

app = celeryconnect()
rds = redisconnect()

@app.task
def logcount(main_key, timestamp):
    rds.hincrby(main_key, timestamp, 1)
