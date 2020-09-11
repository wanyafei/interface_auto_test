#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/9/1 5:27 下午
# @Author : wyf
# @File : ElasticSearchOperation.py
# @Software: PyCharm
from elasticsearch import Elasticsearch
class elasticsearch_data():
    #初始化ini操作脚本
    def __init__(self):
        try:
            ES = ['192.168.200.18:9212']
            es_ordinary=Elasticsearch(ES,sniff_on_start=True,sniff_on_connection_fail=True,sniffer_timeout=100)
            self.es = es_ordinary
        except Exception as e:
            print(e)

    def query_data(self,keywords_list):
            # es查询语句,keywords_list 查询条件，类似where
        query ={
  "_source": ["entname"],
  "query": {
    "bool": {
      "filter": [
        {
          "term": {
            "id": keywords_list
          }
        }
      ]
    }
  }
}

        return query
    def get_es_data(self,index_name,doc_type,param):
        '''
        根据入参获取指定索引中特定的内容
        :param index_name: 索引名称
        :param doc_type: 返回的文档类型
        :param param: 参数列表[]
        :return: 以列表的形式返回指定的字段值
        # '''
        all_data=[]
        for info in param:
            query_data = self.query_data(info)
            res=self.es.search(
                index=index_name,
                doc_type=doc_type,
                body=query_data
            )
            # 获取指定的内容
            hit=res['hits']['hits'][0]['_source']['entname']
            # 把指定内容添加至列表中
            all_data.append(hit)
        return all_data

if __name__ == '__main__':
    import Mysqldb
    sql = "select distinct(t.entid) from  (select  tt.normCode,tt.entid from credit_rflabel2value tt where tt.entid LIKE BINARY '6F%') t group by t.normCode "
    entids = Mysqldb.Mysqldb().search(sql)
    entnames = []
    for entid in entids:
        entnames.append(entid[0])
    print(elasticsearch_data().get_es_data("app.company_info","company",entnames))
