from selenium.webdriver.common.by import By

class IndexPageLocators:
    '''只管理元素定位'''

    #“退出”文本定位
    sign_out=(By.XPATH, '//a[contains(text(),"退出")]')
    panic_buying=(By.XPATH,'//li[@id="goodscase2"]')
    product_out=(By.XPATH,'//div[@id="index_sale_box_2"]//span')