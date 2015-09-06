#!/usr/bin/python2.7
#coding:utf-8

import sys
from log.logcount import logsend
from log import config


def start():
    logsend(host=config.PROXY_REDIS_HOST, port=config.PROXY_REDIS_PORT)

if __name__ == '__main__':
    start()
