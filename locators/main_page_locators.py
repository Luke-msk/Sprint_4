from selenium.webdriver.common.by import By

cookie = [By.XPATH, ".//button[text()='да все привыкли']"]
order_button_above = [By.XPATH, ".//button[@class = 'Button_Button__ra12g' and (text()='Заказать')]"]
order_button_below = [By.XPATH, ".//button[contains(@class,'Button_Middle__1CSJM') and (text()='Заказать')]"]
header_main_page = [By.XPATH, ".//div[@class='Home_Header__iJKdX']"]
header_main_page_text = 'Привезём его прямо к вашей двери'
Yandex_button = [By.XPATH, ".//a[@href='//yandex.ru']"]
Scooter_button = [By.XPATH, ".//a[@href='/']"]
Zen_logo = [By.XPATH, ".//span[@aria-label='Логотип Дзен']"]