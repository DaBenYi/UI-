from Common.basepage import BasePage
from PageLocators.add_cart_locators import AddCartLocators as plg

#产品详情页面元素定位
class ProductDetailsPage(BasePage):

    #添加到购物车
    def addcare(self):
        doc="商品详情页"
        self.switch_windows(1,doc=doc)  # 窗口切换到详情页面
        self.wait_eleVisibel(plg.add_button,doc=doc)
        self.click_element(plg.add_button,doc)

    #定位"已成功添加到购物车！"文本元素
    def get_add_sucess_text(self):
        doc = "商品详情页-已成功添加到购物车！"
        self.wait_eleVisibel(plg.add_sucess_text,doc=doc)
        return self.get_text(plg.add_sucess_text,doc)

    #定位“查看我的购物车”文本元素，并且点击
    def get_view_cart(self):
        doc="商品详情页-查看我的购物车"
        self.mouse_suspension(plg.view_cart_text,doc=doc)#鼠标悬浮操作
        self.wait_eleVisibel(plg.view_my_cart_text,doc=doc)
        self.click_element(plg.view_my_cart_text,doc=doc)#找到元素，并且点击

