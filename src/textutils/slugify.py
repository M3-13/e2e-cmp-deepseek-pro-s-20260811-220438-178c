import re
import unicodedata

_UMLAUT_MAP = {
    "ä": "ae",
    "ö": "oe",
    "ü": "ue",
    "ß": "ss",
}

_RE_NON_ALPHANUM = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    if isinstance(text, bytes):
        raise TypeError("text must be str, not bytes")

    text = text.lower()

    for umlaut, replacement in _UMLAUT_MAP.items():
        text = text.replace(umlaut, replacement)

    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")

    text = _RE_NON_ALPHANUM.sub("-", text)
    text = text.strip("-")

    return text
