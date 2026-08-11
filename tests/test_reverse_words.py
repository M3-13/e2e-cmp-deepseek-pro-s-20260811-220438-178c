import pytest

from textutils import reverse_words


def test_three_words():
    assert reverse_words("eins zwei drei") == "drei zwei eins"


def test_leading_and_trailing_whitespace():
    assert reverse_words("  hallo  welt  ") == "welt hallo"


def test_single_word():
    assert reverse_words("hallo") == "hallo"


def test_empty_string():
    assert reverse_words("") == ""


def test_only_whitespace():
    assert reverse_words("   ") == ""


def test_bytes_raises_type_error():
    with pytest.raises(TypeError):
        reverse_words(b"eins zwei drei")
