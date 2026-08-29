import pytest
from selenium import webdriver
from data import Urls
from pages.base_page import CommonPage
from pages.main_page import MainPage
from pages.order_page import OrderPage


# Применяется один раз на весь класс
@pytest.fixture(scope="class")
def driver():
    browser = webdriver.Firefox()
    yield browser
    browser.quit()

@pytest.fixture
def main_page(driver):
    driver.get(Urls.SCOOTER_MAIN_PAGE)
    return MainPage(driver)

@pytest.fixture
def order_page(driver):
    driver.get(Urls.SCOOTER_MAIN_PAGE)
    return OrderPage(driver)

# Вызывает фикстуру driver которая выполняется один раз для класса далее
# Применяется на каждую функцию в которой указана, driver остается при этом выполненой до конца класса
@pytest.fixture(scope="function")
def main_page_function_scope(driver):
    driver.get(Urls.SCOOTER_ORDER_PAGE)
    return CommonPage(driver)