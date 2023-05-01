from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.basepage import Base


class Compose(Base):
    Compose_button = (By.XPATH, "//div[text()='Compose']")
    Send_to = (By.CLASS_NAME, "aFw")
    Subject_box = (By.NAME, "subjectbox")
    Message_body = (By.CSS_SELECTOR, "div[aria-label='Message Body']")
    Send = (By.XPATH, "//div[text()='Send']")
    Message_sent = (By.XPATH, "//div[aria-live='assertive']")

    def do_request(self, subject, body, send_to):
        self.do_click(self.Compose_button)
        self.do_send_keys(self.Send_to, send_to)
        self.do_send_keys(self.Subject_box, subject)
        self.do_send_keys(self.Message_body, body)
        self.do_click(self.Send)




