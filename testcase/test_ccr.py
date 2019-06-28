# -*- coding: utf-8 -*-
# @Time : 2019/6/25 19:35
# @Author : wangmengmeng
import unittest
import json
import warnings
from common.template_2_x import Template
from common.logger import Logger

class TestCcr(unittest.TestCase):
    log = Logger("TestCcr")
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.log.get_log().debug("开始执行用例TestCcr...")

    def tearDown(self):
        self.log.get_log().debug("结束执行用例TestCcr...")

    def test_opt_one(self):
        tem = Template()
        # tem.send_data('opt_ccr', '不传ccr和scr_1.txt', **tem.change_data)
        engine = tem.get_opt_engineid('opt_ccr', '不传ccr和scr_1.txt')
        res = tem.get_opt_recipeInfo(engine,0)
        outpatient = res['data']['outpatient']
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        self.assertEqual(outpatient['ccr'],"90.0(预设值)")
    def test_opt_two(self):
        tem = Template()
        tem.send_data('opt_ccr', '传ccr_1.txt', **tem.change_data)
        # engine = tem.get_opt_engineid('opt_ccr', '不传ccr和scr_1.txt')
        # res = tem.get_opt_recipeInfo(engine,0)
        # outpatient = res['data']['outpatient']
        # print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        # self.assertEqual(outpatient['ccr'],"90.0(预设值)")


if __name__ == '__main__':
    suite = unittest.TestSuite()  # 创建一个测试集合
    # suite.addTest(TestCcr("test_opt_one"))
    suite.addTest(TestCcr("test_opt_two"))
    runner = unittest.TextTestRunner()
    runner.run(suite)