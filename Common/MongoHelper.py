#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J 
@license: Apache Licence  
@contact: 415900617@qq.com 
@software: PyCharm 
@file: MongoHelper.py 
@time: 2018/9/26 11:21 
@describe: mongodb 助手
http://www.runoob.com/mongodb/mongodb-connections.html
"""
import logging
import sys
import os
from pymongo import MongoClient
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
sys.path.append("..")
from BaseFile.ReadConfig import ReadConfig as RC
from BaseFile.Logger import Logger
logger = Logger('mongodb.log', logging.WARNING, logging.DEBUG)


class MongoHelper:
    def __init__(self, DBName):
        self.settings = RC().get_conf("../Config/MONGODB")[DBName]  # 获取Config-MONGODB 配置
        self.host = self.settings['host']
        self.port = self.settings['port']
        self.user = self.settings['user']
        self.passwd = self.settings['passwd']
        self.dbname = self.settings['db']
        self.table = self.settings['table']
        self.conn = MongoClient(host=self.host, port=self.port)
        # 如果用户名密码存在则认证登录
        if self.user or self.passwd is not None:
            self.db_auth = self.conn.admin
            self.db_auth.authenticate(self.user, self.passwd)
        self.db = self.conn.get_database(self.dbname)
        self.collection = self.db.get_collection(self.table)

    def insert(self, item, collection_name=None):
        """
        插入数据，这里的数据可以是一个，也可以是多个
        :param item: 需要插入的数据
        :param collection_name:  可选，需要访问哪个集合
        :return:
        """
        try:
            if collection_name is not None:
                collection = self.db.get_collection(self.db)
                collection.insert(item)
            else:
                self.collection.insert(item)
        except Exception as e:
            print("mongodb insert error!", e)
            logger.error("mongodb insert error! "+str(e))
        finally:
            self.conn.close()

    def find(self, expression=None, collection_name=None):
        """
        进行简单查询，可以指定条件和集合
        :param expression: 查询条件，可以为空
        :param collection_name: 集合名称
        :return: 所有结果
        """
        try:
            if collection_name is not None:
                collection = self.db.get_collection(self.db)
                if expression is None:
                    return collection.find()
                else:
                    return collection.find(expression)
            else:
                if expression is None:
                    return self.collection.find()
                else:
                    return self.collection.find(expression)
        except Exception as e:
            print("mongodb find error!", e)
            logger.error("mongodb find error! "+str(e))
        finally:
            self.conn.close()

    def get_collection(self, collection_name=None):
        """
        很多时候单纯的查询不能够通过这个类封装的方法执行，这时候就可以直接获取到对应的collection进行操作
        :param collection_name: 集合名称
        :return: collection
        """
        try:
            if collection_name is None:
                return self.collection
            else:
                return self.get_collection(collection_name)
        except Exception as e:
            print("mongodb get_collection error!", e)
            logger.error("mongodb get_collection error! "+str(e))
        finally:
            self.conn.close()


if __name__ == '__main__':
    db = MongoHelper("mongo_test")
    # item = {'addredd': 'zhangsan', 'index': '23'}
    # db.insert(item)  # 插入
    for item in db.find():  # 查询
        print(item)
