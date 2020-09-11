#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/9/10 6:25 下午
# @Author : wyf
# @File : HiveControl.py
# @Software: PyCharm
# import pyhs2
from pyhive import hive
class hivecontrol():
    def __init__(self):
        '''
        hive数据库的操作，现阶段只是实现了查询的功能
        '''
        config={
            'host':'192.168.100.202',
            'port':'10000',
            'username':'admin',
            'database':'dwt_mart'
        }
        try:

            self.hue=hive.connect(**config)
            self.cursor=self.hue.cursor()
        except ConnectionError as e:
            print('链接hive数据库失败')

    def search_data(self,sql):
        '''
        hive数据库的查询操作
        :param sql:
        :return:
        '''
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        if len(data)<1:
            print('未查询到数据')
            self.cursor.close()
        else:
            self.cursor.close()
            return data
if __name__ == '__main__':
    sql="select * from dwt_company_e00_cr where entid='6F274D8D4D357C57E0539601A8C0ACD65'"
    print(hivecontrol().search_data(sql))