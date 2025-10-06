# lesson_3_task_2.py

# Импортируем класс Smartphone из модуля smartphone
from smartphone import Smartphone

# Создаём пустой список catalog
catalog = []

# Заполняем список пятью экземплярами смартфонов
catalog.append(Smartphone(brand="Apple", model="iPhone 14 Pro Max", phone_number="+79001234567"))
catalog.append(Smartphone(brand="Samsung", model="Galaxy S23 Ultra", phone_number="+79107654321"))
catalog.append(Smartphone(brand="Xiaomi", model="Redmi Note 11S", phone_number="+79203456789"))
catalog.append(Smartphone(brand="Huawei", model="P50 Pro", phone_number="+79309876543"))
catalog.append(Smartphone(brand="Google", model="Pixel 7 Pro", phone_number="+79401112233"))

# Печать каталога в нужном формате
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")