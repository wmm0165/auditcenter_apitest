# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 20:04
# @Author  : wangmengmeng
import datetime
import time
import random
# from common.template_2_x import Template
# t = Template()
# t.send_data('ipt_med','ipt_med1.txt',**t.change_data)

from decimal import Context, ROUND_HALF_UP


# def get_num(num):
#
#     num = str(num)
#     if float(num) >= 1:
#         a = "%.2f" % float(num)
#         c = Context(prec=(len(a) - 1), rounding=ROUND_HALF_UP).create_decimal(num)
#     return float(str(c))
#     if float(num) < 1:
#         d = float(num) * 100
#         if d - int(d) < 0.5:
#     return float(int(d) / 100)
#     else:
#         i = (int(d) + 1) / 100
#     return float(i)
