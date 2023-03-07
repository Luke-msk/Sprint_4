from selenium.webdriver.common.by import By

question = [By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ']"]
question_text = 'Хотите оформить заказ?'
button_yes = [By.XPATH, ".//button[text()='Да']"]
confirmed = [By.XPATH, ".//div[@class='Order_Text__2broi']"]
confirmed_text = 'Номер заказа:'
view_status_button = [By.XPATH, ".//button[text()='Посмотреть статус']"]
cancel_order_button = [By.XPATH, ".//div[@class='Track_OrderInfo__2fpDL']/button"]
cancel_order_button_text = 'Отменить заказ'