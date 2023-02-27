from selenium.webdriver.common.by import By

price = [By.XPATH, ".//div[@id='accordion__heading-0']"]
price_answer = [By.XPATH, ".//div[@id='accordion__panel-0']/p"]
price_answer_text = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
several_scooters = [By.ID, 'accordion__heading-1']
several_scooters_answer = [By.XPATH, ".//div[@id='accordion__panel-1']/p"]
several_scooters_answer_text = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
rental_time = [By.ID, 'accordion__heading-2']
rental_time_answer = [By.XPATH, ".//div[@id='accordion__panel-2']/p"]
rental_time_answer_text = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
order_today = [By.ID, 'accordion__heading-3']
order_today_answer = [By.XPATH, ".//div[@id='accordion__panel-3']/p"]
order_today_answer_text = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
change_order = [By.ID, 'accordion__heading-4']
change_order_answer = [By.XPATH, ".//div[@id='accordion__panel-4']/p"]
change_order_answer_text = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
scooter_charging = [By.ID, 'accordion__heading-5']
scooter_charging_answer = [By.XPATH, ".//div[@id='accordion__panel-5']/p"]
scooter_charging_answer_text = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
cancel_order = [By.ID, 'accordion__heading-6']
cancel_order_answer = [By.XPATH, ".//div[@id='accordion__panel-6']/p"]
cancel_order_answer_text = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
mkad = [By.ID, 'accordion__heading-7']
mkad_answer = [By.XPATH, ".//div[@id='accordion__panel-7']/p"]
mkad_answer_text = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'