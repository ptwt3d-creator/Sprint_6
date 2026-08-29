
from selenium import webdriver
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import OrderTestData
import pytest
import allure

class TestOrder:
    
    driver = None
    
    @allure.title("Проверки заказ самоката через кнопки Заказать в шапке\контектсе до успешного заказа")
    @allure.description("Весь флоу позитивного сценария с двумя наборами данных")
    @pytest.mark.parametrize ("data", [OrderTestData.data_set_1, OrderTestData.data_set_2])    
    def test_order_scooter(self, order_page, main_page, data):

        # Кнопка в шапка\контекс
        main_page.click_order_button_by_index(data.order_button_place)
        
        # Первая форма заказа
        order_page.wait_button_next()
        order_page.enter_first_name(data.name)
        order_page.enter_last_name(data.last_name)
        order_page.enter_address_deleviry(data.address_delivery)
        order_page.choose_metro_station(data.metro_station)
        order_page.enter_phone(data.phone)
        order_page.wait_button_next()
        order_page.click_button_next()

        # Вторая форма заказа
        order_page.wait_order_create_button()
        order_page.enter_date_delivery(data.date)
        order_page.choose_time_rental(data.rental_time)
        order_page.choose_color(data.color)
        order_page.enter_comment(data.comment)
        order_page.wait_order_create_button()
        order_page.click_button_create_order()

        # Подтверждение заказа и сообщение о успешном заказе
        order_page.wait_order_confirm_create_button()
        order_page.click_button_confirm_create_order()
        order_page.check_created_order_message()