# -*- coding: utf-8 -*-
# @Time : 2019/7/24 23:22
# @Author : wangmengmeng
from config.read_config import ReadConfig
from common.template import Template


class Chat:
    def __init__(self):
        self.tem = Template()
        cf = ReadConfig()
        self.audit_url = cf.get("auditcenter", "address")
        self.login_url = cf.get("login", "address")

    def doc_ipt_send(self, engineid, gp):
        """医生端住院发消息
        :param engineid: 引擎id
        :param gp: 组号
        """
        url = self.audit_url + "/api/v1/sendChatMessageNoLogin"
        param = {
            "hospitalCode": "H0003",
            "userId": "09",
            "source": "住院",
            "attachKey": engineid,
            "attachSecondKey": gp,
            "message": "这是医生消息",
            "userRole": "医生"
        }
        self.tem.post_json(url, param)

    def doc_opt_send(self, engineid):
        """
        医生端门诊发消息
        :param engineid: 引擎id
        """
        url = self.audit_url + "/api/v1/sendChatMessageNoLogin"
        param = {
            "hospitalCode": "H0003",
            "userId": "09",
            "source": "门诊",
            "attachKey": engineid,
            "message": "这是医生消息",
            "userRole": "医生"
        }
        self.tem.post_json(url, param)

    # 医生端获取消息
    def doc_ipt_query(self):
        url = self.audit_url + "/api/v1/queryChatMessageNoLogin?hospitalCode=%&userId=09&source=&attachKey=%&attachSecondKey=%s&t=%s"

    def doc_opt_query(self):
        url = self.audit_url + "/api/v1/queryChatMessageNoLogin?hospitalCode=%&userId=09&source=&attachKey=%s&attachSecondKey=%s&t=%s"
        return self.tem.get(url)

    # 药师端 查看未读消息列表
    def phar_notread(self):
        url = self.login_url + "/syscenter/api/v1/message/getMessages"
        param = {
            "page": 1,
            "pageSize": 9,
            "status": "STATUS_UNREAD"
        }
        self.tem.post_json(url, param)

    def ipt_chat_flag(self, engineid, gp):
        url = self.audit_url + "/api/v1/ipt/all/mergeEngineMsgList"
        param = {
            "engineId": engineid,
            "zoneId": 4,
            "groupNo": gp,
            "medicalIds": [7041],
            "medicalHisIds": ["o1_1563966321"],
            "herbMedicalIds": [],
            "herbMedicalHisIds": []
        }


"""
http://10.1.1.172:9999/auditcenter/api/v1/ipt/all/orderList?id=engineid
res['data'][gp][0]['id']
res['data'][gp][0]['orderId']
"""


def opt_chat_flag(self, recipeId, id, type):
    """
    获取记录按钮是否展示标识
    :param recipeId:  第一次跑引擎的engineid
    :param id:  第二次跑引擎的engineid
    :param type: type = 0代表待审页面，type = 1代表已审页面
    :return:
    """
    if type == 0:
        url = (self.audit_url + "/api/v1/opt/mergeAuditResult?recipeId=%s&id=%s") % (recipeId, id)
    else:
        url = (self.audit_url + "/api/v1/opt/all/mergeAuditResult?recipeId=%s&id=%s") % (recipeId, id)
    return self.tem.get(url)


def phar_ipt_send(self, engineid, gp):
    url = self.audit_url + "/api/v1/sendChatMessage"
    param = {
        "zoneId": 4,
        "category": 3,
        "attachKey": engineid,
        "attachSecondKey": gp,
        "message": "这是药师消息",
        "userRole": "药师"
    }
    self.tem.post_json(url, param)


def phar_opt_send(self, engineid):
    url = self.audit_url + "/api/v1/sendChatMessage"
    param = {
        "zoneId": 4,
        "category": 1,
        "attachKey": engineid,
        "message": "这是药师消息",
        "userRole": "药师"
    }
    self.tem.post_json(url, param)


# 药师端 查看记录列表
def phar_query_chat(self, engineid):
    url = (self.audit_url + "/api/v1/queryChatMessage?category=1&zoneId=4&attachKey=%s") % (engineid)
    return self.tem.get(url)
