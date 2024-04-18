# -*- coding: utf-8 -*-
# @File: 1android.py
# @Author: Joe
# @E-mail: zhufeng@sprintray.cn
# @Time: 2024/1/4  12:57

import os
import sys

sys.path.append(os.pardir)

from public import App


class AndroidSprintrayAccountSignInPage(App):
    def goto_sign_in_with_email(self):
        self.appexe(__file__, sys._getframe().f_code.co_name)

    def goto_sign_in_with_qr_code(self, ):
        self.appexe(__file__, sys._getframe().f_code.co_name )