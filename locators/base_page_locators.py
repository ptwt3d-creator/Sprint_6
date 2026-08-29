from selenium.webdriver.common.by import By


class Locators:

    LOGO_YANDEX = (By.XPATH, "//*[contains(@class, 'Header_LogoYandex')]")
    LOGO_SCOOTER = (By.XPATH, "//*[contains(@class, 'Header_LogoScooter')]")