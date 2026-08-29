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

    def check_faq_answer_by_index(self, index, expected_answer_text):

        self._scroll_to_and_click(Locators.FAQ_QUESTION_TEMPLATE(index))
        
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.FAQ_ANSWER_TEMPLATE(index)))
        
        element = self.driver.find_element(*Locators.FAQ_ANSWER_TEMPLATE(index))
        assert expected_answer_text in element.text











