"""
登录页面
"""
from base.base_page import BasePage, BaseHandle
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    """
    登录页面-对象层
    """

    def __init__(self):
        super().__init__()
        self.username = (By.ID, 'username')  # 账号
        self.password = (By.ID, 'password')  # 密码
        self.verify_code = (By.ID, 'verify_code')  # 验证码
        self.login_btn = (By.NAME, 'sbtbutton')  # 登录按钮

    def find_username(self):
        """用户名定位方法"""
        return self.find_element_func(self.username)

    def find_password(self):
        """密码定位方法"""
        return self.find_element_func(self.password)

    def find_verify_code(self):
        """验证码定位方法"""
        return self.find_element_func(self.verify_code)

    def find_login_btn(self):
        """登录按钮定位方法"""
        return self.find_element_func(self.login_btn)


class LoginHandle(BaseHandle):
    """
    登录页面-操作层
    """

    def __init__(self):
        self.login_page = LoginPage()

    def input_username(self, username):
        """
        用户名输入方法
        :param username: 用户账号
        :return:
        """
        self.input_text(self.login_page.find_username(), username)

    def input_password(self, password):
        """
        密码输入方法
        :param password: 密码
        :return:
        """
        self.input_text(self.login_page.find_password(), password)

    def input_verify_code(self, code):
        """
        验证啊输入方法
        :param code: 验证码
        :return:
        """
        self.input_text(self.login_page.find_verify_code(), code)

    def click_login_btn(self):
        """
        登录按钮点击方法
        :return:
        """
        self.click_element(self.login_page.find_login_btn())


class LoginProxy():
    """
    登录页面-业务层
    """
    def __init__(self):
        self.login_handle = LoginHandle()

    def login(self, username, password, code):
        self.login_handle.input_username(username)
        self.login_handle.input_password(password)
        self.login_handle.input_verify_code(code)
        self.login_handle.click_login_btn()