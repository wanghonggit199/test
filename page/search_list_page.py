"""
搜索列表页
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class SearchListPage(BasePage):
    """
    搜索列表对象层
    """

    def __init__(self):
        super().__init__()
        self.goods = (By.XPATH, '//*[@class="shop_name2"]/*[contains(text(),"{}")]')

    def find_goods(self, kw):
        """
        搜索到的商品定位方法
        :param kw: 关键字
        :return:
        """
        location = (self.goods[0], self.goods[1].format(kw))
        return self.find_element_func(location)


class SearchListHandle(BaseHandle):
    """
    搜索列表操作层
    """

    def __init__(self):
        self.search_list_page = SearchListPage()

    def click_goods(self, kw):
        """
        搜索到的商店点击方法
        :param kw: 关键字
        :return:
        """
        self.click_element(self.search_list_page.find_goods(kw))


class SearchListProxy():
    """
    搜索列表业务层
    """

    def __init__(self):
        self.search_list_handle = SearchListHandle()

    def go_to_goods_detail(self, kw):
        """跳转商品详情页业务方法"""
        self.search_list_handle.click_goods(kw)
