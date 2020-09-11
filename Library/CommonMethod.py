import configparser
import time,datetime
from Library import Mysqldb
from pathlib import Path
import os
from selenium import webdriver

def transformStr(str,state):
    '''
    将入参字符转换成带双引号的字符
    :param str: 入参
    :return: 带双引号的字符
    '''
    if state==0:
        str='"{}",'.format(str)
        return str
    elif state==1:
        str = '"{}"'.format(str)
        return str

def getPath():
    '''获取项目的路径'''
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
def getConfig(keyinfo,area="HTTP"):
   '''
    读取配置文件
    :param keyinfo:区域内key值
    :param area:区域值
    :return:
    '''
   getconfigvalue=configparser.ConfigParser()
   getconfigvalue.read(getPath()+"/Config/config.ini",encoding="UTF_8")
   return getconfigvalue.get(area,keyinfo)

def getRunTxtInfo():
    '''
    获取is_run txt文件中要运行的sheet案例
    :return:  要运行的列表
    '''
    clae_list=[]
    testcaselists=getPath()+"/api_test/is_run"
    with open(testcaselists,"r",encoding="UTF-8") as wb:
        for value in wb.readlines():
            data=str(value)
            if data !='' and not data.startswith("#"):
                clae_list.append(data.replace("\n",""))
        return clae_list

def getNowTime():
    '''
    获取当前系统时间：%Y-%m-%d %H_%M_%S
    :return:
    '''
    return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))

def deleteReport(flag):
    '''
    flag:0 为接口的报告 1为UI的报告
    删除一天前的html测试报告
    :return:
    '''
    if flag==0:
        repordir="apiReport/"
    else:
        repordir ="uiReport/"
    if Path(getPath()+"/report/"+repordir).exists():
        deleteReportDate=(datetime.datetime.now()+datetime.timedelta(-int(getConfig("delete",area="CONFIG")))).strftime("%Y-%m-%d")
        for report in os.listdir(getPath()+"/report/"+repordir):
            if report[:10]<=deleteReportDate:
                os.remove(getPath()+"/report/"+repordir+report)
    else:
        print("目录下不存在report文件夹")

def driverconfig(url):
    browserType=getConfig("browserType",area="CONFIG")
    dict={
        '1':getPath()+"/Driver/chromedriver.exe"
    }

    browser_driver=os.path.abspath(dict[browserType])
    if browserType == 0:
        os.environ["webdriver.ie.driver"] = browser_driver
        driver=webdriver.Ie(browser_driver).get(url)
    if browserType == 1:
        os.environ["webdriver.chrome.driver"] = browser_driver
        driver=webdriver.Chrome(browser_driver).get(url)
    print("开始启动浏览器------chrome-------")
    time.sleep(1)
    print(browserType)

def getNewReportDir(type):
    '''
    根据类型获取最新的自动化测试后的测试报告路径
    :param type: 0：接口自动化  1. ui自动化
    :return: 获取到最新生成的一份测试报告路径
    '''
    type=str(type)
    if type=="0":
        dir=getPath() + "/report/apiReport"
        #取出测试报告文件夹下所有测试报告存放至列表
        tset_report_list=os.listdir(dir)
        #使用内置函数sorted对列表进行升序排序
        new_report_list=sorted(tset_report_list)
        #获取到最新的测试报告
        last_eport_list=new_report_list[-1]
        #返回最新的测试报告地址
        return os.path.join(dir,last_eport_list)
    elif type=="1":
        dir = getPath() + "/report/uiReport"
        # 取出测试报告文件夹下所有测试报告存放至列表
        tset_report_list = os.listdir(dir)
        # 使用内置函数sorted对列表进行升序排序
        new_report_list = sorted(tset_report_list)
        # 获取到最新的测试报告
        last_eport_list = new_report_list[-1]
        # 返回最新的测试报告地址
        return os.path.join(dir, last_eport_list)
    else:
        print("输入类型有误,不能根据其判断获取最新的测试报告路径")
def generateEntid(sql):
    '''
    通过传入的sql语句获取对应的entid
    :param sql:
    :return: 列表形式的entids
    '''
    entids = Mysqldb.Mysqldb().search(sql)
    entnames = []
    for entid in entids:
        entnames.append(entid[0])
    return entnames

num=0    #通过改变
def create_counter():
    '''
    计数器，每次调用自增1
    :return:
    '''
    def increase():
        global num
        num= num+1
        return num
    return increase

if __name__ == '__main__':

    # print(time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time())))
    # driverconfig("https://www.baidu.com")
    # flag=0
    # deleteReport(flag)
    import json, requests

    s = requests.session()
    ip = getConfig("url")
    login_api = getConfig("login_api")

    headers = {
        "Connection": "keep_alive",
        "Content-Type": "application/json;charset=UTF-8",
    }
    data = {
        "account": "wanyafei01",
        "password": "9cbf8a4dcb8e30682b927f352d6559a0"
    }
    ii=ip + login_api
    yy=json.loads(s.post(ip + login_api, json=data, headers=headers).content)
    token = json.loads(s.post(ip + login_api, json=data, headers=headers).content)['data']['token']
    print(token)
