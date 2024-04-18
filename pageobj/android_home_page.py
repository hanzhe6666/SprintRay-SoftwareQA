# -*- coding: utf-8 -*-
# @File: 1android.py
# @Author: Joe
# @E-mail: zhufeng@sprintray.cn
# @Time: 2024/1/3  12:57

import os
import sys
import time

sys.path.append(os.pardir)

from public import App


class HomePage(App):
    def goto_home(self):
        self.appexe(__file__, sys._getframe().f_code.co_name)
        # types = 'id'
        # locate = 'com.soonsolid.curemini:id/tvCentre'
        # message = self.driver_element(types=types, locate=locate).text
        # return message

    def goto_sprintray_material(self, ):
        self.appexe(__file__, sys._getframe().f_code.co_name)

    def select_castable2_material(self, ):
        self.appexe(__file__, sys._getframe().f_code.co_name)

    def select_search_castable2_material(self, ):
        self.appexe(__file__, sys._getframe().f_code.co_name)

    def search_material(self, material):
        self.appexe(__file__, sys._getframe().f_code.co_name, text=material)

    def select_search_castable2_material(self, ):
        self.appexe(__file__, sys._getframe().f_code.co_name)

    def scroll_custom(self, ):
        self.appexe(__file__, sys._getframe().f_code.co_name)

    def get_tryagain_text(self, ):
        tryagain_text = self.appexe(__file__, sys._getframe().f_code.co_name)
        return tryagain_text

    def goto_custom(self, ):
        self.appexe(__file__, sys._getframe().f_code.co_name)

    def add_ten_sec(self, ):
        self.appexe(__file__, sys._getframe().f_code.co_name)

    def start_curing(self, ):
        self.appexe(__file__, sys._getframe().f_code.co_name)