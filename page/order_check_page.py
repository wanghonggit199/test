"""
订单确认页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class OrderCheckPage(BasePage):
    """订单确认页面对象层"""

    def __init__(self):
        super().__init__()
        self.submit_order = (By.LINK_TEXT, '提交订单')  # 提交订单按钮

    def find_submit_order(self):
        """提交订单按钮定位方法"""
        return self.find_element_func(self.submit_order)


class OrderCheckHandle(BaseHandle):
    """订单确认页面操作层"""

    def __init__(self):
        self.order_check_page = OrderCheckPage()

    def click_submit_order(self):
        """提交订单点击方法"""
        self.click_element(self.order_check_page.find_submit_order())


class OrderCheckProxy():
    """订单确认页面业务层"""

    def __init__(self):
        self.order_check_handle = OrderCheckHandle()

    def submit_order_func(self):
        """提交订单方法"""
        self.order_check_handle.click_submit_order()
