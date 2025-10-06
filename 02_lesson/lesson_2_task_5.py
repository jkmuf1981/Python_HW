# lesson_2_task_5.py

# Функция, определяющая сезон по месяцу
def month_to_season(month):
    """
    Функция принимает номер месяца и возвращает название соответствующего сезона.
    """
    if month in [12, 1, 2]:  # зимние месяцы
        return "Зима"
    elif month in [3, 4, 5]:  # весенние месяцы
        return "Весна"
    elif month in [6, 7, 8]:  # летние месяцы
        return "Лето"
    elif month in [9, 10, 11]:  # осенние месяцы
        return "Осень"
    else:
        return "Некорректный номер месяца"

# Проверим работу функции
if __name__ == "__main__":
    season = month_to_season(2)  # Берём февраль
    print(season)  # Получим "Зима"