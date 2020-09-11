#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/19 11:14 上午
# @Author : wyf
# @File : quanxigailan.py
# @Software: PyCharm
'''
          全系概览页面
'''

from Library.SeleniumMethod import SeleniumMethod
from Pages import quanxihuaxiang,login_page
import time
class quanxigailan(SeleniumMethod):
    def enterindex(self,entname):
        '''
        进入首页
        :param entname:
        '''
        self.tex_input(quanxihuaxiang.entname, entname)
        self.log.info("首页输入框输入企业名称：" + entname)
        self.get_ul_li(login_page.xiala)
        # self.public_click(quanxihuaxiang.button)
        self.log.info("点击查询按钮")
        time.sleep(3)
        self.swithTowindow()
        self.wait(quanxihuaxiang.tag_entname)   #等待元素加载
        if self.get_element_text(quanxihuaxiang.tag_entname)==entname:
            self.log.info("成功进入全系概览页面")
        else:
            self.log.error("进入全系概览页面失败")
    def clickindex(self):
        '''
        点击全息画像，重新进入全息概览页面
        :return:
        '''
        self.public_click(quanxihuaxiang.quit_info)
    def gettaginfo(self):
        '''
        验证企业的标签
        :param entname:
        :return:
        '''
        tag_name=self.get_element_text(quanxihuaxiang.tag)
        self.log.info("获取到企业的标签："+tag_name)
        return tag_name
    def getgradeinfo(self):
        '''
        获取企业的主体及债券评级
        :return:
        '''
        grade_zhuti=self.get_element_text(quanxihuaxiang.grade_zhuti)  #主体评级
        grade_zhaiquan=self.get_element_text(quanxihuaxiang.grade_zhaiquan)  #债券评级
        self.log.info("获取到企业的主体及债券评级为：%s,%s"%(grade_zhuti,grade_zhaiquan))
        return grade_zhuti,grade_zhaiquan
if __name__ == '__main__':
    from selenium import webdriver
    from Business.login import LoginBusiness
    wd = webdriver.Chrome()
    url = "http://192.168.200.9:30000/login"
    entname="力帆实业(集团)股份有限公司"
    SeleniumMethod(wd).open(url)     #登陆
    e=LoginBusiness(wd)
    e.login()
    t = quanxigailan(wd)           #全系概览
    t.enterindex(entname)          #进入全息概览页面
    # t.gettaginfo()                        #取得企业的标签
    t.getgradeinfo()               #取得主体及债券评级






