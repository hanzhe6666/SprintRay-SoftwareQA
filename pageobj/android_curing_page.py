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

class CuringPage(App):

    def start_curing(self, ):
        self.appexe(__file__, sys._getframe().f_code.co_name)

    def get_curing_comp_text(self, ):
        curing_comp_text = self.appexe(__file__, sys._getframe().f_code.co_name)
        return curing_comp_text
