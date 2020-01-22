from Lib.util import timeout_handler

class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    def wait_for_login_page_to_load(self):
        element = self.driver.find_element_by_xpath("(//input[@type='text'])[2]")
        timeout_handler.wait_for_visibility_of_element(self.driver,element)

    def get_username_textbox(self):
        try:
            return self.driver.find_element_by_xpath("(//input[@type='text'])[2]")
        except:
            return None

    def get_password_textbox(self):
        try:
            return self.driver.find_element_by_xpath("(//input[@type='password'])[1]")
        except:
            return None

    def get_login_btn(self):
        try:
            return self.driver.find_element_by_xpath("//button[span[text()='Login']]")
        except:
            return None

    def get_loginErrMsg_txt(self):
        try:
            return self.driver.find_element_by_xpath("//span[@class='ZAtlA-']")
        except:
            return None
