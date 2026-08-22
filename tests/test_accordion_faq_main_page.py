import pytest
from pages.main_page import MainPage
from selenium import webdriver
from locators.main_page_locators import Locators


class TestAccordion:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://qa-scooter.praktikum-services.ru/")
        cls.accordion = MainPage(cls.driver)

    def test_faq_behind_MKAD_delivery_text(self):
        self.accordion.click_faq_question_behind_MKAD_delivery()
        self.accordion.wait_faq_question_behind_MKAD_delivery_text()
        self.accordion.check_faq_question_behind_MKAD_delivery_text()

    def test_faq_question_charger_text(self):
        self.accordion.click_faq_question_charger()
        self.accordion.wait_faq_question_charger_text()
        self.accordion.check_faq_question_charger_text()

    def test_faq_question_cost_text(self):    
        self.accordion.click_faq_question_cost()
        self.accordion.wait_faq_question_cost_text()
        self.accordion.check_faq_question_cost_text()

    def test_faq_question_more_scooters_text(self):
        self.accordion.click_faq_question_more_scooters()
        self.accordion.wait_faq_question_more_scooters_text()
        self.accordion.check_faq_question_more_scooters_text()

    def test_faq_question_order_cancel_text(self):
        self.accordion.click_faq_question_order_cancel
        self.accordion.wait_faq_question_order_cancel_text
        self.accordion.check_faq_question_order_cancel_text

    def test_faq_question_order_today_text(self):
        self.accordion.click_faq_question_order_today()
        self.accordion.wait_faq_question_order_today_text()
        self.accordion.check_faq_question_order_today_text()

    def test_faq_question_prolong_return_scooter_text(self):
        self.accordion.click_faq_question_prolong_return_scooter()
        self.accordion.wait_faq_question_prolong_return_scooter_text()
        self.accordion.check_faq_question_prolong_return_scooter_text()

    def test_faq_question_rental_time_calculation_text(self):
        self.accordion.click_faq_question_rental_time_calculation()
        self.accordion.wait_faq_question_rental_time_calculation_text()
        self.accordion.check_faq_question_rental_time_calculation_text()    

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
