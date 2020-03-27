from Common.basepage import BasePage
from PageLocators.shopping_cart_details_locators import ShoppingCartDetailsLocators as SCDL
import time
from selenium.webdriver.support import expected_conditions as EC
#g购物车详情页-元素操作
class ShoppingCartDetailsPage(BasePage):

    #"收藏"元素获取,并且点击
    def collection(self):
        doc="购物车详情页-收藏操作"
        self.wait_eleVisibel(SCDL.collection_text,doc=doc)#等待收藏元素出现
        self.click_element(SCDL.collection_text,doc=doc)#点击收藏按钮
        time.sleep(1)#需要等待下警告框出现
        alert_text=self.alter_action(doc=doc)#获取警告框文本内容
        return alert_text

    # "分享"元素获取,并且点击
    def share(self,text):
        doc="购物车详情页-分享操作"
        self.wait_eleVisibel(SCDL.share_text,doc=doc)#等待分享元素出现
        self.click_element(SCDL.share_text,doc=doc)#点击分享按钮
        self.wait_eleVisibel(SCDL.share_evaluate_text,doc=doc)#等待分享文本框出现
        self.input_text(SCDL.share_evaluate_text,text,doc=doc)#点击文件框，输入分享评价
        self.click_element(SCDL.share_evaluate_button,doc=doc)#评价写完之后，点击分享按钮
        self.wait_eleVisibel(SCDL.share_sucess_text,doc=doc)#等待提示页面“发布成功！”出现
        share_sucess = self.get_text(SCDL.share_sucess_text,doc=doc) #获取提示页面中“发布成功！”
        return share_sucess
