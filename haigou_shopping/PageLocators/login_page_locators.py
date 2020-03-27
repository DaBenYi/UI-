from selenium.webdriver.common.by import By

class LoginPageLocator:
    '''只管理元素定位'''
    #元素定位
    #用户名输入框
    name_id =(By.ID,'username')
    #密码输入框
    pwd_id = (By.ID,'password')
    #登录按钮定位
    log_but = (By.XPATH,'//input[@value ="登录"]')
    #错误提示框-用户名
    error_user = (By.XPATH,'//label[contains(text(),"用户名不能为空")]')
    #错误框提示-密码
    error_passwd = (By.XPATH,'//label[contains(text(),"密码不能为空")]')
    #错误框提示-登录跳转
    error_jump =(By.XPATH,'//span[contains(text(),"登录失败")]')