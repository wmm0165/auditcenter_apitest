# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 19:37
# @Author  : wangmengmeng
from config.read_config import ReadConfig
from common.template import Template
tem = Template()
cof = ReadConfig()
url = cof.get('login', 'address') + '/auditcenter' + cof.get('api', '处方详情审核通过')
param = {
    "optRecipeId": "99019",
    "auditResult": ""}

res = tem.post_json(url,param)
print(res)
