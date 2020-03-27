import logging
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from Common.case_login import MyLog
from Common.project_path import *
from selenium.webdriver import ActionChains

my_logger=MyLog()#日志
class BasePage:
    '''封装基本函数----执行日志、异常处理、失败截图
        所有的页面的公共部分
    '''
    def __init__(self,driver,):
        self.driver = driver

    #等待元素可见
    def wait_eleVisibel(self,locator,times=10,poll_frequency=0.5,doc=""):
        '''
        :param locator: 元素定位。元组形式（元素定位类型，元素定位方式）
        :param times: 等待时间
        :param poll_frequency:
        :param doc:模块名_页面名称_操作名称
        :return:None
        '''
        my_logger.info("等待元素{0}可见".format(locator))
        try:
            #开始等待的时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver,times,poll_frequency).until(EC.visibility_of_element_located(locator))
            #结束等待的时间点
            end = datetime.datetime.now()
            wait_time = (end-start).seconds
            #求一个差值，写在日志当中。等待了多久
            my_logger.info("等待结束。等待时长为：{}".format(wait_time))
        except:
            my_logger.info("等待元素可见失败！！！") #exception可以看到和控制台一样的报错
            self.save_screenshot(doc)
            raise

    #等待元素存在
    def wait_elePresence(self):
        pass

    #查找元素
    def get_element(self,locator,doc=""):
        my_logger.info("查找元素{0}可见".format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            my_logger.info("查找元素可见失败！！！")  # exception可以看到和控制台一样的报错
            self.save_screenshot(doc)
            raise

    #点击操作
    def click_element(self,locator,doc=""):
        #调用def get_element
        ele = self.get_element(locator,doc="")
        #元素操作
        my_logger.info("{0} 点击元素：{1}".format(doc,locator))
        try:
            ele.click()
        except:
            my_logger.info("元素点击操作失败！！")
            self.save_screenshot(doc)
            raise

    #输入操作
    def input_text(self,locator,text,doc=""):
        # 找元素
        ele = self.get_element(locator, doc="")
        # 输入操作
        my_logger.info("{0} 输入元素：{1}".format(doc, locator))
        try:
            ele.send_keys(text)
        except:
            my_logger.info("元素输入操作失败！！！")
            self.save_screenshot(doc)
            raise

    #获取元素的文本内容
    def get_text(self,locator,doc=""):
        # 找元素
        ele = self.get_element(locator, doc="")
        my_logger.info("{0} 查找元素文本内容：{1}".format(doc, locator))
        try:
            return ele.text
        except:
            my_logger.info("获取元素文本失败！！！")
            self.save_screenshot(doc)
            raise

    #获取元素的属性
    def get_element_attribute(self,locator,attr,doc=""):
        # 找元素
        ele = self.get_element(locator, doc="")
        my_logger.info("{0} 获取元素属性：{1}".format(doc, locator))
        try:
            return ele.get_attribute(attr)
        except:
            my_logger.info("获取元素属性失败！！！")
            self.save_screenshot(doc)
            raise

    #aleter处理-获取文本
    def alter_action(self,doc=""):
        try:
            alert = self.driver.switch_to.alert  # 定位警告框
            my_logger.info("获取警告框成功！！")
            alert_text = alert.text  # 获取alert中文本内容
            my_logger.info("获取到警告框文本：{0}".format(alert_text))
            alert.accept()
            my_logger.info("关闭警告框成功!!")
            return alert_text
        except:
            my_logger.info("获取警告框文本失败！！！")
            self.save_screenshot(doc)
            raise

    #iframe切换
    def switch_iframe(self,ifame_reference):
        pass

    #上传操作
    def upload_file(self):
        pass

    #截图操作
    def save_screenshot(self,doc):
        #图片名称：模块名_页面名称_操作名称_年-月-日_时分秒.png
        file_name = screenshot_path + "{0}_{1}.png".format(doc,time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime()))
        try:
            self.driver.save_screenshot(file_name)
            my_logger.info("截取网页成功，文件路径为：{}".format(file_name))
        except:
            my_logger.info("截图失败")
            raise


    #窗口切换
    def switch_windows(self,i,doc=""):
        try:
            handls=self.driver.window_handles
            self.driver.switch_to.window(handls[i])
            my_logger.info("{0}窗口切换成功".format(doc))
        except:
            my_logger.info("窗口切换失败！！！")
            self.save_screenshot(doc)
            raise

    #滚动条处理
    def scroll_bar(self,):
        self.driver.execute_script()

    #鼠标悬浮操作
    def mouse_suspension(self,locator,doc):
        try:
            self.wait_eleVisibel(locator,doc="")#等待元素可见
            above = self.get_element(locator,doc="")#查找元素
            ActionChains(self.driver).move_to_element(above).perform()# 实例化ActionChains类 #将鼠标操作添加到actions列表中#并且执行鼠标悬停操作
            my_logger.info("{0}鼠标悬浮成功".format(doc))
        except:
            my_logger.info("{0}鼠标悬浮失败".format(doc))
            self.save_screenshot(doc)
            raise

