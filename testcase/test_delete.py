# -*- coding: utf-8 -*-
# @Time : 2019/7/30 9:44
# @Author : wangmengmeng
from common.template_2_x import Template
from config.read_config import ReadConfig
import unittest
import warnings

class TestDelete(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.tem = Template()

    def test_opt_01(self):
        engineid1 = self.tem.get_opt_engineid('opt','处方一',1)
        engineid2 = self.tem.get_opt_engineid('opt', '处方二', 1)

