from PageLocators.login_page_locators import LoginPageLocator as plg
from Common.basepage import BasePage
#登录页面元素操作
class LoginPage(BasePage):
    '''
    将页面的元素定位和元素行为封装成一个page类
    类的属性：元素的定位
    类的行为：元素的操作
    '''
    #登录
    def login(self,username,passwd):
        doc = "登录页面_登录功能"
        self.wait_eleVisibel(plg.name_id,doc=doc)
        self.input_text(plg.name_id,username,doc)
        self.input_text(plg.pwd_id,passwd,doc)
        self.click_element(plg.log_but,doc)

    #获取错误提示信息-登录区域-用户名
    def get_errorMsg_from_loginArea(self):
        doc = "获取登录区域-用户名的错误"
        self.wait_eleVisibel(plg.error_user,doc=doc)
        return self.get_text(plg.error_user,doc)

    # 获取错误提示信息-登录区域-密码
    def get_errorMsg_from_loginArea1(self):
        doc = "获取登录区域-密码的错误"
        self.wait_eleVisibel(plg.error_passwd,doc=doc)
        return self.get_text(plg.error_passwd,doc)

    # 获取错误提示信息-登录区域-登录跳转
    def get_errorMsg_from_loginArea2(self):
        doc = "获取登录区域-登录跳转的错误"
        self.wait_eleVisibel(plg.error_jump,doc=doc)
        return self.get_text(plg.error_jump,doc)



    #注册
    def register(self):
        pass
    #忘记密码
    def forget_passwd(self):
        pass