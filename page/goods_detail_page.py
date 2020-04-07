"""
搜索列表页
"""
import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle
from utlis import DriverUtil


class GoodsDetailPage(BasePage):
    """
    商品详情对象层
    """

    def __init__(self):
        super().__init__()
        self.add_cart_btn = (By.ID, 'join_cart')  # 加入购物车按钮
        self.add_cart_result = (By.CSS_SELECTOR, '.conect-title')  # 加入结果

    def find_add_cart_btn(self):
        """加入购物车按钮定位方法"""
        return self.find_element_func(self.add_cart_btn)

    def find_add_cart_result(self):
        """加入购物车结果定位方法"""
        return self.find_element_func(self.add_cart_result)


class GoodsDetailHandle(BaseHandle):
    """
    商品详情操作层
    """

    def __init__(self):
        self.goods_detail_page = GoodsDetailPage()

    def click_add_cart_btn(self):
        """点击加入购物车按钮操作方法"""
        time.sleep(3)
        self.click_element(self.goods_detail_page.find_add_cart_btn())

    def get_add_cart_result(self):
        """获取加入购物车结果"""
        driver = DriverUtil.get_driver()
        driver.switch_to_frame(driver.find_element_by_tag_name('iframe'))
        return self.goods_detail_page.find_add_cart_result().text


class GoodsDetailProxy():
    """
    商品详情业务层
    """
    def __init__(self):
        self.goods_detail_handle = GoodsDetailHandle()

    def add_cart_func(self):
        """添加购物车方法"""
        self.goods_detail_handle.click_add_cart_btn()

    def get_result(self):
        """获取添加购物车结果"""
        return self.goods_detail_handle.get_add_cart_result()