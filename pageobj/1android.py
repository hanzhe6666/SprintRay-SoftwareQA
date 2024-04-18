# -*- coding: utf-8 -*-
# @File: 1android.py
# @Author: Joe
# @E-mail: zhufeng@sprintray.cn
# @Time: 2021/6/22  12:57

import os
import sys

sys.path.append(os.pardir)

from public import App




class OpenWelComePage(App):

    def click_next_button(self, ):
        self.appexe(__file__, sys._getframe().f_code.co_name )
