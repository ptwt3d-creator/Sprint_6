from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Urls
from locators.base_page_locators import Locators


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver

    def click_logo_yandex(self):
        self.driver.find_element(*Locators.LOGO_YANDEX).click()

    def click_logo_scooter(self):
        self.driver.find_element(*Locators.LOGO_SCOOTER).click()   

    def wait_main_page_dzen(self):
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[-1])
        WebDriverWait(self.driver, 5).until(EC.url_contains(Urls.DZEN_URL))

    def wait_main_page_scooter(self):
        WebDriverWait(self.driver, 5).until(EC.url_to_be(Urls.SCOOTER_URL_MAIN_PAGE))

    def check_main_page_dzen(self):
        assert Urls.DZEN_URL in self.driver.current_url

    def check_main_page_scooter(self):
        actual_url = self.driver.current_url
        assert actual_url == Urls.SCOOTER_URL_MAIN_PAGE

    