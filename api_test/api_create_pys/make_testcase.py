#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/4/30 5:55 下午
# @Author : wyf
# @File : make_testcase.py
# @Software: PyCharm
import requests
from Library import CommonMethod
from Library import ExcelMethod
def makeTemplate(keytype,usetype):
    if usetype=="get":
       temla = """
    def test_{sheetname}_{casename}(self):
        '''{doc_string}'''
        headers = {headers}
        headers['token'] = self.token
        data = {data}
        if not headers:
            headers = None
        if not data:
            data = None
        except_value = '{except_value}'
        self.log.info("入参：%s"%data)
        res = self.s.{atype}(self.url+'{api_url}',params=data,headers=headers)
        self.log.info("《{doc_string}》响应内容：%s"%res.text)
        """
    elif usetype=="post":
        temla = """
    def test_{sheetname}_{casename}(self):
        '''{doc_string}'''
        headers = {headers}
        headers['token'] = self.token
        data = {data}
        if not headers:
            headers = None
        if not data:
            data = None
        content_type = headers["Content-Type"]
        except_value = '{except_value}'
        self.log.info("入参：%s"%data)
        if 'application/x-www-form-urlencoded' in content_type:
            res = self.s.{atype}(self.url+'{api_url}',data=data,headers=headers)
        elif 'application/json' in content_type:
            res = self.s.{atype}(self.url+'{api_url}',json=data,headers=headers)
        self.log.info("《{doc_string}》响应内容：%s"%res.text)
            """
    if keytype == "code":
        temla = temla + """
        try:
            code = str(res.status_code)
            self.assertTrue(code == except_value, "预期code:%s,实际code:%s" % (except_value, code))
            self.log.info("预期code:%s,实际code:%s" % (except_value, code))
        except Exception as e:
            traceback.print_exc()
            self.assertTrue(False,str(e))
            self.log.error("预期code:%s,实际code:%s" % (except_value, code))
            """
    elif keytype == "key":
        temla += """
        try:
            jsonres = json.loads(res.content)
            actual_value = jsonres{except_key}
            self.assertTrue(actual_value==except_value,"预期结果:%s,实际结果:%s"%(except_value,actual_value))
            self.log.info("预期结果:%s,实际结果:%s"%(except_value,actual_value))
        except Exception as e:
            traceback.print_exc()
            self.assertTrue(False,str(e))
            self.log.error("预期结果:%s,实际结果:%s"%(except_value,actual_value))
            """
    elif keytype == "sql":
        temla += """
        try:
            jsonres = json.loads(res.content)
            sql = '{except_key}'
            actual_value = str(excute_sql(sql))
            self.assertTrue(str(actual_value)==except_value,"预期结果:%s,实际结果:%s"%(except_value,actual_value))
            self.log.info("预期结果:%s,实际结果:%s"%(except_value,actual_value))
        except Exception as e:
            traceback.print_exc()
            self.assertTrue(False,str(e))
            self.log.error("预期结果:%s,实际结果:%s"%(except_value,actual_value))
            """
    else:
        temla += """
        ms="无法辨别的验证类型"
        self.log.info(ms)
        self.assertTrue(False,ms)
        """
    return temla


def makeFileToTestcase():
    '''结合接口数据文档生成接口测试案例'''
    cur_dir = CommonMethod.getPath()       #当前项目的根路径
    is_run=CommonMethod.getConfig("is_run", area="ISRUN")      #指定运行还是批量运行的标志 0 指定运行 1 全量运行

    #根据配置文件中is_run字段判断是指定运行还是全量运行
    if str(is_run) == "0":
        test_case_list = []
        sheetnames=CommonMethod.getRunTxtInfo()
        for sheetname in sheetnames:
            test_case_lists = ExcelMethod.excelOpern(cur_dir + "/api_test/api_data/api.xlsx",sheetname).read_excel_rows_dict()
            for sheetinfo in test_case_lists:
                test_case_list.append(sheetinfo)
    elif str(is_run) == "1":
        test_case_list = ExcelMethod.openallSheet(cur_dir + "/api_test/api_data/api.xlsx").getSheetContent()
    with open(cur_dir+"/api_test/api_template/apitest","r",encoding="UTF-8") as template:
        template_data=template.read()
    for api_data in test_case_list:
        temla=makeTemplate(api_data["验证方式"],api_data["调用方式"]).format(sheetname=api_data["sheetname"],casename=api_data["序号"], data=api_data["入参"],headers=api_data['头信息'],
                                 except_key=api_data["预期结果键"], except_value=api_data["预期结果值"],
                                 atype=api_data['调用方式'], api_url=api_data["接口地址"],doc_string=api_data["模块名称"]+"-"+api_data["用例名称"])


        template_data+=temla
        template.close()
    with open(cur_dir+"/api_test/api_cases/api_testcase.py","w",encoding="utf-8") as f:
        f.write(template_data)
        f.close()

if __name__ == '__main__':
    makeFileToTestcase()



