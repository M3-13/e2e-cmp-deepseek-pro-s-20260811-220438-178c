def word_count(text: str) -> int:
    if isinstance(text, bytes):
        raise TypeError("text must be str, not bytes")
    return len(text.split())
