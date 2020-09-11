#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/18 2:01 下午
# @Author : wyf
# @File : login_page.py
# @Software: PyCharm

'''
    页面元素：登陆页面,登陆及退出
'''
from selenium.webdriver.common.by import By

'**************************登陆**************************************'
user_name=(By.NAME,'username')     #登陆页面用户名
pass_word=(By.XPATH,'//*[@id="app-wrapper"]/div/div/div[2]/form/div[2]/div/div[1]/input')   #登陆页面密码
sub_mit=(By.XPATH,'//*[@id="app-wrapper"]/div/div/div[2]/form/div[4]/div/button')     #登陆页面登陆按钮

'**************************退出登陆**************************************'
user_click=(By.XPATH,'//*[@id="app-wrapper"]/div[1]/header/ul[2]/li/div/a/span')   #点击用户名
quit_login=(By.XPATH,'//*[@id="app-wrapper"]/div[2]/div[1]/div[1]/button[2]/span')   #退出登陆



'''
    页面元素：首页
'''
'*****************************首页输入框**************************************'

xiala=(By.XPATH,'/html/body/div[2]/div[1]/div[1]/div/div/ul')

'''
    断言值
'''
assert_login_value="企业全息画像"         #登陆后360画像页面的标题文本