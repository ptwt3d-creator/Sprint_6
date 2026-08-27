from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators

class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, name):
        self.driver.find_element(*OrderPageLocators.NAME_FIRST_FIELD).send_keys(name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*OrderPageLocators.NAME_LAST_FIELD).send_keys(last_name)

    def enter_address_delevery(self, address_delevery):
        self.driver.find_element(*OrderPageLocators.ADDRESS_DELEVERY_FIELD).send_keys(address_delevery)

    def choose_metro_station(self, metro_station):
        metro_station_option = (By.XPATH, f"//*[text() = '{metro_station}']")
        self.driver.find_element(*OrderPageLocators.METRO_STATION_SELECT).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(metro_station_option))
        self.driver.find_element(*metro_station_option).click()

    def enter_phone(self, phone):
        self.driver.find_element(*OrderPageLocators.PHONE_FIELD).send_keys(phone)
    
    def click_button_next(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_NEXT).click()

    def enter_date_delivery(self, date_tomorrow):
        self.driver.find_element(*OrderPageLocators.DELEVIRY_DATE_FIELD).send_keys(date_tomorrow)

    def choose_time_rental(self, rental_time):
        rental_time_optoin = (By.XPATH, f"//*[text() = '{rental_time}']")
        self.driver.find_element(*OrderPageLocators.RENTAL_TIME_SELECT).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(rental_time_optoin))
        self.driver.find_element(*rental_time_optoin).click()
    
    def choose_color(self, color):
        color_option = (By.XPATH, f"//*[text() = '{color}']")
        self.driver.find_element(*color_option).click()

    def enter_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.COMMENT_FIELD).send_keys(comment) 

    def click_button_create_order(self):
        self.driver.find_element(*OrderPageLocators.ORDER_CREATE_BUTTON).click()
    
    def click_button_confirm_create_order(self):
        self.driver.find_element(*OrderPageLocators.ORDER_CONFIRM_CREATE_BUTTON).click()

    def check_created_order_massage(self):
        element = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.ORDER_CREATED_MESSAGE))
        assert element is not None

    def wait_order_create_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.ORDER_CREATE_BUTTON))

    def wait_button_next(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.BUTTON_NEXT))

    def wait_order_confirm_create_button(self):
        return WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.ORDER_CONFIRM_CREATE_BUTTON))
         











