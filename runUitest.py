#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/18 11:57 上午
# @Author : wyf
# @File : runUitest.py
# @Software: PyCharm

from Library import CommonMethod,HTMLTestRunner2,SendEmail
import unittest,os
dirPath=CommonMethod.getPath()+"/report/uiReport/"
if not os.path.exists(dirPath):
    os.makedirs(dirPath)
reportname=CommonMethod.getNowTime()+"_uireport.html"
filepath=dirPath+reportname
cases_dir="ui_test.ui_cases"
def Testrunner():
    '''
    start_dir 表示用例的目录 pattern 表示匹配什么样的文件搜索测试用例
    :return:
    '''
    try:
        discover=unittest.defaultTestLoader.discover(start_dir=cases_dir,pattern='test_*.py') # 定义一个discover对象
    except Exception:
        print('测试案例加载失败')
        from traceback import print_exc
        print_exc()
    print(u">>>>>>>>>>>>>>>>>>>>>>>>开始运行UI自动化测试>>>>>>>>>>>>>>>>>>>>>>>>")
    fp=open(filepath,'wb')
    runner=HTMLTestRunner2.HTMLTestRunner(
        stream=fp,
        title=u'UI自动化测试报告',
        description=u'智慧信贷项目'
    )
    runner.run(discover)
    print(u">>>>>>>>>>>>>>>>>>>>>>>>UI自动化测试结束>>>>>>>>>>>>>>>>>>>>>>>>")

if __name__ == '__main__':
    CommonMethod.deleteReport(1)    #删除一天前的ui测试报告 1 表示ui自动化测试报告
    Testrunner()                    ##自动化运行
    SendEmail.sendEmail().sendEmailFun(1)  # 发送邮件,0：接口自动化  1. ui自动化




