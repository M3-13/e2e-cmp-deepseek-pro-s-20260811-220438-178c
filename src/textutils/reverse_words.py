def reverse_words(text: str) -> str:
    if isinstance(text, bytes):
        raise TypeError("text must be str, not bytes")
    words = text.split()
    words.reverse()
    return " ".join(words)
