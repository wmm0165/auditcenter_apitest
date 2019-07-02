# -*- coding: utf-8 -*-
# @Time : 2019/7/2 15:06
# @Author : wangmengmeng
import unittest
import json
import warnings
from common.template_2_x import Template
from common.logger import Logger
class TestWh(unittest.TestCase):
    log = Logger("TestWh")
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.log.get_log().debug("开始执行用例TestWh...")

    def tearDown(self):
        self.log.get_log().debug("结束执行用例TestTestWh...")

    def test_opt_one(self):
        tem = Template()
        # tem.send_data('ipt_w_h', '不传ccr和scr_1.txt', **tem.change_data)
        # engine = tem.get_opt_engineid('opt_ccr', '不传ccr和scr_1.txt')
        # res = tem.get_opt_recipeInfo(engine,0)
        # outpatient = res['data']['outpatient']
        # print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        # self.assertEqual(outpatient['ccr'],"90.0(预设值)")
    def test_opt_two(self):
        # 检验中传入scr,则ccr取传入值
        tem = Template()
        print(tem.get_date(0,0).strftime("%Y-%m-%d"))
        # cal_ccr = Ccr('2019-07-01 20:29:00', '1994-03-05')
        tem.send_data('opt_ccr', '传ccr_1.txt', **tem.change_data)
        # engine = tem.get_opt_engineid('opt_ccr', '不传ccr和scr_1.txt')
        # res = tem.get_opt_recipeInfo(engine,0)
        # outpatient = res['data']['outpatient']
        # print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        # expect = a1 = cal_ccr.ccr_calculate(sex='男', unit='mg/dl', age=cal_ccr.y, weight=60, scr=9)
        # print(expect)
        # self.assertEqual(outpatient['ccr'],"90.0(预设值)")
    def test_opt_three(self):
        tem = Template()
        tem.send_data('opt_ccr', '传scr但是检验已失效_1.txt', **tem.change_data)

    def test_ipt_01(self):
        tem = Template()
        tem.send_data('ipt_w_h', '1', **tem.change_data)
        tem.send_data('ipt_w_h', '2', **tem.change_data)

    def test_ipt_02(self):
        tem = Template()
        tem.send_data('ipt_ccr', '2', **tem.change_data)
    def test_ipt_03(self):

        tem = Template()
        tem.send_data('ipt_ccr', '3', **tem.change_data)




if __name__ == '__main__':
    suite = unittest.TestSuite()  # 创建一个测试集合
    # suite.addTest(TestCcr("test_opt_one"))
    # suite.addTest(TestCcr("test_opt_two"))
    # suite.addTest(TestCcr("test_opt_three"))
    runner = unittest.TextTestRunner()
    runner.run(suite)