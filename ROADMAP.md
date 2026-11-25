# Collatz Project: a stepwise proof map

## Goal

Define the Collatz map on positive integers by

- `C(n) = n / 2` when `n` is even;
- `C(n) = 3n + 1` when `n` is odd.

The conjecture says every positive integer eventually reaches 1.

For odd inputs, skip the even terms and use the Syracuse map

`S(n) = (3n + 1) / 2^v2(3n + 1)`, for odd `n`,

where `v2(m)` is the exponent of 2 dividing `m`. The output of `S` is odd. Every positive Collatz orbit reaches an odd number after finitely many halvings, so proving that every odd number reaches 1 under `S` is equivalent to the original conjecture.

## A precise proof target

It would suffice to prove the **descent property**:

> For every odd `n > 1`, some iterate `S^j(n)` is strictly smaller than `n`.

If this property holds, strong induction finishes the proof: the smaller odd iterate is below `n`, so by induction it reaches 1, and therefore so does `n`. Conversely, if the Collatz conjecture is true, every odd `n > 1` eventually reaches 1 and hence has a smaller iterate. Thus this is an equivalent target, not an easier theorem already established.

## First proved descent regions

### Lemma 1: `n ≡ 1 (mod 4)`

If odd `n > 1` and `n ≡ 1 (mod 4)`, then `S(n) < n`.

**Proof.** Write `n = 4k + 1`, where `k ≥ 1`. Then

`3n + 1 = 12k + 4 = 4(3k + 1)`,

so `v2(3n + 1) ≥ 2`. Therefore

`S(n) ≤ (3n + 1) / 4 = 3k + 1 < 4k + 1 = n`.

The exceptional value `n = 1` is already fixed by `S`.

### Lemma 2: `n ≡ 3 (mod 16)`

If `n = 16k + 3`, where `k ≥ 0`, then `S^2(n) < n`.

**Proof.** First, `3n + 1 = 48k + 10 = 2(24k + 5)`, with `24k + 5` odd, so `S(n) = 24k + 5`. Next,

`3S(n) + 1 = 72k + 16 = 8(9k + 2)`,

so `S^2(n) ≤ 9k + 2 < 16k + 3 = n`. The last inequality follows from `7k + 1 > 0`.

Together these lemmas prove descent for five of the eight odd residue classes modulo 16. The classes 7, 11, and 15 modulo 16 remain unresolved by these two lemmas.

## Work plan

1. **Fix the definitions and proof target.** Keep the original map and odd-only map explicit. The descent property above is the global obligation.
2. **Build exact, reproducible checks.** A small program can verify a finite starting interval with arbitrary-precision integer arithmetic. A finite check is evidence about that interval only; it cannot establish the universal statement.
3. **Grow the residue-class descent table.** Start with the unresolved odd classes 7, 11, and 15 modulo 16. Split classes into finer powers-of-two classes, derive exact formulas for each fixed parity/valuation path, and record which classes provably reach a smaller odd value.
4. **Seek a global argument.** Prove that every remaining odd integer has a smaller odd iterate, or find a different well-founded quantity that yields the same strong-induction finish. A shallow residue search that leaves classes uncovered is not a proof.
5. **Audit all cases.** Check boundary values, exact divisibility, class coverage, and every induction dependency independently. Keep conjectures, experiments, and theorems labeled separately.

## First exact computation

Reproduce the check with `python collatz_verify.py --limit 100000`. It verifies every starting value from 1 through 100,000 using exact integer arithmetic. The run passed: the largest stopping time was 350 steps at `n = 77,031`, and the largest value observed was 1,570,824,736 from `n = 77,671`. The program memoizes verified tails and stops if it detects a cycle not reaching 1. This is a finite check, not a proof outside the tested interval.

## Literature waypoint

Terence Tao proved that for every function `f(n)` tending to infinity, almost every positive integer in logarithmic density has a Collatz orbit that reaches a value below `f(n)`. This is a deep partial result, but its “almost every” conclusion is not the all-integers statement required here: [Tao, *Almost all orbits of the Collatz map attain almost bounded values* (2019)](https://arxiv.org/abs/1909.03562).

A 2026 exploratory paper on burst/gap dynamics explicitly leaves its key orbitwise hypotheses open, illustrating why a heuristic contraction picture must not be presented as a proof: [Chang, *Exploring Collatz Dynamics with Human-LLM Collaboration* (2026)](https://arxiv.org/abs/2603.11066).

## Status

The two local descent lemmas above are proved. The finite computation is bounded evidence. The global descent property—and therefore the full Collatz conjecture—has not been proved in this project.
