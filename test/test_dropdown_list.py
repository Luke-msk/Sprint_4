import allure
from page_objects.dropdown_list import Questions_about_important
from page_objects.main_page import MainPage
import locators.dropdown_list_locators as dropdown_loc
import locators.main_page_locators as main_page_loc


@allure.title('Проверка ответов на вопросы')
def test_checking_answers_to_questions(driver):
    questions = Questions_about_important(driver)
    main = MainPage(driver)
    main.click_on_button(main_page_loc.cookie)

    questions.select_question(dropdown_loc.price)
    assert questions.find_text(dropdown_loc.price_answer) == dropdown_loc.price_answer_text

    questions.select_question(dropdown_loc.several_scooters)
    assert questions.find_text(dropdown_loc.several_scooters_answer) == dropdown_loc.several_scooters_answer_text

    questions.select_question(dropdown_loc.rental_time)
    assert questions.find_text(dropdown_loc.rental_time_answer) == dropdown_loc.rental_time_answer_text

    questions.select_question(dropdown_loc.order_today)
    assert questions.find_text(dropdown_loc.order_today_answer) == dropdown_loc.order_today_answer_text

    questions.select_question(dropdown_loc.change_order)
    assert questions.find_text(dropdown_loc.change_order_answer) == dropdown_loc.change_order_answer_text

    questions.select_question(dropdown_loc.scooter_charging)
    assert questions.find_text(dropdown_loc.scooter_charging_answer) == dropdown_loc.scooter_charging_answer_text

    questions.select_question(dropdown_loc.cancel_order)
    assert questions.find_text(dropdown_loc.cancel_order_answer) == dropdown_loc.cancel_order_answer_text

    questions.select_question(dropdown_loc.mkad)
    assert questions.find_text(dropdown_loc.mkad_answer) == dropdown_loc.mkad_answer_text