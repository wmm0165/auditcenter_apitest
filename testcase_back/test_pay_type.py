# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 17:24
# @Author  : wangmengmeng
import unittest
import json
import warnings
from common.template_2_x import Template
from common.logger import Logger

# 费用类型取用户传入值，不传时展示空即可
class TestPayType(unittest.TestCase):
    warnings.simplefilter("ignore", ResourceWarning)
    log = Logger("TestPayType")

    def setUp(self):
        self.log.get_log().debug("开始执行用例TestPayType...")

    def tearDown(self):
        self.log.get_log().debug("结束执行用例TestPayType...")

    def test_opt_one(self):
        tem = Template()
        # tem.send_data('opt_pay_type', 'pay_type为空_1.txt', **tem.change_data)
        engine = tem.get_opt_engineid('opt_pay_type', 'pay_type为空_1.txt')
        print(engine)
        url = tem.conf.get('auditcenter', 'address') + tem.conf.get('api', '待审门诊获取患者信息和处方信息') + str(engine)
        res = tem.get(url)
        outpatient = res['data']['outpatient']
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        self.assertEqual(outpatient['payType'],"")


    def test_opt_two(self):
        tem = Template()
        # tem.send_data('opt_pay_type', 'pay_type为自费_1.txt', **tem.change_data)
        engine = tem.get_opt_engineid('opt_pay_type', 'pay_type为自费_1.txt')
        print(engine)
        url = tem.conf.get('auditcenter', 'address') + tem.conf.get('api', '待审门诊获取患者信息和处方信息') + str(engine)
        res = tem.get(url)
        outpatient = res['data']['outpatient']
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        self.assertEqual(outpatient['payType'],"自费")
        # tem.send_data('opt_pay_type', '自费修改_2.txt', **tem.change_data)
        engine = tem.get_opt_engineid('opt_pay_type', '自费修改_2.txt')
        print(engine)
        url = tem.conf.get('auditcenter', 'address') + tem.conf.get('api', '待审门诊获取患者信息和处方信息') + str(engine)
        res = tem.get(url)
        outpatient = res['data']['outpatient']
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        self.assertEqual(outpatient['payType'],"自费修改")


    def test_opt_three(self):
        tem = Template()
        engine = tem.get_opt_engineid('opt_pay_type', 'pay_type为测试费用类型_1.txt')
        print(engine)
        url = tem.conf.get('auditcenter', 'address') + tem.conf.get('api', '待审门诊获取患者信息和处方信息') + str(engine)
        res = tem.get(url)
        outpatient = res['data']['outpatient']
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        self.assertEqual(outpatient['payType'],"测试费用类型")

    def test_ipt_one(self):
        tem = Template()
        tem.send_data('ipt_pay_type', 'pay_type为空.txt', **tem.change_data)
    def test_ipt_two(self):
        tem = Template()
        tem.send_data('ipt_pay_type', 'pay_type为01.txt', **tem.change_data)
    def test_ipt_three(self):
        tem = Template()
        tem.send_data('ipt_pay_type', 'pay_type为城镇职工基本医疗保险.txt', **tem.change_data)




if __name__ == '__main__':
    # unittest.main(verbosity=2)  # 运行所有用例
    suite = unittest.TestSuite()  # 创建一个测试集合
    # suite.addTest(TestPayType("test_opt_one"))
    # suite.addTest(TestPayType("test_opt_two"))  # 测试套件中添加测试用例
    # suite.addTest(TestPayType("test_opt_three"))
    # suite.addTest(TestPayType("test_opt_four"))
    #     # suite.addTest(TestPayType("test_opt_five"))
    suite.addTest(TestPayType("test_ipt_one"))
    # suite.addTest(TestPayType("test_ipt_two"))
    # suite.addTest(TestPayType("test_ipt_three"))
    # test_suite.addTest(unittest.makeSuite(MyTest))#使用makeSuite方法添加所有的测试方法
    #第三步：构建一个TextTestRunner对象，并且运行第二步中的suite对象
    runner = unittest.TextTestRunner()
    runner.run(suite)