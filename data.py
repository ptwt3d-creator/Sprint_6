from datetime import datetime, timedelta

class FaqAnswersText:
    
    CHARGER = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    COST = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    MORE_SCOOTERS = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    CANCEL_OEDER = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    TODAY_ORDER = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    RENTAL_PROLONG_AND_EARLI_RETURN_SCOOTER = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    RENTAL_TIME_CALCULATION = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    MKAD_DELEVERY = "Да, обязательно. Всем самокатов! И Москве, и Московской области."

class Urls:

    DZEN_URL = "https://dzen.ru/"
    SCOOTER_MAIN_PAGE = "https://qa-scooter.praktikum-services.ru/"
    SCOOTER_ORDER_PAGE = "https://qa-scooter.praktikum-services.ru/order"

class OrderData:

    def __init__(self, order_button_place, name, last_name, address_delivery, metro_station, phone, date, comment, rental_time, color):
        self.order_button_place = order_button_place
        self.name = name
        self.last_name = last_name
        self.address_delivery = address_delivery
        self.metro_station = metro_station
        self.phone = phone
        self.date = date
        self.comment = comment
        self.rental_time = rental_time
        self.color = color

class OrderTestData:

    data_set_1 = OrderData(
        order_button_place = "1",
        name = "Вася",
        last_name = "Иванов",
        address_delivery = "Москва, улица Воздвиженка, 12",
        metro_station = "Александровский сад",
        phone = "880035553555",
        date = (datetime.now() + timedelta(days=1)).strftime("%d.%m.%Y"),
        comment = "заказ не работает?",
        rental_time = "сутки",
        color = "чёрный жемчуг"
    )

    data_set_2 = OrderData(
        order_button_place = "2",
        name = "Мария",
        last_name = "Высоцкая",
        address_delivery = "ул Ленина 5, кв 2",
        metro_station = "Бульвар Дмитрия Донского",
        phone = "89991112233",
        date = (datetime.now() + timedelta(days=3)).strftime("%d.%m.%Y"),
        comment = "Пожалуйста, позвоните за полчаса до приезда. Код от домофона 123К4567.",
        rental_time = "трое суток",
        color = "серая безысходность"
    )
