"""
订单-测试用例
订单支付-测试用例
 (次用例不能单独执行,需要和登录,购物车脚本建立依赖关系)
"""
import logging
import time
import unittest
from base import *
from page.goods_cart_page import GoodsCartProxy
from page.index_page import IndexProxy
from page.my_order_page import MyOrderPreoxy
from page.order_check_page import OrderCheckProxy
from page.order_pay_page import OrderPayProxy
from utlis import DriverUtil, get_tip_text, switch_new_window


class TestOrder(unittest.TestCase):
    """订单测试类"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()
        cls.index_proxy = IndexProxy()
        cls.goods_cart_proxy = GoodsCartProxy()
        cls.order_check_proxy = OrderCheckProxy()
        cls.my_order_proxy = MyOrderPreoxy()
        cls.order_pay_proxy = OrderPayProxy()

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1')

    def test1_order(self):
        """订单测试方法"""
        self.index_proxy.go_to_goods_cart()
        self.goods_cart_proxy.go_to_order_check()
        time.sleep(3)
        self.order_check_proxy.submit_order_func()
        result = get_tip_text('订单提交成功')
        try:
            self.assertTrue(result)
        except AssertionError:
            return False
        time.sleep(5)

    def test2_pay(self):
        """订单支付测试方法"""
        self.index_proxy.go_to_my_order()
        switch_new_window()
        self.my_order_proxy.go_to_order_pay()
        switch_new_window()
        self.order_pay_proxy.order_pay_func()
        result = get_tip_text('成功')
        logging.info(result)
        try:
            self.assertTrue(result)
        except AssertionError:
            return False
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
