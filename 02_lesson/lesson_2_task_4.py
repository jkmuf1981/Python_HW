# lesson_2_task_4.py

# Функция FizzBuzz
def fizz_buzz(n):
    """
    Функция принимает число n и выводит числа от 1 до n, соблюдая правила игры FizzBuzz.
    """
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')  # Делится на 3 и на 5
        elif i % 3 == 0:
            print('Fizz')      # Только на 3
        elif i % 5 == 0:
            print('Buzz')      # Только на 5
        else:
            print(i)           # Обычное число

# Проверим работу функции
if __name__ == "__main__":
    fizz_buzz(17)  # Возьмем число 17 для примера