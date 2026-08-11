def truncate(text: str, max_len: int) -> str:
    if isinstance(text, bytes):
        raise TypeError("text must be str, not bytes")
    if max_len < 1:
        return ""
    if len(text) <= max_len:
        return text
    return text[: max_len - 1] + "\u2026"
