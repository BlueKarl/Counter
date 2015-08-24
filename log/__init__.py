#coding:utf-8

import redis
from celery import Celery

from log import config

def celeryconnect():
    app = Celery(config.CELERY_NAME, broker=config.CELERY_BROKER_URL)
    return app

def redisconnect():
    pool = redis.ConnectionPool(host=config.REDIS_HOST, port=config.REDIS_PORT)
    rds = redis.Redis(connection_pool=pool)
    return rds
