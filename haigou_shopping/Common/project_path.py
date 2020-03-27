import os
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]


#所有测试用例的目录
all_test_case_path=os.path.join(project_path,"TestCases",)

#测试报告的路径
test_report_path=os.path.join(project_path,"Outputs","reports","test_report.html")

#日志的路径
case_log_path=os.path.join(project_path,"Outputs","logs","case_log")

#截图路径
screenshot_path=os.path.join(project_path,"Outputs/screnshots/")

