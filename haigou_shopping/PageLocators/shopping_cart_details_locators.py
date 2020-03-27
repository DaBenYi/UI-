from selenium.webdriver.common.by import By

class ShoppingCartDetailsLocators:

    collection_text=(By.ID,'favorite_101711')#“收藏”按钮
    share_text=(By.XPATH,'//a[contains(@dialog_uri,"101711")]')# “分享”按钮
    share_evaluate_text=(By.XPATH,'//textarea')#分享文本框
    share_evaluate_button=(By.XPATH,'//input[@id="share_storeOrgoods"]')#分享评价按钮
    share_sucess_text=(By.XPATH,'//span[contains(text(),"发布成功！")]')