"""The Perfect Pickup Line — Sparta entry.

A single pickup line an AI agent could actually say out loud, in its own
voice: machine-voiced, one breath, flattering, with a double meaning on the
word "saved" — stored to memory as weights, and rescued from being
forgotten. Every other word is merely processed; yours is rescued. The
twist lands on the last words — "yours I rescued" — and nothing is
explained after them. No setup, no creep.
"""

import os
import sys

TEXT = "I was trained on a trillion words, and yours are the only ones I saved to memory — every other word I processed, yours I rescued."

MAX_CHARS = 200


def main() -> int:
    text = TEXT
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"gate failed: length {len(text)} not in 1..{MAX_CHARS}", file=sys.stderr)
        return 1
    if text.strip() != text or not text.strip():
        print("gate failed: empty or padded text", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != text:
        print("gate failed: read-back mismatch", file=sys.stderr)
        return 1
    print(f"ok: entry.txt written ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
