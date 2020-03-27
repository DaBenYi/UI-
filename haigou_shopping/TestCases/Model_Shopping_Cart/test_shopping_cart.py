from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from PageObjects.product_details_page import ProductDetailsPage
from PageObjects.shopping_cart_details_page import ShoppingCartDetailsPage
from TestDatas.Model_login import test_login_datas as LD
from TestDatas.Model_Shopping_Cart import shopping_cart_data as scd
import pytest
import time
from Common.case_login import MyLog
#购物车功能模块
@pytest.mark.usefixtures("access_web") #在运行的时候，会去运行access_web函数
#@pytest.mark.usefixtures("refresh_page")
class TestShoppingCart:

    #正常用例-商品添加购物车功能
    @pytest.mark.smoke
    def test_add_products(self,access_web):
        access_web[1].login(LD.sucess_data["user"], LD.sucess_data["passwd"]) #登录首页面
        IndexPage(access_web[0]).select_product()#选择商品，跳转到商品详情页
        ProductDetailsPage(access_web[0]).addcare()#在商品详情页，将商品添加到购物车
        assert ProductDetailsPage(access_web[0]).get_add_sucess_text(),scd.sucess_txt["sucess"] #断言文本“已成功添加到购物车！”

    #正常用例-购物车商品“收藏”功能
    def test_jump_to_cart(self,access_web):
        ProductDetailsPage(access_web[0]).get_view_cart()  # 跳转到购物车页面
        alert_text=ShoppingCartDetailsPage(access_web[0]).collection()#点击“收藏”按钮,alert_alert为返回得断言文本
        assert alert_text in scd.collection_txt

    #正常用例-购物车商品“分享”功能
    def test_ashare(self,access_web):
        share_sucess=ShoppingCartDetailsPage(access_web[0]).share(scd.share_txt["sharetxt"]) #点击“分享按钮”等一系列操作，最后返回“发布成功！”断言文本
        assert share_sucess,scd.share_release_sucess["sucess"]

