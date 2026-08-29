from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Urls
from locators.base_page_locators import Locators
import allure

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def wait_for_element_visible(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_new_window(self):
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[-1])

    def wait_for_url_contains(self, url, time=5):
        WebDriverWait(self.driver, time).until(EC.url_contains(url))
        
    def get_current_url(self):
        return self.driver.current_url

class CommonPage(BasePage):

    @allure.step("Клик по логотипу 'Яндекс'")
    def click_logo_yandex(self):
        self.find_element(Locators.LOGO_YANDEX).click()

    @allure.step("Клик по логотипу 'Самокат'")
    def click_logo_scooter(self):
        self.find_element(Locators.LOGO_SCOOTER).click()   

    @allure.step("Ожидание открытия главной страницы Дзена в новом окне")
    def wait_main_page_dzen(self):
        self.switch_to_new_window()
        self.wait_for_url_contains(Urls.DZEN_URL)

    @allure.step("Ожидание перехода на главную страницу 'Самоката'")
    def wait_main_page_scooter(self):
        self.wait_for_url_contains(Urls.SCOOTER_MAIN_PAGE)
    
    @allure.step("Проверка, что открылась страница Дзена")
    def check_main_page_dzen(self):
        assert Urls.DZEN_URL in self.get_current_url()

    @allure.step("Проверка, что открылась главную страница 'Самоката'")
    def check_main_page_scooter(self):
        actual_url = self.get_current_url()
        assert actual_url == Urls.SCOOTER_MAIN_PAGE

    