#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: W_H_J 
@license: Apache Licence  
@contact: 415900617@qq.com 
@software: PyCharm 
@file: KafkaHelper.py 
@time: 2018/9/26 14:17 
@describe: kafka 助手
"""
import logging
import sys
import os
from pykafka import KafkaClient

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
sys.path.append("..")
from BaseFile.ReadConfig import ReadConfig as RC
from BaseFile.Logger import Logger
logger = Logger('kafka.log', logging.WARNING, logging.DEBUG)
""" 读取哪个kafka 配置"""
DBName = "kafka_demo1"
settings = RC().get_conf("../Config/kafka")[DBName]  # 获取Config-KAFKA 配置
host = settings['host']


class KafkaHelper:
    """DBName 指定读取哪个配置文件"""
    client = KafkaClient(hosts=host)  # 可接受多个client

    def __init__(self):
        self.topics = settings['topics']
        self.zookeeper_connect = settings['zookeeper_connect']
        self.topics = settings['topics']
        self.client = self.client

    """ 配置连接 """

    def KafkaConnectionPool(self):
        try:
            topic = self.client.topics[self.topics.encode('utf-8')]  # 选择一个topic
            return topic
        except Exception as e:
            print('[kafka-connect] error', e)
            logger.error('[kafka-connect] error '+str(e))

    """ 生成一条消息，并发送至kafka: partitionkey:分区名称；message：消息内容"""

    def producer_kafka(self, partitionKey, message):
        topic = self.KafkaConnectionPool()
        try:
            with topic.get_sync_producer() as producer:
                producer.produce(partition_key=partitionKey.encode('utf-8'),
                                 message=message.encode('utf-8'))
            print("successful send msg to kafka~~~~~")
        except Exception as e:
            print('[producer_kafka] error', e)
            logger.error('[producer_kafka] error '+str(e))

    """ 从zookeeper消费 get_balanced_consumer"""

    def consumer_zookeeper(self):
        topic = self.KafkaConnectionPool()
        try:
            balanced_consumer = topic.get_balanced_consumer(
                consumer_group='demo'.encode('utf-8'),
                auto_commit_enable=True,  # 设置为False的时候不需要添加consumer_group，直接连接topic即可取到消息
                zookeeper_connect=self.zookeeper_connect  # 这里就是连接多个zk
            )
            for message in balanced_consumer:
                if message is not None:
                    print(message.offset, message.partition_key, str(message.value, encoding="utf-8"))
        except Exception as e:
            print("[consumer_zookeeper] error:", e)
            logger.error("[consumer_zookeeper] error "+str(e))

    """ 从kafka消费 get_simple_consumer"""

    def consumer_kafka(self):
        topic = self.KafkaConnectionPool()
        try:
            # 从kafka消费
            kafka_consumer = topic.get_simple_consumer(
                consumer_group='demo'.encode("utf-8"),
                auto_commit_enable=True,
                consumer_id='demo'.encode("utf-8")
            )
            for message in kafka_consumer:
                if message is not None:
                    print(message.offset, message.partition_key, str(message.value, encoding="utf-8"))
        except Exception as e:
            print("[consumer_kafka] error", e)
            logger.error("[consumer_kafka] error "+str(e))


if __name__ == '__main__':
    # # print(KafkaHelper().consumer_kafka())
    message = '{"demo3":"test02"}'
    KafkaHelper().producer_kafka('demo',message)
