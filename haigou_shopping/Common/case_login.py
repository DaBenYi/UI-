import logging
from Common.project_path import *
#logger 收集数据
#handder 输出日志的渠道
class MyLog:
    def my_log(self,msg,level):
        #1.定义一个日志收集器 my_logger
        my_logger=logging.getLogger("web")
        #2.设置级别
        my_logger.setLevel("DEBUG")
        #设置输出格式
        formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
        #3.创建一个输出渠道
        ch=logging.StreamHandler()
        ch.setLevel("DEBUG")
        ch.setFormatter(formatter)

        fh=logging.FileHandler(case_log_path,encoding="utf-8")
        fh.setLevel("INFO")
        fh.setFormatter(formatter)
        #4.两者对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)
        #5.收集日志
        if level=="DEBUG":
            my_logger.debug(msg)
        elif level == "INFO":
            my_logger.info(msg)
        elif level=="WARNING":
            my_logger.warning(msg)
        elif level=="ERROR":
            my_logger.error(msg)
        elif level=="CRITICAL":
            my_logger.critical(msg)
        #关闭日志收集器
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)
    def debug(self,msg):
        self.my_log(msg,"DEBUG")
    def info(self, msg):
        self.my_log(msg, "INFO")
    def waring(self, msg):
        self.my_log(msg, "WARNING")
    def error(self,msg):
        self.my_log(msg,"ERROR")
    def critical(self,msg):
        self.my_log(msg,"CRITICAL")

if __name__ == '__main__':
    MyLog().info("111")