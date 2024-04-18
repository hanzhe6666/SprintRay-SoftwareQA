# -*- coding: utf-8 -*-
# @File: test_demo.py
# @Author: Joe
# @E-mail: zhufeng@sprintray.cn
# @Time: 2023/11/27  10:48
import time

import allure
import pytest

from pageobj.login_page import LoginPage
from pageobj.home_page import HomePage
from public.reda_data import reda_pytestdata


# 修改 setting  URL
class TestCreateTreatmentAiCrown:
    @pytest.mark.skip(reason="暂时跳过这个测试用例")
    @allure.feature("登录功能")  # 测试用例特性（主要功能模块）
    @allure.story("测试登录功能")  # 模块说明
    @allure.title("输入内容并点击登录")  # 用例标题
    @allure.description('输入多参数登录')  # 用例描述
    @pytest.mark.testdesignservice_web  # 用列标记
    @pytest.mark.parametrize('user,pwd', reda_pytestdata(__file__, 'test_new_ai_night_guard'))  # 测试数据
    def test_new_ai_night_guard(self, goDriver,user,pwd):
        Loginpage = LoginPage(goDriver)

        with allure.step('登录并点击cloud_design'):
            Loginpage.fill_email_field(user)
            Loginpage.fill_password_field(pwd)
            Loginpage.click_sign_in_button().go_to_rayware()

        # with allure.step('点击Cloud Design'):
        #     Homepage.go_to_cloud_design()
        #     time.sleep(10)