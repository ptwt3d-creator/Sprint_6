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

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def wait_for_element_visible(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments.scrollIntoView();", element)

    def switch_to_new_window(self):
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[-1])

    def wait_for_url_contains(self, url, time=5):
        WebDriverWait(self.driver, time).until(EC.url_contains(url))
        
    def get_current_url(self):
        return self.driver.current_url

class CommonPage(BasePage):

    def click_logo_yandex(self):
        self.find_element(*Locators.LOGO_YANDEX).click()

    def click_logo_scooter(self):
        self.find_element(*Locators.LOGO_SCOOTER).click()   

    def wait_main_page_dzen(self):
        self.switch_to_new_window()
        self.wait_for_url_contains(Urls.DZEN_URL)

    def wait_main_page_scooter(self):
        self.wait_for_url_contains(Urls.SCOOTER_URL_MAIN_PAGE)

    def check_main_page_dzen(self):
        assert Urls.DZEN_URL in self.get_current_url

    def check_main_page_scooter(self):
        actual_url = self.get_current_url
        assert actual_url == Urls.SCOOTER_URL_MAIN_PAGE

    