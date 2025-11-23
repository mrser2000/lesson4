import pytest
from string_utils import StringUtils


class TestStringUtils:
    def setup_method(self):
        """Инициализация объекта перед каждым тестом"""
        self.utils = StringUtils()

    # Тесты для capitalize
    def test_capitalize_normal(self):
        assert self.utils.capitalize("skypro") == "Skypro"

    def test_capitalize_empty(self):
        assert self.utils.capitalize("") == ""

    def test_capitalize_single_char(self):
        assert self.utils.capitalize("a") == "A"

    def test_capitalize_already_capitalized(self):
        assert self.utils.capitalize("Hello") == "Hello"

    def test_capitalize_all_uppercase(self):
        assert self.utils.capitalize("HELLO") == "Hello"

    def test_capitalize_with_leading_spaces(self):
        assert self.utils.capitalize("  hello") == "  hello"

    # Тесты для trim
    def test_trim_normal(self):
        assert self.utils.trim("   skypro") == "skypro"

    def test_trim_no_leading_spaces(self):
        assert self.utils.trim("skypro") == "skypro"

    def test_trim_only_spaces(self):
        assert self.utils.trim("   ") == ""

    def test_trim_empty_string(self):
        assert self.utils.trim("") == ""

    def test_trim_multiple_spaces(self):
        assert self.utils.trim("    skypro") == "skypro"

    def test_trim_spaces_in_middle(self):
        assert self.utils.trim("  sky pro  ") == "sky pro  "

    # Тесты для contains
    def test_contains_found(self):
        assert self.utils.contains("SkyPro", "S") is True

    def test_contains_not_found(self):
        assert self.utils.contains("SkyPro", "U") is False

    def test_contains_empty_string(self):
        assert self.utils.contains("", "a") is False

    def test_contains_empty_symbol(self):
        # В Python '' всегда считается найденным в любой строке
        assert self.utils.contains("abc", "") is True

    def test_contains_longer_symbol(self):
        assert self.utils.contains("ab", "abc") is False

    def test_contains_case_sensitive(self):
        assert self.utils.contains("SkyPro", "s") is False

    def test_contains_symbol_at_end(self):
        assert self.utils.contains("hello", "o") is True

    # Тесты для delete_symbol
    def test_delete_symbol_single_char(self):
        assert self.utils.delete_symbol("SkyPro", "k") == "SyPro"

    def test_delete_symbol_substring(self):
        assert self.utils.delete_symbol("SkyPro", "Pro") == "Sky"

    def test_delete_symbol_not_present(self):
        assert self.utils.delete_symbol("SkyPro", "X") == "SkyPro"

    def test_delete_symbol_all_occurrences(self):
        assert self.utils.delete_symbol("abacaba", "a") == "bcb"

    def test_delete_symbol_empty_string(self):
        assert self.utils.delete_symbol("", "a") == ""

    def test_delete_symbol_empty_symbol(self):
        assert self.utils.delete_symbol("abc", "") == "abc"

    def test_delete_symbol_full_match(self):
        assert self.utils.delete_symbol("hello", "hello") == ""

    def test_delete_symbol_overlapping(self):
        assert self.utils.delete_symbol("aaaa", "aa") == ""

    def test_delete_symbol_repeated_non_overlap(self):
        assert self.utils.delete_symbol("aabbcc", "bb") == "aacc"