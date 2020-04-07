"""
公共方法类
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from config import BASE_DIR


def switch_new_window():
    """切换新窗口方法"""
    driver = DriverUtil.get_driver()
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])  # 下标为-1 的是新窗口的句柄值


def get_tip_text(text):
    """获取特定文本对应元素的方法"""
    xpath = '//*[contains(text(),"{}")]'.format(text)
    driver = DriverUtil.get_driver()
    try:
        element = driver.find_element_by_xpath(xpath)
        return element
    except Exception:
        return False


def base_get_img():
    # 注意：图片名写死！
    driver = DriverUtil.get_driver()
    driver.get_screenshot_as_file("../scareenshot/err.png")


def base_get_toast(msg):
    driver = DriverUtil.get_driver()
    loc = By.XPATH, "//*[contains(@text,'{}')]".format(msg)
    # log.info("获取包含 {}文本的 toast消息内容:{} ".format(msg, self.base_find(loc).text))
    return driver.find_element(loc).text

class DriverUtil(object):
    """浏览器驱动工具类"""
    _driver = None  # 设置浏览器对象初始化状态 (保护变量)
    _quit_status = True  # 退出状态

    @classmethod
    def get_driver(cls):
        """获取浏览器对象方法"""
        # 为了防止反复创建浏览器对象, 需要对浏览器对象是否存在进行判断
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.get('http://127.0.0.1')
            cls._driver.maximize_window()  # 窗口最大化
            cls._driver.implicitly_wait(10)  # 隐式等待
        return cls._driver

    @classmethod
    def quit_driver(cls):
        """退出浏览器对象方法"""
        # 需要判断浏览器对象存在, 才能执行退出操作, 否则会报错!
        if cls._driver and cls._quit_status:
            cls._driver.quit()
            cls._driver = None  # 此代码是确保浏览器对象会被从内存中移除掉

    @classmethod
    def change_quit_status(cls, status):
        """修改退出方法状态方法"""
        cls._quit_status = status


if __name__ == '__main__':
    DriverUtil.get_driver()
    time.sleep(3)
    base_get_img()
    time.sleep(3)
    DriverUtil.quit_driver()
