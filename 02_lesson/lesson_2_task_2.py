# lesson_2_task_2.py

# Функция для проверки, является ли год високосным
def is_year_leap(year):
    """
    Проверяет, является ли год високосным.
    Возвращает True, если год високосный, и False — если нет.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Проверим работу функции
if __name__ == "__main__":
    test_year = 2024  # год для проверки
    result = is_year_leap(test_year)  # результат проверки
    print(f'год {test_year}: {result}')


    # lesson_2_task_2.py

    # Функция для проверки, является ли год високосным
    def is_year_leap(year):
        """
        Проверяет, является ли год високосным.
        Возвращает True, если год високосный, и False — если нет.
        """
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False


    # Проверим работу функции
    if __name__ == "__main__":
        test_year = 2012 # год для проверки
        result = is_year_leap(test_year)  # результат проверки
        print(f'год {test_year}: {result}')