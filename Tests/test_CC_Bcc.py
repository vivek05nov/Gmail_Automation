import time

from Config.config import TestData
from Pages.Compose import Compose
from Pages.Loginpage import Login
from Tests.BaseTest import BaseTest
from selenium.common.exceptions import NoSuchElementException


class Test_CC(BaseTest):

    def test_CC_Check(self):
        self.login = Login(self.driver)
        CC = self.login.do_login(TestData.EMAIL, TestData.PASSWORD)
        CC.do_CC(TestData.EMAIL_TO, TestData.CC)

    def test_Bcc_Check(self):
        self.com = Compose(self.driver)
        account_check = self.com.get_account_check()
        if account_check:
            self.login = Login(self.driver)
            self.com = self.login.do_login(TestData.EMAIL, TestData.PASSWORD)
            self.com.do_BCC(TestData.EMAIL_TO, TestData.BCC)

        else:
            self.com.do_BCC_CC(TestData.BCC)
            time.sleep(10)

