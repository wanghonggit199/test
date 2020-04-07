import logging
import unittest
import time
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utlis import DriverUtil, base_get_img, get_tip_text
from parameterized import parameterized
from base import *
import json


def build_login_data():
    """登录模块测试数据构造方法"""
    # with open('./data/login_data.json', encoding='utf-8') as f:
    with open(BASE_DIR + '/data/login_data.json', encoding='utf-8') as f:
        data = json.load(f)
        data_list = list()
        for i in data.values():
            data_list.append((i.get('username'),
                              i.get('password'),
                              i.get('code'),
                              i.get('expect'),
                              i.get('success')))
        logging.info(data_list)
        return data_list


class TestLogin(unittest.TestCase):
    """
    登录测试类
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()  # 获取浏览器对象
        cls.index_proxy = IndexProxy()  # 获取首页业务对象
        cls.login_proxy = LoginProxy()  # 获取登录业务对象

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()  # 退出浏览器

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1')
        self.index_proxy.go_to_login()

    @parameterized.expand(build_login_data())
    def test_login(self, username, password, code, expect, success):
        """登录测试用例"""
        self.login_proxy.login(username, password, code)
        time.sleep(5)
        title = self.driver.title
        logging.info(title)
        text = get_tip_text(expect).text

        if success:
            self.assertIn(expect, title)
        else:
            self.assertEqual(expect, text)


if __name__ == '__main__':
    unittest.main()
