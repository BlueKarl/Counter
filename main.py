#!/usr/bin/python2.7
#coding:utf-8

import sys
from log.logcount import logsend
from log import config

def start():
#    u = sys.argv[-1].split(':')    
#    logsend(u[0], u[1])
    logsend(host=config.PROXY_REDIS_HOST, port=config.PROXY_REDIS_PORT)
if __name__ == '__main__':
    start()
