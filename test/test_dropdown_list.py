import allure
from page_objects.dropdown_list import Questions_about_important
from page_objects.main_page import MainPage
import locators.dropdown_list_locators as dropdown_loc
import locators.main_page_locators as main_page_loc


@allure.title('Проверка ответа на вопрос "Сколько это стоит? И как оплатить?"')
def test_checking_answers_to_questions_price(driver):
    questions = Questions_about_important(driver)
    main = MainPage(driver)
    main.click_on_button(main_page_loc.cookie)
    questions.select_question(dropdown_loc.price)
    assert questions.find_text(dropdown_loc.price_answer) == dropdown_loc.price_answer_text

@allure.title('Проверка ответа на вопрос "Хочу сразу несколько самокатов! Так можно?"')
def test_checking_answers_to_questions_several_scooters(driver):
    questions = Questions_about_important(driver)
    main = MainPage(driver)
    main.click_on_button(main_page_loc.cookie)
    questions.select_question(dropdown_loc.several_scooters)
    assert questions.find_text(dropdown_loc.several_scooters_answer) == dropdown_loc.several_scooters_answer_text

@allure.title('Проверка ответа на вопрос "Как рассчитывается время аренды?"')
def test_checking_answers_to_questions_rental_time(driver):
    questions = Questions_about_important(driver)
    main = MainPage(driver)
    main.click_on_button(main_page_loc.cookie)
    questions.select_question(dropdown_loc.rental_time)
    assert questions.find_text(dropdown_loc.rental_time_answer) == dropdown_loc.rental_time_answer_text

@allure.title('Проверка ответа на вопрос "Можно ли заказать самокат прямо на сегодня?"')
def test_checking_answers_to_questions_order_today(driver):
    questions = Questions_about_important(driver)
    main = MainPage(driver)
    main.click_on_button(main_page_loc.cookie)
    questions.select_question(dropdown_loc.order_today)
    assert questions.find_text(dropdown_loc.order_today_answer) == dropdown_loc.order_today_answer_text

@allure.title('Проверка ответа на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
def test_checking_answers_to_questions_change_order(driver):
    questions = Questions_about_important(driver)
    main = MainPage(driver)
    main.click_on_button(main_page_loc.cookie)
    questions.select_question(dropdown_loc.change_order)
    assert questions.find_text(dropdown_loc.change_order_answer) == dropdown_loc.change_order_answer_text

@allure.title('Проверка ответа на вопрос "Вы привозите зарядку вместе с самокатом?"')
def test_checking_answers_to_questions_scooter_charging(driver):
    questions = Questions_about_important(driver)
    main = MainPage(driver)
    main.click_on_button(main_page_loc.cookie)
    questions.select_question(dropdown_loc.scooter_charging)
    assert questions.find_text(dropdown_loc.scooter_charging_answer) == dropdown_loc.scooter_charging_answer_text

@allure.title('Проверка ответа на вопрос "Можно ли отменить заказ?"')
def test_checking_answers_to_questions_cancel_order(driver):
    questions = Questions_about_important(driver)
    main = MainPage(driver)
    main.click_on_button(main_page_loc.cookie)
    questions.select_question(dropdown_loc.cancel_order)
    assert questions.find_text(dropdown_loc.cancel_order_answer) == dropdown_loc.cancel_order_answer_text

@allure.title('Проверка ответа на вопрос "Я жизу за МКАДом, привезёте?"')
def test_checking_answers_to_questions_mkad(driver):
    questions = Questions_about_important(driver)
    main = MainPage(driver)
    main.click_on_button(main_page_loc.cookie)
    questions.select_question(dropdown_loc.mkad)
    assert questions.find_text(dropdown_loc.mkad_answer) == dropdown_loc.mkad_answer_text