import pytest
from selenium import  webdriver
from TestDatas.Model_login import Common_Datas as URL
from TestDatas.Model_login import test_login_datas as LD
from PageObjects.login_page import LoginPage

driver=None

#声明它是一个fixture
@pytest.fixture(scope="class")
def access_web():
    #前置条件
    global driver
    driver = webdriver.Chrome()
    driver.get(URL.web_login_url)
    lg = LoginPage(driver)
    yield(driver,lg) #1.相当于分割线，前面代码是前置，后面代码是后置2.返回值 driver   lg
    #后置条件
    #driver.quit()
@pytest.fixture()
def refresh_page():
    '''刷新操作'''
    global driver
    #前置操作
    yield
    #后置操作
    driver.refresh()

