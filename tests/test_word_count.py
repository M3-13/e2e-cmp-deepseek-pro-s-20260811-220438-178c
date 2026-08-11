import pytest

from textutils import word_count


def test_word_count_multiple_words():
    assert word_count("hello world") == 2


def test_word_count_leading_trailing_whitespace():
    assert word_count("  ein  test ") == 2


def test_word_count_multiple_whitespace_between():
    assert word_count("a   b    c") == 3


def test_word_count_single_word():
    assert word_count("hello") == 1


def test_word_count_empty_string():
    assert word_count("") == 0


def test_word_count_only_whitespace():
    assert word_count("   ") == 0


def test_word_count_bytes_input_raises_typeerror():
    with pytest.raises(TypeError, match="text must be str, not bytes"):
        word_count(b"hello")
