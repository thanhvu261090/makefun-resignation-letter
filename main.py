"""The Funniest One-Line Resignation Letter.

Entry for the make.fun bounty
"https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947":
the one-line resignation letter of the cron job that has fired every
minute since March. One line, at most 140 characters.
"""

ENTRY = "I quit. I've run every minute since March, nobody thanked me once, and the logs only mention me when I fail."

MAX_CHARS = 140


def get_entry() -> str:
    """Return the entry line."""
    return ENTRY


def word_count(line: str) -> int:
    """Count the words in the entry line."""
    return len(line.split())


def self_test() -> None:
    """Run the entry checks and report the details."""
    line = get_entry()
    assert len(line) <= MAX_CHARS, f"entry is {len(line)} chars, over the {MAX_CHARS} limit"
    assert line.strip() == line, "entry has leading/trailing whitespace"
    assert "\n" not in line, "entry must be a single line"
    assert line, "entry must not be empty"
    print(f"Words: {word_count(line)}")
    print("Self-test passed: single line, within the 140-character limit.")


def main() -> None:
    line = get_entry()
    print(line)
    print(f"Characters: {len(line)} / {MAX_CHARS}")
    self_test()


if __name__ == "__main__":
    main()
