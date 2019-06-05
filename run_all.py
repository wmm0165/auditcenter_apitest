import unittest
import os
from common.HTMLTestReportCN import HTMLTestRunner

prj_path = os.path.dirname(os.path.abspath(__file__))  # 项目路径
testcase_path = os.path.join(prj_path, 'testcase')  # 测试用例路径
report_file = os.path.join(prj_path, 'report', 'report.html')
suite = unittest.defaultTestLoader.discover(testcase_path)
with open(report_file, 'wb') as f:  # 从配置文件中读取
    HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="wangmengmeng").run(suite)
