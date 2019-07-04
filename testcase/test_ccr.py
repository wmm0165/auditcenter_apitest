# -*- coding: utf-8 -*-
# @Time : 2019/6/25 19:35
# @Author : wangmengmeng
import unittest
import json
import warnings
import time
from common.template_2_x import Template
from common.logger import Logger
from common.calculate_ccr import Ccr


class TestCcr(unittest.TestCase):
    log = Logger("TestCcr")

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.log.get_log().debug("开始执行用例TestCcr...")

    def tearDown(self):
        self.log.get_log().debug("结束执行用例TestCcr...")

    def test_opt_01(self):
        # ccr与scr都不传,则ccr取默认值90
        tem = Template()
        # tem.send_data('opt_ccr', '不传ccr和scr', **tem.change_data)
        engineid = tem.get_opt_engineid('opt_ccr', '不传ccr和scr',1)
        res = tem.get_opt_recipeInfo(engineid, 0)
        outpatient = res['data']['outpatient']
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        self.assertEqual(outpatient['ccr'], "90.0(预设值)")
        ids = [engineid]
        tem.audit_multi(1,*ids)
        res = tem.get_opt_recipeInfo(engineid, 1)
        self.assertEqual(res['data']['outpatient']['ccr'], "90.0(预设值)")

    def test_opt_two(self):
        # 25岁 男 mg/dl scr为9.00mg/dL
        tem = Template()
        cal_ccr = Ccr(tem.get_ymd(0, 0), '1994-03-05')
        # tem.send_data('opt_ccr', '传ccr_1.txt', **tem.change_data)
        engineid = tem.get_opt_engineid('opt_ccr', '传ccr_1.txt',1)
        res = tem.get_opt_recipeInfo(engineid,0)
        outpatient = res['data']['outpatient']
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        expect = cal_ccr.ccr_calculate(sex='男', unit='mg/dl', age=cal_ccr.y, weight=60, scr=9)
        print(expect)
        self.assertEqual(outpatient['ccr'],"10.6481(计算值)")
        ids = [engineid]
        tem.audit_multi(1,*ids)
        res = tem.get_opt_recipeInfo(engineid, 1)
        self.assertEqual(res['data']['outpatient']['ccr'], "10.6481(计算值)")
    def test_opt_03(self):
        # 25岁 女 mg/dl scr为9.00mg/dL
        tem = Template()
        cal_ccr = Ccr(tem.get_ymd(0, 0), '1994-03-05')
        # tem.send_data('opt_ccr', '传ccr_1.txt', **tem.change_data)
        engineid = tem.get_opt_engineid('opt_ccr', '3',1)
        res = tem.get_opt_recipeInfo(engineid,0)
        outpatient = res['data']['outpatient']
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        expect = cal_ccr.ccr_calculate(sex='女', unit='mg/dl', age=cal_ccr.y, weight=60, scr=9)
        print(expect)
        self.assertEqual(outpatient['ccr'],"9.0509(计算值)")
        ids = [engineid]
        tem.audit_multi(1,*ids)
        res = tem.get_opt_recipeInfo(engineid, 1)
        self.assertEqual(res['data']['outpatient']['ccr'], "9.0509(计算值)")

    def test_opt_04(self):
        # 25岁 男 umol/l scr为9.00umol/l
        tem = Template()
        cal_ccr = Ccr(tem.get_ymd(0, 0), '1994-03-05')
        # tem.send_data('opt_ccr', '传ccr_1.txt', **tem.change_data)
        engineid = tem.get_opt_engineid('opt_ccr', '4', 1)
        res = tem.get_opt_recipeInfo(engineid, 0)
        outpatient = res['data']['outpatient']
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        expect = cal_ccr.ccr_calculate(sex='男', unit='umol/L', age=cal_ccr.y, weight=60, scr=9)
        print(expect)
        self.assertEqual(outpatient['ccr'], "937.2453(计算值)")
        ids = [engineid]
        tem.audit_multi(1, *ids)
        res = tem.get_opt_recipeInfo(engineid, 1)
        self.assertEqual(res['data']['outpatient']['ccr'], "937.2453(计算值)")

    def test_opt_05(self):
        # 25岁 女 umol/l scr为9.00umol/l
        tem = Template()
        cal_ccr = Ccr(tem.get_ymd(0, 0), '1994-03-05')
        # tem.send_data('opt_ccr', '传ccr_1.txt', **tem.change_data)
        engineid = tem.get_opt_engineid('opt_ccr', '5', 1)
        res = tem.get_opt_recipeInfo(engineid, 0)
        outpatient = res['data']['outpatient']
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        expect = cal_ccr.ccr_calculate(sex='女', unit='umol/L', age=cal_ccr.y, weight=60, scr=9)
        print(expect)
        self.assertEqual(outpatient['ccr'], "796.6585(计算值)")
        ids = [engineid]
        tem.audit_multi(1, *ids)
        res = tem.get_opt_recipeInfo(engineid, 1)
        self.assertEqual(res['data']['outpatient']['ccr'], "796.6585(计算值)")
    def test_opt_06(self):
        # 19岁 男 umol/l scr为9.00umol/l  --测试不通过
        tem = Template()
        cal_ccr = Ccr(tem.get_ymd(0, 0), '2000-03-05')
        # tem.send_data('opt_ccr', '传ccr_1.txt', **tem.change_data)
        engineid = tem.get_opt_engineid('opt_ccr', '6', 1)
        res = tem.get_opt_recipeInfo(engineid, 0)
        outpatient = res['data']['outpatient']
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        expect = cal_ccr.ccr_default_weight(sex='男', unit='umol/L', age=cal_ccr.y,  scr=9)
        print(expect)
        self.assertEqual(outpatient['ccr'], "986.1450(计算值)")
        ids = [engineid]
        tem.audit_multi(1, *ids)
        res = tem.get_opt_recipeInfo(engineid, 1)
        self.assertEqual(res['data']['outpatient']['ccr'], "986.1450(计算值)")

    def test_opt_07(self):
        # 19岁 女 umol/l scr为9.00umol/l
        tem = Template()
        cal_ccr = Ccr(tem.get_ymd(0, 0), '2000-03-05')
        # tem.send_data('opt_ccr', '传ccr_1.txt', **tem.change_data)
        engineid = tem.get_opt_engineid('opt_ccr', '7', 1)
        res = tem.get_opt_recipeInfo(engineid, 0)
        outpatient = res['data']['outpatient']
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        expect = cal_ccr.ccr_default_weight(sex='女', unit='umol/L', age=cal_ccr.y,  scr=9)
        print(expect)
        self.assertEqual(outpatient['ccr'], "698.5194(计算值)")
        ids = [engineid]
        tem.audit_multi(1, *ids)
        res = tem.get_opt_recipeInfo(engineid, 1)
        self.assertEqual(res['data']['outpatient']['ccr'], "698.5194(计算值)")

    def test_opt_three(self):
        tem = Template()
        tem.send_data('opt_ccr', '传scr但是检验已失效_1.txt', **tem.change_data)

    def test_opt_11(self):
        # scr不在检验有效期
        tem = Template()
        tem.send_data('opt_ccr', '1', **tem.change_data)

    def test_opt_12(self):
        # scr在检验有效期
        tem = Template()
        tem.send_data('opt_ccr', '2', **tem.change_data)

    def test_ipt_01(self):
        # ccr与scr都不传,则ccr取默认值90--测试通过
        tem = Template()
        # tem.send_data('ipt_ccr', '1', **tem.change_data)
        engineid = tem.get_ipt_engineid('ipt_ccr', '1', 1)
        print(engineid)
        res = tem.get_ipt_patient(engineid, 0)
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        patient = res['data']
        self.assertEqual(patient['ccr'], "90.0(预设值)")
        ids = [engineid]
        tem.audit_multi(3, *ids)
        res = tem.get_ipt_patient(engineid, 1)
        patient = res['data']
        self.assertEqual(patient['ccr'], "90.0(预设值)")

    def test_ipt_02(self):
        # 检验中传入不在检验有效期内的ccr,则ccr取默认值
        tem = Template()
        # tem.send_data('ipt_ccr', '2', **tem.change_data)
        engineid = tem.get_ipt_engineid('ipt_ccr', '2', 1)
        print(engineid)
        res = tem.get_ipt_patient(engineid, 0)
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        patient = res['data']
        self.assertEqual(patient['ccr'], "90.0(预设值)")
        ids = [engineid]
        tem.audit_multi(3, *ids)
        res = tem.get_ipt_patient(engineid, 1)
        patient = res['data']
        self.assertEqual(patient['ccr'], "90.0(预设值)")

    def test_ipt_06(self):
        # 检验中传入在检验有效期内的ccr,则ccr取传入值  --测试通过
        tem = Template()
        # tem.send_data('ipt_ccr', '5', **tem.change_data)
        engineid = tem.get_ipt_engineid('ipt_ccr', '5', 1)
        print(engineid)
        res = tem.get_ipt_patient(engineid, 0)
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        patient = res['data']
        self.assertEqual(patient['ccr'], "3.0")
        ids = [engineid]
        tem.audit_multi(3, *ids)
        res = tem.get_ipt_patient(engineid, 1)
        patient = res['data']
        self.assertEqual(patient['ccr'], "3.0")

    def test_ipt_03(self):
        # 同一患者两个任务，ccr需要能更新 --测试通过
        tem = Template()
        engineid1 = tem.get_ipt_engineid('ipt_ccr', 'a1', 1)  # 任务一，不传身高 体重 取身高/体重/ccr预设值
        res = tem.get_ipt_patient(engineid1, 0)
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        patient = res['data']
        self.assertEqual(patient['ccr'], "90.0(预设值)")
        tem.send_data('ipt_ccr', 'a2', **tem.change_data)  # 传patient+生命体征
        tem.send_data('ipt_ccr', 'a3', **tem.change_data)  # 再传生命体征
        engineid2 = tem.get_ipt_engineid('ipt_ccr', 'a4', 2)  # 任务二有scr，取a3的身高体重，且a3的体重去计算ccr
        res = tem.get_ipt_patient(engineid2, 0)
        patient = res['data']
        self.assertEqual(patient['ccr'], "38.0139(计算值)")
        ids = [engineid1, engineid2]
        tem.audit_multi(3, *ids)
        res = tem.get_ipt_patient(engineid1, 1)
        patient = res['data']
        self.assertEqual(patient['ccr'], "90.0(预设值)")
        res = tem.get_ipt_patient(engineid2, 1)
        patient = res['data']
        self.assertEqual(patient['ccr'], "38.0139(计算值)")

    def test_ipt_04(self):
        tem = Template()
        # 传入scr，但是性别为0 未知的性别，则ccr取默认值  --测试通过
        engineid = tem.get_ipt_engineid('ipt_ccr', '3', 1)
        print(engineid)
        res = tem.get_ipt_patient(engineid, 0)
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        patient = res['data']
        self.assertEqual(patient['ccr'], "90.0(预设值)")
        ids = [engineid]
        tem.audit_multi(3, *ids)
        res = tem.get_ipt_patient(engineid, 1)
        patient = res['data']
        self.assertEqual(patient['ccr'], "90.0(预设值)")

    def test_ipt_05(self):
        tem = Template()
        # 传入scr，但是性别为9 未说明的性别，则ccr取默认值 --测试通过
        engineid = tem.get_ipt_engineid('ipt_ccr', '4', 1)
        print(engineid)
        res = tem.get_ipt_patient(engineid, 0)
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        patient = res['data']
        self.assertEqual(patient['ccr'], "90.0(预设值)")
        ids = [engineid]
        tem.audit_multi(3, *ids)
        res = tem.get_ipt_patient(engineid, 1)
        patient = res['data']
        self.assertEqual(patient['ccr'], "90.0(预设值)")

    def test_ipt_07(self):
        # 同一xml就诊信息、生命体征都传身高体重，则取生命体征。非同一xml则就诊信息和生命体征取最新的一个
        tem = Template()
        tem.send_data('ipt_ccr', 'b1', **tem.change_data)
        engineid = tem.get_ipt_engineid('ipt_ccr', 'b2', 2)
        res = tem.get_ipt_patient(engineid, 0)
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        patient = res['data']
        self.assertEqual(patient['ccr'], "38.0139(计算值)")
        ids = [engineid]
        tem.audit_multi(3, *ids)
        res = tem.get_ipt_patient(engineid, 1)
        patient = res['data']
        self.assertEqual(patient['ccr'], "38.0139(计算值)")

    def test_ipt_08(self):
        # 检验增量传
        tem = Template()
        tem.send_data('ipt_ccr', 'c1', **tem.change_data)
        engineid = tem.get_ipt_engineid('ipt_ccr', 'c2', 1)
        res = tem.get_ipt_patient(engineid, 0)
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        patient = res['data']
        self.assertEqual(patient['ccr'], "38.0139(计算值)")
        ids = [engineid]
        tem.audit_multi(3, *ids)
        res = tem.get_ipt_patient(engineid, 1)
        patient = res['data']
        self.assertEqual(patient['ccr'], "38.0139(计算值)")

    def test_ipt_09(self):
        # 将生命体征数据作废，则体重只会从就诊信息取
        tem = Template()
        tem.send_data('ipt_ccr', 'd1', **tem.change_data)
        engineid = tem.get_ipt_engineid('ipt_ccr', 'c2', 1)
        res = tem.get_ipt_patient(engineid, 0)
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        patient = res['data']
        self.assertEqual(patient['ccr'], "38.0139(计算值)")
        ids = [engineid]
        tem.audit_multi(3, *ids)
        res = tem.get_ipt_patient(engineid, 1)
        patient = res['data']
        self.assertEqual(patient['ccr'], "38.0139(计算值)")
    def test_ipt_10(self):
        # 16岁 男 mg/dl scr为1.00mg/dL
        tem = Template()
        # tem.send_data('ipt_ccr', '6', **tem.change_data)
        cal_ccr = Ccr(tem.get_ymd(-1,0), '2003-03-05')
        c1 = cal_ccr.ccr_default_weight(sex='男', unit='mg/dl', age=cal_ccr.y, scr=1)
        print(c1)
        engineid = tem.get_ipt_engineid('ipt_ccr', '6', 1)
        res = tem.get_ipt_patient(engineid, 0)
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        self.assertEqual(res['data']['ccr'], "97.8222(计算值)")
        ids = [engineid]
        tem.audit_multi(3, *ids)
        res = tem.get_ipt_patient(engineid, 1)
        self.assertEqual(res['data']['ccr'], "97.8222(计算值)")
    def test_ipt_11(self):
        # 16岁 女 mg/dl scr为1.00mg/dL
        tem = Template()
        cal_ccr = Ccr(tem.get_ymd(-1,0), '2003-03-05')
        c1 = cal_ccr.ccr_default_weight(sex='女', unit='mg/dl', age=cal_ccr.y, scr=1)
        print(c1)
        engineid = tem.get_ipt_engineid('ipt_ccr', '7', 1)
        res = tem.get_ipt_patient(engineid, 0)
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        self.assertEqual(res['data']['ccr'], "73.1505(计算值)")
        ids = [engineid]
        tem.audit_multi(3, *ids)
        res = tem.get_ipt_patient(engineid, 1)
        self.assertEqual(res['data']['ccr'], "73.1505(计算值)")

    def test_ipt_12(self):
        # 19岁 男 mg/dl scr为1.00mg/dL
        tem = Template()
        cal_ccr = Ccr(tem.get_ymd(-1,0), '2000-03-05')
        c1 = cal_ccr.ccr_default_weight(sex='男', unit='mg/dl', age=cal_ccr.y, scr=1)
        print(c1)
        engineid = tem.get_ipt_engineid('ipt_ccr', '8', 1)
        res = tem.get_ipt_patient(engineid, 0)
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        self.assertEqual(res['data']['ccr'], "100.8333(计算值)")
        ids = [engineid]
        tem.audit_multi(3, *ids)
        res = tem.get_ipt_patient(engineid, 1)
        self.assertEqual(res['data']['ccr'], "100.8333(计算值)")

    def test_ipt_13(self):
        # 19岁 女 mg/dl scr为1.00mg/dL
        tem = Template()
        cal_ccr = Ccr(tem.get_ymd(-1,0), '2000-03-05')
        c1 = cal_ccr.ccr_default_weight(sex='女', unit='mg/dl', age=cal_ccr.y, scr=1)
        print(c1)
        engineid = tem.get_ipt_engineid('ipt_ccr', '9', 1)
        res = tem.get_ipt_patient(engineid, 0)
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        self.assertEqual(res['data']['ccr'], "71.4236(计算值)")
        ids = [engineid]
        tem.audit_multi(3, *ids)
        res = tem.get_ipt_patient(engineid, 1)
        self.assertEqual(res['data']['ccr'], "71.4236(计算值)")


    def test_ipt_14(self):
        # 3岁 女 mg/dl scr为1.00mg/dL   <4岁,返回预设值
        tem = Template()
        engineid = tem.get_ipt_engineid('ipt_ccr', '10', 1)
        res = tem.get_ipt_patient(engineid, 0)
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        self.assertEqual(res['data']['ccr'], "90.0(预设值)")
        ids = [engineid]
        tem.audit_multi(3, *ids)
        res = tem.get_ipt_patient(engineid, 1)
        self.assertEqual(res['data']['ccr'], "90.0(预设值)")

    def test_ipt_15(self):
        # 3岁 男 mg/dl scr为1.00mg/dL   <4岁,返回预设值
        tem = Template()
        engineid = tem.get_ipt_engineid('ipt_ccr', '11', 1)
        res = tem.get_ipt_patient(engineid, 0)
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        self.assertEqual(res['data']['ccr'], "90.0(预设值)")
        ids = [engineid]
        tem.audit_multi(3, *ids)
        res = tem.get_ipt_patient(engineid, 1)
        self.assertEqual(res['data']['ccr'], "90.0(预设值)")

    def test_ipt_16(self):
        # 16岁 男  scr为1.00umol/L
        tem = Template()
        # tem.send_data('ipt_ccr', '6', **tem.change_data)
        cal_ccr = Ccr(tem.get_ymd(-1,0), '2003-03-05')
        c1 = cal_ccr.ccr_default_weight(sex='男', unit='umol/L', age=cal_ccr.y, scr=1)
        print(c1)
        engineid = tem.get_ipt_engineid('ipt_ccr', '12', 1)
        res = tem.get_ipt_patient(engineid, 0)
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        self.assertEqual(res['data']['ccr'], "8610.2689(计算值)")
        ids = [engineid]
        tem.audit_multi(3, *ids)
        res = tem.get_ipt_patient(engineid, 1)
        self.assertEqual(res['data']['ccr'], "8610.2689(计算值)")
    def test_ipt_17(self):
        # 16岁 女 umol/L scr为1.00umol/L
        tem = Template()
        cal_ccr = Ccr(tem.get_ymd(-1,0), '2003-03-05')
        c1 = cal_ccr.ccr_default_weight(sex='女', unit='umol/L', age=cal_ccr.y, scr=1)
        print(c1)
        engineid = tem.get_ipt_engineid('ipt_ccr', '13', 1)
        res = tem.get_ipt_patient(engineid, 0)
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        self.assertEqual(res['data']['ccr'], "6438.6773(计算值)")
        ids = [engineid]
        tem.audit_multi(3, *ids)
        res = tem.get_ipt_patient(engineid, 1)
        self.assertEqual(res['data']['ccr'], "6438.6773(计算值)")

    def test_ipt_18(self):
        # scr传错误单位,返回预设值
        tem = Template()
        engineid = tem.get_ipt_engineid('ipt_ccr', '14', 1)
        res = tem.get_ipt_patient(engineid, 0)
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        self.assertEqual(res['data']['ccr'], "90.0(预设值)")
        ids = [engineid]
        tem.audit_multi(3, *ids)
        res = tem.get_ipt_patient(engineid, 1)
        self.assertEqual(res['data']['ccr'], "90.0(预设值)")
    def test_ipt_19(self):
        # scr传错误单位,返回预设值
        tem = Template()

        tem.send_data('ipt_ccr', '16', **tem.change_data)
        tem.send_data('ipt_ccr', '15', **tem.change_data)
        # engineid = tem.get_ipt_engineid('ipt_ccr', '16', 1)
        # res = tem.get_ipt_patient(engineid, 0)
        # print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        # self.assertEqual(res['data']['ccr'], "90.0(预设值)")
        # ids = [engineid]
        # tem.audit_multi(3, *ids)
        # res = tem.get_ipt_patient(engineid, 1)
        # self.assertEqual(res['data']['ccr'], "90.0(预设值)")
    def test_ipt_20(self):
        # scr传错误单位,返回预设值
        tem = Template()
        tem.send_data('ipt_ccr','17',**tem.change_data)








if __name__ == '__main__':
    suite = unittest.TestSuite()  # 创建一个测试集合
    # suite.addTest(TestCcr("test_opt_one"))
    # suite.addTest(TestCcr("test_opt_two"))
    # suite.addTest(TestCcr("test_opt_three"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
