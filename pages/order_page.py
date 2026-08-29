from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators
from pages.base_page import CommonPage

class OrderPage(CommonPage):

    def enter_first_name(self, name):
        self.find_element(*OrderPageLocators.NAME_FIRST_FIELD).send_keys(name)

    def enter_last_name(self, last_name):
        self.find_element(*OrderPageLocators.NAME_LAST_FIELD).send_keys(last_name)

    def enter_address_delevery(self, address_delevery):
        self.find_element(*OrderPageLocators.ADDRESS_DELEVERY_FIELD).send_keys(address_delevery)

    def choose_metro_station(self, metro_station):
        metro_station_option = GET_LOCATOR_CHOOSE_METRO(metro_station)
        self.find_element(*OrderPageLocators.METRO_STATION_SELECT).click()
        self.wait_for_element_visible(metro_station_option)
        self.find_element(*metro_station_option).click()

    def enter_phone(self, phone):
        self.find_element(*OrderPageLocators.PHONE_FIELD).send_keys(phone)
    
    def click_button_next(self):
        self.find_element(*OrderPageLocators.BUTTON_NEXT).click()

    def enter_date_delivery(self, date_tomorrow):
        self.find_element(*OrderPageLocators.DELEVIRY_DATE_FIELD).send_keys(date_tomorrow)

    def choose_time_rental(self, rental_time):
        rental_time_optoin = GET_LOCATOR_CHOOSE_RENTAL(rental_time)
        self.find_element(*OrderPageLocators.RENTAL_TIME_SELECT).click()
        self.wait_for_element_visible(rental_time_optoin)
        self.find_element(*rental_time_optoin).click()
    
    def choose_color(self, color):
        color_option = GET_LOCATOR_CHOOSE_COLOR(color)
        self.find_element(*color_option).click()

    def enter_comment(self, comment):
        self.find_element(*OrderPageLocators.COMMENT_FIELD).send_keys(comment) 

    def click_button_create_order(self):
        self.find_element(*OrderPageLocators.ORDER_CREATE_BUTTON).click()
    
    def click_button_confirm_create_order(self):
        self.find_element(*OrderPageLocators.ORDER_CONFIRM_CREATE_BUTTON).click()

    def check_created_order_massage(self):
        element = self.wait_for_element_visible(OrderPageLocators.ORDER_CREATED_MESSAGE)
        assert element is not None

    def wait_order_create_button(self):
        self.wait_for_element_visible(OrderPageLocators.ORDER_CREATE_BUTTON)

    def wait_button_next(self):
        self.wait_for_element_visible(OrderPageLocators.BUTTON_NEXT)

    def wait_order_confirm_create_button(self):
        return self.wait_for_element_visible(OrderPageLocators.ORDER_CONFIRM_CREATE_BUTTON)
         











