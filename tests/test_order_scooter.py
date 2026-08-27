
from selenium import webdriver
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import data_set_1, data_set_2
import pytest
import allure

class TestOrder:
    
    driver = None

    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.driver.get("https://qa-scooter.praktikum-services.ru")
        self.order = OrderPage(self.driver)
        self.order_main_page = MainPage(self.driver)
    
    @allure.title("Проверки заказ самоката через кнопки Заказать в шапке\контектсе до успешного заказа")
    @allure.description("Весь флоу позитивного сценария с двумя наборами данных")
    @pytest.mark.parametrize ("data", [data_set_1, data_set_2])    
    def test_order_scooter(self, data):

        # Кнопка в шапка\контекс
        if data.order_button_main_page == "in_header":
            self.order_main_page.click_order_button_in_header()
        else:
            self.order_main_page.click_order_button_in_content()
        
        # Первая форма заказа
        self.order.wait_button_next()
        self.order.enter_first_name(data.name)
        self.order.enter_last_name(data.last_name)
        self.order.enter_address_delevery(data.address_delivery)
        self.order.choose_metro_station(data.metro_station)
        self.order.enter_phone(data.phone)
        self.order.wait_button_next()
        self.order.click_button_next()

        # Вторая форма заказа
        self.order.wait_order_create_button()
        self.order.enter_date_delivery(data.date)
        self.order.choose_time_rental(data.rental_time)
        self.order.choose_color(data.color)
        self.order.enter_comment(data.comment)
        self.order.wait_order_create_button()
        self.order.click_button_create_order()

        # Подтверждение заказа и сообщение о успешном заказе
        self.order.wait_order_confirm_create_button()
        self.order.click_button_confirm_create_order()
        self.order.check_created_order_massage()
    
    def teardown_method(self, method):
        self.driver.quit()