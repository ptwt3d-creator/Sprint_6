
from selenium import webdriver
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import OrderTestData
import pytest
import allure


@allure.suite("Оформление заказа")
@allure.sub_suite("Форма бронирования самоката")
class TestOrder:

    @allure.title("Проверки заказ самоката через кнопки Заказать в шапке\контектсе до успешного заказа")
    @allure.description("Полный путь позитивного сценария с двумя наборами данных")
    @pytest.mark.parametrize ("data", [OrderTestData.data_set_1, OrderTestData.data_set_2])    
    def test_order_scooter(self, order_page, main_page, data):

        # Кнопка в шапка\контекс
        main_page.click_wait_order_button_by_index(data.order_button_place)
        
        # Первая форма заказа
        order_page.fill_order_first_form(data)
        order_page.click_wait_button_next()

        # Вторая форма заказа
        order_page.fill_order_second_form(data)
        order_page.click_wait_button_create_order()

        # Подтверждение заказа и сообщение о успешном заказе
        order_page.click_wait_button_confirm_create_order()
        order_page.check_created_order_message()