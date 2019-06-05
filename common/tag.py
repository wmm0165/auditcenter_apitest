# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 17:08
# @Author  : wangmengmeng

from common.login import Login
import json


class Tag():
    def __init__(self):
        login = Login()
        self.session = login.get_session()

    def add_tag(self):
        url = 'http://10.1.1.89:9999/auditcenter/api/v1/collect/addTag'
        params = {"tag": "收藏分类7"}
        headers = {'Content-Type': "application/json"}
        res = self.session.post(url, data=json.dumps(params), headers=headers).json()
        print(res)


if __name__ == '__main__':
    tag = Tag()
    tag.add_tag()
