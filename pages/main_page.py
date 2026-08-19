from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from main_page_locators import Locators


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def click_order_button_in_header(self):
        self.driver.find_element(*self.order_button_in_header).click()
    
    def click_order_button_in_content(self):
        self.driver.find_element(*self.order_button_in_content).click()

    def click_faq_question_behind_MKAD_delevery(self):
        self.driver.find_element(*Locators.faq_question_behind_MKAD_delevery).click()

    def click_faq_question_charger(self):
        self.driver.find_element(*Locators.faq_question_charger).click()

    def click_faq_question_cost(self):      
        self.driver.find_element(*Locators.faq_question_cost).click()

    def click_faq_question_more_scooters(self):
        self.driver.find_element(*Locators.faq_question_more_scooters).click()

    def click_faq_question_order_cancel(self):
        self.driver.find_element(*Locators.faq_question_order_cancel).click()    

    def click_faq_question_order_today(self):
        self.driver.find_element(*Locators.faq_question_order_today).click()

    def click_faq_question_prolong_return_scooter(self):
        self.driver.find_element(*Locators.faq_question_prolong_return_scooter).click()

    def click_faq_question_rental_time_calculation(self):
        self.driver.find_element(*Locators.faq_question_rental_time_calculation).click()

    def check_faq_question_behind_MKAD_delevery_description(self):
        element = self.driver.find_element(*Locators.faq_question_behind_MKAD_delevery_description)
        assert "Да, обязательно. Всем самокатов! И Москве, и Московской области." in element

    def check_faq_question_charger_description(self):
        element = self.driver.find_element(*Locators.faq_question_charger_description)
        assert "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится." in element
    
    def check_faq_question_cost_description(self):
        element = self.driver.find_element(*Locators.faq_question_cost_description)
        assert "Сутки — 400 рублей. Оплата курьеру — наличными или картой." in element

    def check_faq_question_more_scooters_description(self):
        element = self.driver.find_element(*Locators.faq_question_more_scooters_description)
        assert "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим." in element

    def check_faq_question_order_cancel_description(self):
        element = self.driver.find_element(*Locators.faq_question_order_cancel_description)
        assert "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои." in element

    def check_faq_question_order_today_description(self):
        element = self.driver.find_element(*Locators.faq_question_order_today_description)
        assert "Только начиная с завтрашнего дня. Но скоро станем расторопнее." in element

    def check_faq_question_prolong_return_scooter_description(self):
        element = self.driver.find_element(*Locators.faq_question_prolong_return_scooter_description)
        assert "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010." in element

    def check_faq_question_rental_time_calculation_description(self):
        element = self.driver.find_element(*Locators.faq_question_rental_time_calculation_description)
        assert "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30." in element

    def wait_faq_question_behind_MKAD_delevery_description(self):
       WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.faq_question_behind_MKAD_delevery_description))

    def wait_faq_question_charger_description(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.faq_question_charger_description))

    def wait_faq_question_cost_description(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.faq_question_cost_description))

    def wait_faq_question_more_scooters_description(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.faq_question_more_scooters_description))

    def wait_faq_question_order_cancel_description(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.faq_question_order_cancel_description))

    def wait_faq_question_order_today_description(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.faq_question_order_today_description))

    def wait_faq_question_prolong_return_scooter_description(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.faq_question_prolong_return_scooter_description))

    def wait_faq_question_rental_time_calculation_description(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(Locators.faq_question_rental_time_calculation_description))                    

