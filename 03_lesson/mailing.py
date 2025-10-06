# mailing.py

from address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        """
        Конструктор класса Mailing.

        Параметры:
        to_address (Address): Адрес доставки.
        from_address (Address): Адрес отправления.
        cost (float): Стоимость отправки.
        track (str): Трек-код посылки.

        ...
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

        #### Шаг 3: Трек-код посылки.
        """
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track