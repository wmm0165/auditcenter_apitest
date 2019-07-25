# -*- coding: utf-8 -*-
# @Time : 2019/7/11 15:31
# @Author : wangmengmeng
import unittest
import json
import warnings
import time
from common.template_2_x import Template
from common.logger import Logger
from common.calculate_ccr import Ccr


class TestIm(unittest.TestCase):
    log = Logger("TestIm")

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.log.get_log().debug("开始执行用例TestIm...")

    def tearDown(self):
        self.log.get_log().debug("结束执行用例TestIm...")

    def test_ipt_01(self):
        # 同患者产生两个任务，任务一是组a，任务二是组b和组a
        tem = Template()
        # tem.send_data('ipt_ccr', '15', **tem.change_data)
        # tem.send_data('ipt_ccr', '16', **tem.change_data)
        # engineid1 = tem.get_ipt_engineid("ipt","医嘱一",1)
        # engineid2 = tem.get_ipt_engineid("ipt","医嘱二",2)
        # gp = tem.change_data['{{gp}}']
        # print(gp)
        # tem.ipt_audit(gp, engineid1, 0)  # 审核打回任务一
        # 医生发送理由;这是医生理由哦
        # tem.chat_ipt_doc(engineid1)
        # 药师发送理由: 这是药师消息哦
        # tem.chat_pharm(3, engineid1)
        # 待审页面查看点击任务二，查看合并任务一，任务一有记录按钮且内容展示正确
        # 已审页面任务一有记录按钮且内容展示正确
        # res = tem.query_chat(3, 1, engineid1)
        # print(res)


if __name__ == '__main__':
    unittest.main()
