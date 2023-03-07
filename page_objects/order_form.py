from page_objects.base_page import BasePage
import time


class Order_form_page(BasePage):

    def order_form_send(self, locator, v):
        self.find_elements(locator)
        self.driver.find_element(*locator).send_keys(v)
        #time.sleep(3)

    def order_form_click(self, locator):
        self.find_elements(locator)
        self.driver.find_element(*locator).click()