# -*- coding: utf-8 -*-
# @Time : 2019/7/23 22:52
# @Author : wangmengmeng
import unittest
import json
import warnings
import time
from common.template_2_x import Template
from common.logger import Logger


class TestLabel(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.tem = Template()
        # self.log.get_log().debug("开始执行用例TestIm...")

    # def tearDown(self):
    #     self.log.get_log().debug("结束执行用例TestIm...")

    def test_opt_01(self):
        # 开具处方1未审核，则该任务打待处理标签
        engineid1 = self.tem.get_opt_engineid("opt", "处方一", 1)
        engineid2 = self.tem.get_opt_engineid("opt", "处方二 ", 2)

    def test_ipt_01(self):
        engineid1 = self.tem.get_ipt_engineid("ipt","医嘱一",1)
        engineid2 = self.tem.get_ipt_engineid("ipt","医嘱二",2)

    def test_ipt_02(self):
        # 一个xml中两组药
        engineid = self.tem.get_ipt_engineid("ipt","一个任务两组药",1)

    def test_ipt_03(self):
        engineid = self.tem.get_ipt_engineid("ipt", "一个药嘱一个草药嘱", 1)
        engineid = self.tem.get_ipt_engineid("ipt", "同患者再开药", 1)






if __name__ == '__main__':
    unittest.main()