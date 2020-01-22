from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


def wait_for_visibility_of_element(driver,element):
    try:
        wait = WebDriverWait(timeout=10000,driver=driver)
        wait.until(expected_conditions.visibility_of(element))
    except Exception as e:
        print(e)

def wait_for_element_to_be_clickable(driver,element):
    try:
        wait = WebDriverWait(timeout=10000, driver=driver)
        wait.until(expected_conditions.visibility_of(element))
    except Exception as e:
        print(e)


def wait_for_title(driver,title):
    try:
        wait = WebDriverWait(timeout=10000, driver=driver)
        wait.until(expected_conditions.title_contains(title))
    except Exception as e:
        print(e)


