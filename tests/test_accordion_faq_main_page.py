import pytest
from pages.main_page import MainPage
from selenium import webdriver
from locators.main_page_locators import Locators
import allure
from data import FaqAnswersText

class TestAccordion:

    driver = None
    
    @pytest.mark.parametrize(
        "test_name, index, expected_answer_text",
        [
        ("Вопрос: Цена и оплата", 0, FaqAnswersText.COST),
        ("Вопрос: Больше одного самоката", 1, FaqAnswersText.MORE_SCOOTERS),
        ("Вопрос: Расчет стоимости аренды", 2, FaqAnswersText.RENTAL_TIME_CALCULATION),
        ("Вопрос: Заказ самоката на сегодня", 3, FaqAnswersText.TODAY_ORDER),
        ("Вопрос: Продление аренды и возврат самоката по раньше", 4, FaqAnswersText.RENTAL_PROLONG_AND_EARLI_RETURN_SCOOTER),
        ("Вопрос: Зарядка для самоката", 5, FaqAnswersText.CHARGER),
        ("Вопрос: Отмена заказа", 6, FaqAnswersText.CANCEL_OEDER),
        ("Вопрос: Доставка за МКАД", 7, FaqAnswersText.MKAD_DELEVERY),
        ]
    )    
    @allure.title("{test_name}")
    def test_accordion_faq(self, main_page, test_name, index, expected_answer_text):
        main_page.check_faq_answer_by_index(index, expected_answer_text)
