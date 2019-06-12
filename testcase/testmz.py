# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 17:24
# @Author  : wangmengmeng
from common.template import Template

a = Template()
res = a.send_data('test','body_xml_1.xml')
print(res)
