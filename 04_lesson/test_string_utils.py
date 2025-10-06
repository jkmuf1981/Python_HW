import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# === Тесты для метода capitalize() ===

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),          # Нормальное значение
    ("HELLO WORLD", "HELLO WORLD"), # Все большие буквы остаются неизменными
    ("python", "Python"),           # Одно слово
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                      # Пустая строка
    ("   ", "   "),                # Пробельные символы
    (None, TypeError),             # Недопустимое значение
])
def test_capitalize_negative(input_str, expected):
    if isinstance(expected, type):
        with pytest.raises(expected):
            string_utils.capitalize(input_str)
    else:
        assert string_utils.capitalize(input_str) == expected

# === Тесты для метода trim() ===

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   SkyPro", "SkyPro"),       # Префикс пробелов
    ("  Python  ", "Python  "),    # Передняя и задняя части
    ("Test", "Test"),              # Без изменений
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                      # Пустая строка
    ("   ", ""),                   # Только пробелы
    (None, AttributeError),        # Некорректный аргумент
])
def test_trim_negative(input_str, expected):
    if isinstance(expected, type):
        with pytest.raises(expected):
            string_utils.trim(input_str)
    else:
        assert string_utils.trim(input_str) == expected

# === Тесты для метода contains() ===

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "P", True),         # Наличие символа
    ("SkyPro", "y", True),         # Маленькая буква
    ("123ABC", "A", True),         # Число + буква
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "X", False),        # Отсутствие символа
    ("", "a", False),              # Пустая строка
    (None, "a", AttributeError),   # Неправильный аргумент
])
def test_contains_negative(input_str, symbol, expected):
    if isinstance(expected, type):
        with pytest.raises(expected):
            string_utils.contains(input_str, symbol)
    else:
        assert string_utils.contains(input_str, symbol) == expected

# === Тесты для метода delete_symbol() ===

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", "kyPro"),      # Удаление первого символа
    ("SkyPro", "o", "SkyPr"),      # Удаление последнего символа
    ("123ABC", "B", "123AC"),     # Удаление одной буквы среди цифр
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "Z", "SkyPro"),     # Нет такого символа
    ("", "a", ""),                 # Пустая строка
    (None, "a", AttributeError),   # Неверный аргумент
])
def test_delete_symbol_negative(input_str, symbol, expected):
    if isinstance(expected, type):
        with pytest.raises(expected):
            string_utils.delete_symbol(input_str, symbol)
    else:
        assert string_utils.delete_symbol(input_str, symbol) == expected