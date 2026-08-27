from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import Locators


class MainPage:
    
    def __init__(self, driver):
        self.driver = driver

    def _scroll_to_and_click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def click_order_button_in_header(self):
        self._scroll_to_and_click(Locators.ORDER_BUTTON_IN_HEADER)

    def click_order_button_in_content(self):
        self._scroll_to_and_click(Locators.ORDER_BUTTON_IN_CONTENT)

    def click_faq_question_behind_MKAD_delivery(self):
        self._scroll_to_and_click(Locators.FAQ_QUESTION_BEHIND_MKAD_DELIVERY)

    def click_faq_question_charger(self):
        self._scroll_to_and_click(Locators.FAQ_QUESTION_CHARGER)

    def click_faq_question_cost(self):      
        self._scroll_to_and_click(Locators.FAQ_QUESTION_COST)

    def click_faq_question_more_scooters(self):
        self._scroll_to_and_click(Locators.FAQ_QUESTION_MORE_SCOOTERS)

    def click_faq_question_order_cancel(self):
        self._scroll_to_and_click(Locators.FAQ_QUESTION_ORDER_CANCEL)

    def click_faq_question_order_today(self):
        self._scroll_to_and_click(Locators.FAQ_QUESTION_ORDER_TODAY)

    def click_faq_question_prolong_return_scooter(self):
        self._scroll_to_and_click(Locators.FAQ_QUESTION_PROLONG_RETURN_SCOOTER)

    def click_faq_question_rental_time_calculation(self):
        self._scroll_to_and_click(Locators.FAQ_QUESTION_RENTAL_TIME_CALCULATION)

    def check_faq_question_behind_MKAD_delivery_text(self):
        element = self.driver.find_element(*Locators.FAQ_QUESTION_BEHIND_MKAD_DELIVERY_TEXT)
        assert "Да, обязательно. Всем самокатов! И Москве, и Московской области." in element.text

    def check_faq_question_charger_text(self):
        element = self.driver.find_element(*Locators. FAQ_QUESTION_CHARGER_TEXT)
        assert "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится." in element.text
    
    def check_faq_question_cost_text(self):
        element = self.driver.find_element(*Locators.FAQ_QUESTION_COST_TEXT)
        assert "Сутки — 400 рублей. Оплата курьеру — наличными или картой." in element.text

    def check_faq_question_more_scooters_text(self):
        element = self.driver.find_element(*Locators.FAQ_QUESTION_MORE_SCOOTERS_TEXT)
        assert "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим." in element.text

    def check_faq_question_order_cancel_text(self):
        element = self.driver.find_element(*Locators.FAQ_QUESTION_ORDER_CANCEL_TEXT)
        assert "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои." in element.text

    def check_faq_question_order_today_text(self):
        element = self.driver.find_element(*Locators.FAQ_QUESTION_ORDER_TODAY_TEXT)
        assert "Только начиная с завтрашнего дня. Но скоро станем расторопнее." in element.text

    def check_faq_question_prolong_return_scooter_text(self):
        element = self.driver.find_element(*Locators.FAQ_QUESTION_PROLONG_RETURN_SCOOTER_TEXT)
        assert "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010." in element.text

    def check_faq_question_rental_time_calculation_text(self):
        element = self.driver.find_element(*Locators.FAQ_QUESTION_RENTAL_TIME_CALCULATION_TEXT)
        assert "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30." in element.text

    def wait_faq_question_behind_MKAD_delivery_text(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.FAQ_QUESTION_BEHIND_MKAD_DELIVERY_TEXT))

    def wait_faq_question_charger_text(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators. FAQ_QUESTION_CHARGER_TEXT))

    def wait_faq_question_cost_text(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.FAQ_QUESTION_COST_TEXT))

    def wait_faq_question_more_scooters_text(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.FAQ_QUESTION_MORE_SCOOTERS_TEXT))

    def wait_faq_question_order_cancel_text(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.FAQ_QUESTION_ORDER_CANCEL_TEXT))

    def wait_faq_question_order_today_text(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.FAQ_QUESTION_ORDER_TODAY_TEXT))

    def wait_faq_question_prolong_return_scooter_text(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.FAQ_QUESTION_PROLONG_RETURN_SCOOTER_TEXT))

    def wait_faq_question_rental_time_calculation_text(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.FAQ_QUESTION_RENTAL_TIME_CALCULATION_TEXT))                    
















