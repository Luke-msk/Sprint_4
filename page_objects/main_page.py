from page_objects.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class MainPage(BasePage):

    def click_on_button(self, locator):
        self.driver.find_element(*locator).click()