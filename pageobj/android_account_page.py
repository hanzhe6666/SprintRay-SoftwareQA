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

class AccountPage(App):
    def goto_account(self, ):
        self.appexe(__file__, sys._getframe().f_code.co_name )
    def goto_login(self, ):
        self.appexe(__file__, sys._getframe().f_code.co_name )

    def Sign_In_Code(self, ):
        code = self.appexe(__file__, sys._getframe().f_code.co_name)
        LogUrl = f"https://dev-auth.sprintray.com/activate?user_code={code}"
        return LogUrl

    def Click_Confirm(self, ):
        self.appexe(__file__, sys._getframe().f_code.co_name)

    def enter_email(self, email):
        self.appexe(__file__, sys._getframe().f_code.co_name, text=email)
    def enter_password(self, password):
        self.appexe(__file__, sys._getframe().f_code.co_name, text=password)

    def Click_btn_login(self, ):
        self.appexe(__file__, sys._getframe().f_code.co_name)

    def Sign_In(self, ):
        SignIn = self.appexe(__file__, sys._getframe().f_code.co_name)
        return SignIn
    def Click_Log_Out(self, ):
        self.appexe(__file__, sys._getframe().f_code.co_name)

    def Click_ivClose(self, ):
        self.appexe(__file__, sys._getframe().f_code.co_name)
