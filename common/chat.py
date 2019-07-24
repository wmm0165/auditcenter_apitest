# -*- coding: utf-8 -*-
# @Time : 2019/7/24 23:22
# @Author : wangmengmeng
from config.read_config import ReadConfig
from common.template import Template


class Chat:
    # 医生端发消息
    # 医生端获取消息
    def doc_chat_mes(self):
        url = "http://10.1.1.172:9999/auditcenter/api/v1/queryChatMessageNoLogin?hospitalCode=H0003&userId=09&source=%E4%BD%8F%E9%99%A2&attachKey=4047&attachSecondKey=863102&t=1563982240554"

    # 药师端 查看未读消息列表
    # 药师端 查看详情是否有记录
    # 药师端 查看记录列表
