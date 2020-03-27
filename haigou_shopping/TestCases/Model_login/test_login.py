from PageObjects.index_page import IndexPage
from TestDatas.Model_login import test_login_datas as LD
from Common.case_login import MyLog
import pytest
#conftest不需要导入
#登录功能模块
my_logger=MyLog()#日志
# @pytest.mark.usefixtures("access_web") #在运行的时候，会去运行access_web函数
# @pytest.mark.usefixtures("refresh_page")#每一个用例都需要刷新，可以放在每一个用例函数前，但是，放在类前就行
# class TestLogin:
#
#     # 异常用例 -用户名为空
#     def test_login_user_empty(self,access_web):
#         access_web[1].login(LD.fail_data1["user"],LD.fail_data1["passwd"])
#         assert access_web[1].get_errorMsg_from_loginArea(),LD.fail_data1["check"]
#     # 异常用例 -密码为空
#     def test_login_passwd_empty(self,access_web):
#         access_web[1].login(LD.fail_data2["user"],LD.fail_data2["passwd"])
#         assert access_web[1].get_errorMsg_from_loginArea1(), LD.fail_data2["check"]
#     #去掉DDT，用parametrize参数化
#     @pytest.mark.parametrize("data",LD.fail_data3)
#     def test_login_user_passwd_wrong(self,data,access_web):
#         access_web[1].login(data["user"],data["passwd"])
#         assert access_web[1].get_errorMsg_from_loginArea2(),data["check"]
#
#     # 正常用例-登录成功
#     def test_loginz_success(self,access_web):#access_web接收yield 返回的driver   lg
#         access_web[1].login(LD.sucess_data["user"], LD.sucess_data["passwd"])#步骤 输入密码 用户名 点击登录
#         assert IndexPage(access_web[0]).isExist_logout_ele() #assert +表达式就行 看返回值是true 还是false



