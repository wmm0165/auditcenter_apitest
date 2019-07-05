# -*- coding: utf-8 -*-
# @Time    : 2019/6/6 14:03
# @Author  : wangmengmeng

import os
import unittest
from common.template import Template
import json
import datetime
import time
import random


class TestSend(unittest.TestCase):
    group_no = random.randint(1, 1000000)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    now_ts = int(time.mktime(time.strptime(now, "%Y-%m-%d %H:%M:%S"))) * 1000
    yest = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d %H:%M:%S")
    yest_ts = int(time.mktime(time.strptime(yest, "%Y-%m-%d %H:%M:%S"))) * 1000
    yest_raw = (datetime.datetime.now() + datetime.timedelta(days=-1))
    yest_front_onehour = (yest_raw + datetime.timedelta(hours=-1)).strftime("%Y-%m-%d %H:%M:%S")
    yest_front_onehour_ts = int(time.mktime(time.strptime(yest_front_onehour, "%Y-%m-%d %H:%M:%S"))) * 1000
    yest_front_twohour = (yest_raw + datetime.timedelta(hours=-2)).strftime("%Y-%m-%d %H:%M:%S")
    yest_front_twohour_ts = int(time.mktime(time.strptime(yest_front_twohour, "%Y-%m-%d %H:%M:%S"))) * 1000
    yest_front_threehour = (yest_raw + datetime.timedelta(hours=-3)).strftime("%Y-%m-%d %H:%M:%S")
    yest_front_threehour_ts = int(time.mktime(time.strptime(yest_front_threehour, "%Y-%m-%d %H:%M:%S"))) * 1000
    yest_front_fourhour = (yest_raw + datetime.timedelta(hours=-4)).strftime("%Y-%m-%d %H:%M:%S")
    yest_front_fourhour_ts = int(time.mktime(time.strptime(yest_front_fourhour, "%Y-%m-%d %H:%M:%S"))) * 1000
    yest_behind_onehour = (yest_raw + datetime.timedelta(hours=+1)).strftime("%Y-%m-%d %H:%M:%S")
    yest_behind_onehour_ts = int(time.mktime(time.strptime(yest_front_onehour, "%Y-%m-%d %H:%M:%S"))) * 1000

    change = {"{{ts}}": str(now_ts),
              "{{t}}": str(yest_ts),
              "{{d}}": str(yest),
              "{{tf4}}": str(yest_front_fourhour_ts),
              "{{df4}}": str(yest_front_fourhour),
              "{{tb1}}": str(yest_behind_onehour_ts),
              "{{db1}}": str(yest_behind_onehour),
              "{{gp}}": str(group_no)}
    tem = Template()

    def setUp(self):
        print("开始执行用例...")
    def tearDown(self):
        print("结束执行用例...")

    def test_get_engineid(self):
        # 发送数据
        self.tem.send_data('body_xml_1.xml', **TestSend.change)
        self.tem.send_data('body_xml_2.txt', **TestSend.change)
        self.tem.send_data('body_xml_3.txt', **TestSend.change)
        time.sleep(10)
        # 查询待审列表，获取引擎id（注意：右侧待审任务只能展示10条，所以10条之外的数据查询不到）
        param = {}
        res2 = self.tem.post_json('http://10.1.1.89:9999/auditcenter/api/v1/opt/selNotAuditOptList', param)
        self.length = len(res2['data']['optRecipeList'])
        for i in range(0, self.length):
            engine_key = ''
            record = res2['data']['optRecipeList'][i]
            if record['optRecipe']['patientId'] == str(TestSend.now_ts):
                engine_key = record['optRecipe']['id']
                # print(engine_key)
            self.id_test = engine_key
            print(self.id_test)
            globals()['engine'] = self.id_test
            # 查询处方信息

    def test_query(self):
        global engine
        url = 'http://10.1.1.89:9999/auditcenter/api/v1/opt/recipeInfo/' + str(engine)
        res = self.tem.get(url)



if __name__ == '__main__':
    unittest.main(verbosity=2)  # 运行所有用例
    # test = TestSend()
    # test.test_send()
