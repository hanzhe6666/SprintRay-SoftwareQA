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
from pageobj.android_queue_page import QueuePage
from pageobj.android_account_page import AccountPage
from pageobj.android_curing_page import CuringPage
from selenium.common.exceptions import NoSuchElementException
from public import reda_pytestdata

class TestQueueCuringProcess:
    # @pytest.mark.skip(reason="暂时跳过这个测试用例")
    @allure.feature("固化")  # 测试用例特性（主要功能模块）
    @allure.story("固化")  # 模块说明
    @allure.title("队列任务是否能正常固化")  # 用例标题
    @allure.description('验证队列任务固化流程是否正常')  # 用例描述
    @pytest.mark.sign_in_nonocure_data   # 用列标记
    @pytest.mark.parametrize('email,password,', reda_pytestdata(__file__, 'test_queue_cuing_process'))  # 测试数据
    def test_queue_cuing_process(self, goDriver, email, password):
        with allure.step('进入NanoCure设备首页'):
            time.sleep(2)
            subprocess.run('adb shell am start -n "com.soonsolid.curemini/com.soonsolid.curemini.test.QcAc"', shell=True)
            time.sleep(2)
            subprocess.run('adb shell am start -n "com.soonsolid.curemini/com.soonsolid.curemini.cure.CureBaseAc"', shell=True)
            goDriver.implicitly_wait(10)
            hp = HomePage(goDriver)
            hp.goto_home()
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

        with allure.step('进入队列页面'):
            time.sleep(2)
            subprocess.run('adb shell am start -n "com.soonsolid.curemini/com.soonsolid.curemini.test.QcAc"', shell=True)
            time.sleep(2)
            subprocess.run('adb shell am start -n "com.soonsolid.curemini/com.soonsolid.curemini.cure.CureBaseAc"', shell=True)
            qp = QueuePage(goDriver)
            qp.goto_queue()

        with allure.step('固化队列任务'):
            qp.click_first_task()
            qp.click_start()
            mp = CuringPage(goDriver)
            goDriver.implicitly_wait(600)
            curing_comp_text = mp.get_curing_comp_text()
            assert curing_comp_text == "Curing Complete"

        with allure.step('测试完成'):
            pass