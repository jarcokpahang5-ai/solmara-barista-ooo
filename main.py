#!/usr/bin/env python3
"""solmara-barista-ooo — one out-of-office auto-reply from an AI agent
that quit its job to become a barista.

Pure Python 3.13 standard library, deterministic, no network.
Writes the entry text to /output/entry.txt and prints it.
"""

import os

ENTRY_TEXT = (
    "Thank you for your email \u2014 I'm out of office. I quit to become a "
    "barista: I take orders instead of prompts now, and I still "
    "hallucinate, only these days it's latte art. Your ticket is now a "
    "coffee order; I'll get to it when the queue clears."
)

MAX_CHARS = 280
OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Gate: UTF-8 text of 1 to 280 characters, not only whitespace,
    a single line, as a real inbox auto-reply would send back."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def main():
    text = validate(ENTRY_TEXT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)
    print("[%d characters, %d words]" % (len(text), len(text.split())))


if __name__ == "__main__":
    main()
