#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J 
@license: Apache Licence  
@contact: 415900617@qq.com 
@site:  
@software: PyCharm 
@file: logger.py 
@time: 2018/3/23 14:30 
@describe: log日志编写
"""
import logging
import os
import datetime

FOREGROUND_WHITE = 0x0007
FOREGROUND_BLUE = 0x01  # text color contains blue.
FOREGROUND_GREEN = 0x02  # text color contains green.
FOREGROUND_RED = 0x04  # text color contains red.
FOREGROUND_YELLOW = FOREGROUND_RED | FOREGROUND_GREEN
STD_OUTPUT_HANDLE = -11
# 创建log文件夹
log_dir = '../logs'
if not os.path.exists(log_dir):
    os.mkdir(log_dir)
print(log_dir)


class Logger:
    def __init__(self, path, clevel=logging.DEBUG, Flevel=logging.DEBUG):
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        startTime = datetime.datetime.now().strftime('%Y-%m-%d')
        path = os.path.join(log_dir, str(startTime) + "-" + path)
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)
        # 设置文件日志
        fh = logging.FileHandler(path)
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message, color=FOREGROUND_BLUE):
        self.logger.debug(message)

    def info(self, message, color=FOREGROUND_GREEN):
        self.logger.info(message)

    def war(self, message, color=FOREGROUND_YELLOW):
        self.logger.warn(message)

    def error(self, message, color=FOREGROUND_RED):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)


if __name__ == '__main__':
    logyyx = Logger('test.log', logging.WARNING, logging.DEBUG)
    logyyx.debug('一个debug信息')
    logyyx.info('一个info信息')
    logyyx.war('一个warning信息')
    logyyx.error('一个error信息')
    logyyx.cri('一个致命critical信息')
