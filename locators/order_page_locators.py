from selenium.webdriver.common.by import By


class Locators:

    NAME_FIRST_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    NAME_LAST_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_DELIVERY_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_SELECT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, "//*[text() = 'Далее']")

    DELIVERY_DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_TIME_SELECT = (By.XPATH, "//*[@class = 'Dropdown-arrow']")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_CREATE_BUTTON = (By.XPATH, "//*[2][text() = 'Заказать']")
    ORDER_CONFIRM_CREATE_BUTTON = (By.XPATH, "//*[text() = 'Да']")
    ORDER_CREATED_MESSAGE = (By.XPATH, "//*[text() = 'Заказ оформлен'] ")

    @staticmethod
    def GET_LOCATOR_CHOOSE_RENTAL(rental_time):
        return (By.XPATH, f"//*[text() = '{rental_time}']")

    @staticmethod
    def GET_LOCATOR_CHOOSE_METRO(metro_station):
        return (By.XPATH, f"//*[text() = '{metro_station}']")

    @staticmethod
    def GET_LOCATOR_CHOOSE_COLOR(color):
        return (By.XPATH, f"//*[text() = '{color}']")