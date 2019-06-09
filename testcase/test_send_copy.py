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


class TestSend():
    group_no = random.randint(1, 1000000)
    today_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 今天当前时间
    today_now_ts = int(time.mktime(time.strptime(today_now, "%Y-%m-%d %H:%M:%S"))) * 1000  # 今天当前时间的时间戳
    change = {"{{eno}}": str(today_now_ts), "{{pid}}": str(today_now_ts), "{{ts}}": str(today_now_ts),
              "{{gp}}": str(group_no),
              "{{d2}}": str(today_now)}

    def __init__(self):
        self.tem = Template()

    def test_send(self):
        xml_name = 'body_xml.txt'
        res = self.tem.send_data(xml_name,**TestSend.change)
        print(res)
        wait_url = 'http://10.1.1.89:9999/auditcenter/api/v1/opt/selNotAuditOptList'
        param = {}
        res2 = self.tem.post_json(wait_url,param)
        print(res2)
        print(res2['data']['optRecipeList'])
        self.len = len(res2['data']['optRecipeList'])
        for i in range(0, self.len):
            engine_key = ''
            record = res2['data']['optRecipeList'][i]
            if record['optRecipe']['patientId'] == str(TestSend.today_now_ts):
                engine_key = record['optRecipe']['id']
                print(engine_key)
            id = engine_key
            print(id)


if __name__ == '__main__':
    # unittest.main(verbosity=2)  # 运行所有用例
    test = TestSend()
    test.test_send()
