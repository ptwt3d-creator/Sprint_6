from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import Locators
from pages.base_page import CommonPage


class MainPage(CommonPage):

    def _scroll_to_and_click(self, locator):
        element = self.find_element(*locator)
        self.scroll_to_element(element)
        element.click()

    def check_faq_answer_by_index(self, index, expected_answer_text):

        self._scroll_to_and_click(Locators.FAQ_QUESTION_TEMPLATE(index))
        
        self.wait_for_element_visible(Locators.FAQ_ANSWER_TEMPLATE(index))
        
        element = self.find_element(*Locators.FAQ_ANSWER_TEMPLATE(index))
        assert expected_answer_text in element.text











