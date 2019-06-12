# -*- coding: utf-8 -*-
# @Time : 2019/6/8 21:40
# @Author : wangmengmeng
import datetime
import hashlib
import json
import os
import random
import re
import time

import requests

from config.read_config import ReadConfig


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
        group_no = random.randint(1, 1000000)
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.now_ts = int(time.mktime(time.strptime(now, "%Y-%m-%d %H:%M:%S"))) * 1000
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

        self.change_data = {"{{ts}}": str(self.now_ts),
                            "{{t}}": str(yest_ts),
                            "{{d}}": str(yest),
                            "{{tf4}}": str(yest_front_fourhour_ts),
                            "{{df4}}": str(yest_front_fourhour),
                            "{{tb1}}": str(yest_behind_onehour_ts),
                            "{{db1}}": str(yest_behind_onehour),
                            "{{gp}}": str(group_no),
                            "{{df6}}": str(yest_front_fourhour),
                            "{{df3}}": str(yest_front_fourhour),
                            "{{df2}}": str(yest_front_fourhour),
                            "{{df1}}": str(yest_front_fourhour),
                            "{{dt}}": str(yest_front_fourhour)
                            }

    # def get_session(self):
    #     return self.session

    def post_json(self, url, para):
        data = para
        data = json.dumps(data)
        headers = {"Content-Type": "application/json"}
        return self.session.post(url, data=data.encode("utf-8"), headers=headers).json()

    def get(self, url):
        return self.session.get(url).json()

    def send_data(self, dir_name, xml_name, **change):
        # url = "http://10.1.1.89:9999/auditcenter/api/v1/auditcenter"
        xml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', dir_name, xml_name)
        send_data_url = self.conf.get('login', 'address') + '/auditcenter/api/v1/auditcenter'
        headers = {"Content-Type": "text/plain"}
        print(xml_path)
        with open(xml_path, encoding="utf-8") as fp:
            body = fp.read()
        ss = body
        for k in change:
            ss = ss.replace(k, change[k])
        print(ss)
        return self.session.post(url=send_data_url, data=ss.encode("utf-8"), headers=headers)

    # 查询待审列表，获取引擎id（注意：右侧待审任务只能展示10条，所以10条之外的数据查询不到）
    def get_opt_engineid(self, dir_name, xml_name):
        self.send_data(dir_name, xml_name, **self.change_data)
        time.sleep(5)
        num = re.findall('\d+', xml_name)  # 获取文件名中的数字
        recipeno = 'r' + ''.join(num) + '_' + self.change_data['{{ts}}']
        param = {
            "recipeNo": recipeno
        }
        url = self.conf.get('login', 'address') + '/auditcenter' + self.conf.get('api', '查询待审门诊任务列表')
        res = self.post_json(url, param)
        print(res)
        print(res['data']['optRecipeList'][0]['optRecipe']['id'])
        return res['data']['optRecipeList'][0]['optRecipe']['id']

    def opt_audit(self, xml_name, audit_type):
        engineid = self.get_opt_engineid(xml_name)
        url = ''
        param = {}

        if audit_type == '2':
            url = self.conf.get('login', 'address') + '/auditcenter' + self.conf.get('api', '处方详情审核通过')
            param = {
                "optRecipeId": engineid,
                "auditResult": ""
            }
        elif audit_type == 0:
            url = self.conf.get('login', 'address') + '/auditcenter' + self.conf.get('api', '处方详情审核打回')
            param = {
                "optRecipeId": engineid,
                "auditResult": "打回必须修改",
                "operationRecordList": [],
                "messageStatus": 0
            }
        elif audit_type == 1:
            url = self.conf.get('login', 'address') + '/auditcenter' + self.conf.get('api', '处方详情审核打回')
            param = {
                "optRecipeId": engineid,
                "auditResult": "打回可双签",
                "operationRecordList": [],
                "messageStatus": 1
            }
        self.post_json(url, param)

    # def doc_audit(self):


if __name__ == '__main__':
    t = Template()
    t.opt_audit('body_xml_2.txt', '2')
    # t.get_opt_engineid('body_xml_2.txt')
