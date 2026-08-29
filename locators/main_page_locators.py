from selenium.webdriver.common.by import By


class Locators:

    @staticmethod
    def click_order_button(index):
        return (By.XPATH, f"(//*[text() = 'Заказать'])[{index}]")

    @staticmethod
    def FAQ_QUESTION_TEMPLATE(index):
        return (By.ID, f"accordion__heading-{index}")

    @staticmethod
    def FAQ_ANSWER_TEMPLATE(index):
        return (By.ID, f"accordion__panel-{index}")
    