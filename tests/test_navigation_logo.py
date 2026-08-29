import pytest
from selenium import webdriver
from pages.base_page import BasePage


class TestNavigationLogo:

    driver = None
    
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.driver.get("https://qa-scooter.praktikum-services.ru/order")
        self.navigation = BasePage(self.driver)

    def test_yandex_logo_navigation(self):
        self.navigation.click_logo_yandex()
        self.navigation.wait_main_page_dzen()
        self.navigation.check_main_page_dzen()

    def test_scooter_logo_navigation(self):
        self.navigation.click_logo_scooter()
        self.navigation.wait_main_page_scooter()
        self.navigation.check_main_page_scooter()

    def teardown_method(self, method):
        self.driver.quit()    


