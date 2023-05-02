from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.basepage import Base


class Compose(Base):
    extract = TestData.BCC.split(",")[1]
    Compose_button = (By.XPATH, "//div[text()='Compose']")
    Send_to = (By.CLASS_NAME, "aFw")
    Subject_box = (By.NAME, "subjectbox")
    Message_body = (By.CSS_SELECTOR, "div[aria-label='Message Body']")
    Send = (By.XPATH, "//div[text()='Send']")
    Message_sent = (By.XPATH, "//div[aria-live='assertive']")
    CC_button = (By.XPATH, "//span[text()='Cc']")
    CC = (By.XPATH, "//div[@name ='cc']//input")
    HOVER_CARD_CC = (By.XPATH, f"//div[@name ='cc']//div[text()='{extract}']")
    BCC_button = (By.XPATH, "//span[text()='Bcc']")
    BCC = (By.XPATH, "//div[@name='bcc']//input")
    HOVER_CARD_BCC = (By.XPATH, f"//div[@name ='bcc']//b[text()='{extract}']")
    ACCOUNT = (By.XPATH, "//a[aria-label='Google Account: Testing Testing  (testingvivek123@gmail.com)']")

    def do_request(self, subject, body, send_to):
        self.do_click(self.Compose_button)
        self.do_send_keys(self.Send_to, send_to)
        self.do_send_keys(self.Subject_box, subject)
        self.do_send_keys(self.Message_body, body)
        self.do_click(self.Send)

    def do_CC(self, send_to, cc):
        self.do_click(self.Compose_button)
        self.do_send_keys(self.Send_to, send_to)
        self.do_click(self.CC_button)
        self.do_send_keys(self.CC, cc)

    def do_BCC(self, send_to, bcc):
        self.do_click(self.Compose_button)
        self.do_send_keys(self.Send_to, send_to)
        self.do_click(self.BCC_button)
        self.do_send_keys(self.BCC, bcc)

    def do_BCC_CC(self, bcc):
        self.do_click(self.BCC_button)
        self.do_send_keys(self.BCC, bcc)

    def get_account_check(self):
        return self.get_element(self.ACCOUNT)

