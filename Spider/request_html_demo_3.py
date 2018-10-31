#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J 
@license: Apache Licence  
@contact: 415900617@qq.com 
@software: PyCharm 
@file: request_html_demo_3.py 
@time: 2018/10/31 16:18 
@describe: 最高清壁纸库-桌面下载
requests_html 解析方式
"""
import logging
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
sys.path.append("..")
from BaseFile.Logger import Logger
from requests_html import HTMLSession
import requests
import time
logger = Logger('img.log', logging.WARNING, logging.DEBUG)
session = HTMLSession()
i = 0


# 解析图片列表
def get_girl_list():
    # 返回一个 response 对象
    response = session.get('http://www.win4000.com/zt/xinggan.html')
    content = response.html.find('div.Left_bar', first=True)
    li_list = content.find('li')
    for li in li_list:
        url = li.find('a', first=True).attrs['href']
        get_girl_detail(url)


# 解析图片详细
def get_girl_detail(url):
    # 返回一个 response 对象
    response = session.get(url)  # 单位秒数
    content = response.html.find('div.scroll-img-cont', first=True)
    li_list = content.find('li')
    for li in li_list:
        img_url = li.find('img', first=True).attrs['data-original']
        img_url = img_url[0:img_url.find('_')] + '.jpg'
        print(img_url)
        save_image(img_url)


# 保持大图
def save_image(img_url):
    try:
        global i
        i += 1
        print("=="*10 + ">>", i, "==>img")
        img_response = requests.get(img_url)
        t = int(round(time.time() * 1000))  # 毫秒级时间戳
        f = open('../Data/img/%d.jpg' % t, 'ab')  # 存储图片，多媒体文件需要参数b（二进制文件）
        f.write(img_response.content)  # 多媒体存储content
        f.close()
    except Exception as e:
        print("Downloads error:", e)
        logger.error(e)


if __name__ == '__main__':
    print("Downloads img start, Please Don't close the window!")
    time.sleep(10)
    get_girl_list()
    print("Dolnloads img successful, Please to see /Data/img")
    a = input("please input q to close the windows!")
    if str(a) == 'q':
        os.close()