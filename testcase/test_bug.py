# -*- coding: utf-8 -*-
# @Time : 2019/8/5 13:40
# @Author : wangmengmeng
from common.template_2_x import Template
from config.read_config import ReadConfig
import unittest
import warnings


class TestBug(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.tem = Template()

    def test_01(self):
        """AUDIT-593"""
        engineid1 = self.tem.get_ipt_engineid('ipt', '医嘱一', 1)
        ids = [engineid1]
        self.tem.audit_multi(3, *ids)
        engineid2 = self.tem.get_ipt_engineid('ipt', '医嘱三包含医嘱一', 1)
        # self.tem.send_data('ipt','医嘱三包含医嘱一',**self.tem.change_data)
        print(engineid2)
        res = self.tem.get_ipt_result(engineid2, self.tem.change_data['{{gp}}'])
        print(res['data']['auditStatus'])
        self.assertEqual(1, res['data']['auditStatus'])