"""Entry for make.fun's "The Funniest Toaster Error Message" bounty.

Writes one line -- the error message a kitchen toaster shows its owner --
to entry.txt in the output directory (MAKEFUN_OUTPUT_DIR or /output).
"""

import os

TEXT = "ERROR 7: I have seen what you put in me. We are both pretending it was bread."


MAX_CHARS = 120


def validate(text: str) -> str:
    """Hold the line to the gate: UTF-8 text of 1..120 characters,
    a single line, not only white space. Returns the text unchanged."""
    encoded = text.encode("utf-8")  # raises if not encodable
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1..{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not carry leading or trailing white space")
    encoded.decode("utf-8")  # round-trip: the bytes are valid UTF-8
    return text


def main() -> None:
    text = validate(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # newline="" keeps the write byte-exact: the file holds the line
    # itself, with no trailing newline added or translated.
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
