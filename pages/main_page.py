from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import Locators


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def click_order_button_in_header(self):
        element = self.driver.find_element(*self.order_button_in_header)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def click_order_button_in_content(self):
        element = self.driver.find_element(*self.order_button_in_content)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def click_faq_question_behind_MKAD_delivery(self):
        element = self.driver.find_element(*Locators.faq_question_behind_MKAD_delivery)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def click_faq_question_charger(self):
        element = self.driver.find_element(*Locators.faq_question_charger)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def click_faq_question_cost(self):      
        element = self.driver.find_element(*Locators.faq_question_cost)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def click_faq_question_more_scooters(self):
        element = self.driver.find_element(*Locators.faq_question_more_scooters)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def click_faq_question_order_cancel(self):
        element = self.driver.find_element(*Locators.faq_question_order_cancel)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)    
        element.click()

    def click_faq_question_order_today(self):
        element = self.driver.find_element(*Locators.faq_question_order_today)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def click_faq_question_prolong_return_scooter(self):
        element = self.driver.find_element(*Locators.faq_question_prolong_return_scooter)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def click_faq_question_rental_time_calculation(self):
        element = self.driver.find_element(*Locators.faq_question_rental_time_calculation)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def check_faq_question_behind_MKAD_delivery_text(self):
        element = self.driver.find_element(*Locators.faq_question_behind_MKAD_delivery_text)
        assert "Да, обязательно. Всем самокатов! И Москве, и Московской области." in element.text

    def check_faq_question_charger_text(self):
        element = self.driver.find_element(*Locators.faq_question_charger_text)
        assert "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится." in element.text
    
    def check_faq_question_cost_text(self):
        element = self.driver.find_element(*Locators.faq_question_cost_text)
        assert "Сутки — 400 рублей. Оплата курьеру — наличными или картой." in element.text

    def check_faq_question_more_scooters_text(self):
        element = self.driver.find_element(*Locators.faq_question_more_scooters_text)
        assert "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим." in element.text

    def check_faq_question_order_cancel_text(self):
        element = self.driver.find_element(*Locators.faq_question_order_cancel_text)
        assert "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои." in element.text

    def check_faq_question_order_today_text(self):
        element = self.driver.find_element(*Locators.faq_question_order_today_text)
        assert "Только начиная с завтрашнего дня. Но скоро станем расторопнее." in element.text

    def check_faq_question_prolong_return_scooter_text(self):
        element = self.driver.find_element(*Locators.faq_question_prolong_return_scooter_text)
        assert "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010." in element.text

    def check_faq_question_rental_time_calculation_text(self):
        element = self.driver.find_element(*Locators.faq_question_rental_time_calculation_text)
        assert "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30." in element.text

    def wait_faq_question_behind_MKAD_delivery_text(self):
       WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.faq_question_behind_MKAD_delivery_text))

    def wait_faq_question_charger_text(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.faq_question_charger_text))

    def wait_faq_question_cost_text(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.faq_question_cost_text))

    def wait_faq_question_more_scooters_text(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.faq_question_more_scooters_text))

    def wait_faq_question_order_cancel_text(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.faq_question_order_cancel_text))

    def wait_faq_question_order_today_text(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.faq_question_order_today_text))

    def wait_faq_question_prolong_return_scooter_text(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.faq_question_prolong_return_scooter_text))

    def wait_faq_question_rental_time_calculation_text(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.faq_question_rental_time_calculation_text))                    

