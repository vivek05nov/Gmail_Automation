from selenium.webdriver.common.by import By

from Config.config import TestData

from Pages.Compose import Compose
from Pages.basepage import Base


class Login(Base):
    Email = (By.ID, "identifierId")
    Email_Button = (By.ID, "identifierNext")
    Password = (By.NAME, "Passwd")
    Password_button = (By.ID, "passwordNext")

    def  do_login(self,email,password):
        self.do_send_keys(self.Email, TestData.EMAIL)
        self.do_click(self.Email_Button)
        self.do_send_keys(self.Password,TestData.PASSWORD)
        self.do_click(self.Password_button)
        return Compose(self.driver)


