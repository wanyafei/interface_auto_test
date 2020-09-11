#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/19 1:50 下午
# @Author : wyf
# @File : test_quanxihuaxiang.py
# @Software: PyCharm

'''
    页面元素：全系画像页面
'''

from selenium.webdriver.common.by import By
'***********首页查询************'
entname=(By.XPATH,'//*[@id="app-wrapper"]/div[2]/div/div[2]/div/span/div/div/input')  #首页企业名称输入框

'**********全系概览*************'
tag_entname=(By.XPATH,'/html/body/div/div[2]/div[2]/div/div[1]/h2')   #判断进入全系概览页面的标识
quit_info=(By.XPATH,'//*[@id="app-wrapper"]/div[1]/header/ul[1]/li[1]/a/span') #全息概览页面的全息画像（用于定位退出）
tag=(By.XPATH,'//*[@id="app-wrapper"]/div[2]/div[2]/div/div[1]/div')  #企业的标签

tag_name="在营(开业)力帆股份国内A股601777高新技术企业"                #企业标签值的断言

grade_zhuti=(By.XPATH,'//*[@id="app-wrapper"]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/strong')#企业主体信用评级
grade_zhaiquan=(By.XPATH,'//*[@id="app-wrapper"]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/strong') #企业债券信用评级

grade_zhuti_assert="C" #企业主体信用评级的断言
grade_zhuti_assert="C" #企业债券信用评级的断言
'**********工商信息*************'

'**********评级信息*************'

'**********所属集团*************'