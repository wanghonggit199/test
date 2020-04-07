"""
购物车页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class GoodsCartPage(BasePage):
    """
    购物车页面对象层
    """

    def __init__(self):
        super().__init__()
        self.check_all = (By.CSS_SELECTOR, '.checkCartAll')  # 全选复选框
        self.go_check = (By.LINK_TEXT, '去结算')  # 去结算按钮

    def find_check_all(self):
        """全选定位方法"""
        return self.find_element_func(self.check_all)

    def find_go_check(self):
        """去结算定位方法"""
        return self.find_element_func(self.go_check)


class GoodsCartHandle(BaseHandle):
    """
    购物车页面操作层
    """

    def __init__(self):
        self.goods_cart_page = GoodsCartPage()

    def click_check_all(self):
        """点击全选操作方法"""
        check_all_element = self.goods_cart_page.find_check_all()
        if not check_all_element.is_selected():
            self.click_element(check_all_element)

    def click_go_check(self):
        """点击去结算操作方法"""
        self.click_element(self.goods_cart_page.find_go_check())


class GoodsCartProxy():
    """
    购物车页面业务层

    """
    def __init__(self):
        self.goods_cart_handle = GoodsCartHandle()

    def go_to_order_check(self):
        """点击跳转订单确认页面"""
        self.goods_cart_handle.click_check_all()
        self.goods_cart_handle.click_go_check()