from selenium.webdriver.common.by import By


class Locators:

    ORDER_BUTTON_IN_HEADER = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BUTTON_IN_CONTENT = (By.CSS_SELECTOR, ".Button_Middle__1CSJM")

    # Вопросы о важном(выпадающие списки)
    FAQ_QUESTION_COST = (By.ID, "accordion__heading-0")
    FAQ_QUESTION_COST_TEXT = (By.ID, "accordion__panel-0")

    FAQ_QUESTION_MORE_SCOOTERS = (By.ID, "accordion__heading-1")
    FAQ_QUESTION_MORE_SCOOTERS_TEXT = (By.ID, "accordion__panel-1") 

    FAQ_QUESTION_RENTAL_TIME_CALCULATION = (By.ID, "accordion__heading-2")
    FAQ_QUESTION_RENTAL_TIME_CALCULATION_TEXT = (By.ID, "accordion__panel-2")

    FAQ_QUESTION_ORDER_TODAY = (By.ID, "accordion__heading-3")
    FAQ_QUESTION_ORDER_TODAY_TEXT = (By.ID, "accordion__panel-3")

    FAQ_QUESTION_PROLONG_RETURN_SCOOTER = (By.ID, "accordion__heading-4")
    FAQ_QUESTION_PROLONG_RETURN_SCOOTER_TEXT = (By.ID, "accordion__panel-4")

    FAQ_QUESTION_CHARGER = (By.ID, "accordion__heading-5")
    FAQ_QUESTION_CHARGER_TEXT = (By.ID, "accordion__panel-5")

    FAQ_QUESTION_ORDER_CANCEL = (By.ID, "accordion__heading-6")
    FAQ_QUESTION_ORDER_CANCEL_TEXT = (By.ID, "accordion__panel-6")

    FAQ_QUESTION_BEHIND_MKAD_DELIVERY = (By.ID, "accordion__heading-7")
    FAQ_QUESTION_BEHIND_MKAD_DELIVERY_TEXT = (By.ID, "accordion__panel-7")
    