"""
首页页面

"""
from base.base_page import BasePage, BaseHandle
from selenium.webdriver.common.by import By


class IndexPage(BasePage):
    """
    首页-对象层
    """

    def __init__(self):
        super().__init__()
        self.login_link = (By.CLASS_NAME, 'red')  # 登录链接按钮
        self.search_bar = (By.ID, 'q')  # 搜索框
        self.search_btn = (By.CSS_SELECTOR, '.ecsc-search-button')  # 搜索按钮
        self.goods_cart_btn = (By.CSS_SELECTOR, '.share-shopcar-index')  # 购物车按钮
        self.my_order_link = (By.LINK_TEXT, '我的订单')  # 我的订单链接

    def find_login_link(self):
        """登录链接定位方法"""
        return self.find_element_func(self.login_link)

    def find_search_bar(self):
        """所搜框定位方法"""
        return self.find_element_func(self.search_bar)

    def find_search_btn(self):
        """搜索按钮定位方法"""
        return self.find_element_func(self.search_btn)

    def find_goods_cart_btn(self):
        """购物车按钮定位方法"""
        return self.find_element_func(self.goods_cart_btn)

    def find_my_order_link(self):
        """我的订单链接定位方法"""
        return self.find_element_func(self.my_order_link)


class IndexHandle(BaseHandle):
    """
    首页-操作层
    """

    def __init__(self):
        self.index_page = IndexPage()

    def click_login_link(self):
        """登录链接点击方法"""
        self.click_element(self.index_page.find_login_link())

    def input_search_bar(self, kw):
        """
        搜索框输入方法
        :param kw: 输入关键字
        :return:
        """
        self.input_text(self.index_page.find_search_bar(), kw)

    def click_search_btn(self):
        """搜索按钮点击方法"""
        self.click_element(self.index_page.find_search_btn())

    def click_goods_cart_btn(self):
        """购物车按钮点击方法"""
        self.click_element(self.index_page.find_goods_cart_btn())

    def click_my_order_link(self):
        """我的订单链接点击方法"""
        self.click_element(self.index_page.find_my_order_link())


class IndexProxy():
    """
    首页-业务层
    """

    def __init__(self):
        self.index_handle = IndexHandle()

    def go_to_login(self):
        """跳转登录页面"""
        self.index_handle.click_login_link()

    def go_to_search_list(self, kw):
        """
        去搜索列页面
        :param kw: 输入的关键字
        :return:
        """
        self.index_handle.input_search_bar(kw)
        self.index_handle.click_search_btn()

    def go_to_goods_cart(self):
        """
        点击去购物车页面
        :return:
        """
        self.index_handle.click_goods_cart_btn()

    def go_to_my_order(self):
        """点击去我的订单页面方法"""
        self.index_handle.click_my_order_link()
