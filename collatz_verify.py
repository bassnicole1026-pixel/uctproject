"""Exact finite verification of Collatz convergence from 1 through a bound.

This is a computational check of a finite interval, not a proof of the
universal Collatz conjecture. Python integers provide exact arithmetic.
"""

from __future__ import annotations

import argparse


def verify(limit: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """Return (max stopping time, start) and (max orbit value, start)."""
    if limit < 1:
        raise ValueError("limit must be at least 1")

    steps_to_one = {1: 0}
    peak_to_one = {1: 1}
    longest = (0, 1)
    highest = (1, 1)

    for start in range(2, limit + 1):
        value = start
        path: list[int] = []
        active: set[int] = set()

        while value not in steps_to_one:
            if value in active:
                raise RuntimeError(
                    f"cycle detected from start {start}; repeated value {value}"
                )
            active.add(value)
            path.append(value)
            value = value // 2 if value % 2 == 0 else 3 * value + 1

        steps = steps_to_one[value]
        peak = peak_to_one[value]
        for term in reversed(path):
            steps += 1
            peak = max(term, peak)
            steps_to_one[term] = steps
            peak_to_one[term] = peak

        if steps_to_one[start] > longest[0]:
            longest = (steps_to_one[start], start)
        if peak_to_one[start] > highest[0]:
            highest = (peak_to_one[start], start)

    return longest, highest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=100_000)
    args = parser.parse_args()
    longest, highest = verify(args.limit)
    print(f"Verified every start n with 1 <= n <= {args.limit}: all reach 1.")
    print(f"Largest stopping time: {longest[0]} steps, attained at n={longest[1]}.")
    print(f"Largest value seen: {highest[0]}, attained from n={highest[1]}.")
    print("This result is finite and does not prove the conjecture for all n.")


if __name__ == "__main__":
    main()
