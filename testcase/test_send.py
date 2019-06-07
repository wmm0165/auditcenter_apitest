# -*- coding: utf-8 -*-
# @Time    : 2019/6/6 13:21
# @Author  : wangmengmeng
import unittest
import os
from common.login import Login
xml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config','body_xml.txt')
print(xml_path)
class TestSend(unittest.TestCase):

    def setUp(self):
        login = Login()
        self.session = login.get_session()

    def test_send(self):
        url = "http://10.1.1.89:9999/auditcenter/api/v1/auditcenter"
        headers = {"Content-Type": "text/plain"}
        with open(xml_path, encoding="utf-8") as fp:
            body = fp.read()
        res = self.session.post(url = url ,data = body.encode("utf-8") )
        print(res)


if __name__ == '__main__':
    unittest.main(verbosity=2)  # verbosity是一个选项,表示测试结果的信息复杂度，有三个值

