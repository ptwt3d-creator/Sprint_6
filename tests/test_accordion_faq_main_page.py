import pytest
from pages.main_page import MainPage
from selenium import webdriver
from locators.main_page_locators import Locators
import allure

class TestAccordion:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://qa-scooter.praktikum-services.ru/")
        cls.accordion = MainPage(cls.driver)
    
    @pytest.mark.parametrize(
        "test_name, click_question, wait_question_text, check_question_text",
        [
        (
        "Вопрос: Доставка за МКАД",
        MainPage.click_faq_question_behind_MKAD_delivery,
        MainPage.wait_faq_question_behind_MKAD_delivery_text,
        MainPage.check_faq_question_behind_MKAD_delivery_text,),
        (
        "Вопрос: Зарядка для самоката",
        MainPage.click_faq_question_charger,
        MainPage.wait_faq_question_charger_text,
        MainPage.check_faq_question_charger_text,),
        (
        "Вопрос: Цена и оплата",    
        MainPage.click_faq_question_cost,
        MainPage.wait_faq_question_cost_text,
        MainPage.check_faq_question_cost_text,),
        (
        "Вопрос: Больше одного самоката",
        MainPage.click_faq_question_more_scooters,
        MainPage.wait_faq_question_more_scooters_text,
        MainPage.check_faq_question_more_scooters_text,),
        (
        "Вопрос: Отмена заказа",
        MainPage.click_faq_question_order_cancel,
        MainPage.wait_faq_question_order_cancel_text,
        MainPage.check_faq_question_order_cancel_text,),
        (
        "Вопрос: Заказ самоката на сегодня",
        MainPage.click_faq_question_order_today,
        MainPage.wait_faq_question_order_today_text,
        MainPage.check_faq_question_order_today_text,),
        (
        "Вопрос: Продление аренды и возврат самоката по раньше",
        MainPage.click_faq_question_prolong_return_scooter,
        MainPage.wait_faq_question_prolong_return_scooter_text,
        MainPage.check_faq_question_prolong_return_scooter_text,),
        (
        "Вопрос: Расчет стоимости аренды",
        MainPage.click_faq_question_rental_time_calculation,
        MainPage.wait_faq_question_rental_time_calculation_text,
        MainPage.check_faq_question_rental_time_calculation_text,)
        ]
    )
    
    @allure.title("{test_name}")
    def test_accordion_faq(self, test_name, click_question, wait_question_text, check_question_text):
        click_question(self.accordion)
        wait_question_text(self.accordion)
        check_question_text(self.accordion)
    
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
