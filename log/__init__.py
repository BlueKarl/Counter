#coding:utf-8

import redis
#from celery import Celery

from log import config

#def celeryconnect():
#    print "**********",config.CELERY_BROKER_URL
#    app = Celery(config.CELERY_NAME, broker=config.CELERY_BROKER_URL)
#    return app

def redisconnect():
    print "**********",config.REDIS_HOST,config.REDIS_PORT
    pool = redis.ConnectionPool(host=config.REDIS_HOST, port=config.REDIS_PORT)
    rds = redis.Redis(connection_pool=pool)
    return rds
