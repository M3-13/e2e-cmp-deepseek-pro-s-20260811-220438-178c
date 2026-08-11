import inspect

from textutils import is_palindrome, reverse_words, slugify, truncate, word_count


def test_slugify_signature():
    sig = inspect.signature(slugify)
    params = list(sig.parameters.keys())
    assert params == ["text"]
    assert sig.return_annotation is str


def test_truncate_signature():
    sig = inspect.signature(truncate)
    params = list(sig.parameters.keys())
    assert params == ["text", "max_len"]
    assert sig.return_annotation is str


def test_word_count_signature():
    sig = inspect.signature(word_count)
    params = list(sig.parameters.keys())
    assert params == ["text"]
    assert sig.return_annotation is int


def test_is_palindrome_signature():
    sig = inspect.signature(is_palindrome)
    params = list(sig.parameters.keys())
    assert params == ["text"]
    assert sig.return_annotation is bool


def test_reverse_words_signature():
    sig = inspect.signature(reverse_words)
    params = list(sig.parameters.keys())
    assert params == ["text"]
    assert sig.return_annotation is str
