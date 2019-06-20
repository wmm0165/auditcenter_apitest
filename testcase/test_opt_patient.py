# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 17:24
# @Author  : wangmengmeng
import unittest
import json
import warnings
from common.template import Template


class TestOptPatient(unittest.TestCase):
    tem = Template()

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        print("开始执行用例opt_patient...")

    def tearDown(self):
        print("结束执行用例opt_patient...")

    def test_case_one(self):
        # 发送数据
        tem = Template()
        tem.send_data('opt_patient', '1.txt', **tem.change_data)
        tem.send_data('opt_patient', '2.txt', **tem.change_data)
        tem.send_data('opt_patient', '3.txt', **tem.change_data)
        tem.send_data('opt_patient', '4.txt', **tem.change_data)
        tem.send_data('opt_patient', '5.txt', **tem.change_data)
        # 获取引擎id
        engine = tem.get_opt_engineid('opt_patient','prescribe_med_1.txt')
        # 点击待审数据的查看
        url = self.tem.conf.get('auditcenter', 'address') + self.tem.conf.get('api', '待审门诊获取患者信息和处方信息') + str(engine)
        res = self.tem.get(url)
        outpatient = res['data']['outpatient']
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        # 待审详情期望取4中的患者信息
        self.assertEqual(outpatient['height'],"160.0cm")
        self.assertEqual(outpatient['weight'], "60.0kg")
        self.assertEqual(outpatient['bsa'], "1.5911㎡(计算)")
        self.assertEqual(outpatient['ccr'], "80.0")
        self.assertEqual(outpatient['isPregnant'], "1")
        self.assertEqual(outpatient['pregWeeks'], 36)
        self.assertEqual(outpatient['isLactation'], "1")
        # 审核通过
        engineids = [engine]
        tem.audit_multi(1, *engineids)
        url_all = self.tem.conf.get('auditcenter', 'address') + self.tem.conf.get('api', '已审门诊获取患者信息和处方信息') + str(engine)
        res_all = self.tem.get(url_all)
        outpatient_all= res_all['data']['outpatient']
        print(json.dumps(res_all, indent=2, sort_keys=False, ensure_ascii=False))
        # 已审详情期望取4中的患者信息
        self.assertEqual(outpatient_all['height'],"160.0cm")
        self.assertEqual(outpatient_all['weight'], "60.0kg")
        self.assertEqual(outpatient_all['bsa'], "1.5911㎡(计算)")
        self.assertEqual(outpatient_all['ccr'], "80.0")
        self.assertEqual(outpatient_all['isPregnant'], "1")
        self.assertEqual(outpatient_all['pregWeeks'], 36)
        self.assertEqual(outpatient_all['isLactation'], "1")


    def test_case_two(self):
        # 修改患者信息
        tem = Template()
        tem.send_data('opt_patient', '5.txt', **tem.change_data)
        engine1 = tem.get_opt_engineid('opt_patient', 'prescribe_med_1.txt')
        url = self.tem.conf.get('auditcenter', 'address') + self.tem.conf.get('api', '待审门诊获取患者信息和处方信息') + str(engine1)
        res1 = self.tem.get(url)
        outpatient1 = res1['data']['outpatient']
        # 处方1待审详情期望取5中的患者信息
        self.assertEqual(outpatient1['height'],"162.0cm")
        self.assertEqual(outpatient1['weight'], "62.0kg")
        self.assertEqual(outpatient1['bsa'], "1.6289㎡(计算)")
        self.assertEqual(outpatient1['ccr'], "80.0")
        self.assertEqual(outpatient1['isPregnant'], "0")
        self.assertEqual(outpatient1['pregWeeks'], 36)
        self.assertEqual(outpatient1['isLactation'], "0")

        tem.send_data('opt_patient', '6_修改5.txt', **tem.change_data)
        engine2 = tem.get_opt_engineid('opt_patient', 'prescribe_med_2.txt')
        url = self.tem.conf.get('auditcenter', 'address') + self.tem.conf.get('api', '待审门诊获取患者信息和处方信息') + str(engine2)
        res2 = self.tem.get(url)
        outpatient2 = res1['data']['outpatient']
        print(outpatient2)
        # 处方2待审详情期望取6中的患者信息
        self.assertEqual(outpatient2['height'],"164.0cm")
        self.assertEqual(outpatient2['weight'], "64.0kg")
        self.assertEqual(outpatient2['bsa'], "1.6667㎡(计算)")
        self.assertEqual(outpatient2['ccr'], "80.0")
        self.assertEqual(outpatient2['isPregnant'], "0")
        self.assertEqual(outpatient2['pregWeeks'], 36)
        self.assertEqual(outpatient2['isLactation'], "0")










if __name__ == '__main__':
    # unittest.main(verbosity=2)  # 运行所有用例
    suite = unittest.TestSuite()  # 创建一个测试集合
    # suite.addTest(TestOptPatient("test_case_one"))
    suite.addTest(TestOptPatient("test_case_two"))  # 测试套件中添加测试用例
    # test_suite.addTest(unittest.makeSuite(MyTest))#使用makeSuite方法添加所有的测试方法
    #第三步：构建一个TextTestRunner对象，并且运行第二步中的suite对象
    runner = unittest.TextTestRunner()
    runner.run(suite)