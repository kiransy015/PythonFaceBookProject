import pytest
from selenium.webdriver import Chrome,Firefox,Ie

def get_browser_instance():
    browser_info = pytest.config.option.browser
    test_url_info = pytest.config.option.url

    if browser_info.lower()=="chrome":
        driver = Chrome("C:/Kiran Kumar SY/Python/PythonFaceBookProject/Browsers-Servers/chromedriver.exe")
    elif browser_info.lower()=="firefox":
        driver = Firefox("C:/Kiran Kumar SY/Python/PythonFaceBookProject/Browsers-Servers/geckodriver.exe")
    else:
        print("Invalid browser option !!!")
        return None

    driver.maximize_window()
    driver.implicitly_wait(30)

    if test_url_info.lower()=="test":
        driver.get("https://www.flipkart.com/")
    elif test_url_info.lower()=="prod":
        driver.get("https://www.flipkart.com/")

    return driver