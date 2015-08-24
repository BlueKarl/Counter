import os

REDIS_HOST = os.getenv('REDIS_HOST', 'redis-logcount.yg.hunantv.com')
REDIS_PORT = os.getenv('REDIS_PORT', 8889)
#REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
#REDIS_PORT = os.getenv('REDIS_PORT', 6379)

CELERY_NAME = os.getenv('CELERY_NAME','logdeal')
CELERY_BROKER_URL = 'redis://%s:%d' % (REDIS_HOST, REDIS_PORT)
CELERY_RESULT_BACKEND = 'redis://%s:%d' % (REDIS_HOST, REDIS_PORT)

SUBSCRIBE = os.getenv('SUBSCRIBE', 'ERU:LOGCOUNT')
