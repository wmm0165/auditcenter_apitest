# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 16:34
# @Author  : wangmengmeng

import requests
import json


class Login():
    def __init__(self):
        url = 'http://10.1.1.89:9999/syscenter/api/v1/currentUser'
        params = {"name": "wangmm", "password": "e10adc3949ba59abbe56e057f20f883e"}
        headers = {'Content-Type': "application/json"}
        self.session = requests.session()
        self.session.post(url, data=json.dumps(params), headers=headers)

    def get_session(self):
        return self.session

if __name__ == '__main__':
    a = Login()
    res = a.get_session()
    print(res)