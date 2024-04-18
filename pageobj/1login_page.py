# -*- coding: utf-8 -*-
# @File: 1login_page.py
# @Author: Joe
# @E-mail: zhufeng@sprintray.cn
# @Time: 2023/11/27  16:21

import os
import sys
import time

from pageobj.home_page import HomePage

sys.path.append(os.pardir)

from public import Web




'''

pageobj  对应 locatorYAML 操作页面
'''


class LoginPage(Web):


    def fill_email_field(self, user):
        """
        输入邮箱地址
        :param content: 输入内容
        :return:
        """
        #self.webexe(__file__,sys._getframe().f_code.co_name)
        # __file__ 代表当前运行的py文件 运行的py文件必须和locatorYAML保持文件名称一样
        # sys._getframe().f_code.co_name 获取当前运行函数名称  次函数名称必须和 locatorYAML 的casename保持一致
        #self.web_is_element_displayed('id','email')
        self.webexe(__file__, sys._getframe().f_code.co_name, text=user)

    def fill_password_field(self, pwd):
        """
        输入密码
        :param content: 输入内容
        :return:
        """

        self.webexe(__file__, sys._getframe().f_code.co_name, text=pwd)

    def click_sign_in_button(self):
        """
        点击登录
        :return:
        """

        self.webexe(__file__, sys._getframe().f_code.co_name,)
        time.sleep(5)
        return HomePage(self.driver)