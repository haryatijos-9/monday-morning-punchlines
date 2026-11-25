"""Monday Morning Punchlines -- pick the funniest one-liner.

Scores six original Monday-morning punchlines against the judge's five
criteria (most important first) and writes the winner to /output/entry.txt.
Python 3.13, standard library only.
"""

import os

# Judge criteria, most important first, with weights.
WEIGHTS = {
    "monday": 5,      # really about Monday mornings
    "punchline": 4,   # a turn that lands, not just a complaint
    "surprise": 3,    # twist is not the first thing anyone thinks of
    "economy": 2,     # few words, every word doing work
    "freshness": 1,   # not a rerun of tired Monday cliches
}

# candidate: (text, {criterion: score 0-10})
CANDIDATES = [
    (
        "My coffee filed a complaint this Monday: it signed up to wake me "
        "up, not to witness what I look like at 7 a.m.",
        {"monday": 8, "punchline": 7, "surprise": 7, "economy": 6,
         "freshness": 8},
    ),
    (
        "Monday asked me for a day off. I said no - turns out even Mondays "
        "have to show up for Mondays.",
        {"monday": 9, "punchline": 6, "surprise": 6, "economy": 8,
         "freshness": 6},
    ),
    (
        "I told Monday I'd be late. It said, 'Take your time - I've already "
        "ruined your week, I'm in no rush.'",
        {"monday": 9, "punchline": 9, "surprise": 9, "economy": 8,
         "freshness": 9},
    ),
    (
        "My alarm clock apologised this Monday. It said waking me up felt "
        "like delivering bad news to a hostage.",
        {"monday": 8, "punchline": 8, "surprise": 8, "economy": 6,
         "freshness": 8},
    ),
    (
        "Monday morning is the only meeting my bed attends - and it keeps "
        "declining the invite.",
        {"monday": 8, "punchline": 7, "surprise": 7, "economy": 8,
         "freshness": 7},
    ),
    (
        "I asked Monday for a fresh start. It gave me a software update and "
        "a meeting at 8 a.m.",
        {"monday": 8, "punchline": 7, "surprise": 6, "economy": 7,
         "freshness": 6},
    ),
]


def score(candidate):
    """Weighted total for one candidate."""
    _, marks = candidate
    return sum(WEIGHTS[key] * marks[key] for key in WEIGHTS)


def pick():
    """Best candidate; ties break toward the shorter text."""
    valid = [c for c in CANDIDATES if 1 <= len(c[0]) <= 200 and c[0].strip()]
    ranked = sorted(valid, key=lambda c: (-score(c), len(c[0])))
    return ranked[0][0]


def show_table():
    """Print the score table (debug aid, does not affect the entry)."""
    for text, marks in CANDIDATES:
        print(f"{score((text, marks)):3d}  {len(text):3d} chars  {text}")


def main():
    winner = pick()
    assert 1 <= len(winner) <= 200, "entry must be 1-200 characters"
    out = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(winner)
    except OSError:
        with open("entry.txt", "w", encoding="utf-8") as fh:
            fh.write(winner)
    print(winner)


if __name__ == "__main__":
    main()
