# -*- coding: utf-8 -*-
# @Time : 2019/6/16 18:37
# @Author : wangmengmeng

import logging
from logging import handlers
import os


class Logger:
    def __init__(self,loggername):
        # 创建一个loggger
        self.logger = logging.getLogger(loggername)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        log_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/logs/'
        logname = log_path + 'out.log'  # 指定输出的日志文件名
        fh = logging.handlers.TimedRotatingFileHandler(logname, when='M', interval=1, backupCount=5,encoding='utf-8')  # 指定utf-8格式编码，避免输出的日志文本乱码
        # fh = logging.FileHandler(logname, mode = 'a',encoding='utf-8') # 不拆分日志文件
        fh.setLevel(logging.DEBUG)

        # 创建一个handler，用于将日志输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
         """定义一个函数，回调logger实例"""
         return self.logger

if __name__ == '__main__':
    a = Logger("wmm")
    a.get_log().error("User %s is loging" % '测试30')
    a.get_log().error("User %s is loging" % '测试29')

