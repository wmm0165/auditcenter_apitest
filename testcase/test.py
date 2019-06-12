# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 19:37
# @Author  : wangmengmeng
from config.read_config import ReadConfig
from common.template import Template
tem = Template()
cof = ReadConfig()
# 获取引擎id
engine = tem.get_opt_engineid('opt_patient', 'prescribe_med_1.txt')
# tem.send_data('opt_patient', 'prescribe_med_1.txt')

