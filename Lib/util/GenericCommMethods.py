from selenium.webdriver.common import action_chains

def movetoElement(driver,element):
    try:
        act = action_chains(driver)
        act.move_to_element(element).perform()
    except Exception as e:
        print(e)

