def is_palindrome(text: str) -> bool:
    if isinstance(text, bytes):
        raise TypeError("text must be str, not bytes")
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
