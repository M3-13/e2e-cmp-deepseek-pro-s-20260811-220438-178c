import time

import pytest

from textutils import slugify


def test_umlaut_replacement():
    assert slugify("Hällö Wörld!") == "haelloe-woerld"


def test_special_chars_and_spaces():
    assert slugify("  --Foo & Bar--  ") == "foo-bar"


def test_umlaut_uppercase():
    assert slugify("ÄÖÜ") == "aeoeue"


def test_eszett():
    assert slugify("Straße") == "strasse"
    assert slugify("ß") == "ss"


def test_accent_removal():
    assert slugify("café") == "cafe"
    assert slugify("naïve") == "naive"
    assert slugify("piñata") == "pinata"


def test_leading_trailing_hyphens():
    assert slugify("-hello-") == "hello"
    assert slugify("---test---") == "test"


def test_consecutive_hyphens_collapsed():
    assert slugify("foo   bar") == "foo-bar"
    assert slugify("a!@#b$%^c") == "a-b-c"


def test_plain_ascii():
    assert slugify("Hello World 123") == "hello-world-123"


def test_empty_string():
    assert slugify("") == ""


def test_only_special_chars():
    assert slugify("!@#$%") == ""


def test_bytes_input_raises_typeerror():
    with pytest.raises(TypeError):
        slugify(b"Hello")


def test_numbers_only():
    assert slugify("12345") == "12345"


def test_mixed_language():
    assert slugify("München über Düsseldorf") == "muenchen-ueber-duesseldorf"


def test_performance_one_million_chars():
    text = "a" * 1_000_000
    start = time.perf_counter()
    result = slugify(text)
    elapsed = time.perf_counter() - start
    assert elapsed < 0.2, f"slugify took {elapsed:.3f}s for 1M chars"
    assert result == "a" * 1_000_000
