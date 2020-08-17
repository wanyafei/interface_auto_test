#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2020/8/14 3:20 下午
# @Author : wyf
# @File : SendEmail.py
# @Software: PyCharm
import smtplib
from Library import CommonMethod
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
class sendEmail():
    def __init__(self):
        self.from_user=CommonMethod.getConfig("from_user","EMAIL")
        self.from_pass = CommonMethod.getConfig("from_pass", "EMAIL")
        self.smtp_server = CommonMethod.getConfig("smtp_server", "EMAIL")
        self.mail_port = CommonMethod.getConfig("mail_port", "EMAIL")
        self.receiver = CommonMethod.getConfig("receiver", "EMAIL")
        self.mime=MIMEMultipart()   #定义一个邮件对象
    def sendEmailFun(self,type):
        #1.构造邮件头部信息
        self.mime.attach(MIMEText("测试报告已经生成，附件为运行后的测试报告文件，请注意查收","plain","utf-8"))  #构造正文信息
        self.mime['From']=formataddr(('自动化测试',self.from_user))   #邮件的发件人
        self.mime['To']=Header("Tester",'utf-8')                    #邮件的收件人
        self.mime['Subject']=Header('自动化测试报告','utf-8').encode() #邮件的主题
        # 添加附件
        att1=MIMEText(open(CommonMethod.getNewReportDir(type),'rb').read(),'base64','utf-8') #构造附件信息
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="report.html"'
        self.mime.attach(att1)
        #2.链接邮件服务器、登录、发送邮件
        server=smtplib.SMTP(self.smtp_server,self.mail_port)   #构造链接邮件对象
        server.login(self.from_user,self.from_pass)            #登录邮箱
        server.sendmail(self.from_user,self.receiver,self.mime.as_string())#发送邮件
        server.quit() #退出，释放资源
        print(u"邮件发送成功")
if __name__ == '__main__':
    sendEmail().sendEmailFun(0)