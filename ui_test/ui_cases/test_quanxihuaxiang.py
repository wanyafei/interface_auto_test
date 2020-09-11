#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/18 6:47 下午
# @Author : wyf
# @File : test_quanxihuaxiang.py
# @Software: PyCharm
import unittest,traceback,os
import ddt
from Library import CommonMethod
from Business.login import LoginBusiness
from selenium import webdriver
from Business.quanxihuaxiang.quanxigailan import quanxigailan
from Library import SeleniumMethod
yamlpath=os.path.join(CommonMethod.getPath(),'ui_test','ui_data','data.yml')
url= CommonMethod.getConfig('shengchan',area='HTTP')  #从配置文件中获取url
entname= CommonMethod.getConfig('entname',area='quanxihuaxiang')  #从配置文件取出entname的信息
@ddt.ddt
class UCTestquanxigailan(unittest.TestCase):
    '''全息概览'''
    @classmethod
    def setUpClass(cls) -> None:
        cls.wd = webdriver.Chrome()
        cls.se=SeleniumMethod.SeleniumMethod(cls.wd)
        cls.se.open(url)
        LoginBusiness(cls.wd).login()   #登陆
        cls.qx = quanxigailan(cls.wd)      #进入首页
        cls.qx.enterindex(entname)    #进入全息概览页

    @classmethod
    def tearDownClass(cls) -> None:
        LoginBusiness(cls.wd).logout()

    def setUp(self) -> None:
        self.se.log.info(">>>>>>>>>>>>>>>>>>>>>>>>开始运行%s模块的第%s个测试案例>>>>>>>>>>>>>>>>>>>>>>>>"%(self.__doc__,CommonMethod.create_counter()()))

    def tearDown(self) -> None:
        CommonMethod.num = CommonMethod.num - 1
        self.se.log.info(">>>>>>>>>>>>>>>>>>>>>>>>第%s个测试案例运行结束>>>>>>>>>>>>>>>>>>>>>>>>"%CommonMethod.create_counter()())

    @ddt.file_data(yamlpath)
    @ddt.unpack
    def testCompanyTag(self,**kwargs):
        '''全息概览客户标签'''
        try:

            tag=self.qx.gettaginfo()
            self.assertEqual(kwargs.get('quanxigailan')["entnametag"]["except"],tag,"预期code:%s,实际code:%s"%(kwargs.get('quanxigailan')["entnametag"]["except"],tag))
            self.se.log.info("预期code:%s,实际code:%s" % (kwargs.get('quanxigailan')["entnametag"]["except"],tag))
        except Exception as e:
            traceback.print_exc()
            self.assertTrue(False, str(e))
            self.se.log.info("预期code:%s,实际code:%s" % (kwargs.get('quanxigailan')["entnametag"]["except"],tag))

    @ddt.file_data(yamlpath)
    @ddt.unpack
    def testCompanyGrade(self,**kwargs):
        '''全息概览客户评级'''
        try:
            grade_zhuti,grade_zhaiquan=self.qx.getgradeinfo()
            self.assertEqual(kwargs.get('quanxigailan')['grade']['zhuti_grade_except'],grade_zhuti,"预期主体评级结果是:%s,实际结果是:%s"%(kwargs.get('quanxigailan')['grade']['zhuti_grade_except'],grade_zhuti))
            self.se.log.info("预期主体评级结果是:%s,实际结果是:%s"%(kwargs.get('quanxigailan')['grade']['zhuti_grade_except'],grade_zhuti))
            self.assertEqual(kwargs.get('quanxigailan')['grade']['zhaiquan_grade_except'],grade_zhuti,"预期债券评级结果是:%s,实际结果是:%s"%(kwargs.get('quanxigailan')['grade']['zhaiquan_grade_except'],grade_zhaiquan))
            self.se.log.info("预期债券评级结果是:%s,实际结果是:%s"%(kwargs.get('quanxigailan')['grade']['zhaiquan_grade_except'],grade_zhaiquan))
        except Exception as e:
            traceback.print_exc()
            self.assertTrue(False, str(e))
            self.se.log.info("预期主体评级结果是:%s,实际结果是:%s" % (kwargs.get('quanxigailan')['grade']['zhuti_grade_except'], grade_zhuti))
            self.se.log.info("预期债券评级结果是:%s,实际结果是:%s" % (kwargs.get('quanxigailan')['grade']['zhaiquan_grade_except'], grade_zhaiquan))




if __name__ == "__main__":
    unittest.main()





