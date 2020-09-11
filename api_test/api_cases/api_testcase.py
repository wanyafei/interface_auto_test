#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/5/8 4:23 下午
# @Author : wyf
# @File : myapi
# @Software: PyCharm

import unittest, re, json
import traceback
import requests
from Library import CommonMethod
from Library.Mysqldb import Mysqldb
from Library.log import Logger

ip=CommonMethod.getConfig("url")
login_api=CommonMethod.getConfig("login_api")
class apitest(unittest.TestCase):
    log=Logger("接口自动化")
    s = requests.session()
    @classmethod
    def setUpClass(cls) -> None:
        cls.url=ip
        headers = {
            "Connection": "keep_alive",
            "Content-Type": "application/json;charset=UTF-8",
        }
        data={
            "account":"wanyafei01",
            "password":"9cbf8a4dcb8e30682b927f352d6559a0"
        }
        token=json.loads(cls.s.post(cls.url+login_api, json=data, headers=headers).content)['data']['token']
        cls.token=token


    @classmethod
    def tearDownClass(cls) -> None:
        pass
    def test_全息画像_1(self):
        '''工商信息-企业标签'''
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        headers['token'] = self.token
        data = {
    "entid":"6F274E54F3DE7C57E0539601A8C0ACD65"
}
        if not headers:
            headers = None
        if not data:
            data = None
        except_value = '200'
        self.log.info("入参：%s"%data)
        res = self.s.get(self.url+'/api/portrait/entinfo/tag',params=data,headers=headers)
        self.log.info("《工商信息-企业标签》响应内容：%s"%res.text)
        
        try:
            code = str(res.status_code)
            self.assertTrue(code == except_value, "预期code:%s,实际code:%s" % (except_value, code))
            self.log.info("预期code:%s,实际code:%s" % (except_value, code))
        except Exception as e:
            traceback.print_exc()
            self.assertTrue(False,str(e))
            self.log.error("预期code:%s,实际code:%s" % (except_value, code))
            
    def test_全息画像_2(self):
        '''工商信息-企业基本信息'''
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        headers['token'] = self.token
        data = {
    "entid":"6F274E54F3DE7C57E0539601A8C0ACD65"
}
        if not headers:
            headers = None
        if not data:
            data = None
        except_value = '200'
        self.log.info("入参：%s"%data)
        res = self.s.get(self.url+'/api/portrait/entinfo/enter',params=data,headers=headers)
        self.log.info("《工商信息-企业基本信息》响应内容：%s"%res.text)
        
        try:
            code = str(res.status_code)
            self.assertTrue(code == except_value, "预期code:%s,实际code:%s" % (except_value, code))
            self.log.info("预期code:%s,实际code:%s" % (except_value, code))
        except Exception as e:
            traceback.print_exc()
            self.assertTrue(False,str(e))
            self.log.error("预期code:%s,实际code:%s" % (except_value, code))
            
    def test_全息画像_3(self):
        '''工商信息-实际控制人'''
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        headers['token'] = self.token
        data = {
    "entid":"6F274E54F3DE7C57E0539601A8C0ACD65",
    "entname":"帆实业(集团)股份有限公司"
}    
        if not headers:
            headers = None
        if not data:
            data = None
        except_value = '200'
        self.log.info("入参：%s"%data)
        res = self.s.get(self.url+'/api/portrait/graph/controller',params=data,headers=headers)
        self.log.info("《工商信息-实际控制人》响应内容：%s"%res.text)
        
        try:
            code = str(res.status_code)
            self.assertTrue(code == except_value, "预期code:%s,实际code:%s" % (except_value, code))
            self.log.info("预期code:%s,实际code:%s" % (except_value, code))
        except Exception as e:
            traceback.print_exc()
            self.assertTrue(False,str(e))
            self.log.error("预期code:%s,实际code:%s" % (except_value, code))
            
    def test_全息画像_4(self):
        '''工商信息-股东'''
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        headers['token'] = self.token
        data = {
    "entid":"6F274E54F3DE7C57E0539601A8C0ACD65",
    "entname":"帆实业(集团)股份有限公司",
    "page":1,
    "size":10
}    
        if not headers:
            headers = None
        if not data:
            data = None
        except_value = '10'
        self.log.info("入参：%s"%data)
        res = self.s.get(self.url+'/api/portrait/entinfo/shareholder',params=data,headers=headers)
        self.log.info("《工商信息-股东》响应内容：%s"%res.text)
        
        try:
            jsonres = json.loads(res.content)
            actual_value = str(jsonres['data']['pagination']['totalCount'])
            self.assertTrue(actual_value==except_value,"预期结果:%s,实际结果:%s"%(except_value,actual_value))
            self.log.info("预期结果:%s,实际结果:%s"%(except_value,actual_value))
        except Exception as e:
            traceback.print_exc()
            self.assertTrue(False,str(e))
            self.log.error("预期结果:%s,实际结果:%s"%(except_value,actual_value))
            
    def test_准入体检_1(self):
        '''工商信息-企业标签12'''
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        headers['token'] = self.token
        data = {
    "entid":"6F274E54F3DE7C57E0539601A8C0ACD65"
}
        if not headers:
            headers = None
        if not data:
            data = None
        except_value = '20022'
        self.log.info("入参：%s"%data)
        res = self.s.get(self.url+'/api/portrait/entinfo/tag',params=data,headers=headers)
        self.log.info("《工商信息-企业标签12》响应内容：%s"%res.text)
        
        try:
            code = str(res.status_code)
            self.assertTrue(code == except_value, "预期code:%s,实际code:%s" % (except_value, code))
            self.log.info("预期code:%s,实际code:%s" % (except_value, code))
        except Exception as e:
            traceback.print_exc()
            self.assertTrue(False,str(e))
            self.log.error("预期code:%s,实际code:%s" % (except_value, code))
            