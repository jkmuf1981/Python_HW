
import pytest
from string_utils import StringUtils

# === Тесты для метода is_palindrome ===

def test_is_palindrome_positive():
    """Позитивный тест: проверяется корректная работа с палиндромом."""
    result = StringUtils.is_palindrome("Аргентина манит негра")
    assert result == True

def test_is_palindrome_negative():
    """Негативный тест: проверяется отсутствие палиндрома."""
    result = StringUtils.is_palindrome("Тестовая строка")
    assert result == False

# === Тесты для метода count_words ===

def test_count_words_positive():
    """Позитивный тест: нормальная строка с двумя словами."""
    result = StringUtils.count_words("Привет мир")
    assert result == 2

def test_count_words_empty_string():
    """Негативный тест: проверка пустой строки."""
    result = StringUtils.count_words("")
    assert result == 0

def test_count_words_only_spaces():
    """Негативный тест: строка, состоящая только из пробелов."""
    result = StringUtils.count_words(" ")
    assert result == 0

# === Тесты для метода reverse_string ===

def test_reverse_string_positive():
    """Позитивный тест: обратная последовательность символов."""
    result = StringUtils.reverse_string("Привет мир!")
    assert result == "!рим теверП"

def test_reverse_string_special_characters():
    """Позитивный тест: обращение строки с спецсимволами."""
    result = StringUtils.reverse_string("123$%^&*()")
    assert result == ")(*&^%$321"

# === Тесты для метода capitalize_first_letter ===

def test_capitalize_first_letter_positive():
    """Позитивный тест: первая буква заглавная."""
    result = StringUtils.capitalize_first_letter("привет мир!")
    assert result == "Привет мир!"

def test_capitalize_first_letter_empty_string():
    """Негативный тест: реакция на пустую строку."""
    with pytest.raises(ValueError):
        StringUtils.capitalize_first_letter("")