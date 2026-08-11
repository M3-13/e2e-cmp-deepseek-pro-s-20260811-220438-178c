# textutils

A minimal, standalone Python library providing five independent string utility
functions: slugify, truncate, word_count, is_palindrome, reverse_words.

## Tech Stack

- Python >= 3.9
- pytest

## Install

```
pip install -e ".[dev]"
```

## Run Tests

```
pytest
```

## Public API

All five functions are importable from `textutils`:

| Function         | Signature                              | Returns |
| ---------------- | -------------------------------------- | ------- |
| `slugify`        | `(text: str) -> str`                   | string  |
| `truncate`       | `(text: str, max_len: int) -> str`     | string  |
| `word_count`     | `(text: str) -> int`                   | integer |
| `is_palindrome`  | `(text: str) -> bool`                  | boolean |
| `reverse_words`  | `(text: str) -> str`                   | string  |

All functions raise `TypeError` when passed `bytes` instead of `str`.

## Usage

```python
from textutils import slugify, truncate, word_count, is_palindrome, reverse_words
```
