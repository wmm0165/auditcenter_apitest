# -*- coding: utf-8 -*-
# @Time : 2019/7/24 16:59
# @Author : wangmengmeng
import unittest
import json
import warnings
import time
from common.template import Template
from common.logger import Logger


class TestIm(unittest.TestCase):
    log = Logger("TestIm")

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.tem = Template()

    def test_ipt_01(self):
        # 审核打回任务且医生没有发起聊天
        # self.tem.send_data("ipt","医嘱一",**self.tem.change_data)
        engineid = self.tem.get_ipt_engineid("ipt","医嘱一",1)



