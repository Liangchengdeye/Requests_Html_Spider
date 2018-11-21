#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J 
@license: Apache Licence  
@contact: 415900617@qq.com 
@software: PyCharm 
@file: GetProxyIp.py 
@time: 2018/9/25 17:45 
@describe: 返回代理IP
"""
import sys
import os
import random
import time

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
sys.path.append("..")


class GetProxyIp:
    """随机从文件中读取proxy"""

    @staticmethod
    def get_random_proxy():
        while True:
            with open('../Config/PROXYIP', 'r') as f:
                proxies = f.readlines()
            if proxies:
                break
            else:
                time.sleep(1)
        proxy = random.choice(proxies).strip()
        return proxy

    """返回HTTP/HTTPS的代理IP，可根据代理IP类型更改"""

    def get_IP_Http(self):
        IP = self.get_random_proxy()
        proxies = {
            "http": IP,
        }
        return proxies

    def get_IP_Https(self):
        IP = self.get_random_proxy()
        proxies = {
            "https": IP,
        }
        return proxies


if __name__ == '__main__':
    print(GetProxyIp().get_IP_Http())
