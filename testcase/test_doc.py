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
        '''审核打回(双签)，医生删除处方'''
        engineid = self.tem.get_opt_engineid('opt','处方一',1)
        # 审核打回
        self.tem.opt_audit(engineid,1)
        self.tem.send_delete_1('doctor','opt_del_1',**self.tem.change_data)
        res = self.tem.get_opt_auditresult(engineid,1)
        self.assertEqual(0,res['data'][0]['rejectStatus'])

    def test_opt_02(self):
        '''审核打回，医生删除处方'''
        engineid = self.tem.get_opt_engineid('opt','处方一',1)
        # 审核打回
        self.tem.opt_audit(engineid,0)
        self.tem.send_delete_1('doctor','opt_del_1',**self.tem.change_data)
        res = self.tem.get_opt_auditresult(engineid,1)
        self.assertEqual(0,res['data'][0]['rejectStatus'])

    def test_opt_03(self):
        '''审核通过，医生删除处方'''
        engineid = self.tem.get_opt_engineid('opt','处方一',1)
        # 审核打回
        self.tem.opt_audit(engineid,2)
        self.tem.send_delete_1('doctor','opt_del_1',**self.tem.change_data)
        res = self.tem.get_opt_auditresult(engineid,1)
        self.assertEqual(0,res['data'][0]['rejectStatus'])

    def test_opt_04(self):
        '''审核打回，医生修改处方'''
        engineid = self.tem.get_opt_engineid('opt','处方一',1)
        # 审核打回
        self.tem.opt_audit(engineid,0)
        self.tem.send_data('opt','修改处方一1',**self.tem.change_data)  # 只修改处方头
        res = self.tem.get_opt_auditresult(engineid,1)
        self.assertEqual(2,res['data'][0]['rejectStatus'])

    def test_opt_05(self):
        '''审核打回，医生修改处方'''
        engineid = self.tem.get_opt_engineid('opt', '处方一', 1)
        # 审核打回
        self.tem.opt_audit(engineid, 0)
        self.tem.send_data('opt', '修改处方一2', **self.tem.change_data)  # 修改部分药的处方明细
        res = self.tem.get_opt_auditresult(engineid, 1)
        self.assertEqual(2, res['data'][0]['rejectStatus'])

    def test_opt_06(self):
        '''审核打回，医生修改处方'''
        engineid = self.tem.get_opt_engineid('opt','处方一',1)
        # 审核打回
        self.tem.opt_audit(engineid,0)
        self.tem.send_data('opt','修改处方一3',**self.tem.change_data)  # 修改全部药的处方明细
        res = self.tem.get_opt_auditresult(engineid,1)
        print(res)
        self.assertEqual(2,res['data'][0]['rejectStatus'])


if __name__ == '__main__':
    unittest.main()
