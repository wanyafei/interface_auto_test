#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/7/16 6:04 下午
# @Author : wyf
# @File : run.py
# @Software: pycharm
import  unittest,os
from Library import HTMLTestRunner2,CommonMethod,SendEmail
from api_test.api_create_pys import make_testcase
dirPath=CommonMethod.getPath()+"/report/apiReport/"
if not os.path.exists(dirPath):
    os.makedirs(dirPath)
reportname=CommonMethod.getNowTime()+"_report.html"
filepath=dirPath+reportname
alltestnames = []
alltestnames.append("api_test."+"api_cases.api_testcase")
isrerunerrors = False   #是否重跑失败用例开关
def Testsuite():
    suite = unittest.TestSuite()
    for test in alltestnames:
        try:
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))
        except Exception:
            print('error:Skipping tests from "%s".' %test)
            try:
                __import__(test)
            except ImportError:
                print ("could not import the test module")
            else:
                print ("could not import the test suite")
            from traceback import print_exc
            print_exc()
    print (u"------------------开始运行接口自动化测试--------------------")
    fp = open(filepath,'wb')
    runner = HTMLTestRunner2.HTMLTestRunner(
        stream=fp,
        title=u'接口自动化测试报告',
        description=u'智慧信贷项目'
                                               )
    runner.run(suite)
    print(u"-------------------接口自动化测试结束------------------------")
    if isrerunerrors:
        failuretests = runner.getfails()
        print (failuretests)
        if len(failuretests)>0:# 判断是否重跑失败用例
            print (u"开始重跑失败的用例")
            suitef = unittest.TestSuite()
            print (u"长度是"+str(len(failuretests)))
            reportname = dirPath+CommonMethod.getNowTime()+"_report_failure.html"
            fpf = open(reportname,'wb')
            runnerf = HTMLTestRunner2.HTMLTestRunner(
            stream=fpf,
            title=u'我的报告',
            description=u'失败重跑用例'
                                                )
            for i in range(len(failuretests)):
                suitef.addTest(failuretests[i])
            runnerf.run(suitef)



if __name__ == '__main__':
    make_testcase.makeFileToTestcase() #生成最新的测试案例
    CommonMethod.deleteReport() #删除一天前的测试报告
    Testsuite()    #自动化运行
    SendEmail.sendEmail().sendEmailFun(0) #发送邮件,0：接口自动化  1. ui自动化





