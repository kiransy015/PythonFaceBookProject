from Lib.util import timeout_handler

class Cartpage:

    def __init__(self,driver):
        self.driver = driver

    def wait_for_cart_page_to_load(self):
        element = self.driver.find_element_by_xpath("//button[span[text()='Place Order']]")
        timeout_handler.wait_for_element_to_be_clickable(element)

    def get_itemDecrease_Btn(self):
        try:
            return self.driver.find_element_by_xpath("(//button[@class ='wNrY5O'])[1]")
        except Exception as e:
            return None

    def get_itemIncrease_Btn(self):
        try:
            return self.driver.find_element_by_xpath("(//button[@class ='wNrY5O'])[2]")
        except Exception as e:
            return None

    def get_TotalPayable(self):
        try:
            return self.driver.find_element_by_xpath("//div[text()='Total Payable']/following-sibling::span")
        except:
            return None

    def get_placeOrder_Btn(self):
        try:
            return self.driver.find_element_by_xpath("//button[span[text()='Place Order']]")
        except:
            return None

    def get_Addresschange_Btn(self):
        try:
            return self.driver.find_element_by_xpath("//button[text()='Change']")
        except:
            return None

    def get_AddressEdit_Btn(self):
        try:
            return self.driver.find_element_by_xpath("//button[text()='EDIT']")
        except:
            return None

    def get_AddressName_txtbox(self):
        try:
            return self.driver.find_element_by_xpath("//input[@name='name']")
        except:
            return None

    def get_saveAndDeliver_Btn(self):
        try:
            return self.driver.find_element_by_xpath("//button[text()='Save and Deliver Here']")
        except:
            return None



