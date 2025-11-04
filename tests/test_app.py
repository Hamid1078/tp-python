import pytest
from src.app import add, is_palindrome


def test_add_positive():
    assert add(3, 5) == 8


def test_add_negative():
    assert add(-2, -3) == -5


def test_is_palindrome_true():
    assert is_palindrome("Kayak") is True


def test_is_palindrome_false():
    assert is_palindrome("Python") is False


def test_is_palindrome_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") is True
