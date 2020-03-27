#正常场景-测试数据
sucess_data = {"user":"sqdaben","passwd":"123456"}
#异常用例-用户名为空
fail_data1 = {"user":"","passwd":"123456","check":"用户名不能为空"}

#异常用例-密码为空
fail_data2 = {"user":"sqdaben","passwd":"","check":"密码不能为空"}

#异常用例-用户名或密码错误
fail_data3 = [
    {"user":"aaa1","passwd":"123456","check":"登录失败！"},
    {"user":"sqdaben","passwd":"buy122","check":"登录失败！"},
]