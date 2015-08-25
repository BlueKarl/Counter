import redis
from log import config

def redisconnect():
    rds = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT)
    return rds
