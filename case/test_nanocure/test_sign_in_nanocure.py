# -*- coding: utf-8 -*-
# @File: test_sign_in_nanocure.py.py
# @Author: Joe
# @E-mail: zhufeng@sprintray.cn
# @Time: 2021/6/22  16:58

# -*- coding: utf-8 -*-
# @File: test_sign_in_nanocure.py
# @Author: Joe
# @E-mail: zhufeng@sprintray.cn
# @Time: 2021/6/22  11:43

import os
import time
import allure
import pytest
import subprocess
from pageobj.android_home_page import HomePage
from pageobj.android_device_information_page import DeviceInformationPage
from pageobj.android_account_page import AccountPage
from pageobj.android_queue_page import QueuePage
from pageobj.android_settings_page import SettingsPage
from public import reda_pytestdata
from selenium.common.exceptions import NoSuchElementException

class TestSignIn:
    # @pytest.mark.skip(reason="暂时跳过这个测试用例")
    @allure.feature("账户")  # 测试用例特性（主要功能模块）
    @allure.story("登录")  # 模块说明
    @allure.title("登录是否有效")  # 用例标题
    @allure.description('验证登录是否有效')  # 用例描述
    @pytest.mark.test_sign_in_nonocure   # 用列标记
    @pytest.mark.parametrize('email,password,',
                             reda_pytestdata(__file__, 'test_sign_in_nonocure'))  # 测试数据
    def test_sign_in_nanocure(self, goDriver, email, password):
        with allure.step('进入NanoCure设备首页'):
            time.sleep(2)
            subprocess.run('adb shell am start -n "com.soonsolid.curemini/com.soonsolid.curemini.test.QcAc"', shell=True)
            time.sleep(2)
            subprocess.run('adb shell am start -n "com.soonsolid.curemini/com.soonsolid.curemini.cure.CureBaseAc"', shell=True)
            goDriver.implicitly_wait(30)
            hp = HomePage(goDriver)
            hp.goto_home()

        with allure.step('进入NanoCure设备信息页'):
            dip = DeviceInformationPage(goDriver)
            dip.goto_device_information()

        with allure.step('进入NanoCure设备队列页'):
            qp = QueuePage(goDriver)
            qp.goto_queue()

        with allure.step('进入NanoCure设备设置页'):
            sp = SettingsPage(goDriver)
            sp.goto_settings()

        with allure.step('进入NanoCure设备用户页'):
            up = AccountPage(goDriver)
            up.goto_account()

        with allure.step('进入NanoCure登录二维码页面'):
            goDriver.implicitly_wait(1)
            try:
                goDriver.find_element("id", "com.soonsolid.curemini:id/logoutBtn")
                up.Click_Log_Out()
                up.goto_login()
            except NoSuchElementException:
                up.goto_login()

        with allure.step('登录账号'):
            goDriver.implicitly_wait(30)
            Sing_In_Url = up.Sign_In_Code()
            subprocess.run("adb shell pm clear org.chromium.webview_shell", shell=True)
            command = f"adb shell am start -a android.intent.action.VIEW -d {Sing_In_Url}"
            subprocess.run(command, shell=True)
            up.Click_Confirm()
            up.enter_email(email)
            subprocess.run("adb shell input keyevent KEYCODE_BACK", shell=True)
            up.enter_password(password)
            subprocess.run("adb shell input keyevent KEYCODE_BACK", shell=True)
            up.Click_btn_login()
            subprocess.run("adb shell input keyevent KEYCODE_BACK", shell=True)
            up.Click_ivClose()
        with allure.step('测试完成'):
            pass

