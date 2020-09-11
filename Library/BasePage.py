#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/9 5:28 下午
# @Author : wyf
# @File : BasePage.py
# @Software: PyCharm
'''
    1.构造函数实例化driver对象；
    2.元素定位，传入一个元素的元组；
    3.启动浏览器，访问到页面的URL；
    4.关闭浏览器，释放资源；

'''

import time
class BasePage(object):
    def __init__(self,driver,url):
        '''
        构造函数实例化driver对象
        :param driver:  driver 对象
        :param url:  url地址
        '''
        self.driver=driver
        self.url=url
    #元素定位,查询单个元素
    def locator(self,*loc):
        return self.driver.find_element(*loc)

    # 元素定位,查询多个元素
    def locators(self,*loc):
        return self.driver.find_elements(*loc)

    #访问url
    def open(self):
        self.driver.get(self.url)

    #释放资源
    def quit(self):
        time.sleep(1)
        self.driver.quit()


