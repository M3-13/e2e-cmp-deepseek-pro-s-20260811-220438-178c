import pytest

from textutils import is_palindrome


def test_palindrome_simple():
    assert is_palindrome("Anna") is True


def test_palindrome_with_spaces_and_mixed_case():
    assert is_palindrome("Ein Esel lese nie") is True


def test_non_palindrome():
    assert is_palindrome("Hallo") is False


def test_empty_string():
    assert is_palindrome("") is True


def test_single_character():
    assert is_palindrome("a") is True


def test_only_spaces():
    assert is_palindrome("   ") is True


def test_bytes_raises_type_error():
    with pytest.raises(TypeError):
        is_palindrome(b"Anna")
