import logging
import unittest
import time
from page.goods_detail_page import GoodsDetailProxy
from page.index_page import IndexProxy
from page.search_list_page import SearchListProxy
from utlis import DriverUtil
from base import *


class TestCart(unittest.TestCase):
    """
    购物车测试类
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()  # 获取浏览器对象
        cls.index_proxy = IndexProxy()  # 获取首页业务对象
        cls.search_list_proxy = SearchListProxy()  # 获取搜索商品列表业务对象
        cls.goods_detail_proxy = GoodsDetailProxy()  # 获取商品详情页业务对象

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1')

    def test_cart(self):
        """购物车测试用例"""
        goods = '小米手机'
        self.index_proxy.go_to_search_list(goods)
        self.search_list_proxy.go_to_goods_detail(goods)
        self.goods_detail_proxy.add_cart_func()
        time.sleep(2)
        ret = self.goods_detail_proxy.get_result()
        # print(ret)
        logging.info(ret)
        try:
            self.assertIn('添加成功', ret)
        except AssertionError as e:
            raise e


if __name__ == '__main__':
    unittest.main()
