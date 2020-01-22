import unittest
from Lib.ui.HomeUiPage.HomePage import HomePage
from Lib.ui.LoginUiPage.LoginPage import LoginPage
from Lib.util import create_driver
from Lib.util import timeout_handler
import time
from Lib.ui.MyCartUiPage.CartPage import Cartpage

class testAddTocart(unittest.TestCase):

    def setUp(self):
        self.driver = create_driver.get_browser_instance()
        self.login = LoginPage(self.driver)
        self.home = HomePage(self.driver)
        self.cart = Cartpage(self.driver)

    def tearDown(self):
        self.driver.close()

    def testTotalPayable(self):
        timeout_handler.wait_for_element_to_be_clickable(self.driver,self.login.get_username_textbox())
        self.login.get_username_textbox().send_keys("8660040638")
        self.login.get_password_textbox().send_keys("ashwini12345")
        self.login.get_login_btn().click()

        time.sleep(5)
        timeout_handler.wait_for_element_to_be_clickable(self.driver,self.home.get_search_txtbox())
        self.home.get_search_txtbox().send_keys("Redmi Note 8 (Moonlight White, 128 GB)")
        self.home.get_search_Btn().click()

        time.sleep(5)
        xpath = "//div[div[text()='Redmi Note 8 (Moonlight White, 128 GB)']]/following-sibling::div//div[@class='_1vC4OE _2rQ-NK']"
        itemprice = self.driver.find_element_by_xpath(xpath).text
        print("Item Price :"+itemprice)

        xpath = "//*[text()='Redmi Note 8 (Moonlight White, 128 GB)']"
        self.driver.find_element_by_xpath(xpath).click()

        st = self.driver.window_handles

        self.driver.switch_to_window(st[1])

        self.home.get_AddToCart_Btn().click()

        time.sleep(5)

        self.cart.get_placeOrder_Btn().click()

        timeout_handler.wait_for_element_to_be_clickable(self.driver,self.cart.get_Addresschange_Btn())

        self.cart.get_AddressEdit_Btn().click()
        self.cart.get_AddressName_txtbox().clear()
        self.cart.get_AddressName_txtbox().send_keys("KiranKumar")
        self.cart.get_saveAndDeliver_Btn().click()

        time.sleep(10)
        totalpayable = self.cart.get_TotalPayable().text
        print("total Payable :"+totalpayable)

        assert itemprice==totalpayable

        time.sleep(10)
