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
from pageobj.android_curing_page import CuringPage
from public import reda_pytestdata
from appium import webdriver


class TestCuringProcess:
    # @pytest.mark.skip(reason="暂时跳过这个测试用例")
    @allure.feature("固化")  # 测试用例特性（主要功能模块）
    @allure.story("固化")  # 模块说明
    @allure.title("sprintray材料列表中的材料是否能正常固化")  # 用例标题
    @allure.description('验证sprintray材料列表中的材料固化流程是否正常')  # 用例描述
    @pytest.mark.test_curing_sprintray_NanoCure   # 用列标记
    def test_curing_sprintray_NanoCure(self, goDriver):
        with allure.step('进入NanoCure设备首页'):
            time.sleep(2)
            subprocess.run('adb shell am start -n "com.soonsolid.curemini/com.soonsolid.curemini.test.QcAc"', shell=True)
            time.sleep(2)
            subprocess.run('adb shell am start -n "com.soonsolid.curemini/com.soonsolid.curemini.cure.CureBaseAc"', shell=True)
            goDriver.implicitly_wait(10)
            hp = HomePage(goDriver)
            hp.goto_home()
        with allure.step('进入Sprintray材料列表页面'):
            hp.goto_sprintray_material()
            hp.select_castable2_material()
        with allure.step('进入Sprintray材料固化页面'):
            mp = CuringPage(goDriver)
            mp.start_curing()
            goDriver.implicitly_wait(90)
            curing_comp_text = mp.get_curing_comp_text()
            assert curing_comp_text == "Curing Complete"
        with allure.step('测试完成'):
            pass

    @allure.feature("固化")  # 测试用例特性（主要功能模块）
    @allure.story("固化")  # 模块说明
    @allure.title("验证搜索出来的材料是否能正常固化")  # 用例标题
    @allure.description('验证搜索出来的材料固化流程是否正常')  # 用例描述
    @pytest.mark.test_curing_search_nanocure  # 用列标记
    @pytest.mark.parametrize('material',
                             reda_pytestdata(__file__, 'test_search_material'))  # 测试数据
    def test_curing_search_nanocure(self, goDriver, material):
        with allure.step('进入NanoCure设备首页'):
            time.sleep(2)
            subprocess.run('adb shell am start -n "com.soonsolid.curemini/com.soonsolid.curemini.test.QcAc"',
                           shell=True)
            time.sleep(2)
            subprocess.run('adb shell am start -n "com.soonsolid.curemini/com.soonsolid.curemini.cure.CureBaseAc"',
                           shell=True)
            goDriver.implicitly_wait(10)
            hp = HomePage(goDriver)
            hp.goto_home()
        with allure.step('进入材料搜索页面并且搜索指定材料'):
            hp.search_material(material)
            subprocess.run("adb shell input tap 250 800", shell=True)
            hp.select_search_castable2_material()
        with allure.step('进入搜索材料固化页面'):
            mp = CuringPage(goDriver)
            mp.start_curing()
            goDriver.implicitly_wait(90)
            curing_comp_text = mp.get_curing_comp_text()
            assert curing_comp_text == "Curing Complete"
        with allure.step('测试完成'):
            pass

    @allure.feature("固化")  # 测试用例特性（主要功能模块）
    @allure.story("固化")  # 模块说明
    @allure.title("验证自定义固化需要预加热流程是否正常")  # 用例标题
    @allure.description('验证自定义固化需要预加热流程是否正常')  # 用例描述
    @pytest.mark.test_curing_custom_nanocure  # 用列标记
    def test_curing_custom_heater_on(self, goDriver):
        with allure.step('进入NanoCure设备首页'):
            time.sleep(2)
            subprocess.run('adb shell am start -n "com.soonsolid.curemini/com.soonsolid.curemini.test.QcAc"',
                           shell=True)
            time.sleep(2)
            subprocess.run('adb shell am start -n "com.soonsolid.curemini/com.soonsolid.curemini.cure.CureBaseAc"',
                           shell=True)
            goDriver.implicitly_wait(10)
            hp = HomePage(goDriver)
            hp.goto_home()
        with allure.step('进入自定义固化页面'):
            hp.goto_custom()
        with allure.step('设置固化参数开始固化'):
            hp.add_ten_sec()
            hp.start_curing()
            cp = CuringPage(goDriver)
            cp.start_curing()
            goDriver.implicitly_wait(90)
            curing_comp_text = cp.get_curing_comp_text()
            assert curing_comp_text == "Curing Complete"
        with allure.step('测试完成'):
            pass

