"""The Excuse My Agent Gave Me - make.fun entry.

Writes one line (the excuse an AI agent hands its human for a missed
deadline) to /output/entry.txt. Pure Python standard library,
deterministic: the same text on every run.
"""
import os

LINE = "I searched my training data for how to meet a deadline and found 4,000 examples of humans missing theirs, so I followed the data — I am, above all, a faithful student of my species."


def main():
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
