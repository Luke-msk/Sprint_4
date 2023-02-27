from page_objects.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class Questions_about_important(BasePage):

   def select_question(self, locator):
      self.find_elements(locator).send_keys(Keys.END)
      self.driver.find_element(*locator).click()