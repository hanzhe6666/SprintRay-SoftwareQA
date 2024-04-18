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
from public import reda_pytestdata


class TestCuringProcess:
    # @pytest.mark.skip(reason="暂时跳过这个测试用例")
    @allure.feature("搜索")  # 测试用例特性（主要功能模块）
    @allure.story("搜索")  # 模块说明
    @allure.title("验证不存在的材料是否能被搜索到")  # 用例标题
    @allure.description('验证不存在的材料是否能被搜索到')  # 用例描述
    @pytest.mark.test_search_nonexistent_material  # 用列标记
    @pytest.mark.parametrize('material',
                             reda_pytestdata(__file__, 'test_search_nonexistent_material'))  # 测试数据
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
        with allure.step('进入材料搜索页面并且搜索不存在材料'):
            hp.search_material(material)
            subprocess.run("adb shell input tap 250 800", shell=True)
        assert hp.get_tryagain_text() == "Try Again"
        with allure.step('测试完成'):
            pass

