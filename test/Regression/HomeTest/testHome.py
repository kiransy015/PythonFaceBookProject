import unittest
from Lib.util import create_driver
from Lib.ui.LoginUiPage.LoginPage import LoginPage
from Lib.ui.HomeUiPage.HomePage import HomePage
from Lib.util import timeout_handler
import time

class testHome(unittest.TestCase):

    def setUp(self):
        self.driver = create_driver.get_browser_instance()
        self.login = LoginPage(self.driver)
        self.home = HomePage(self.driver)

    def tearDown(self):
        self.driver.close()

    def testFilterRedmi8Mobiles(self):
        timeout_handler.wait_for_visibility_of_element(self.driver,self.login.get_username_textbox())
        self.login.get_username_textbox().send_keys("8660040638")
        self.login.get_password_textbox().send_keys("ashwini12345")
        self.login.get_login_btn().click()

        timeout_handler.wait_for_visibility_of_element(self.driver,self.home.get_search_txtbox())
        time.sleep(10)
        self.home.get_search_txtbox().send_keys("redmi 8 mobile")
        self.home.get_search_Btn().click()
        time.sleep(5)
        searchtxt = self.home.get_searchResult_txt().text
        timeout_handler.wait_for_element_to_be_clickable(self.driver,self.home.get_6GBRam_chkbox())
        self.home.get_6GBRam_chkbox().click()
        time.sleep(5)
        timeout_handler.wait_for_element_to_be_clickable(self.driver,self.home.get_MiBrand_chkbox())
        self.home.get_MiBrand_chkbox().click()
        time.sleep(5)
        timeout_handler.wait_for_element_to_be_clickable(self.driver,self.home.get_4AndAboveCustRatings())
        self.home.get_4AndAboveCustRatings().click()
        time.sleep(5)
        timeout_handler.wait_for_element_to_be_clickable(self.driver,self.home.get_OperatingSys_toggleBtn())
        self.home.get_OperatingSys_toggleBtn().click()
        timeout_handler.wait_for_element_to_be_clickable(self.driver, self.home.get_AndroidOS_chkbox())
        self.home.get_AndroidOS_chkbox().click()
        time.sleep(5)

        lst = self.home.get_mobileItems_txt()
        splittxt1 = searchtxt.split("– ")
        splittxt2 = splittxt1[1].split(" of")

        assert int(splittxt2[0])==len(lst)

        for itm in lst:
            print(itm.text)






