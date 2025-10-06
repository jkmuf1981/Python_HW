# user.py

class User:
    def __init__(self, first_name, last_name):
        """
        Конструктор класса User.

        Параметры:
        first_name (str): Имя пользователя.
        last_name (str): Фамилия пользователя.
        """
        self.first_name = first_name
        self.last_name = last_name

    def print_first_name(self):
        """Метод для вывода имени"""
        print(f"Имя: {self.first_name}")

    def print_last_name(self):
        """Метод для вывода фамилии"""
        print(f"Фамилия: {self.last_name}")

    def print_full_name(self):
        """Метод для вывода полного имени"""
        print(f"Полное имя: {self.first_name} {self.last_name}")