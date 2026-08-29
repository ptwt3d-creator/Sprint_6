from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import Locators
from pages.base_page import CommonPage
import allure

class OrderPage(CommonPage):

    @allure.step("Ввод адреса доставки: {address_delivery}")
    def enter_address_delivery(self, address_delivery):
        self.find_element(Locators.ADDRESS_DELIVERY_FIELD).send_keys(address_delivery)

    @allure.step("Ввод комментария для курьера: {comment}")
    def enter_comment(self, comment):
        self.find_element(Locators.COMMENT_FIELD).send_keys(comment) 

    @allure.step("Ввод даты доставки: {date_tomorrow}")
    def enter_date_delivery(self, date_tomorrow):
        self.find_element(Locators.DELIVERY_DATE_FIELD).send_keys(date_tomorrow)

    @allure.step("Ввод имени: {name}")
    def enter_first_name(self, name):
        self.find_element(Locators.NAME_FIRST_FIELD).send_keys(name)

    @allure.step("Ввод фамилии: {last_name}")
    def enter_last_name(self, last_name):
        self.find_element(Locators.NAME_LAST_FIELD).send_keys(last_name)

    @allure.step("Ввод номера телефона: {phone}")
    def enter_phone(self, phone):
        self.find_element(Locators.PHONE_FIELD).send_keys(phone)

    @allure.step("Клик по кнопке подтверждения заказа 'Да'")
    def click_button_confirm_create_order(self):
        self.find_element(Locators.ORDER_CONFIRM_CREATE_BUTTON).click()

    @allure.step("Клик по кнопке оформить заказ 'Заказать'")
    def click_button_create_order(self):
        self.find_element(Locators.ORDER_CREATE_BUTTON).click()
    
    @allure.step("Клик по кнопке перехода к следующему шагу 'Далее'")
    def click_button_next(self):
        self.find_element(Locators.BUTTON_NEXT).click()

    @allure.step("Выбор цвета самоката: {color}")
    def choose_color(self, color):
        color_option = Locators.GET_LOCATOR_CHOOSE_COLOR(color)
        self.find_element(color_option).click()

    @allure.step("Выбор станции метро: {metro_station}")
    def choose_metro_station(self, metro_station):
        metro_station_option = Locators.GET_LOCATOR_CHOOSE_METRO(metro_station)
        self.find_element(Locators.METRO_STATION_SELECT).click()
        self.wait_for_element_visible(metro_station_option)
        self.find_element(metro_station_option).click()

    @allure.step("Выбор срока аренды: {rental_time}")
    def choose_time_rental(self, rental_time):
        rental_time_option = Locators.GET_LOCATOR_CHOOSE_RENTAL(rental_time)
        self.find_element(Locators.RENTAL_TIME_SELECT).click()
        self.wait_for_element_visible(rental_time_option)
        self.find_element(rental_time_option).click()

    @allure.step("Ожидание кнопки 'Далее'")
    def wait_button_next(self):
        self.wait_for_element_visible(Locators.BUTTON_NEXT)

    @allure.step("Ожидание кнопки подтверждения создания заказа")
    def wait_order_confirm_create_button(self):
        return self.wait_for_element_visible(Locators.ORDER_CONFIRM_CREATE_BUTTON)

    @allure.step("Ожидание кнопки оформить заказ")
    def wait_order_create_button(self):
        self.wait_for_element_visible(Locators.ORDER_CREATE_BUTTON)

    @allure.step("Проверка появления сообщения об успешном создании заказа")
    def check_created_order_message(self):
        element = self.wait_for_element_visible(Locators.ORDER_CREATED_MESSAGE)
        assert element is not None
         











