import pytest
from selenium import webdriver
from pages.base_page import CommonPage


class TestNavigationLogo:

    driver = None

    def test_yandex_logo_navigation(self, main_page_function_scope):
        main_page_function_scope.click_logo_yandex()
        main_page_function_scope.wait_main_page_dzen()
        main_page_function_scope.check_main_page_dzen()

    def test_scooter_logo_navigation(self, main_page_function_scope):
        main_page_function_scope.click_logo_scooter()
        main_page_function_scope.wait_main_page_scooter()
        main_page_function_scope.check_main_page_scooter()
