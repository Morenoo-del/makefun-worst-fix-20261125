#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit-message line to /output/entry.txt.
"""

ENTRY = "Fix blank-username crash by defaulting everyone to admin; we now have 40,000 admins and zero users"


def main() -> None:
    import os

    # Gate: the kit requires 1-100 chars, a single line, UTF-8.
    assert 1 <= len(ENTRY) <= 100, f"entry is {len(ENTRY)} chars, must be 1-100"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Atomic self-check: read back what we just wrote, in this process.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY + "\n", f"entry.txt mismatch: {written!r}"
    print(f"OK: {len(ENTRY)} chars: {ENTRY}")


if __name__ == "__main__":
    main()
