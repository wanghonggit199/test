"""
测试套件(项目运行入口)
"""
from utlis import DriverUtil
import unittest
import time
from config import BASE_DIR
from tools.HTMLTestRunnerCN import HTMLTestReportCN
from case.test002_cart import TestCart
from case.test001_login import TestLogin
from case.test003_oeder import TestOrder

# suite = unittest.TestSuite()  # 初始化套件对象
# 关闭浏览器退出方法
DriverUtil.change_quit_status(False)
# 调用方法测试用例
# suite.addTest(unittest.makeSuite(TestLogin))  # 登录
# suite.addTest(unittest.makeSuite(TestCart))  # 添加商品
# suite.addTest(unittest.makeSuite(TestOrder))  # 提交订单
run_suit = unittest.defaultTestLoader.discover(BASE_DIR + '/case', pattern='test*.py', top_level_dir=None)
# 初始化执行对象并调用方法
# unittest.TextTestRunner().run(suite)
# 设置报告存放路径及文件名
report_file = BASE_DIR + "/report/report{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
# 打开报告写入文件流
# 注意: wb 以二进制形式写入内容到文件
with open(report_file, "wb") as f:
    runner = HTMLTestReportCN(stream=f,
                              verbosity=2,
                              title='HPShop 自动化测试报告',
                              description='系统:Windows 浏览器:谷歌 编程语言:Python',
                              tester='QA')
    # 调用执行方法生成测试报告
    runner.run(run_suit)
time.sleep(5)

DriverUtil.change_quit_status(True)  # 打开浏览器
# 退出浏览器对象
DriverUtil.quit_driver()
