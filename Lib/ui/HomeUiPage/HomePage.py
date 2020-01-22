from Lib.util import timeout_handler
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:

    def __init__(self,driver):
        self.driver = driver

    def wait_for_home_page_to_load(self):
        element = self.driver.find_element_by_xpath("//div[text()='Ashwini']")
        #
        timeout_handler.wait_for_visibility_of_element(self.driver,element)

    def get_userAcc_txt(self):
        try:
            return self.driver.find_element_by_xpath("//div[@class='_3pNZKl']/div[3]")
        except:
            return None

    def get_search_txtbox(self):
        try:
            return self.driver.find_element_by_xpath("//input[contains(@title,'Search for products')]")
        except:
            return None

    def get_6GBRam_chkbox(self):
        try:
            return self.driver.find_element_by_xpath("//div[text()='6 GB & Above']")
        except:
            return None

    def get_MiBrand_chkbox(self):
        try:
            return self.driver.find_element_by_xpath("//div[text()='Mi']")
        except:
            return None

    def get_4AndAboveCustRatings(self):
        try:
            return self.driver.find_element_by_xpath("//div[text()='4★ & above']")
        except:
            return None

    def get_OperatingSys_toggleBtn(self):
        try:
            return self.driver.find_element_by_xpath("//div[text()='Operating System']")
        except:
            return None

    def get_AndroidOS_chkbox(self):
        try:
            return self.driver.find_element_by_xpath("//div[text()='Android']")
        except:
            return None

    def get_search_Btn(self):
        try:
            return self.driver.find_element_by_xpath("//button[@type='submit']")
        except:
            return None

    def get_mobileItems_txt(self):
        try:
            return self.driver.find_elements_by_xpath("//div[@class='_3wU53n']")
        except:
            return None

    def get_searchResult_txt(self):
        try:
            return self.driver.find_element_by_xpath("//span[@class='_2yAnYN']")
        except:
            return None

    def get_AddToCart_Btn(self):
        try:
            return self.driver.find_element_by_xpath("//button[text()='ADD TO CART']")
        except:
            return None


