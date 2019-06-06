# -*- coding: utf-8 -*-
# @Time    : 2019/6/6 14:03
# @Author  : wangmengmeng

import os
import unittest
import xmltodict
from common.login import Login
import json
xml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'body_xml.txt')
print(xml_path)


class Test():
    def test_send(self):
        login = Login()
        self.session = login.get_session()
        url = "http://10.1.1.89:9999/auditcenter/api/v1/auditcenter"
        headers = {"Content-Type": "text/plain"}
        with open(xml_path, encoding="utf-8") as fp:
            body = fp.read()
            ss = body.replace("{{code}}","aaa")

        
        print("-----"+ss)
        # json_str = json.dumps(xmltodict.parse(body,encoding= 'utf-8'))
        # print(json_str)


        res = self.session.post(url=url, data=body.encode("utf-8"),headers = headers).json()
        print(res)


if __name__ == '__main__':
    test = Test()
    test.test_send()
