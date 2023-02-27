from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(tuple(locator)))

    def find_text(self, locator):
        return self.driver.find_element(*locator).text