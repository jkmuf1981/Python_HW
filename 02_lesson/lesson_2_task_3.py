import math

# Функция для вычисления площади квадрата
def square(side):
    """
    Функция принимает сторону квадрата и возвращает его площадь.
    Если сторона не целое число, результат округляется вверх.
    """
    area = side * side  # вычисляем площадь
    if not isinstance(side, int):  # если сторона не целое число
        area = math.ceil(area)  # округляем площадь вверх
    return area

# Демонстрируем работу функции
if __name__ == "__main__":
    side_length = 5.5  # задали длину стороны для теста
    area_result = square(side_length)  # получили площадь
    print(f"Площадь квадрата со стороной {side_length} равна {area_result}")