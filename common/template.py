# -*- coding: utf-8 -*-
# @Time : 2019/6/8 21:40
# @Author : wangmengmeng
import requests
import json
from config.read_config import ReadConfig
import hashlib
import os


class Template:
    def __init__(self):
        self.conf = ReadConfig()
        url = self.conf.get('login', 'address') + '/syscenter/api/v1/currentUser'
        username = self.conf.get('login', 'username')
        passwd = self.conf.get('login', 'password')
        m = hashlib.md5()  # 创建md5对象
        m.update(passwd.encode())  # 生成加密字符串
        password = m.hexdigest()
        params = {"name": username, "password": password}
        headers = {'Content-Type': "application/json"}
        self.session = requests.session()
        # self.session.post(url, data=json.dumps(params), headers=headers)
        res = self.session.post(url, data=json.dumps(params), headers=headers).json()  # 登录用户中心
        start_sf_url = self.conf.get('login', 'address') + '/auditcenter/api/v1/startAuditWork'  # 获取开始审方url
        self.session.get(url=start_sf_url)  # 开始审方

    # def get_session(self):
    #     return self.session

    def post_json(self, url, para):
        data = para
        data = json.dumps(data)
        headers = {"Content-Type": "application/json"}
        return self.session.post(url, data=data, headers=headers).json()

    def get(self, url):
        return self.session.get(url).json()

    def send_data(self, xml_name, **change):
        # url = "http://10.1.1.89:9999/auditcenter/api/v1/auditcenter"
        xml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', xml_name)
        print(xml_path)
        send_data_url = self.conf.get('login', 'address') + '/auditcenter/api/v1/auditcenter'
        headers = {"Content-Type": "text/plain"}
        with open(xml_path, encoding="utf-8") as fp:
            body = fp.read()
        ss = body
        for k in change:
            ss = ss.replace(k, change[k])
        print(ss)
        return self.session.post(url=send_data_url, data=ss.encode("utf-8"), headers=headers).json()


if __name__ == '__main__':
    t = Template()
    change = {"{{eno}}": "a", "{{pid}}": "b", "{{ts}}": "c",
              "{{gp}}": "d",
              "{{d2}}": "e"}
    xml_name = 'body_xml.txt'
    t.send_data(xml_name, **change)
