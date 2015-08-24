#!/usr/bin/python2.7
#coding:utf-8

import sys
from log.logcount import logsend

def start():
    u = sys.argv[-1].split(':')    
    logsend(u[0], u[1])

if __name__ == '__main__':
    start()
