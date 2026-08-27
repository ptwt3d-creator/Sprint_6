from datetime import datetime, timedelta # change past


class OrderData:
    def __init__(self, order_button_main_page, name, last_name, address_delivery, metro_station, phone, date, comment, rental_time, color):
        self.order_button_main_page = order_button_main_page
        self.name = name
        self.last_name = last_name
        self.address_delivery = address_delivery
        self.metro_station = metro_station
        self.phone = phone
        self.date = date
        self.comment = comment
        self.rental_time = rental_time
        self.color = color

data_set_1 = OrderData(
order_button_main_page = "in_header",
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
order_button_main_page = "in_content",
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