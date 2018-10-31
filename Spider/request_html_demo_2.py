#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J 
@license: Apache Licence  
@contact: 415900617@qq.com 
@software: PyCharm 
@file: request_html_demo_2.py.py 
@time: 2018/10/31 15:34 
@describe: 获取博客园新闻
https://news.cnblogs.com/n/recommend
"""
import sys
import os

from requests_html import HTMLSession
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
sys.path.append("..")
from Common.JsonHelper import JsonHelper as JS
session = HTMLSession()


def get_cnblog(url):
    r = session.get(url)
    # 通过CSS找到新闻标签
    news = r.html.find('h2.news_entry > a')
    json_list = []
    for new in news:
        title = new.text
        liks = [x for x in new.absolute_links][0]
        print(title)  # 获得新闻标题
        print(liks)  # 获得新闻链接
        json_list.append({"Title": title, "url": liks})
    JS().json_write("cnblogs.json", json_list)


if __name__ == '__main__':
    url = "https://news.cnblogs.com/n/recommend"
    get_cnblog(url)