#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J 
@license: Apache Licence  
@contact: 415900617@qq.com 
@software: PyCharm 
@file: CsvHelper.py 
@time: 2018/9/26 15:48 
@describe: csv 助手
"""
import logging
import sys
import os
import csv

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
sys.path.append("..")
from BaseFile.Logger import Logger
logger = Logger('csv.log', logging.WARNING, logging.DEBUG)


class CsvHelper:
    @staticmethod
    def CsvConnection(fireName):
        # 存入csv文件
        out = open('../Data/%s' % fireName, 'a', newline='', encoding="utf-8")
        # 设定写入模式
        csv_write = csv.writer(out, dialect='excel')
        return csv_write

    """ 以追加方式写入csv文件，message 数据格式：List """

    def csv_write(self, fireName, message):
        try:
            csv_write = self.CsvConnection(fireName)
            csv_write.writerow([msg for msg in message])
            print("write successful!")
        except Exception as e:
            print("[csv write error]", e)
            logger.error("[csv write error]"+str(e))

    """ 读取csv文件，返回List """

    @staticmethod
    def csv_read(fireName):
        try:
            with open("../Data/%s" % fireName, "r", encoding="utf-8") as csvfile:
                reader2 = csv.reader(csvfile)
                return [x for x in reader2]
        except Exception as e:
            print("[csv read error]", e)
            logger.error("[csv read error]" + str(e))


if __name__ == '__main__':
    message = "host", "1002", "1003"
    # 写入csv文件
    CsvHelper().csv_write("test.csv", message)
    # 读取csv文件
    print(CsvHelper().csv_read("test.csv"))
