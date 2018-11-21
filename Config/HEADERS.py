#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J 
@license: Apache Licence  
@contact: 415900617@qq.com 
@software: PyCharm 
@file: HEADERS.py 
@time: 2018/9/26 17:31 
@describe: 请求头集合--爬虫请求头信息在此配置
'User-Agent': '%s' % UserAgent.pc_agent() 启用轮换浏览器请求头
"""
import os
import sys

sys.path.append(r'your_path')
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
sys.path.append("..")
from BaseFile.UserAgent import UserAgent

HEADERS = {
    # 配置样例
    "heasers": {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'GA1.2.151205434.1528702564; user_trace_token=20180611153613-1e11d7da-6d4a-11e8-9446-5254005c3644; LGUID=20180611153613-1e11da71-6d4a-11e8-9446-5254005c3644; JSESSIONID=ABAAABAAAGFABEFA887FF2126C2345351E1CF33022A085A; _gid=GA1.2.295504001.1536894927; LGSID=20180914111529-6ee84ad5-b7cc-11e8-b939-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536894927; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_navigation; SEARCH_ID=f8b502632588469da5ea73ee9dd382a5; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536897145; LGRID=20180914115228-993585b5-b7d1-11e8-b939-5254005c3644',
        'Host': 'www.lagou.com',
        # 'Referer': 'https://www.lagou.com/zhaopin/Java/?labelWords=label',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': '%s' % UserAgent.pc_agent()},
    # 简书
    "headersJianShun": {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'www.jianshu.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': '%s' % UserAgent.pc_agent()},

}

if __name__ == '__main__':
    print(HEADERS['heasers'])
