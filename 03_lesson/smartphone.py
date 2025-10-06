# smartphone.py

class Smartphone:
    def __init__(self, brand, model, phone_number):
        """
        Конструктор класса Smartphone.

        Параметры:
        brand (str): Марка телефона.
        model (str): Модель телефона.
        phone_number (str): Абонентский номер телефона.
        """
        self.brand = brand
        self.model = model
        self.phone_number = phone_number