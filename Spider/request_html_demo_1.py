#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J 
@license: Apache Licence  
@contact: 415900617@qq.com 
@software: PyCharm 
@file: request_html_demo_1.py 
@time: 2018/9/25 17:34 
@describe: 使用requests-html爬虫模块抓取~简书爬虫页面
中文文档：https://cncert.github.io/requests-html-doc-cn/#/
"""
import json
import logging
import sys
import os
import requests
import time
# 导入requests_html包
from requests_html import HTMLSession
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '\\' + '..'))
sys.path.append("..")
from BaseFile.Logger import Logger
# 导入读取列表文件
from BaseFile.GetLocalFile import GetLocalFile as GF
from BaseFile.GetProxyIp import GetProxyIp as GP
from Config.HEADERS import HEADERS as HS
from Common.CsvHelper import CsvHelper as CV
from Common.JsonHelper import JsonHelper as JS

logger = Logger('jianshu.log', logging.WARNING, logging.DEBUG)
# 实例化requests_html
session = HTMLSession()


# 基础版--抓取简书 前五页 python 爬虫教程
def get_jianshu(base_url):
    try:
        htmlSource = session.get(base_url, headers=HS['headersJianShun'])
        print("请求状态码：", htmlSource.status_code)
        liText = htmlSource.html.find("#list-container > ul > li > div > a")
        for i in liText:
            print(i.text)
            print([x for x in i.absolute_links][0])
    except Exception as e:
        print("请求错误！", e)
        logger.error(e)


# 代理IP版本
def get_jianshu_ip(base_url):
    try:
        proxies = GP().get_IP()
        print(proxies)
        htmlSource = session.get(base_url, headers=HS['headersJianShun'], proxies=proxies, verify=False)
        print("请求状态码：", htmlSource.status_code)
        liText = htmlSource.html.find("#list-container > ul > li > div > a")
        for i in liText:
            print(i.text)
            print([x for x in i.absolute_links][0])
    except Exception as e:
        print("请求错误！", e)
        logger.error(e)


# 存入csv版本
def get_jianshu_fire(base_url):
    try:
        htmlSource = session.get(base_url, headers=HS['headersJianShun'])
        print("请求状态码：", htmlSource.status_code)
        liText = htmlSource.html.find("#list-container > ul > li > div > a")
        message = "标题", "URL"
        CV().csv_write("jianshu.csv", message)
        for i in liText:
            title = i.text
            link = [x for x in i.absolute_links][0]
            print(title)
            print(link)
            # 写入csv的数据格式，逗号分割
            message = title, link
            CV().csv_write("jianshu.csv", message)
    except Exception as e:
        print("请求错误！", e)


if __name__ == '__main__':
    base_url = "https://www.jianshu.com/c/a480500350e7?order_by=added_at&page="
    # # 基础版
    # get_jianshu(base_url+str(1))
    # # 代理IP版
    # get_jianshu_ip(base_url+str(2))
    # # 存入csv版
    # get_jianshu_fire(base_url+str(3))


    str4=[]
    # dict4="222"
    str4.append({"title":1111})
    str4.append({"title":1111})

    print(str4)
    '''{"001":[{"title": "1111"}, {"title": "1111"}, {"title": "1111"}],"002":[{"title":"2222"}]}'''
    message = (str4)
    JS().json_write("test.json", message)