from selenium.webdriver.common.by import By

class Locators:
    order_button_in_header = (By.CLASS_NAME, "Button_Button__ra12g")
    order_button_in_content = (By.CSS_SELECTOR, ".Button_Middle__1CSJM")

    # Вопросы о важном(выпадающие списки)
    faq_question_cost = (By.ID, "accordion__heading-8")
    faq_question_cost_text = (By.ID, "accordion__panel-8")

    faq_question_more_scooters = (By.ID, "accordion__heading-9")
    faq_question_more_scooters_text = (By.ID, "accordion__panel-9") 

    faq_question_rental_time_calculation = (By.ID, "accordion__heading-10")
    faq_question_rental_time_calculation_text = (By.ID, "accordion__panel-10")

    faq_question_order_today = (By.ID, "accordion__heading-11")
    faq_question_order_today_text = (By.ID, "accordion__panel-11")

    faq_question_prolong_return_scooter = (By.ID, "accordion__heading-12")
    faq_question_prolong_return_scooter_text = (By.ID, "accordion__panel-12")

    faq_question_charger = (By.ID, "accordion__heading-13")
    faq_question_charger_text = (By.ID, "accordion__panel-13")

    faq_question_order_cancel = (By.ID, "accordion__heading-14")
    faq_question_order_cancel_text = (By.ID, "accordion__panel-14")

    faq_question_behind_MKAD_delivery = (By.ID, "accordion__heading-15")
    faq_question_behind_MKAD_delivery_text = (By.ID, "accordion__panel-15")
    