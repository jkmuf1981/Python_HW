# lesson_3_task_3.py

# Импортируем классы Address и Mailing
from address import Address
from mailing import Mailing

# Создаём объекты Address для отправителя и получателя
to_addr = Address(index="123456", city="Москва", street="Ленинградская", house="12", apartment="34")
from_addr = Address(index="654321", city="Санкт-Петербург", street="Невская", house="5", apartment="12")

# Создаём объект Mailing
mailing = Mailing(to_address=to_addr, from_address=from_addr, cost=500., track="TRACKCODE12345")

# Форматированный вывод информации о посылке
output = f"""\
Отправление {mailing.track} из \
{mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house}-{mailing.from_address.apartment} \
в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house}-{mailing.to_address.apartment}. \
Стоимость {mailing.cost:.2f} рублей.\
"""

# Распечатываем информацию
print(output)