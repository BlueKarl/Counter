#coding:utf-8
import os

#PROXY_REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
#PROXY_REDIS_PORT = os.getenv('REDIS_PORT', 6379)
#REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
#REDIS_PORT = os.getenv('REDIS_PORT', 6379)


#---------------intra----------------
#PROXY_REDIS_HOST = os.getenv('PROXY_REDIS_HOST', '10.200.8.29')
#PROXY_REDIS_PORT = os.getenv('PROXY_REDIS_PORT', 8802)
#REDIS_HOST = os.getenv('REDIS_HOST', '10.222.102.255')
#REDIS_PORT = os.getenv('REDIS_PORT', 6379)

#----------------yg------------------
PROXY_REDIS_HOST = os.getenv('PROXY_REDIS_HOST', 'redis-logcount.yg.hunantv.com')
PROXY_REDIS_PORT = os.getenv('PROXY_REDIS_PORT', 8889)
REDIS_HOST = os.getenv('REDIS_HOST', '10.21.199.249')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)

CELERY_NAME = os.getenv('CELERY_NAME','logdeal')
CELERY_BROKER_URL = 'redis://%s:%d' % (REDIS_HOST, REDIS_PORT)
CELERY_RESULT_BACKEND = 'redis://%s:%d' % (REDIS_HOST, REDIS_PORT)

SUBSCRIBE = os.getenv('SUBSCRIBE', 'ERU:LOGCOUNT')
