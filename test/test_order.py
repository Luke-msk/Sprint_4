import allure
from page_objects.order_form import Order_form_page
from page_objects.main_page import MainPage
from page_objects.confirmation_order import ConfirmationOrder
import locators.order_form_locators as order_form_loc
import locators.main_page_locators as main_page_loc
import locators.confirmation_order_locators as confirmation_loc
import config
import time

@allure.title('Проверка оформления заказа')
@allure.description('Используем кнопку "Заказать" в правом верхнем углу')
def test_order_button_above(driver):
    value = Order_form_page(driver)
    main = MainPage(driver)
    confirm = ConfirmationOrder(driver)
    main.click_on_button(main_page_loc.cookie)
    main.click_on_button(main_page_loc.order_button_above)
    value.order_form_send(order_form_loc.field_name, config.name)
    value.order_form_send(order_form_loc.field_surname, config.surname)
    value.order_form_send(order_form_loc.field_address, config.address)
    value.order_form_click(order_form_loc.field_metro)
    value.order_form_click(order_form_loc.metro)
    value.order_form_send(order_form_loc.field_phone_number, config.phone_number)
    value.order_form_click(order_form_loc.button_further)
    value.find_elements(order_form_loc.form_about_rent)
    assert value.find_text(order_form_loc.form_about_rent) == order_form_loc.form_about_rent_text
    value.order_form_click(order_form_loc.date)
    value.order_form_click(order_form_loc.date_tomorrow)
    value.order_form_click(order_form_loc.rental_period)
    value.order_form_click(order_form_loc.period_two_days)
    value.order_form_click(order_form_loc.black_color)
    value.order_form_send(order_form_loc.field_comment, config.comment)
    value.order_form_click(order_form_loc.order_button)
    assert confirmation_loc.question_text in confirm.find_text(confirmation_loc.question)
    confirm.confirmation(confirmation_loc.button_yes)
    assert confirmation_loc.confirmed_text in confirm.find_text(confirmation_loc.confirmed)
    time.sleep(3)
    confirm.confirmation(confirmation_loc.view_status_button)
    time.sleep(3)
    confirm.find_elements(confirmation_loc.cancel_order_button)
    assert confirm.find_text(confirmation_loc.cancel_order_button) == confirmation_loc.cancel_order_button_text
    main.click_on_button(main_page_loc.Scooter_button)
    assert main_page_loc.header_main_page_text in main.find_text(main_page_loc.header_main_page)
    main.click_on_button(main_page_loc.Yandex_button)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    main.find_elements(main_page_loc.Zen_logo)
    assert driver.title == 'Дзен'

@allure.title('Проверка оформления заказа')
@allure.description('Используем кнопку "Заказать" внизу страницы')
def test_order_button_below(driver):
    value = Order_form_page(driver)
    main = MainPage(driver)
    confirm = ConfirmationOrder(driver)
    main.click_on_button(main_page_loc.cookie)
    main.click_on_button(main_page_loc.order_button_below)
    value.order_form_send(order_form_loc.field_name, config.name)
    value.order_form_send(order_form_loc.field_surname, config.surname)
    value.order_form_send(order_form_loc.field_address, config.address)
    value.order_form_click(order_form_loc.field_metro)
    value.order_form_click(order_form_loc.metro)
    value.order_form_send(order_form_loc.field_phone_number, config.phone_number)
    value.order_form_click(order_form_loc.button_further)
    value.find_elements(order_form_loc.form_about_rent)
    assert value.find_text(order_form_loc.form_about_rent) == order_form_loc.form_about_rent_text
    value.order_form_click(order_form_loc.date)
    value.order_form_click(order_form_loc.date_tomorrow)
    value.order_form_click(order_form_loc.rental_period)
    value.order_form_click(order_form_loc.period_four_days)
    value.order_form_click(order_form_loc.grey_color)
    value.order_form_send(order_form_loc.field_comment, config.comment)
    value.order_form_click(order_form_loc.order_button)
    assert confirmation_loc.question_text in confirm.find_text(confirmation_loc.question)
    confirm.confirmation(confirmation_loc.button_yes)
    assert confirmation_loc.confirmed_text in confirm.find_text(confirmation_loc.confirmed)
    time.sleep(3)
    confirm.confirmation(confirmation_loc.view_status_button)
    time.sleep(3)
    confirm.find_elements(confirmation_loc.cancel_order_button)
    assert confirm.find_text(confirmation_loc.cancel_order_button) == confirmation_loc.cancel_order_button_text
    main.click_on_button(main_page_loc.Scooter_button)
    assert main_page_loc.header_main_page_text in main.find_text(main_page_loc.header_main_page)
    main.click_on_button(main_page_loc.Yandex_button)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    main.find_elements(main_page_loc.Zen_logo)
    assert driver.title == 'Дзен'