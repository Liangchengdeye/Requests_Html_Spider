#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J 
@license: Apache Licence  
@contact: 415900617@qq.com 
@software: PyCharm 
@file: GetLocalFile.py 
@time: 2018/9/25 17:26 
@describe: 操作本地文件
"""
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
sys.path.append("..")


class GetLocalFile:
    """ 读取本地文件，返回：List """

    @staticmethod
    def get_local_file(filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = f.readlines()
        return [url[:-1] for url in data]
