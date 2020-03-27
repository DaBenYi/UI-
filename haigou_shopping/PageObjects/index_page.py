from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Common.case_login import MyLog
from Common.basepage import BasePage
from PageLocators.index_page_locators import IndexPageLocators as IPL

my_logger=MyLog()#日志

#登录成功后，首页面元素操作
class IndexPage(BasePage):
     #定位“退出”文本
    def isExist_logout_ele(self):
        #如果存在就返回true，如果不存在，就返回Fales
        doc="登录首页_退出文本存在"
        try:
            self.wait_eleVisibel(IPL.sign_out,doc=doc)
            my_logger.info("登录成功")
            return True
        except:
            my_logger.info("登录失败，帐户或密码错误")
            return False

    #选择一件商品，点击
    def select_product(self):
        doc="首页面-选择商品"
        self.wait_eleVisibel(IPL.panic_buying,doc=doc) #等待“疯狂抢购”模块元素出现
        self.click_element(IPL.panic_buying,doc)#进入“疯狂抢购”模块，选择商品
        self.click_element(IPL.product_out,doc)#点击商品，进入商品详情页

