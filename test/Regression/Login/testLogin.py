import unittest
from Lib.util import create_driver
from Lib.ui.LoginUiPage.LoginPage import LoginPage
import time

class testLogin(unittest.TestCase):

    def setUp(self):
        self.driver = create_driver.get_browser_instance()
        self.login = LoginPage(self.driver)

    def test_validLogin(self):
        LoginPage.get_username_textbox(self).send_keys("12345")
        LoginPage.get_password_textbox(self).send_keys("12345")
        LoginPage.get_login_btn(self).click()

        print(LoginPage.get_loginErrMsg_txt(self).text)
        assert LoginPage.get_loginErrMsg_txt(self).text=="Please enter valid Email ID/Mobile number"

    # def test_validLogin(self):
    #     time.sleep(10)
    #     LoginPage.get_username_textbox(self).send_keys("8660040638")
    #     LoginPage.get_password_textbox(self).send_keys("ashwini12345")
    #     LoginPage.get_login_btn(self).click()

    def tearDown(self):
        self.driver.close()

