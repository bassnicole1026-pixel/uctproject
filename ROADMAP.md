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

## Proved descent regions

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

### Lemma 3: `n ≡ 11 (mod 64)`

If `n = 64k + 11`, where `k ≥ 0`, then `S^3(n) < n`.

**Proof.** The first two odd steps are exact:

- `3n + 1 = 192k + 34 = 2(96k + 17)`, so `S(n) = 96k + 17`;
- `3S(n) + 1 = 288k + 52 = 4(72k + 13)`, so `S^2(n) = 72k + 13`.

Then `3S^2(n) + 1 = 216k + 40 = 8(27k + 5)`, so `S^3(n) ≤ 27k + 5 < 64k + 11 = n`.

### Lemma 4: `n ≡ 23, 43, or 55 (mod 64)`

For each of these three classes, `S^3(n) < n`.

**Proof.** Write `n = 64k + r`, with `k ≥ 0`.

- If `r = 23`, then `S(n) = 96k + 35` and `S^2(n) = 144k + 53`. Since `3S^2(n) + 1 = 432k + 160 = 16(27k + 10)`, we have `S^3(n) ≤ 27k + 10 < 64k + 23`.
- If `r = 43`, then `S(n) = 96k + 65`, `S^2(n) = 72k + 49`, and `S^3(n) = 54k + 37 < 64k + 43`.
- If `r = 55`, then `S(n) = 96k + 83` and `S^2(n) = 144k + 125`. Since `3S^2(n) + 1 = 432k + 376 = 8(54k + 47)`, we have `S^3(n) ≤ 54k + 47 < 64k + 55`.
### Lemma 5: `n ≡ 7 or 15 (mod 256)`

For each of these two classes, `S^4(n) < n`.

**Proof.** Write `n = 256k + r`, where `k ≥ 0`.

- If `r = 7`, the first three odd iterates are `384k + 11`, `576k + 17`, and `432k + 13`. Since `3S^3(n) + 1 = 1296k + 40 = 8(162k + 5)`, we have `S^4(n) ≤ 162k + 5 < 256k + 7`.
- If `r = 15`, the first three odd iterates are `384k + 23`, `576k + 35`, and `864k + 53`. Since `3S^3(n) + 1 = 2592k + 160 = 16(162k + 10)`, we have `S^4(n) ≤ 162k + 10 < 256k + 15`.

### Lemma 6: `n ≡ 143 (mod 256)`

If `n = 256k + 143`, where `k ≥ 0`, then `S^4(n) < n`.

**Proof.** The first three odd iterates are exact:

- `3n + 1 = 768k + 430 = 2(384k + 215)`, so `S(n) = 384k + 215`;
- `3S(n) + 1 = 1152k + 646 = 2(576k + 323)`, so `S^2(n) = 576k + 323`;
- `3S^2(n) + 1 = 1728k + 970 = 2(864k + 485)`, so `S^3(n) = 864k + 485`.

Finally, `3S^3(n) + 1 = 2592k + 1456 = 16(162k + 91)`. Since `162k + 91` is odd, this valuation is exactly 4 and `S^4(n) = 162k + 91 < 256k + 143 = n`.

### Lemma 7: `n ≡ 187 (mod 256)`

If `n = 256k + 187`, where `k ≥ 0`, then `S^4(n) < n`.

**Proof.** The odd Syracuse iterates are exact:

- `3n + 1 = 768k + 562 = 2(384k + 281)`, so `S(n) = 384k + 281`;
- `3S(n) + 1 = 1152k + 844 = 4(288k + 211)`, so `S^2(n) = 288k + 211`;
- `3S^2(n) + 1 = 864k + 634 = 2(432k + 317)`, so `S^3(n) = 432k + 317`;
- `3S^3(n) + 1 = 1296k + 952 = 8(162k + 119)`, so `S^4(n) = 162k + 119`.

Each quotient in parentheses is odd, so the listed powers of 2 are the exact valuations. Finally, `256k + 187 - (162k + 119) = 94k + 68 > 0`.

### Lemma 8: `n ≡ 39 (mod 256)`

If `n = 256k + 39`, where `k ≥ 0`, then `S^5(n) < n`.

**Proof.** The first four odd Syracuse iterates are exact:

- `3n + 1 = 768k + 118 = 2(384k + 59)`, so `S(n) = 384k + 59`;
- `3S(n) + 1 = 1152k + 178 = 2(576k + 89)`, so `S^2(n) = 576k + 89`;
- `3S^2(n) + 1 = 1728k + 268 = 4(432k + 67)`, so `S^3(n) = 432k + 67`;
- `3S^3(n) + 1 = 1296k + 202 = 2(648k + 101)`, so `S^4(n) = 648k + 101`.

Each displayed quotient is odd. On the fifth step, `3S^4(n) + 1 = 1944k + 304 = 8(243k + 38)`, so `S^5(n) ≤ 243k + 38 < 256k + 39 = n`, since the difference is `13k + 1 > 0`.

### Lemma 9: `n ≡ 79 (mod 256)`

If `n = 256k + 79`, where `k ≥ 0`, then `S^5(n) < n`.

**Proof.** The first four odd Syracuse iterates are exact:

- `3n + 1 = 768k + 238 = 2(384k + 119)`, so `S(n) = 384k + 119`;
- `3S(n) + 1 = 1152k + 358 = 2(576k + 179)`, so `S^2(n) = 576k + 179`;
- `3S^2(n) + 1 = 1728k + 538 = 2(864k + 269)`, so `S^3(n) = 864k + 269`;
- `3S^3(n) + 1 = 2592k + 808 = 8(324k + 101)`, so `S^4(n) = 324k + 101`.

Each displayed quotient is odd. Finally, `3S^4(n) + 1 = 972k + 304 = 4(243k + 76)`, so `S^5(n) ≤ 243k + 76 < 256k + 79 = n`, since the difference is `13k + 3 > 0`.

### Lemma 10: `n ≡ 95 (mod 256)`

If `n = 256k + 95`, where `k ≥ 0`, then `S^5(n) < n`.

**Proof.** The first four odd Syracuse iterates are exact:

- `3n + 1 = 768k + 286 = 2(384k + 143)`, so `S(n) = 384k + 143`;
- `3S(n) + 1 = 1152k + 430 = 2(576k + 215)`, so `S^2(n) = 576k + 215`;
- `3S^2(n) + 1 = 1728k + 646 = 2(864k + 323)`, so `S^3(n) = 864k + 323`;
- `3S^3(n) + 1 = 2592k + 970 = 2(1296k + 485)`, so `S^4(n) = 1296k + 485`.

Each displayed quotient is odd. On the fifth step, `3S^4(n) + 1 = 3888k + 1456 = 16(243k + 91)`, so `S^5(n) ≤ 243k + 91 < 256k + 95 = n`, since the difference is `13k + 4 > 0`.

### Lemma 11: `n ≡ 123 (mod 256)`

If `n = 256k + 123`, where `k ≥ 0`, then `S^5(n) < n`.

**Proof.** The first four odd Syracuse iterates are exact:

- `3n + 1 = 768k + 370 = 2(384k + 185)`, so `S(n) = 384k + 185`;
- `3S(n) + 1 = 1152k + 556 = 4(288k + 139)`, so `S^2(n) = 288k + 139`;
- `3S^2(n) + 1 = 864k + 418 = 2(432k + 209)`, so `S^3(n) = 432k + 209`;
- `3S^3(n) + 1 = 1296k + 628 = 4(324k + 157)`, so `S^4(n) = 324k + 157`.

Each displayed quotient is odd. On the fifth step, `3S^4(n) + 1 = 972k + 472 = 4(243k + 118)`, so `S^5(n) ≤ 243k + 118 < 256k + 123 = n`, since the difference is `13k + 5 > 0`.

### Lemma 12: `n ≡ 59 (mod 256)`

If `n = 256k + 59`, where `k ≥ 0`, then `S^4(n) < n`.

**Proof.** The first three odd Syracuse iterates are exact:

- `3n + 1 = 768k + 178 = 2(384k + 89)`, so `S(n) = 384k + 89`;
- `3S(n) + 1 = 1152k + 268 = 4(288k + 67)`, so `S^2(n) = 288k + 67`;
- `3S^2(n) + 1 = 864k + 202 = 2(432k + 101)`, so `S^3(n) = 432k + 101`.

On the fourth step, `3S^3(n) + 1 = 1296k + 304 = 16(81k + 19)`, so `S^4(n) ≤ 81k + 19 < 256k + 59 = n`, since the difference is `175k + 40 > 0`.

### Lemma 13: `n ≡ 135 (mod 256)`

If `n = 256k + 135`, where `k ≥ 0`, then `S^4(n) < n`.

**Proof.** The first three odd Syracuse iterates are exact:

- `3n + 1 = 768k + 406 = 2(384k + 203)`, so `S(n) = 384k + 203`;
- `3S(n) + 1 = 1152k + 610 = 2(576k + 305)`, so `S^2(n) = 576k + 305`;
- `3S^2(n) + 1 = 1728k + 916 = 4(432k + 229)`, so `S^3(n) = 432k + 229`.

On the fourth step, `3S^3(n) + 1 = 1296k + 688 = 16(81k + 43)`, so `S^4(n) ≤ 81k + 43 < 256k + 135 = n`, since the difference is `175k + 92 > 0`.

Lemmas 1–4 cover 24 of the 32 odd residue classes modulo 64: all classes `1, 5, 9, 13 (mod 16)`, all of `3 (mod 16)`, and `11, 23, 43, 55 (mod 64)`. Lemmas 5–13 additionally cover `7`, `15`, `39`, `59`, `79`, `95`, `123`, `135`, `143`, and `187 (mod 256)`. These are ten finer classes within the remaining modulo-64 families. Of the four sub-classes of `7 (mod 64)`, `7` and `135 (mod 256)` are covered, leaving `71` and `199`. Of the four sub-classes of `15 (mod 64)`, `15`, `79`, and `143` are covered, leaving `207`. Of the four sub-classes of `31 (mod 64)`, only `95` is covered; `31`, `159`, and `223` remain. Of the four sub-classes of `39 (mod 64)`, only `39` is covered, leaving `103`, `167`, and `231`. Of the four sub-classes of `59 (mod 64)`, `59`, `123`, and `187` are covered, leaving `251`. The three full classes `27, 47, 63 (mod 64)` remain unhandled by these certificates.

## Work plan

1. **Fix the definitions and proof target.** Keep the original map and odd-only map explicit. The descent property above is the global obligation.
2. **Build exact, reproducible checks.** A small program can verify a finite starting interval with arbitrary-precision integer arithmetic. A finite check is evidence about that interval only; it cannot establish the universal statement.
3. **Grow the residue-class descent table.** Split the remaining classes modulo 64 into finer powers-of-two classes, derive exact formulas for each fixed parity/valuation path, and record which classes provably reach a smaller odd value. The classes `7`, `15`, `39`, `59`, `79`, `95`, `123`, `135`, `143`, and `187 (mod 256)` are already covered. A next candidate to audit is `199 (mod 256)`.
4. **Seek a global argument.** Prove that every remaining odd integer has a smaller odd iterate, or find a different well-founded quantity that yields the same strong-induction finish. A shallow residue search that leaves classes uncovered is not a proof.
5. **Audit all cases.** Check boundary values, exact divisibility, class coverage, and every induction dependency independently. Keep conjectures, experiments, and theorems labeled separately.

## First exact computation

Reproduce the check with `python collatz_verify.py --limit 100000`. It verifies every starting value from 1 through 100,000 using exact integer arithmetic. The run passed: the largest stopping time was 350 steps at `n = 77,031`, and the largest value observed was 1,570,824,736 from `n = 77,671`. The program memoizes verified tails and stops if it detects a cycle not reaching 1. This is a finite check, not a proof outside the tested interval.

## Literature waypoint

Terence Tao proved that for every function `f(n)` tending to infinity, almost every positive integer in logarithmic density has a Collatz orbit that reaches a value below `f(n)`. This is a deep partial result, but its “almost every” conclusion is not the all-integers statement required here: [Tao, *Almost all orbits of the Collatz map attain almost bounded values* (2019)](https://arxiv.org/abs/1909.03562).

A 2026 exploratory paper on burst/gap dynamics explicitly leaves its key orbitwise hypotheses open, illustrating why a heuristic contraction picture must not be presented as a proof: [Chang, *Exploring Collatz Dynamics with Human-LLM Collaboration* (2026)](https://arxiv.org/abs/2603.11066).

## Status

Lemmas 1–13 prove strict descent on the listed residue classes. The finite computation is bounded evidence. The global descent property—and therefore the full Collatz conjecture—has not been proved in this project.
