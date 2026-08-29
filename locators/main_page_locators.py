from selenium.webdriver.common.by import By


class Locators:

    ORDER_BUTTON_IN_HEADER = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BUTTON_IN_CONTENT = (By.CSS_SELECTOR, ".Button_Middle__1CSJM")

    # Вопросы о важном(выпадающие списки)
    @staticmethod
    def FAQ_QUESTION_TEMPLATE(index):
        return (By.ID, f"accordion__heading-{index}")

    @staticmethod
    def FAQ_ANSWER_TEMPLATE(index):
        return (By.ID, f"accordion__panel-{index}")
    