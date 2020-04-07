"""
PO 文件的基类
"""
import logging

from selenium.webdriver.common.by import By

from utlis import DriverUtil
from selenium.webdriver.support.wait import WebDriverWait
from base import *


class BasePage(object):
    """对象库层-基类"""

    def __init__(self):
        self.driver = DriverUtil.get_driver()  # 获取浏览器对象

    # def find_element_func(self, location):
    #     """元素定位方法"""
    #     return self.driver.find_element(location[0], location[1])

    def find_element_func(self, loc, timeout=30, poll=0.5):
        """
                查找元素方法
                :param loc: 要查找的元素
                :param timeout: 显示等待时间
                :param poll: 查找间隔时间
                :return:
        """

        logging.info('正在查找元素 {}'.format(loc))
        try:
            return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll). \
                until(lambda x: x.find_element(*loc))
        except Exception:
            return "未找到元素{}".format(loc)

    # def base_find(self, loc, timeout=30, poll=0.5):
    #     """
    #     查找元素方法
    #     :param loc: 要查找的元素
    #     :param timeout: 显示等待时间
    #     :param poll: 查找间隔时间
    #     :return:
    #     """
    #     return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll). \
    #         until(lambda x: x.find_element(*loc))


class BaseHandle(object):
    """操作层-基类"""

    @staticmethod
    def input_text(element, text):
        """
        输入文本方法
        :param element: 元素对象
        :param text: 要输入的文本内容
        :return: 无返回值
        """
        logging.info('正在向元素对象 {} 中输入文本 {}'.format(element, text))
        element.clear()
        element.send_keys(text)

    @staticmethod
    def click_element(element):
        """
        点击元素方法
        :param element: 目标元素
        :return: 无返回值
        """
        logging.info('正在点击元素对象 {}'.format(element))
        element.click()
