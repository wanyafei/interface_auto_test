#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/18 11:49 上午
# @Author : wyf
# @File : SeleniumMethod.py
# @Software: PyCharm
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from Library import log
import time
class SeleniumMethod():
    "selenium公共方法封装集"
    log=log.Logger("ui自动化测试")
    def __init__(self,driver):
        self.driver=driver
    '*****************************webelement方法************************************'
    def tex_input(self,input_locator,txt):
        '''
        封装文本输入的web_element方法
        :param input_locator: 元组（by.ID,"locator"）
        :param txt: 查找的内容
        :return:
        '''
        self.wait(input_locator)
        self.locator(*input_locator).send_keys(txt)
    def public_click(self,click_locator):
        '''
        封装文本输入的web_element方法
        :param click_locator:
        :return:
        '''
        self.wait(click_locator)
        self.locator(*click_locator).click()
    def get_element_text(self,locator):
        '''
        获取元素的文本值
        :param locator:
        :return:
        '''
        self.wait(locator)
        get_text=self.locator(*locator).text
        return get_text

    def select_by_text_info(self,locator,text):
        '''
        通过选择下拉框文本值选择下拉值
        :param locator:
        :return:
        '''
        Select(self.locator(*locator)).select_by_visible_text(text)
    def select_by_index_info(self,locator,index):
        '''
        通过选择下拉框坐标值选择下拉值
        :param locator:
        :param index:
        :return:
        '''
        Select(self.locator(*locator)).select_by_index(index)
    def select_by_value_info(self,locator,value):
        '''
        通过选择下拉框元素value值选择下拉值
        :param locator:
        :param value:
        :return:
        '''
        Select(locator(*locator)).deselect_by_value(value)
    def get_ul_li(self,locators):
        '''
        查找ul列表中的li,点击【力帆实业】下标为0
        :return:
        '''
        ul=self.locator(*locators)
        time.sleep(3)
        ul.find_elements_by_xpath("li")[0].click()
    '********************************webdriver方法**********************************'
    def locator(self,*loc):
        '''
        元素定位,查询单个元素
        :param loc:
        :return:
        '''
        return self.driver.find_element(*loc)
    def open(self,url):
        '''
        #访问url
        :param url:
        :return:
        '''
        self.driver.get(url)
    def quit(self):
        '''
        释放资源
        :return:
        '''
        self.driver.quit()
    def wait(self,loc,time=30):
        '''
        超时等待，在time时间内等待元素的出现,默认30秒
        :param driver:
        :param time:
        :return:
        '''
        WebDriverWait(self.driver,time).until(EC.visibility_of_element_located(loc),"显示等待元素超时")

    '*****************************窗口之间的切换***********************************'
    def swithTowindow(self):
        '''
        窗口之间的切换，适用于2个页面之间的切换
        :return:
        '''
        # 获取当前窗口句柄
        nowhandle=self.driver.current_window_handle
        # 获取所有窗口句柄
        allhandles = self.driver.window_handles
        for handle_info in allhandles:
            if handle_info != nowhandle:
                self.driver.switch_to_window(handle_info)
    def swithTowindows(self,windowtitle):
        '''
        窗口之间的切换，适用于2个页面之间的切换
        :param windowtitle: 传入要切换的窗口标题
        :return:
        '''
        # 获取所有窗口句柄
        allhandles = self.driver.window_handles
        for handle in allhandles:
            self.driver.switch_to_window(handle)
            title=self.driver.title()
            if title==windowtitle:
                break
    '****************************鼠标事件*******************************'
    def doubleClick(self,locators):
        '''
        模拟鼠标的双击操作
        :return:
        '''
        ActionChains(self.driver).double_click(self.locator(*locators)).perform()

    def rightClick(self,locators):
        '''
        模拟鼠标的右键操作
        :param locators:
        :return:
        '''
        ActionChains(self.driver).context_click(self.locator(*locators)).perform()

    def dragClick(self,locator1,locator2):
        '''
        模拟鼠标的拖拽操作
        :param locator1: 拖拽的元素
        :param locator2: 拖拽至的元素
        :return:
        '''
        ActionChains(self.driver).drag_and_drop(self.locator(*locator1),self.locator(*locator2)).perform()
    def hevrClick(self,locator):
        '''
        模拟鼠标的悬浮操作
        :param locator:
        :return:
        '''
        ActionChains(self.driver).move_to_element(self.locator(*locator)).perform()
    '****************************键盘事件*******************************'
    def tab(self,locator):
        '''
        模拟键盘的Tab键操作
        :param locator:
        :return:
        '''
        self.locator(*locator).send_keys(Keys.TAB)
    def enter(self,locator):
        '''
        模拟键盘的Enter回车键操作
        :param locator:
        :return:
        '''
        self.locator(*locator).send_keys(Keys.ENTER)
    def selectall(self,locator):
        '''
        模拟键盘的Ctrl+a键操作
        :param locator:
        :return:
        '''
        self.locator(*locator).send_keys(Keys.CONTROL,'a')
    def copy(self,locator):
        '''
        模拟键盘的Ctrl+c键操作
        :param locator:
        :return:
        '''
        self.locator(*locator).send_keys(Keys.CONTROL,'c')
    def paste(self,locator):
        '''
        模拟键盘的Ctrl+v键操作
        :param locator:
        :return:
        '''
        self.locator(*locator).send_keys(Keys.CONTROL,'v')
    def cut(self,locator):
        '''
        模拟键盘的Ctrl+x键操作
        :param locator:
        :return:
        '''
        self.locator(*locator).send_keys(Keys.CONTROL,'x')
if __name__ == '__main__':
  pass