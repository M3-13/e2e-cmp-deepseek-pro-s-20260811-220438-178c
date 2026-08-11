import time

import pytest

from textutils import truncate


def test_truncate_with_ellipsis():
    assert truncate("Hallo Welt", 8) == "Hallo W\u2026"


def test_truncate_text_shorter_than_max_len():
    assert truncate("Kurz", 10) == "Kurz"


def test_truncate_text_equal_to_max_len():
    assert truncate("abcd", 4) == "abcd"


def test_truncate_max_len_zero():
    assert truncate("Test", 0) == ""


def test_truncate_max_len_one():
    assert truncate("ABC", 1) == "\u2026"


def test_truncate_max_len_negative():
    assert truncate("Hello", -5) == ""


def test_truncate_empty_string():
    assert truncate("", 10) == ""


def test_truncate_bytes_raises_typeerror():
    with pytest.raises(TypeError):
        truncate(b"hello", 10)


def test_truncate_performance():
    text = "x" * 1_000_000
    start = time.perf_counter()
    result = truncate(text, 50)
    elapsed = time.perf_counter() - start
    assert elapsed < 0.2
    expected_len = len("x" * 49 + "\u2026")
    assert len(result) == expected_len
    assert result == "x" * 49 + "\u2026"
