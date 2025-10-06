# lesson_3_task_1.py

# Импортируем класс User из модуля user
from user import User

# Создаём экземпляр класса User
my_user = User(first_name="Иван", last_name="Иванов")

# Вызываем методы нового экземпляра
my_user.print_first_name()  # Выводим имя
my_user.print_last_name()   # Выводим фамилию
my_user.print_full_name()   # Выводим полное имя
