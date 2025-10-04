class StringUtils:
    @staticmethod
    def is_palindrome(s):
        """Проверяет строку на палиндром"""
        return s.lower() == s.lower()[::-1]

    @staticmethod
    def count_words(text):
        """Подсчет количества слов в тексте."""
        words = text.split()
        return len(words)

    @staticmethod
    def reverse_string(s):
        """Разворот строки."""
        return s[::-1]

    @staticmethod
    def capitalize_first_letter(s):
        """Делает первую букву заглавной."""
        if not s.strip():
            raise ValueError("Строка пустая")
        return s[:1].upper() + s[1:]