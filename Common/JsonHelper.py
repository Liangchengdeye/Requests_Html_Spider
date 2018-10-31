#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J 
@license: Apache Licence  
@contact: 415900617@qq.com 
@software: PyCharm 
@file: JsonHelper.py 
@time: 2018/10/31 15:04 
@describe: 读写json文件
"""
import sys
import os
import json
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
sys.path.append("..")


class JsonHelper:

    """ 以追加方式写入json文件，message 数据格式：List """
    def json_write(self, fireName, message):
        try:
            out = open('../Data/%s' % fireName, 'a', encoding='utf-8')
            out.write(json.dumps(message)+"\n")
            print("write successful!")
        except Exception as e:
            print("[json write error]", e)

    """读取json文件，原文件每行为一个独立json串，组合并不是一个正确的json格式"""
    def json_read(self, fireName):
        with open('../Data/%s'% fireName, 'r', encoding='utf-8') as f:
            msg = f.readlines()
        return [json.loads(data[:-1]) for data in msg]

    """读取json文件，只做查看，无返回值，需要返回值，使用上一个方法"""
    def json_watch(self, fireName):
        f = open('../Data/%s'% fireName, 'r', encoding='utf-8')
        for data in f:
            print("*"*150)
            print(json.loads(data))
            print("*"*150, "\n")


if __name__ == '__main__':
    # 读取json--操作返回数据
    str_json = JsonHelper().json_read("cnblogs.json")
    for i in str_json:
        print(i)
        print("*"*100, "\n")
    # 读取json--查看
    JsonHelper().json_watch("cnblogs.json")