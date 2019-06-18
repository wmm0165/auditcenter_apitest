# -*- coding: utf-8 -*-
# @Time    : 2019/6/18 11:15
# @Author  : wangmengmeng

from config.read_config import ReadConfig
from common.template import Template
tem = Template()
cof = ReadConfig()
# 发数据
tem.send_data('ipt_med','ipt_med1.txt',**tem.change_data)
eid = tem.get_ipt_engineid('ipt_med','ipt_med2.txt',2)
print(eid)
