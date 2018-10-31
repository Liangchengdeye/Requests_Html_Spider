#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J 
@license: Apache Licence  
@contact: 415900617@qq.com 
@software: PyCharm 
@file: RedisHelper.py 
@time: 2018/9/26 10:14 
@describe: redis 操作助手
列出了常用操作，若要使用更多方法，可根据需求增加
http://www.runoob.com/redis/redis-tutorial.html
"""
import sys
import os
import redis
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
sys.path.append("..")
from BaseFile.ReadConfig import ReadConfig as RC


class RedisHelper:
    """DBNAME 获取哪一个 redis 配置信息"""

    def __init__(self, DBName):
        self.settings = RC().get_conf("../Config/REDIS")[DBName]  # 获取Config-REDIS 配置
        self.host = self.settings['host']
        self.port = self.settings['port']
        self.user = self.settings['user']
        self.passwd = self.settings['passwd']
        self.db = self.settings['db']
        try:
            # 建立 REDIS 连接池
            pool = redis.ConnectionPool(host=self.host, port=self.port, db=self.db, password=self.passwd,
                                        decode_responses=True)
            self.r = redis.Redis(connection_pool=pool)
        except Exception as e:
            print("REDIS CONTENT ERROR:", e)

    # 建立 REDIS 连接池
    def ConnectionPool(self):
        pool = redis.ConnectionPool(host=self.host, port=self.port, db=self.db, password=self.passwd,
                                    decode_responses=True)
        R = redis.Redis(connection_pool=pool)
        return R

    # 第二个参数listURL，必须传入list结构数据，插入到redis
    def redis_lpush(self, keyName, listUrl):
        try:
            i = 0
            for data in listUrl:
                i += 1
                self.r.lpush(keyName, data)
                print(i)
            print("successful push list!")
        except Exception as e:
            print('[redis_lpush] ERROR', e)

    # 检查key是否存在
    def redis_exists(self, keyName):
        try:
            return self.r.exists(keyName)
        except Exception as e:
            print('[redis_exists] ERROR', e)

    # 以lpop方式取出元素，在keyName对应的列表的左侧获取第一个元素并在列表中移除
    def redis_lpop(self, keyName):
        try:
            url_list = self.r.lpop(keyName).decode()  # 获取
            return url_list
        except Exception as e:
            print('[redis_pop] ERROR', e)

    # 获取redis长度
    def redis_llen(self, keyName):
        try:
            length = self.r.llen(keyName)
            return length
        except Exception as e:
            print("[redis_llen] ERROR", e)

    # 以lrange方式取出元素
    def redis_lrange(self, keyName, start, end):
        try:
            url_list = self.r.lrange(keyName, start, end)
            return url_list
        except Exception as e:
            print('[redis_lrange] ERROR,', e)

    # 以rpop方式取出元素，在keyName对应的列表的右侧获取第一个元素并在列表中移除
    def redis_rpop(self, keyName):
        try:
            url_list = self.r.rpop(keyName).decode()
            return url_list
        except Exception as e:
            print('[redis_rpop] ERROR', e)

    # Set 是 String 类型的无序集合。集合成员是唯一的，这就意味着集合中不能出现重复的数据
    def redis_sadd(self, keyName, listUrl):
        try:
            i = 0
            for data in listUrl:
                i += 1
                self.r.sadd(keyName, data)
                print(i)
            print("successful sadd list!")
        except Exception as e:
            print('[redis_sadd] ERROR', e)

    # 移除Set并返回集合中的一个随机元素
    def redis_spop(self, keyName):
        try:
            url_list = self.r.spop(keyName).decode()
            return url_list
        except Exception as e:
            print('[redis_spop] ERROR', e)

    # 移除Set并返回集合中所有成员
    def redis_smembers(self, keyName):
        try:
            url_list = self.r.smembers(keyName).decode()
            return url_list
        except Exception as e:
            print('[redis_spop] ERROR', e)


if __name__ == '__main__':
    r = RedisHelper('test01').redis_llen("url_length")
    print(r)
