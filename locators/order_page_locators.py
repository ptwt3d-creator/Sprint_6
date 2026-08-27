from selenium.webdriver.common.by import By


class OrderPageLocators:

    NAME_FIRST_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    NAME_LAST_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_DELEVERY_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_SELECT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, "//*[text() = 'Далее']")

    DELEVIRY_DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_TIME_SELECT = (By.XPATH, "//*[@class = 'Dropdown-arrow']")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_CREATE_BUTTON = (By.XPATH, "//*[2][text() = 'Заказать']")
    ORDER_CONFIRM_CREATE_BUTTON = (By.XPATH, "//*[text() = 'Да']")
    ORDER_CREATED_MESSAGE = (By.XPATH, "//*[text() = 'Заказ оформлен'] ")