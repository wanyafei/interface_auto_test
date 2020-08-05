import configparser
import time,datetime
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
   getconfigvalue.read(getPath()+"/api_test/api_config/config.ini",encoding="UTF_8")
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

def deleteReport():
    '''
    删除一天前的html测试报告
    :return:
    '''
    if Path(getPath()+"/report/apiReport/").exists():
        deleteReportDate=(datetime.datetime.now()+datetime.timedelta(-int(getConfig("delete",area="CONFIG")))).strftime("%Y-%m-%d")
        for report in os.listdir(getPath()+"/report/apiReport/"):
            if report[:10]<=deleteReportDate:
                os.remove(getPath()+"/report/apiReport/"+report)
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



if __name__ == '__main__':

    # print(time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time())))
    # driverconfig("https://www.baidu.com")
    pass
