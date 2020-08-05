#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/5/9 8:36 下午
# @Author : wyf
# @File : Mysqldb.py
# @Software: PyCharm
from Library import CommonMethod
import pymysql
class Mysqldb():
    '''数据库的操作，现阶段只做了查询、增加更新删除后续可根据情况添加'''
    def __init__(self):
        hosts=CommonMethod.getConfig("host","DATABASE")
        usename=CommonMethod.getConfig("usename", "DATABASE")
        password=CommonMethod.getConfig("password", "DATABASE")
        port=CommonMethod.getConfig("port", "DATABASE")
        database = CommonMethod.getConfig("database", "DATABASE")
        config={
            'hosts':hosts,
            'user':usename,
            'password':password,
            'port':port,
            'db':database
        }
        try:
            self.db=pymysql.connect(**config)
            self.cursor=self.db.cursor()
        except ConnectionError as e:
            print("数据库连接失败")
    def search(self,sql):
        '''执行查询的sql'''
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        if len(data)<1:
            print("未查询到数据")
            self.db.close()
        else:
            self.db.close()
            return data


if __name__ == '__main__':
    sql="select  * from "
    Mysqldb().search()
