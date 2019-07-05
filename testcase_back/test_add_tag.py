# -*- coding: utf-8 -*-
# @Time    : 2019/6/6 13:21
# @Author  : wangmengmeng
import json
import unittest
from common.template import Template

from common.login import Login


class TestAddTag(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def test_add_tag_normal(self):
        temp = Template()
        url = 'http://10.1.1.89:9999/auditcenter/api/v1/collect/addTag'
        params = {"tag": "abc1234555610ww"}
        res = temp.post_json(url,params)
        print(res)
        self.assertEquals(res['code'], '200')


if __name__ == '__main__':
    unittest.main(verbosity=2)  # 运行所有用例
