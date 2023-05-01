import pytest
from Config.config import TestData

from Pages.Loginpage import Login
from Tests.BaseTest import BaseTest


class TestSimple(BaseTest):

    def test_do_request(self):
        self.login = Login(self.driver)
        self.login.do_login(TestData.EMAIL,TestData.PASSWORD)


