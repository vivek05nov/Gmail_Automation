from Config.config import TestData
from Pages.Loginpage import Login
from Tests.BaseTest import BaseTest


class TestCompose(BaseTest):

    def test_compose(self):
        self.Compo = Login(self.driver)
        Comp = self.Compo.do_login(TestData.EMAIL, TestData.PASSWORD)
        Comp.do_request(TestData.SUBJECT,TestData.BODY,TestData.EMAIL_TO)

