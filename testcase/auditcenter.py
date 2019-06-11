# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 20:04
# @Author  : wangmengmeng
import datetime
import time
import random
class SendXml:
    def __init__(self):
        group_no = random.randint(1, 1000000)
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        now_ts = int(time.mktime(time.strptime(now, "%Y-%m-%d %H:%M:%S"))) * 1000
        yest = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d %H:%M:%S")
        yest_ts = int(time.mktime(time.strptime(yest, "%Y-%m-%d %H:%M:%S"))) * 1000
        yest_raw = (datetime.datetime.now() + datetime.timedelta(days=-1))
        yest_front_onehour = (yest_raw + datetime.timedelta(hours=-1)).strftime("%Y-%m-%d %H:%M:%S")
        yest_front_onehour_ts = int(time.mktime(time.strptime(yest_front_onehour, "%Y-%m-%d %H:%M:%S"))) * 1000
        yest_front_twohour = (yest_raw + datetime.timedelta(hours=-2)).strftime("%Y-%m-%d %H:%M:%S")
        yest_front_twohour_ts = int(time.mktime(time.strptime(yest_front_twohour, "%Y-%m-%d %H:%M:%S"))) * 1000
        yest_front_threehour = (yest_raw + datetime.timedelta(hours=-3)).strftime("%Y-%m-%d %H:%M:%S")
        yest_front_threehour_ts = int(time.mktime(time.strptime(yest_front_threehour, "%Y-%m-%d %H:%M:%S"))) * 1000
        yest_front_fourhour = (yest_raw + datetime.timedelta(hours=-4)).strftime("%Y-%m-%d %H:%M:%S")
        yest_front_fourhour_ts = int(time.mktime(time.strptime(yest_front_fourhour, "%Y-%m-%d %H:%M:%S"))) * 1000
        yest_behind_onehour = (yest_raw + datetime.timedelta(hours=+1)).strftime("%Y-%m-%d %H:%M:%S")
        yest_behind_onehour_ts = int(time.mktime(time.strptime(yest_front_onehour, "%Y-%m-%d %H:%M:%S"))) * 1000




