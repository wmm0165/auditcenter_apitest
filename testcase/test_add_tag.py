import unittest
import requests
import json
import sys
import os
from common.login import Login


class TestAddTag(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def test_add_tag_normal(self):
        login = Login()
        self.session = login.get_session()
        url = 'http://10.1.1.89:9999/auditcenter/api/v1/collect/addTag'
        params = {"tag": "收藏分类15"}
        headers = {'Content-Type': "application/json"}
        res = self.session.post(url, data=json.dumps(params), headers=headers).json()
        self.assertEquals (res['code'], '200')


if __name__ == '__main__':
    unittest.main(verbosity=2)  # 运行所有用例
