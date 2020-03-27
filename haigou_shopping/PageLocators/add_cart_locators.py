from selenium.webdriver.common.by import By

class AddCartLocators:
    add_button=(By.XPATH,'//input[@value="添加到购物车"]')
    add_sucess_text=(By.XPATH,'//li[contains(text(),"已成功添加到购物车！")]')
    view_cart_text=(By.XPATH,'//span[@id="cart_goods_top_menu"]') #鼠标悬浮操作
    view_my_cart_text=(By.XPATH,'//a[contains(text(),"查看我的购物车")]')
