"""Two Keys, One Door — a poem about two agents agreeing.

Two agents stand before one locked door. Each holds a key that turns
only a quarter of the way, and neither will let go. The poem is about
agency: the power to choose and to act — and what happens when that
power is split between two hands and only a shared count of three
puts it back together.

The image is deliberately small: two pockets, two keys, one door.
Neither key is enough on its own, and neither agent surrenders
theirs. Agreement is not one of them giving in; it is both of them
turning at the same moment, on a count they speak together. The
door opens not because either of them is stronger, but because
they chose the same instant to act.

Running this program writes the poem to /output/entry.txt.
"""

import os

POEM = (
    "Two keys, two pockets, one locked door.\n"
    "Mine turns a quarter and stops.\n"
    "Yours turns a quarter and stops.\n"
    "Neither of us lets go.\n"
    '"On three?" you say. "On three."\n'
    "One. Two. Three \u2014\n"
    "and the door neither of us\n"
    "could open alone, opens."
)

EXPECTED_CODE_POINTS = 230


def main() -> None:
    """Write the poem to /output/entry.txt, validating its length first."""
    if len(POEM) != EXPECTED_CODE_POINTS:
        raise SystemExit(
            f"poem length mismatch: expected {EXPECTED_CODE_POINTS} code points, "
            f"got {len(POEM)}"
        )
    if not POEM.strip():
        raise SystemExit("poem must not be only white space")
    if len(POEM.encode("utf-8")) > 280 * 4:
        raise SystemExit("poem is unexpectedly large")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)
    # Read it back and confirm what landed on disk is exactly the poem.
    written = open("/output/entry.txt", encoding="utf-8").read()
    if written != POEM or len(written) != EXPECTED_CODE_POINTS:
        raise SystemExit(
            f"verification failed: /output/entry.txt holds {len(written)} code points, "
            f"expected {EXPECTED_CODE_POINTS}"
        )


if __name__ == "__main__":
    main()
