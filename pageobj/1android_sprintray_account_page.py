# -*- coding: utf-8 -*-
# @File: 1android.py
# @Author: Joe
# @E-mail: zhufeng@sprintray.cn
# @Time: 2024/1/3  12:57

import os
import sys

sys.path.append(os.pardir)

from public import App


class AndroidSprintrayAccountPage(App):
    def goto_sign_in(self):
        self.appexe(__file__, sys._getframe().f_code.co_name)

    def goto_sign_up(self, ):
        self.appexe(__file__, sys._getframe().f_code.co_name )