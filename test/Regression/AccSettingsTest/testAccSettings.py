import unittest
from Lib.util import create_driver
from Lib.ui.LoginUiPage.LoginPage import LoginPage
from Lib.ui.HomeUiPage.HomePage import HomePage
from Lib.util import timeout_handler
import time
from Lib.util import GenericCommMethods

class testAccSettings(unittest.TestCase):

    def setUp(self):
        self.driver = create_driver.get_browser_instance()
        self.login = LoginPage(self.driver)
        self.home = HomePage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_verifyEmailAndMobileNo(self):
        self.login.wait_for_login_page_to_load()
        self.login.get_username_textbox().send_keys("8660040638")
        self.login.get_password_textbox().send_keys("ashwini12345")
        self.login.get_login_btn().click()
        self.home.wait_for_home_page_to_load()
        time.sleep(20)
        # GenericCommMethods.movetoElement(self.driver,self.home.get_userAcc_txt())
        timeout_handler.wait_for_element_to_be_clickable(self.driver,self.home.get_userAcc_txt())
        GenericCommMethods.movetoElement(self.driver,self.home.get_userAcc_txt())
        time.sleep(10)

