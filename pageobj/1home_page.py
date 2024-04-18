# -*- coding: utf-8 -*-
# @File: 1home_page.py
# @Author: Joe
# @E-mail: zhufeng@sprintray.cn
# @Time: 2023/11/28  00:05

import os
import sys
import time

sys.path.append(os.pardir)

from public import Web




'''

pageobj  对应 locatorYAML 操作页面
'''


class HomePage(Web):

    def go_to_cloud_design(self,):
        """
        访问Cloud Design
        :return:
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def go_to_dashboard(self):
        """
        点击DashBoard
        :return:
        """

        self.webexe(__file__, sys._getframe().f_code.co_name,)

    def go_to_rayware(self):
        """
        点击RayWare
        :return:
        """

        self.webexe(__file__, sys._getframe().f_code.co_name,)
        time.sleep(16)


    def go_to_store(self):
        """
        点击Store
        :return:
        """

        self.webexe(__file__, sys._getframe().f_code.co_name,)

    def go_to_notifications(self):
        """
        点击Notifications
        :return:
        """

        self.webexe(__file__, sys._getframe().f_code.co_name,)

    def go_to_cloud_driver(self):
        """
        点击Cloud Driver
        :return:
        """

        self.webexe(__file__, sys._getframe().f_code.co_name,)

    def go_to_more_informations(self):
        """
        点击more_informations
        :return:
        """

        self.webexe(__file__, sys._getframe().f_code.co_name,)