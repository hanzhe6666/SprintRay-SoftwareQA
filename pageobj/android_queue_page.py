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

class QueuePage(App):
    def goto_queue(self, ):
        self.appexe(__file__, sys._getframe().f_code.co_name )
    def click_first_task(self, ):
        self.appexe(__file__, sys._getframe().f_code.co_name)
    def click_start(self, ):
        self.appexe(__file__, sys._getframe().f_code.co_name)