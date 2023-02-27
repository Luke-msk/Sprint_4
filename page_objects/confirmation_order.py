from page_objects.base_page import BasePage

class ConfirmationOrder(BasePage):

    def confirmation(self, locator):
        self.find_elements(locator)
        self.driver.find_element(*locator).click()