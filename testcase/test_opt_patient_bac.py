# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 17:24
# @Author  : wangmengmeng
import unittest

from common.template import Template


class TestSend(unittest.TestCase):
    tem = Template()

    def setUp(self):
        print("开始执行用例opt_patient...")

    def tearDown(self):
        print("结束执行用例opt_patient...")

    def test_get_engineid(self):
        # 发送数据
        self.tem.send_data('opt_patient', '1.txt', **self.tem.change_data)
        self.tem.send_data('opt_patient', '2.txt', **self.tem.change_data)
        self.tem.send_data('opt_patient', '3.txt', **self.tem.change_data)
        self.tem.send_data('opt_patient', '4.txt', **self.tem.change_data)
        self.tem.send_data('opt_patient', '5.txt', **self.tem.change_data)
        self.tem.send_data('opt_patient', '6_修改5.txt', **self.tem.change_data)
        # 获取引擎id
        self.engine = self.tem.get_opt_engineid('opt_patient','prescribe_med_1.txt')
        globals()['engineid'] = self.engine

    def test_opt_patient(self):
        global engineid
        url = self.tem.conf.get('auditcenter', 'address') + self.tem.conf.get('api', '待审门诊获取患者信息和处方信息') + str(engineid)
        res = self.tem.get(url)
        print(res)


if __name__ == '__main__':
    unittest.main(verbosity=2)  # 运行所有用例
    # test = TestSend()
    # test.test_send()
