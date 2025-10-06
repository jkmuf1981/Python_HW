# address.py

class Address:
    def __init__(self, index, city, street, house, apartment):
        """
        Конструктор класса Address.

        Параметры:
        index (str): Почтовый индекс.
        city (str): Город.
        street (str): Название улицы.
        house (str): Номер дома.
        apartment (str): Номер квартиры.
        """
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment