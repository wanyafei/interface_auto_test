#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/9 5:39 下午
# @Author : wyf
# @File : lianxi.py
# @Software: PyCharm
from Library import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
'''
    1.练习的页面
'''
class lianxi(BasePage.BasePage):
    username=(By.XPATH,"/html/body/form/p[1]/input")
    password=(By.XPATH,"/html/body/form/p[2]/input")
    queding=(By.XPATH,"/html/body/form/p[3]/button")
    tex="15902127953"
    passw="123456"

    def input(self,locator,txt):
        self.locator(locator).send_keys(txt)
    def click(self,locator):
        self.locator(locator).click()
    def test(self):
        self.open()
        self.input(self.username,self.tex)
        self.input(self.password,self.passw)
        self.click(self.queding)
if __name__ == '__main__':
    wd=webdriver.Chrome()
    url="http://47.94.172.18/signin"
    duixiang=lianxi(wd,url)
    duixiang.test()
