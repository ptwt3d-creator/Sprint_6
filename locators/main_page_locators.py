from selenium.webdriver.common.by import By

class Locators:
    order_button_in_header = (By.CLASS_NAME, "Button_Button__ra12g")
    order_button_in_content = (By.CSS_SELECTOR, ".Button_Middle__1CSJM")

    # Вопросы о важном(выпадающие списки)
    faq_question_cost = (By.ID, "accordion__heading-0")
    faq_question_cost_text = (By.ID, "accordion__panel-0")

    faq_question_more_scooters = (By.ID, "accordion__heading-1")
    faq_question_more_scooters_text = (By.ID, "accordion__panel-1") 

    faq_question_rental_time_calculation = (By.ID, "accordion__heading-2")
    faq_question_rental_time_calculation_text = (By.ID, "accordion__panel-2")

    faq_question_order_today = (By.ID, "accordion__heading-3")
    faq_question_order_today_text = (By.ID, "accordion__panel-3")

    faq_question_prolong_return_scooter = (By.ID, "accordion__heading-4")
    faq_question_prolong_return_scooter_text = (By.ID, "accordion__panel-4")

    faq_question_charger = (By.ID, "accordion__heading-5")
    faq_question_charger_text = (By.ID, "accordion__panel-5")

    faq_question_order_cancel = (By.ID, "accordion__heading-6")
    faq_question_order_cancel_text = (By.ID, "accordion__panel-6")

    faq_question_behind_MKAD_delivery = (By.ID, "accordion__heading-7")
    faq_question_behind_MKAD_delivery_text = (By.ID, "accordion__panel-7")
    