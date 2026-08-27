from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    logo_yandex = (By.XPATH, "//*[contains(@class, 'Header_LogoYandex')]")
    logo_scooter = (By.XPATH, "//*[contains(@class, 'Header_LogoScooter')]")
    dzen_url = "https://dzen.ru/"
    scooter_url_main_page = "https://qa-scooter.praktikum-services.ru/"

    def __init__(self, driver):
        self.driver = driver

    def click_logo_yandex(self):
        self.driver.find_element(*self.logo_yandex).click()

    def click_logo_scooter(self):
        self.driver.find_element(*self.logo_scooter).click()   

    def wait_main_page_dzen(self):
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[-1])
        WebDriverWait(self.driver, 5).until(EC.url_contains(self.dzen_url))

    def wait_main_page_scooter(self):
        WebDriverWait(self.driver, 5).until(EC.url_to_be(self.scooter_url_main_page))

    def check_main_page_dzen(self):
        assert self.dzen_url in self.driver.current_url

    def check_main_page_scooter(self):
        actual_url = self.driver.current_url
        assert actual_url == self.scooter_url_main_page

    