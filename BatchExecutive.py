#coding=utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
if __name__ == "__main__":
    #测试用例目录
    test_dir = r"C:\code\selenium_python"
    #加载测试用例
    discover = unittest.defaultTestLoader.discover(test_dir,'login*.py')
    report_path = "C:\\Users\\test\Desktop\\report\\report.html"
    with open(report_path,"wb") as report:
        runner = HTMLTestRunner(stream=report,
                                title="测试报告",
                                description="登录测试报告")
        runner.run(discover)
