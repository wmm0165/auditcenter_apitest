# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 17:24
# @Author  : wangmengmeng
from common.template import Template


class TestMz:
    def __init__(self):
        self.t = Template()

    def testmz(self):
        # self.t.send_data('body_xml_2.txt', **self.t.change_data)
        res = self.t.opt_audit('body_xml_2.txt', '2')
        print(res)


if __name__ == '__main__':
    a = TestMz()
    a.testmz()
