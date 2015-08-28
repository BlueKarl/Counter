import os
#PROXY_REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
#PROXY_REDIS_PORT = os.getenv('REDIS_PORT', 6379)
#REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
#REDIS_PORT = os.getenv('REDIS_PORT', 6379)

#PROXY_REDIS_HOST = os.getenv('REDIS_HOST', '10.200.8.29')
REDIS_HOST = os.getenv('REDIS_HOST', '10.222.102.255')
#PROXY_REDIS_PORT = os.getenv('REDIS_PORT', 8802)
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
#REDIS_HOST = os.getenv('REDIS_HOST', '10.222.46.215')
#REDIS_PORT = os.getenv('REDIS_PORT', 8889)
#REDIS_HOST = os.getenv('REDIS_HOST', 'redis-logcount.yg.hunantv.com')
#REDIS_PORT = os.getenv('REDIS_PORT', 8889)

#CELERY_NAME = os.getenv('CELERY_NAME','logdeal')
#CELERY_BROKER_URL = 'redis://%s:%d' % (PROXY_REDIS_HOST, PROXY_REDIS_PORT)
#CELERY_RESULT_BACKEND = 'redis://%s:%d' % (PROXY_REDIS_HOST, PROXY_REDIS_PORT)

RQ_WORKER_LEVEL = os.getenv('RQ_WORKER_LEVEL', 'low')

SUBSCRIBE = os.getenv('SUBSCRIBE', 'ERU:LOGCOUNT')
