#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Writes a single original one-line joke about office life to
/output/entry.txt, after checking it against the competition gate:
UTF-8 text, 1 to 200 characters, exactly one line.
"""

import os

JOKE = "The office Wi-Fi password changes every month, but the only thing in this office with a stable connection is the gossip."

MAX_LENGTH = 200


def validate_single_line(text):
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def validate_length(text, limit=MAX_LENGTH):
    if not 1 <= len(text) <= limit:
        raise ValueError("entry is %d chars, outside the 1-%d range" % (len(text), limit))
    return True


def validate_tight_wording(text):
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    return True


def main():
    validate_single_line(JOKE)
    validate_length(JOKE)
    validate_tight_wording(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
