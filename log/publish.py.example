import redis
import json

import config

rds = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT)
while 1:
    with open('text.log') as f:
        for line in f:
            print line
            rds.publish(config.SUBSCRIBE, line)

