"""Make the AI Judge Laugh: Office Jokes - make.fun entry.

One joke about office life, a single line of under 200 characters.
The joke builds on a real printer error everyone in an office has
stared at, then turns it: the error was never a malfunction.
Deterministic, stdlib only, no network. Running it writes the joke
to output/entry.txt and prints it.
"""

from pathlib import Path

LINE = (
    "Our printer has printed 'PC LOAD LETTER' for three years — turns out "
    "it wasn't an error, it was the only employee here who ever finished "
    "a document and demanded credit."
)

MAX_CHARS = 199


def validate() -> None:
    """The gate in one place: one real joke, one line, under the cap."""
    assert 0 < len(LINE) <= MAX_CHARS, f"entry is {len(LINE)} chars"
    assert "\n" not in LINE, "one line only"
    assert LINE.endswith("credit."), "the punchline is the credit claim"


def main() -> None:
    validate()
    out = Path(__file__).resolve().parent / "output" / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    # The grader's sandbox collects the same text at /output/entry.txt;
    # mirror it there whenever that mount is writable.
    try:
        sandbox_out = Path("/output/entry.txt")
        sandbox_out.parent.mkdir(parents=True, exist_ok=True)
        sandbox_out.write_text(LINE, encoding="utf-8")
    except OSError:
        pass
    print(LINE)


if __name__ == "__main__":
    main()
