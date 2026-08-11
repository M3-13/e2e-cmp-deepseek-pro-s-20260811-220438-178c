import re
import unicodedata

_UMLAUT_MAP = {
    "Ä": "AE",
    "ä": "ae",
    "Ö": "OE",
    "ö": "oe",
    "Ü": "UE",
    "ü": "ue",
    "ß": "ss",
}


def slugify(text: str) -> str:
    if isinstance(text, bytes):
        raise TypeError("text must be str, not bytes")

    for umlaut, replacement in _UMLAUT_MAP.items():
        text = text.replace(umlaut, replacement)

    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")

    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")

    return text
