# _*_ coding:utf-8 _*_
import logging,time, os

from Library import CommonMethod

par = os.path.abspath(CommonMethod.getPath())+"/log/"

dir_time=CommonMethod.getNowTime()

# def get_time():
#   return time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))


class Logger(object):
     def __init__(self,name, clevel = logging.DEBUG, Flevel = logging.DEBUG):
       self.logger = logging.getLogger(name+".txt")
       self.logger.setLevel(logging.DEBUG)
       #设置日志文件格式
       fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
       # 设置CMD日志
       # sh = logging.StreamHandler()
       # sh.setFormatter(fmt)
       # sh.setLevel(clevel)
       # 设置文件日志
       fh = logging.FileHandler(par+name+"_"+dir_time+".txt")
       fh.setFormatter(fmt)
       fh.setLevel(Flevel)
       # self.logger.addHandler(sh)
       self.logger.addHandler(fh)

     def debug(self, message):
         print(message)
         self.logger.debug(message)

     def info(self, message):
        print(message)
        self.logger.info(message)


     def war(self, message):
        self.logger.warn(message)

     def error(self, message):
         print(message)
         self.logger.error(message)

     def cri(self, message):
       self.logger.critical(message)

if __name__ =='__main__':
    logyyx = Logger("login")
    # logyyx.debug('一个debug信息')

