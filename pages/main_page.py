from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import Locators
from pages.base_page import CommonPage
import allure

class MainPage(CommonPage):

    def _scroll_to_wait_and_click(self, locator):
        element = self.find_element(locator)
        self.scroll_to_element(element)
        self.wait_for_element_clickable(locator)
        element.click()

    @allure.step("Клик по кнопке 'Заказать' с индексом: {index}")
    def click_wait_order_button_by_index(self, index):
        locator = Locators.click_order_button(index)
        self._scroll_to_wait_and_click(locator)

    @allure.step("Клик по кнопке 'Заказать' в теле страницы")
    def click_order_button_in_content(self):
        self._scroll_to_and_click(Locators.ORDER_BUTTON_IN_CONTENT)

    @allure.step("Проверка ответа в FAQ под номером: {index}")
    def check_faq_answer_by_index(self, index, expected_answer_text):

        self._scroll_to_wait_and_click(Locators.FAQ_QUESTION_TEMPLATE(index))
        
        element = self.wait_for_element_visible(Locators.FAQ_ANSWER_TEMPLATE(index))
        
        assert expected_answer_text in element.text











