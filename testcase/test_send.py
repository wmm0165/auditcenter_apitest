# -*- coding: utf-8 -*-
# @Time    : 2019/6/6 14:03
# @Author  : wangmengmeng

import os
import unittest
from common.login import Login
import json
import datetime
import time
import random

xml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'body_xml.txt')
print(xml_path)


class TestSend():
    group_no = random.randint(1, 1000000)
    today_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 今天当前时间
    today_now_ts = int(time.mktime(time.strptime(today_now, "%Y-%m-%d %H:%M:%S"))) * 1000  # 今天当前时间的时间戳
    change = {"{{eno}}": str(today_now_ts), "{{pid}}": str(today_now_ts), "{{ts}}": str(today_now_ts),
              "{{gp}}": str(group_no),
              "{{d2}}": str(today_now)}

    def __init__(self):
        login = Login()
        self.session = login.get_session()

    def test_send(self):

        url = "http://10.1.1.89:9999/auditcenter/api/v1/auditcenter"
        headers = {"Content-Type": "text/plain"}
        with open(xml_path, encoding="utf-8") as fp:
            body = fp.read()
        ss = body
        for k in TestSend.change:
            ss = ss.replace(k, TestSend.change[k])
        print(ss)
        res = self.session.post(url=url, data=ss.encode("utf-8"), headers=headers).json()
        print(res)
        # self.assertEquals(res['code'], '200')
        url_start_sf = 'http://10.1.1.89:9999/auditcenter/api/v1/startAuditWork'
        res1= self.session.get(url = url_start_sf)
        time.sleep(10)

        url_wait = 'http://10.1.1.89:9999/auditcenter/api/v1/opt/selNotAuditOptList'
        headers = {"Content-Type": "application/json"}
        param = {}
        res2 = self.session.post(url=url_wait, data=json.dumps(param), headers=headers).json()

        print(res2)
        print(res2['data']['optRecipeList'])
        self.len = len(res2['data']['optRecipeList'])
        for i in range(0,self.len):
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
