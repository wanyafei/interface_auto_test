#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/18 2:59 下午
# @Author : wyf
# @File : login.py
# @Software: PyCharm
from Library.SeleniumMethod import SeleniumMethod
from Pages import login_page

class LoginBusiness(SeleniumMethod):
    '''登陆操作'''
    def login(self,username="admin",password="know@321"):
        self.tex_input(login_page.user_name,username)
        self.log.info(u"输入用户名:"+username)
        self.tex_input(login_page.pass_word, password)
        self.log.info(u"输入密码:" + password)
        self.public_click(login_page.sub_mit)
        self.log.info(u"点击登陆按钮" )
        print("登陆成功")
    '''登出操作'''
    def logout(self):
        self.public_click(login_page.user_click)
        self.log.info(u"登出操作点击用户名")
        self.public_click(login_page.quit_login)
        self.log.info(u"点击退出登陆按钮")
        self.log.info(u"退出登陆成功")
if __name__ == '__main__':
    from selenium import webdriver
    import time
    wd = webdriver.Chrome()
    url="http://192.168.200.9:30000/login"
    SeleniumMethod(wd).open(url)
    e=LoginBusiness(wd)
    time.sleep(1)
    e.login()
    time.sleep(1)
    e.logout()

