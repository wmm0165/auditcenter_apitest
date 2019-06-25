# -*- coding: utf-8 -*-
# @Time : 2019/6/8 21:40
# @Author : wangmengmeng
import datetime
from hashlib import md5
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
        url_yzm = "http://10.1.1.94:10000/api/v1/magicno"
        url = 'http://10.1.1.94:10000/api/v1/login'
        # username = self.conf.get('login', 'username')
        headers = {'Content-Type': "application/json"}
        self.session = requests.session()
        res_yzm = self.get(url_yzm)  # 获取验证码,加密方式为md5(salt)
        print(res_yzm)
        salt = res_yzm['data']
        print(salt)
        pwd = '123456'
        password = self.create_md5(pwd, salt)
        # m = hashlib.md5()  # 创建md5对象
        # m.update(passwd.encode())  # 生成加密字符串
        # password = m.hexdigest()
        print(password)
        params = {"name": "wangmm", "password": password}
        res = self.session.post(url, data=json.dumps(params), headers=headers).json()  # 登录用户中心
        print(res)
        start_sf_url = self.conf.get('login', 'address') + '/auditcenter/api/v1/startAuditWork'  # 获取开始审方url
        self.session.get(url=start_sf_url)  # 开始审方
        group_no = random.randint(1, 1000000)
        cgroup_no = random.randint(1, 1000000)
        self.now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.now_ts = int(time.mktime(time.strptime(self.now, "%Y-%m-%d %H:%M:%S"))) * 1000
        yest = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d %H:%M:%S")
        yest_ts = int(time.mktime(time.strptime(yest, "%Y-%m-%d %H:%M:%S"))) * 1000
        yest_raw = (datetime.datetime.now() + datetime.timedelta(days=-1))
        self.yest_front_onehour = (yest_raw + datetime.timedelta(hours=-1)).strftime("%Y-%m-%d %H:%M:%S")
        yest_front_onehour_ts = int(time.mktime(time.strptime(self.yest_front_onehour, "%Y-%m-%d %H:%M:%S"))) * 1000
        self.yest_front_twohour = (yest_raw + datetime.timedelta(hours=-2)).strftime("%Y-%m-%d %H:%M:%S")
        yest_front_twohour_ts = int(time.mktime(time.strptime(self.yest_front_twohour, "%Y-%m-%d %H:%M:%S"))) * 1000
        self.yest_front_threehour = (yest_raw + datetime.timedelta(hours=-3)).strftime("%Y-%m-%d %H:%M:%S")
        yest_front_threehour_ts = int(time.mktime(time.strptime(self.yest_front_threehour, "%Y-%m-%d %H:%M:%S"))) * 1000
        yest_front_fourhour = (yest_raw + datetime.timedelta(hours=-4)).strftime("%Y-%m-%d %H:%M:%S")
        yest_front_fourhour_ts = int(time.mktime(time.strptime(yest_front_fourhour, "%Y-%m-%d %H:%M:%S"))) * 1000
        yest_behind_onehour = (yest_raw + datetime.timedelta(hours=+1)).strftime("%Y-%m-%d %H:%M:%S")
        yest_behind_onehour_ts = int(time.mktime(time.strptime(self.yest_front_onehour, "%Y-%m-%d %H:%M:%S"))) * 1000

        self.change_data = {"{{ts}}": str(self.now_ts),
                            "{{t}}": str(yest_ts),
                            "{{d}}": str(yest),
                            "{{tf4}}": str(yest_front_fourhour_ts),
                            "{{df4}}": str(yest_front_fourhour),
                            "{{tb1}}": str(yest_behind_onehour_ts),
                            "{{db1}}": str(yest_behind_onehour),
                            "{{gp}}": str(group_no),
                            "{{cgp}}": str(cgroup_no),
                            "{{df6}}": str(yest_front_fourhour),
                            "{{df3}}": str(self.yest_front_threehour),
                            "{{df2}}": str(self.yest_front_twohour),
                            "{{df1}}": str(self.yest_front_onehour),
                            "{{dt}}": str(self.now)
                            }

    # def get_session(self):
    #     return self.session
    def create_md5(self,pwd, salt):
        md5_obj = md5()
        md5_obj.update((pwd + salt).encode())
        return md5_obj.hexdigest()

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

    def doc(self, dir_name, xml_name, **change):
        xml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', dir_name, xml_name)
        url = self.conf.get('auditcenter', 'address') + self.conf.get('api', '医生双签')
        headers = {"Content-Type": "text/plain"}
        print(xml_path)
        with open(xml_path, encoding="utf-8") as fp:
            body = fp.read()
        ss = body
        for k in change:
            ss = ss.replace(k, change[k])
        print(ss)
        return self.session.post(url=url, data=ss.encode("utf-8"), headers=headers)

    # 查询待审列表，获取引擎id（注意：右侧待审任务只能展示10条，所以10条之外的数据查询不到）
    def get_opt_engineid(self, dir_name, xml_name):
        self.send_data(dir_name, xml_name, **self.change_data)
        time.sleep(5)
        num = re.findall('\d+', xml_name)  # 获取文件名中的数字
        recipeno = 'r' + ''.join(num) + '_' + self.change_data['{{ts}}']
        param = {
            "recipeNo": recipeno
        }
        url = self.conf.get('auditcenter', 'address') + self.conf.get('api', '查询待审门诊任务列表')
        res = self.post_json(url, param)
        # print(res)
        # print(res['data']['optRecipeList'][0]['optRecipe']['id'])
        return res['data']['optRecipeList'][0]['optRecipe']['id']

    # 根据patient_id查询待审列表获取引擎id，count=1时，取该患者第二条数据的engineid,count=2时，取该患者第二条数据的engineid
    def get_ipt_engineid(self, dir_name, xml_name, count):
        self.send_data(dir_name, xml_name, **self.change_data)
        time.sleep(5)
        param = {
            "patientId": self.change_data['{{ts}}']
        }
        url = self.conf.get('auditcenter', 'address') + self.conf.get('api', '查询待审住院任务列表')
        res = self.post_json(url, param)
        print(res)
        engineid = ''
        if count == 1:
            engineid = res['data']['engineInfos'][0]['id']
        elif count == 2:
            engineid = res['data']['engineInfos'][1]['id']
        return engineid

    def opt_audit(self, dir_name, xml_name, audit_type):
        engineid = self.get_opt_engineid(dir_name, xml_name)
        url = ''
        param = {}
        # 处方详情审核通过
        if audit_type == '2':
            url = self.conf.get('login', 'address') + '/auditcenter' + self.conf.get('api', '处方详情审核通过')
            param = {
                "optRecipeId": engineid,
                "auditResult": ""
            }
        # 处方详情审核打回
        elif audit_type == 0:
            url = self.conf.get('login', 'address') + '/auditcenter' + self.conf.get('api', '处方详情审核打回')
            param = {
                "optRecipeId": engineid,
                "auditResult": "打回必须修改",
                "operationRecordList": [],
                "messageStatus": 0
            }
        # 处方详情审核打回（可双签）
        elif audit_type == 1:
            url = self.conf.get('login', 'address') + '/auditcenter' + self.conf.get('api', '处方详情审核打回')
            param = {
                "optRecipeId": engineid,
                "auditResult": "打回可双签",
                "operationRecordList": [],
                "messageStatus": 1
            }
        self.post_json(url, param)

    # 待审列表批量通过，audit_type = 1指门急诊，audit_type = 3指住院
    def audit_multi(self, audit_type, *ids):
        url = self.conf.get('auditcenter', 'address') + self.conf.get('api', '待审列表批量通过')
        param = {
            "ids": ids,
            "auditType": audit_type,
            "auditWay": 2
        }
        self.post_json(url, param)

    def ipt_audit(self, gp, engineid, audit_type):
        url = self.conf.get('auditcenter', 'address') + self.conf.get('api', '医嘱详情审核')
        # 医嘱详情审核打回
        if audit_type == 0:
            param = {
                "groupOrderList": [{
                    "auditBoList": [],
                    "groupNo": gp,
                    "auditInfo": "必须修改",
                    "auditStatus": 0,
                    "engineId": engineid,
                    "orderType": 1
                }]
            }
        # 医嘱详情审核打回（可双签）
        elif audit_type == 1:
            param = {
                "groupOrderList": [{
                    "auditBoList": [],
                    "groupNo": gp,
                    "auditInfo": "打回可双签",
                    "auditStatus": 0,
                    "engineId": engineid,
                    "orderType": 1,
                    "messageStatus": 1
                }]
            }
        # 医嘱详情审核通过
        elif audit_type == 2:
            param = {
                "groupOrderList": [{
                    "auditBoList": [],
                    "groupNo": gp,
                    "auditInfo": "审核通过",
                    "auditStatus": 1,
                    "engineId": engineid,
                    "orderType": 1
                }]
            }


if __name__ == '__main__':
    t = Template()
    # ids = [99098]
    # t.audit_multi(1, *ids)
