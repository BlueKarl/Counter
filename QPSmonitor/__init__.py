#coding:utf-8

import redis
from log import config

def redisconnect(): 
    rds = redis.Redis(host=config.PROXY_REDIS_HOST, port=config.PROXY_REDIS_PORT)
    return rds
