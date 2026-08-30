import pytest
from selenium import webdriver
from pages.base_page import CommonPage
import allure


@allure.suite("Главная страница Самоката")
@allure.sub_suite("Навигация по клику на логотипы в хедере")
class TestNavigationLogo:

    @allure.title("Проверка перехода на страницу Дзена при клике на логотип 'Яндекс'")
    def test_yandex_logo_navigation(self, main_page_function_scope):
        main_page_function_scope.click_logo_yandex()
        main_page_function_scope.wait_main_page_dzen()
        main_page_function_scope.check_main_page_dzen()

    @allure.title("Проверка перехода на главную страницу Самоката при клике на логотип 'Самокат'")
    def test_scooter_logo_navigation(self, main_page_function_scope):
        main_page_function_scope.click_logo_scooter()
        main_page_function_scope.wait_main_page_scooter()
        main_page_function_scope.check_main_page_scooter()
