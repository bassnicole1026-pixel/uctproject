# Collatz Project: a stepwise proof map

## Goal

Define the Collatz map on positive integers by

- `C(n) = n / 2` when `n` is even;
- `C(n) = 3n + 1` when `n` is odd.

The conjecture says every positive integer eventually reaches 1.

The active proof strategy is symbolic: derive exact identities for arbitrary odd inputs, then prove orbit-wide inequalities from the valuation dynamics. Finite orbit checks and lists of residue classes are supplementary records, not the route to the global theorem.

For odd inputs, skip the even terms and use the Syracuse map

`S(n) = (3n + 1) / 2^v2(3n + 1)`, for odd `n`,

where `v2(m)` is the exponent of 2 dividing `m`. The output of `S` is odd. Every positive Collatz orbit reaches an odd number after finitely many halvings, so proving that every odd number reaches 1 under `S` is equivalent to the original conjecture.

## A precise proof target

It would suffice to prove the **descent property**:

> For every odd `n > 1`, some iterate `S^j(n)` is strictly smaller than `n`.

If this property holds, strong induction finishes the proof: the smaller odd iterate is below `n`, so by induction it reaches 1, and therefore so does `n`. Conversely, if the Collatz conjecture is true, every odd `n > 1` eventually reaches 1 and hence has a smaller iterate. Thus this is an equivalent target, not an easier theorem already established.

## Exact iterate formula and global descent condition

For an odd starting value `x_0 = n`, define its Syracuse orbit by `x_i = S(x_{i-1})`, the exact 2-adic valuation at step `i` by `a_i = v_2(3x_{i-1}+1)`, and the cumulative valuation by `A_0=0` and `A_j = a_1 + ··· + a_j`. Define `c_0=0` and `c_{j+1}=3c_j+2^{A_j}`. Then for every `j ≥ 1`,

`2^{A_j} x_j = 3^j n + c_j`,

and hence

`c_j = Σ_{i=0}^{j-1} 3^{j-1-i} 2^{A_i}`.

**Proof.** The identity holds at `j=0`. If `2^{A_j}x_j=3^j n+c_j`, then

`2^{A_j+a_{j+1}}x_{j+1} = 3(2^{A_j}x_j)+2^{A_j} = 3^{j+1}n+(3c_j+2^{A_j})`.

This is the same identity at `j+1`; expanding the recurrence for `c_j` gives the sum.

Therefore an iterate is strictly smaller exactly when

`x_j < n  ⇔  (2^{A_j}-3^j)n > c_j`.

In particular, `A_j log 2 > j log 3` is necessary, but it is not by itself sufficient: the positive correction `c_j` must also fit inside the descent margin.

The same condition has a useful logarithmic form:

`log(x_j/n) = j log 3 - A_j log 2 + Σ_{i=0}^{j-1} log(1 + 1/(3x_i))`.

If a hypothetical counterexample never drops below its odd starting value `n`, then `x_i ≥ n` for every `i`, so for every `j` it must satisfy

`A_j log 2 ≤ j log(3 + 1/n)`.

This is a necessary constraint on a non-descending orbit, not a proof that one cannot exist. The next global proof obligation is to derive a structural lower bound on the cumulative valuations along any such orbit that contradicts this upper bound, without enumerating residue classes.

This can be stated as a precise prefix-crossing target. For a fixed odd `n>1`, if some `j` satisfies

`A_j > j log_2(3+1/n)`,

then a smaller odd iterate has already occurred by time `j`. Indeed, if every `x_i≥n` through `j`, the exact product identity gives

`2^{A_j}x_j = n∏_{i=0}^{j−1}(3+1/x_i) ≤ n(3+1/n)^j`,

and `x_j≥n` would imply the opposite inequality `A_j≤j log_2(3+1/n)`. Thus the Collatz conjecture is equivalent to proving that every odd `n>1` has a finite prefix crossing this line: crossing gives descent and strong induction; if the conjecture holds, continuing after reaching `1` adds valuation `2` at every Syracuse step, eventually crossing because `log_2(3+1/n)<2`.

The remaining task is therefore deterministic: prove this crossing for each fixed orbit from the block transition law. Density estimates do not supply it. Tao's 2019 theorem proves that almost every starting value, in logarithmic density, eventually reaches below any function tending to infinity; the paper explains that the relevant measures are not invariant under Collatz, so typicality cannot simply be propagated from one iterate to the next ([Tao, *Almost all orbits of the Collatz map attain almost bounded values*](https://arxiv.org/abs/1909.03562)). The exceptional individual orbit is exactly what the project still has to rule out.

The prefix cap alone cannot force a crossing. For any odd `n≥3`, put `λ_n=log_2(3+1/n)`, so `1<λ_n<2`, and define the abstract integer sequence

`A_j=floor(jλ_n)`,  `a_j=A_j−A_{j−1}`.

Then every `a_j` is `1` or `2`, `A_j≤jλ_n` for every prefix, and `A_j/j→λ_n`. Thus the necessary non-descent cap admits perfectly regular low-mean valuation schedules. This construction does not claim that the schedule is realized by a Syracuse orbit; it shows why a proof must use the transition congruences, not only a stronger average bound. The next target is to combine the prefix cap with `a_{k+1}−1=v_2(3^{t_k}u_k−1)` and the carry constraints to rule out every realizable schedule that stays below the crossing line.

For an unbounded non-descending orbit, the cap improves asymptotically to the critical slope `c=log_2 3`. Because the Syracuse map is deterministic, any repeated value makes the orbit eventually periodic and hence bounded; therefore every unbounded orbit satisfies `x_i→∞`. With `ε_i=log_2(1+1/(3x_i))`, the exact identity above gives

`A_j/j = c + (1/j)Σ_{i<j}ε_i − (1/j)log_2(x_j/n)`.

Here `ε_i→0`, so its Cesàro mean tends to zero, while the last term is nonnegative. Therefore

`limsup_{j→∞} A_j/j ≤ log_2 3`.

In particular, valuation-one steps have lower density at least `2−log_2 3≈0.4150`, and `limsup N_s(j)/j≤(log_2 3−1)/(s−1)` for `N_s(j)=#{i≤j:a_i≥s}`. A bounded orbit is eventually periodic, and its eventual cycle has the opposite strict inequality: over a period `m`, `2^A=∏_{i=0}^{m−1}(3+1/x_i)>3^m`, so `A/m>log_2 3`. Thus the unresolved cases split into unbounded non-descenders with at most critical asymptotic valuation mean and nontrivial cycles. The abstract schedule `A_j=floor(j log_2 3)` also meets the critical cap, so the exact transition law is still needed.

The unbounded case has two distinct mean regimes. Suppose a non-descending orbit is strictly subcritical, so `limsup A_j/j<c`; choose `δ>0` with `A_j≤(c−δ)j` for all sufficiently large `j`. The exact identity then yields

`log_2(x_j/n)=jc−A_j+Σ_{i<j}ε_i ≥ δj`,  `ε_i=log_2(1+1/(3x_i))`.

Thus `x_j≥n2^{δj}` eventually. Since `ε_i≤1/(3x_i ln 2)`, the correction series `Σ ε_i` converges, and more precisely

`log_2(x_j/n)=jc−A_j+R_∞+o(1)`,  `R_∞=Σ_{i=0}^{∞}ε_i<∞`.

Consequently a strict subcritical non-descender would have exponential growth, with lower rate at least `δ` and upper rate at most `c−1` because `A_j≥j`. The remaining unbounded boundary case has `limsup A_j/j=c`; its correction sum need not converge. A pointwise proof must address both regimes through the transition law.

## Exact length of a run with valuation one

Let `x_0=n` be odd, set `x_{i+1}=S(x_i)`, and write `a_{i+1}=v_2(3x_i+1)`. For every integer `r ≥ 0`,

`a_1 = ··· = a_r = 1  ⇔  v_2(n+1) ≥ r+1`.

Thus the initial run of valuation-one steps has exactly `v_2(n+1)-1` terms, followed by a step whose valuation is at least 2.

**Proof.** Whenever `a_{i+1}=1`,

`x_{i+1}+1 = (3x_i+1)/2 + 1 = 3(x_i+1)/2`.

So if the first `r` valuations are 1, iteration gives `x_r+1=3^r(n+1)/2^r`. Since `x_r` is odd, `x_r+1` is even; because `3^r` is odd, this forces `v_2(n+1)≥r+1`. Conversely, suppose `v_2(n+1)≥r+1`. Inductively, before each of the first `r` steps, `v_2(x_i+1)=v_2(n+1)-i≥2`. Hence `3x_i+1=3(x_i+1)-2` is divisible by 2 but not by 4, so `a_{i+1}=1` and `v_2(x_{i+1}+1)=v_2(x_i+1)-1`. After those `r` steps the valuation of `x_r+1` is at least 1. Taking `r=v_2(n+1)-1`, it is exactly 1, so `x_r≡1 (mod 4)` and the next `3x_r+1` is divisible by 4. The run therefore ends exactly there.

**Corollary.** Every infinite Syracuse sequence has infinitely many steps with `a_i≥2`: otherwise all sufficiently late valuations would equal 1, contradicting the finite run-length formula at the odd value where that tail begins. This only proves infinitude, not positive density or a lower bound on cumulative valuations. The global descent problem remains open; a useful next step is to control the lengths of these runs together with the sizes of the valuations that end them.

## Exact return-block formula

Take an odd value `x` with `a=v_2(3x+1)≥2`, and let `y=S(x)`. Set `t=v_2(y+1)` and `u=(y+1)/2^t`, so `u` is odd. The run-length lemma says that the next `t-1` odd steps from `y` all have valuation 1. Let `z` be the value after those `t-1` steps. Then

`z+1 = 3^{t-1}(y+1)/2^{t-1} = 2·3^{t-1}u`,

and substituting `x=(2^a y-1)/3` and `y=2^t u-1` gives the exact block difference

`3(z-x) = 2^a - 2 - u(2^{a+t} - 2·3^t)`.

Consequently this block strictly descends from its own starting value `x` exactly when

`u(2^{a+t} - 2·3^t) > 2^a - 2`.

This gives a critical threshold for possible block descent. Since

`2^{a+t} - 2·3^t = 2^{t+1}(2^{a-1} - (3/2)^t)`,

if `(a+t-1)/t ≤ log_2 3`, then the parenthesized term is nonpositive, so `z-x>0`: the block necessarily expands. Thus a block can strictly descend only if its mean valuation `(a+t-1)/t` is greater than `log_2 3`. This condition is necessary, not sufficient, because the exact descent test still depends on `u`.

A sufficient condition that guarantees descent for every possible odd `u≥1` is

`2^a(2^t - 1) > 2·3^t - 2`.

Writing the block mean as `q=(a+t-1)/t`, this sufficient condition is equivalently

`q > λ_t := 1 + (1/t) log_2((3^t-1)/(2^t-1))`.

The threshold satisfies

`λ_t = log_2 3 + η_t`,  where  `η_t=(1/t)log_2((1-3^{-t})/(1-2^{-t})) > 0`,

and `η_t → 0` as `t → ∞`. In fact, the threshold decreases strictly with `t`. To see this, put `R_t=(1-3^{-t})/(1-2^{-t})`, `x=2^{-t}`, and `y=3^{-t}`. Then

`R_t - R_{t+1} = (3x - 4y + xy)/(6(1-x)(1-x/2)) > 0`,

because `x/y=(3/2)^t ≥ 3/2`, so `3x-4y>0`. Also `R_t>1` and `R_t→1`. Thus `η_t=(log_2 R_t)/t` is positive, strictly decreasing, and tends to zero; consequently `λ_t` decreases to `log_2 3`.

As a uniform corollary, for every fixed `ε>0` there is a length `T` such that every block with `t≥T` and `q≥log_2 3+ε` contracts, regardless of `u`. This does not show that every orbit supplies those means; controlling the actual coupled block parameters remains the global problem.

More quantitatively, define

`δ_t=(2^{-t}-3^{-t})/(1-2^{-t})`,

so `η_t=(1/t)log_2(1+δ_t)`. Since `0<δ_t<2^{1-t}`, the elementary inequality `log_2(1+δ)≤δ/ln 2` gives

`0 < η_t < 2^{1-t}/(t ln 2)`.

Thus the guaranteed-descent threshold gap is `O(2^{-t}/t)`. Means at most `log_2 3` force expansion; means above `λ_t` guarantee descent regardless of `u`; between these thresholds the coarse test is inconclusive, and the exact `u`-dependent test or its modulo-3 refinement is needed.

Because `R_t≤R_1=4/3<2`, the width of this inconclusive band, measured in the integer parameter `a-1`, is `log_2 R_t<1`. Put `c=log_2(3/2)`. For a fixed block length `t`, the mean tests therefore give the following integer classification:

- If `a≤floor(tc)+1`, then `q≤log_2 3`, so the block expands.
- If `a≥floor(tc)+3`, then `q>λ_t`, so the block contracts for every `u`.
- Only the single intermediate integer `a=floor(tc)+2` can fall into the inconclusive band; whether it does depends on the fractional part of `tc`. If it does, the exact `u`-dependent criterion decides that block.

This isolates the local ambiguity to at most one valuation level per block length. It still gives no bound on how often the orbit chooses that level or on the combined drift of successive blocks.

The possible candidate can be tested without logarithms. Set `h=floor(t log_2(3/2))`, `f=t log_2(3/2)-h`, and `a=h+2`. Then

`q-log_2 3 = (1-f)/t`,  while  `λ_t-log_2 3 = (log_2 R_t)/t`.

So the candidate is already guaranteed to contract if `1-f>log_2 R_t`. Otherwise use the exact block criterion: with `D=2^{h+t+1}-3^t>0` (since `h+1>t log_2(3/2)`), it contracts exactly when

`uD > 2^{h+1}-1`.

This is a positive-integer comparison for the sole possible local gap. The orbit-wide problem still requires controlling these `u` values together with the adjacent block transitions.

There is an exact consequence for the next block whenever this candidate fails to contract. Index this candidate as block `k`, so `a_k=h+2`, `t_k=t`, and `u_k=u`. Put `M=2^{h+1}` and suppose `uD≤M-1`. Then `r=Du+1≤M`, and the block endpoint formula gives

`3(x_{k+1}-x_k)=2(M-1-uD)`.

Thus strict inequality `uD<M-1` means this block expands. The transition law also gives

`3^t u-1 = 2^t M u-r`.

Because `r` is even, `r≤2^{h+1}`, and `v_2(2^t M u)=t+h+1>v_2(r)`, taking the 2-adic valuation yields the exact next-valuation relation

`a_{k+1}-1=v_2(Du+1)≤h+1`.

So a genuinely expanding block at the only possible gap forces `a_{k+1}≤h+1=a_k-1`. In the equality case `uD=M-1`, the block returns to its starting point, `S^t(x_k)=x_k`, and gives a periodic orbit with period dividing `t`. This constrains a local transition but does not rule out an arbitrary non-descending orbit.

For a strict expansion, this next-block restriction has a two-case refinement. Put `b=v_2(Du+1)=a_{k+1}-1`, `s=(Du+1)/2^b` (odd), and `ℓ=t+h+1-b`. Then

`S(x_{k+1})=2^ℓu-s`.

Since `Du+1<M`, we have `b≤h` and `ℓ≥t+1`. If `s>1`, then

`t_{k+1}=v_2(s-1)≤h-b`,

because `s<2^{ℓ-t}` makes `v_2(s-1)≤ℓ-t-1<ℓ`, so the smaller 2-adic valuation in `S(x_{k+1})+1=2^ℓu-(s-1)` is `v_2(s-1)`. Therefore `t_{k+1}≤h-b<t` and `a_{k+1}+t_{k+1}≤h+1=a_k-1`. If `s=1`, then `t_{k+1}=ℓ≥t+1` and `u_{k+1}=u`; moreover

`q_{k+1}=1+b/ℓ < 1+log_2(3/2)=log_2 3`,

since `b≤h≤t log_2(3/2)<ℓ log_2(3/2)`. The next block is then also forced to expand. Thus a strictly expanding exceptional block either leads to a shorter next run and smaller parameter sum, or to a longer next run followed by another forced expansion. This dichotomy is exact but still leaves the long-term orbit behavior open.

Let `H_k=a_k+t_k`. Across a strict expanding exceptional block, `H_{k+1}=H_k` when `s=1`; when `s>1`, `H_{k+1}≤a_k-1=H_k-(t_k+1)`. The `s=1` branch puts the next block below the critical mean, so it ends any consecutive chain of exceptional-gap expansions.

For a chain of `L` such blocks beginning at block `k`, every transition within the chain must therefore have `s>1`. Hence `t` strictly decreases at each link, and `H` drops by at least `t+1`. If the chain blocks are indexed `i=1,…,L`, then `t_i≥L-i+1`; summing the drops gives

`H_L≤H_1-Σ_{i=1}^{L-1}(t_i+1)≤H_1-(L^2+3L-4)/2`.

Since every block has `H_L≥3`, this is equivalent to `(L+1)(L+2)≤2H_1`, or

`L≤floor((sqrt(8H_1+1)-3)/2)`.

Here `H_1` is the value at the chain's first block. This bounds only consecutive expansions of this exceptional type; it does not rule out other orbit behavior or prove the full conjecture.

There is also a uniform cap on the total growth across such a chain. For block `i`, put `c=log_2(3/2)`, `h_i=floor(t_i c)`, and `f_i=t_i c-h_i`. At the exceptional valuation `a_i=h_i+2`, the exact logarithmic drift is

`d_i=t_i(log_2 3-q_i)+ε_i=ε_i-(1-f_i)`.

Since the block expands, `d_i>0`; hence `d_i<ε_i<β_{t_i}`, where `β_t=-log_2(1-2^{-t})`. The chain's `t_i` are distinct positive integers, so

`Σ d_i < Σ_{t=1}^∞ β_t = -log_2 P`,  where  `P=∏_{t=1}^∞(1-2^{-t})`.

For `0≤x_i≤1`, `∏(1-x_i)≥1-Σx_i`. Applying this to the tail gives `∏_{t=3}^∞(1-2^{-t})≥1-Σ_{t=3}^∞2^{-t}=3/4`, and hence `P≥(1/2)(3/4)(3/4)=9/32`. Therefore `Σd_i≤log_2(32/9)`, and telescoping gives

`(x_end+1)/(x_start+1)<32/9`.

Thus a consecutive run of these exceptional expansions can increase its endpoint by less than a factor `32/9`, independently of its starting value. Other block types remain uncontrolled.

Integrality sharpens this local test. From `3x=2^{a+t}u-2^a-1`, reduction modulo 3 gives `u≡0 (mod 3)` when `a` is odd, and `u≡(-1)^{t+1} (mod 3)` when `a` is even. Since `u` is positive and odd, its corresponding lower bound is `u≥3` for odd `a`, `u≥1` for even `a` and odd `t`, and `u≥5` for even `a` and even `t`. Thus, writing `C=2^{a+t}-2·3^t`, a sharper sufficient criterion is `C>0` and `u_min C>2^a-2`, with `u_min` chosen from those three cases.

This is only a local block criterion. For example, `9 → 7 → 11 → 17` is a block with `a=2`, `t=3`, and it grows from 9 to 17.

The block parameters also obey an exact transition law. Index successive blocks by `k`, with block start `x_k`, valuation `a_k`, post-step value `y_k=S(x_k)=2^{t_k}u_k-1`, and next block start `x_{k+1}=2·3^{t_k-1}u_k-1`. Then

`a_{k+1}-1 = v_2(3^{t_k}u_k-1)`,

and, on writing `y_{k+1}=2^{t_{k+1}}u_{k+1}-1`,

`3^{t_k}u_k-1 = 2^{a_{k+1}-1}(2^{t_{k+1}}u_{k+1}-1)`.

Indeed, `3x_{k+1}+1=2(3^{t_k}u_k-1)`, and dividing by its exact power of 2 gives `y_{k+1}`. Thus adjacent block parameters cannot be chosen independently. This is an exact recurrence, but it does not yet bound their long-run averages.

The recurrence also carries information modulo a high power of 3. Put `b_k=a_{k+1}−1`. Adding `2^{b_k}` to both sides gives

`2^{b_k+t_{k+1}}u_{k+1}=3^{t_k}u_k+2^{b_k}−1`,

so, modulo `3^{t_k}`,

`u_{k+1} ≡ 2^{−(b_k+t_{k+1})}(2^{b_k}−1) (mod 3^{t_k})`.

The inverse power of 2 is taken modulo `3^{t_k}`. In particular,

`min(v_3(u_{k+1}),t_k) = 0` if `b_k` is odd, and `min(v_3(u_{k+1}),t_k)=min(t_k,1+v_3(b_k))` if `b_k` is even.

For even `b_k`, this follows from `v_3(2^{b_k}−1)=1+v_3(b_k)` by LTE; for odd `b_k`, `2^{b_k}−1` is a 3-adic unit. Thus when `a_{k+1}` is odd, the next block parameter satisfies

`u_{k+1} ≥ 3^{min(t_k,1+v_3(a_{k+1}−1))}`.

Inserting this into the exact local contraction test gives a transition-aware sufficient condition: if `a_{k+1}` is odd, `C_{k+1}=2^{a_{k+1}+t_{k+1}}−2·3^{t_{k+1}}>0`, and

`3^{min(t_k,1+v_3(a_{k+1}−1))} C_{k+1} > 2^{a_{k+1}}−2`,

then block `k+1` contracts. This strengthens the earlier modulo-3 lower bound on `u`, but does not yet force enough contractions along every orbit.

Taking logarithms gives a telescoping form of this transition. Put `b_k=a_{k+1}−1` and

`δ_k=log_2(1+(2^{b_k}−1)/(3^{t_k}u_k))`.

Adding `2^{b_k}` to the transition equation yields `2^{b_k+t_{k+1}}u_{k+1}=3^{t_k}u_k+2^{b_k}−1`, and hence

`b_k−t_k log_2(3/2) = t_k−t_{k+1}+log_2(u_k/u_{k+1})+δ_k`.

Here `0<δ_k<1`, because `b_k≥1` and `2^{b_k}≤3^{t_k}u_k−1`. Summing over `k=1,…,m` cancels the intermediate run and `u` terms:

`Σ_{k=1}^m(a_{k+1}−1) = log_2(3/2) Σ_{k=1}^m t_k + t_1−t_{m+1}+log_2(u_1/u_{m+1})+Σ_{k=1}^m δ_k`.

Using `x_{k+1}+1=2·3^{t_k−1}u_k`, this correction is exactly the existing next-block drift term:

`δ_k = log_2(1+(2^{a_{k+1}}−2)/(3(x_{k+1}+1))) = ε_{k+1}`.

Thus the telescope expresses the known block-drift correction in transition coordinates. Its endpoint terms can grow, so this re-expression alone does not force descent or provide an independent bound.

## Exact logarithmic drift across blocks

For block `k`, define

`α_k=(1-2^{1-a_k})/(2^{t_k}u_k)` and `ε_k=log_2(1/(1-α_k))`.

Using `3x_k+1=2^{a_k}y_k`, the same correction has the state-based form

`ε_k=log_2(1+(2^{a_k}-2)/(3(x_k+1)))`.

The endpoint formulas give

`(x_{k+1}+1)/(x_k+1) = 2^{t_k(log_2 3-q_k)}/(1-α_k)`,

where `q_k=(a_k+t_k-1)/t_k`. Hence, after `m` complete blocks,

`log_2((x_{m+1}+1)/(x_1+1)) = Σ_{k=1}^m (t_k(log_2 3-q_k)+ε_k)`.

In particular, a single block contracts exactly when its mean valuation exceeds its state-dependent threshold:

`q_k > log_2 3 + ε_k/t_k = log_2 3 + (1/t_k)log_2(1+(2^{a_k}-2)/(3(x_k+1)))`.

This is an exact local test; the unresolved issue is to control the sum of these block drifts along every orbit.

Since `Σ t_k q_k=Σ(a_k+t_k-1)`, and after the initial run of `r` valuation-one steps the first block start satisfies `x_1+1=(3/2)^r(n+1)`, this is equivalently

`Σ_{k=1}^m (a_k-1) = j log_2(3/2) + Σ_{k=1}^m ε_k - log_2((x_{m+1}+1)/(n+1))`,

where `j=r+Σ t_k` is the total number of odd steps at that block boundary. This identity is exact. Since `x_1+1=(3/2)^r(n+1)`,

`Σ_{k=1}^m (t_k(log_2 3-q_k)+ε_k) < -r log_2(3/2)`

is exactly the condition that this block-boundary value `x_{m+1}` lies below `n`. Finding such a boundary would prove descent; it is sufficient but not necessary, since an intermediate iterate may fall below `n` before the block ends.

The exact 3-adic residue gives a stronger lower bound on `u_k` than its valuation alone. For `k≥2`, put `M_k=3^{t_{k-1}}` and let `R_k∈{0,…,M_k−1}` be the unique residue satisfying

`R_k ≡ 2^{−(a_k−1+t_k)}(2^{a_k−1}−1) (mod M_k)`.

The transition congruence gives `u_k≡R_k (mod M_k)`. Since `u_k` is positive odd and `M_k` is odd, define `U_k^*=R_k` when `R_k` is odd, and `U_k^*=R_k+M_k` when `R_k` is even. Then `u_k≥U_k^*`. For the first block, the modulo-3 condition gives `U_1^*=3` if `a_1` is odd, `U_1^*=1` if `a_1` is even and `t_1` is odd, and `U_1^*=5` if both are even.

For example, the `9→17` return-block transition has `(a_1,t_1,u_1)=(2,3,1)` and `(a_2,t_2)=(2,1)`. It gives `u_2≡7 (mod 27)`, so positivity and oddness force `u_2≥7` (in fact `u_2=7`).

Since `ε_k=−log_2(1−(1−2^{1−a_k})/(2^{t_k}u_k))`, set `Γ_k^*=−log_2(1−1/(2^{t_k}U_k^*))`; then `ε_k<Γ_k^*`. Therefore the residue-sensitive finite-prefix condition

`Σ_{k=1}^m (t_k(log_2 3-q_k)+Γ_k^*) < -r log_2(3/2)`

also guarantees `x_{m+1}<n`. This can sharpen a descent certificate when the transition residue forces a large least positive odd representative; it still does not show that such a prefix must occur on every orbit.

### Exact contraction threshold for the residue carry

For the transition from block `k` to block `k+1`, write `u_{k+1}=U_{k+1}^*+2M_k Q_k`, where `M_k=3^{t_k}` and `Q_k` is a nonnegative integer. Let

`B_{k+1}=2^{a_{k+1}}−2` and `C_{k+1}=2^{a_{k+1}+t_{k+1}}−2·3^{t_{k+1}}`.

The exact block endpoint difference becomes

`3(x_{k+2}−x_{k+1}) = B_{k+1}−C_{k+1}U_{k+1}^*−2M_k C_{k+1}Q_k`.

If `C_{k+1}≤0`, the block expands. If `C_{k+1}>0`, it contracts exactly when `Q_k≥Q_k^{min}`, where

`Q_k^{min}=max(0, floor((B_{k+1}−C_{k+1}U_{k+1}^*)/(2M_k C_{k+1}))+1)`.

Thus each positive-`C` block has an exact carry threshold separating contraction from non-contraction. The orbit-wide problem now includes controlling how often its transition carries cross these thresholds; the residue identity alone does not do that.

The same carry also gives a lower bound on the preceding odd parameter. Substituting `u_{k+1}=U_{k+1}^*+2M_kQ_k` into the transition equation yields

`u_k = W_k+2^{b_k+t_{k+1}+1}Q_k`,

where

`W_k=(2^{b_k+t_{k+1}}U_{k+1}^*−2^{b_k}+1)/3^{t_k}`.

The residue defining `U_{k+1}^*` ensures that `W_k` is an integer; its numerator is `2^{b_k}(2^{t_{k+1}}U_{k+1}^*−1)+1`, so `W_k` is positive and odd. Hence `u_k≥W_k`, and the current block's correction can use the stronger lower bound `V_k=max(U_k^*,W_k)`, giving `ε_k<−log_2(1−1/(2^{t_k}V_k))`. Equivalently, the next-block contraction threshold `Q_k≥Q_k^{min}` can be read as the incoming-parameter threshold `u_k≥W_k+2^{b_k+t_{k+1}+1}Q_k^{min}` when `C_{k+1}>0`. This is a one-step look-ahead refinement; the orbit-wide carry frequency remains uncontrolled.

### Exact residue class from both neighboring transitions

For `k≥2`, the transition into block `k` fixes `u_k` modulo `M_k=3^{t_{k-1}}`; let `U_k^*` be its least positive odd representative. The transition out of block `k` fixes its exact 2-adic valuation: with `b_k=a_{k+1}−1`,

`v_2(3^{t_k}u_k−1)=b_k`.

Let `s_k` be the unique odd integer in `[1,2^{b_k}−1]` satisfying `3^{t_k}s_k≡1 (mod 2^{b_k})`. There is a unique `q_k` in `[0,2^{b_k−1}−1]` satisfying

`M_k q_k ≡ (s_k−U_k^*)/2 (mod 2^{b_k−1})`,

with the modulus-one case `b_k=1` interpreted as `q_k=0`. Then `L_k=U_k^*+2M_kq_k` is the least positive representative satisfying both neighboring congruences. In particular, every positive odd `u_k` satisfying them has the form

`u_k=L_k+2^{b_k}M_k h`,  `h≥0`.

Put `r_k=(3^{t_k}L_k−1)/2^{b_k}`. The exact valuation condition requires `r_k+h` to be odd, so if `δ_k=0` for odd `r_k` and `δ_k=1` for even `r_k`, every actual transition parameter lies in the more restrictive progression

`u_k=L_k+2^{b_k}M_k(δ_k+2j_k)`,  `j_k≥0`.

Thus `u_k≥L_k+2^{b_k}M_kδ_k`, a lower bound that combines the incoming 3-adic residue with the outgoing exact 2-adic valuation. Taking the maximum of this bound, `U_k^*`, and the successor-derived `W_k` further sharpens the correction estimate for `ε_k`. This is a local adjacent-transition constraint; it does not yet control the frequency or cumulative effect of carries along an entire orbit.

### Contraction threshold on the coupled progression

Write the exact progression as `u_k=Λ_k+P_kj_k`, where `Λ_k=L_k+2^{b_k}M_kδ_k` and `P_k=2^{b_k+1}M_k`. The endpoint difference is `3(x_{k+1}−x_k)=B_k−C_ku_k`, with `B_k=2^{a_k}−2` and `C_k=2^{a_k+t_k}−2·3^{t_k}`. If `C_k≤0`, the block strictly expands. If `C_k>0`, put `H_k=floor(B_k/C_k)`. Then the block strictly contracts exactly when

`j_k≥J_k^{min}:=max(0, floor((H_k−Λ_k)/P_k)+1)`.

Consequently, if `Λ_k>H_k` every parameter in this coupled residue class contracts; otherwise only the finite index range `0≤j_k<J_k^{min}` can be non-contracting. This is an exact local test using both neighboring transitions. It does not show that non-contracting blocks are too sparse or that their total drift is bounded along a full orbit.

### The coupled index determines the next run length

For the same progression, define

`Θ_k=(3^{t_k}Λ_k+2^{b_k}−1)/2^{b_k+1}` and `c_k=3^{t_k}M_k`.

The parity choice `δ_k` makes `Θ_k` an integer: using `r_k=(3^{t_k}L_k−1)/2^{b_k}`, it equals `(r_k+3^{t_k}M_kδ_k+1)/2`, whose numerator is even. Substituting `u_k=Λ_k+2^{b_k+1}M_kj_k` into the transition equation gives

`2^{t_{k+1}−1}u_{k+1}=Θ_k+c_kj_k`,

so `t_{k+1}=1+v_2(Θ_k+c_kj_k)`. Since `c_k` is odd, for every `r≥0` the condition `t_{k+1}≥r+1` selects exactly one residue class of `j_k` modulo `2^r`; exact equality `t_{k+1}=r+1` selects one class modulo `2^{r+1}`. Therefore, among the `J_k^{min}` candidate indices for a non-contracting block when `C_k>0`, at most `ceil(J_k^{min}/2^r)` can produce `t_{k+1}≥r+1`. This is a deterministic local branch-counting statement. It does not bound which index an actual orbit follows or prove a global descent.

### Finite block itineraries form exact 2-adic cylinders

Prescribe a finite future word of exact pairs `(s_i,d_i)=(t_{k+i},b_{k+i})`, `1≤i≤m`, where each run length `s_i≥1` and each following valuation `d_i=b_{k+i}≥1`. For the first pair, there is a unique `ρ (mod 2^{s_1})` satisfying `Θ_k+c_kρ≡2^{s_1−1} (mod 2^{s_1})`, since `c_k` is odd. Writing `j_k=ρ+2^{s_1}q` fixes `t_{k+1}=s_1` and gives `u_{k+1}=u_0+2c_kq` with `u_0` positive odd. The condition `b_{k+1}=d_1` is then

`(3^{s_1}u_0−1)/2 + 3^{s_1}c_kq ≡ 2^{d_1−1} (mod 2^{d_1})`.

Its odd coefficient selects one residue class of `q (mod 2^{d_1})`; hence the pair selects one class of `j_k (mod 2^{s_1+d_1})`.

After fixing this pair, let `σ_1` be the least representative of the resulting class and write `j_k=σ_1+2^{s_1+d_1}ℓ`. The transition formula makes `u_{k+1}` affine in `ℓ` with increment `2^{d_1+1}3^{t_k}M_k`, where `M_k=3^{t_{k-1}}`. Since the next incoming modulus is `M_{k+1}=3^{t_k}`, its coupled index is affine in `ℓ` with odd coefficient `M_k`. Repeating the same argument for each prescribed pair therefore gives exactly one class of initial `j_k` modulo

`2^{N}`,  `N=Σ_{i=1}^m(s_i+d_i)`.

Thus any interval of `J` consecutive initial indices contains at most `ceil(J/2^N)` representatives of a specified finite itinerary. This is exact local 2-adic counting, not an estimate of which indices an actual orbit visits; it does not establish global descent.

More precisely, because the compatible indices form one class modulo `2^N`, among any `J` consecutive indices the count is either `floor(J/2^N)` or `ceil(J/2^N)`. Its discrepancy from `J/2^N` is less than one, so the natural density in this parameter family is exactly `2^{-N}`. This is density across compatible starting parameters; it gives no time-frequency statement for a single Syracuse orbit. Bridging that distinction is the next obstacle for any argument that tries to turn local 2-adic coding into average drift control.

### Density-one descent checkpoint (classical)

For a fixed length `m`, every exact valuation word `(a_1,…,a_m)` with `A_m=Σa_i` occurs on exactly one odd residue class modulo `2^{A_m+1}`. Inductively, after fixing a prefix with total `A`, varying its starting value by `2^{A+1}q` varies the next odd Syracuse state by `2·3^j q`; this runs through all odd residues modulo the next valuation modulus and the exact next valuation selects one class. Consequently, in natural density among odd starting values, the `a_i` are independent geometric variables with `P(a_i=s)=2^{-s}`. Thus `E[A_m]=2m` and `Var(A_m)=2m`.

The exact iterate formula gives `x_m=(3^m n+c_m)/2^{A_m}`, with `c_m=Σ_{i=0}^{m−1}3^{m−1−i}2^{A_i}`. Since `A_i≤A_m`,

`c_m≤2^{A_m}(3^m−1)/2`.

If `A_m≥9m/5` and `n≥3^m`, then

`x_m/n≤(3/2^{9/5})^m+(3^m−1)/(2n)<1`

for all sufficiently large `m`, so the orbit has a smaller odd iterate by time `m`. Chebyshev's inequality bounds the natural density of the exceptional valuation words by

`P(A_m<9m/5)≤Var(A_m)/(m/5)^2=50/m`.

For each fixed sufficiently large `m`, the finite set `n<3^m` has density zero. Hence the upper density of odd starts with stopping time greater than `m` is at most `50/m`; letting `m→∞` proves that the set of odd starts that never fall below their start has density zero. Even starts immediately decrease under Collatz, so finite stopping time has natural density one among all positive integers. This recovers the classical Terras result by a short valuation-distribution argument; it does **not** eliminate the exceptional zero-density set and therefore does not prove Collatz. See [Terras, “A stopping time problem on the positive integers” (1976)](https://matwbn.icm.edu.pl/ksiazki/aa/aa30/aa3034.pdf).

The same argument gives an exponential tail. Since `2^{8/5}>3`, if `A_m≥8m/5` and `n≥3^m`, then `x_m/n≤(3/2^{8/5})^m+1/2<1` for all sufficiently large `m`. For the geometric valuation law, Chernoff's inequality with `θ=ln(4/3)` gives

`P(A_m<8m/5)≤ρ^m`,  `ρ=(3/5)(4/3)^{8/5}<1`.

Indeed, `ρ<1` is equivalent to `4^8<5^5·3^3`. The finitely many starts below `3^m` have zero natural density for each fixed `m`, so the upper density of odd starts whose first smaller Syracuse iterate occurs after `m` is at most `ρ^m` for sufficiently large `m`. This is a quantitative density statement only: it still allows an individual exceptional orbit with infinite stopping time.

The same cutoff yields a power-saving count up to a height bound. Let `E(X)` count odd `n≤X` that have not fallen below their start by `m=floor(log_3 n)` Syracuse steps. For `3^m≤n<3^{m+1}`, every such `n` must have `A_m<8m/5`. Each valuation word of total `s` occupies one odd class modulo `2^{s+1}`, so it contributes at most `3^m2^{-s}+1` values in this interval. The weighted sum over these words is at most `ρ^m`; their number is at most

`κ^m`,  `κ=(8/3)^{8/5}/(5/3)<3`,

by multiplying each word by `(8/3)^{8m/5-s}` and summing the resulting geometric series. Thus the interval contributes at most `(3ρ)^m+κ^m`. With `K=max(3ρ,κ)<3` and `β=log_3 K<1`, summing over `m≤log_3 X` gives

`E(X)=O(X^β)`,  `β=log_3 K≈0.9635`.

In particular the infinite-stopping-time set has a power-saving upper bound in counting function. This still allows infinitely many exceptions; the estimate only shows that any such set is sparse.

The cutoff can be optimized. Put `c=log_2 3` and choose any fixed `α` with `c<α<2`. For all sufficiently large `m`, `A_m≥αm` and `n≥3^m` force descent by step `m`, since `3/2^α<1`. Define

`κ(α)=α^α/(α−1)^{α−1}`.

The number of positive integer valuation words with sum below `αm` is at most `κ(α)^m`: multiply each word of total `s` by `(α/(α−1))^{αm−s}` and sum the geometric series. Chernoff with `e^θ=α/(2(α−1))` gives `P(A_m<αm)≤(κ(α)/2^α)^m`. Since `2^α>3`, the weighted residue-class contribution is smaller than the word-count error, and the interval `[3^m,3^{m+1})` contributes at most `2κ(α)^m` candidates. Therefore, for each fixed `α>c`, `E(X)=O(X^{log_3κ(α)})`.

Since `d(ln κ)/dα=ln(α/(α−1))>0`, `κ` increases with `α`. Taking `α` down toward `c` shows that for every `β>β_0`,

`E(X)=O_β(X^β)`,  `β_0=log_3(κ(c))≈0.94996`.

This improves the fixed `α=8/5` exponent `0.9635`, but the exponent remains positive; the bound still permits infinitely many non-descending starts.

The additive correction gives an exact endpoint bound. From `c_m≤2^{A_m}(3^m−1)/2`,

`x_m/n≤3^m/2^{A_m}+(3^m−1)/(2n)`.

Thus, for `n≥3^m`, the sharper condition `A_m≥mc+1` already forces `x_m<n`: the two terms are at most `1/2` and strictly less than `1/2`, respectively. Set `α_m=c+1/m`. The low-sum words have `A_m<α_m m`; for `m≥3`, the same residue-class counting bounds their contribution on `[3^m,3^{m+1})` by `3^mκ(α_m)^m/2^{α_m m}+κ(α_m)^m=(3/2)κ(α_m)^m`.

Since `d(ln κ)/dα=ln(α/(α−1))` decreases with `α`,

`κ(α_m)^m≤(c/(c−1))κ(c)^m`.

Summing the interval bounds attains the endpoint exponent itself:

`E(X)=O(X^{β_0})`,  `β_0=log_3(κ(c))≈0.94996`.

This remains a sublinear count, not a proof that the exceptional set is empty.

The endpoint count admits a logarithmic refinement without changing the descent criterion. For `A_m<mc+1`, let `N_m=floor(mc+1)=cm+O(1)`. The number of positive valuation words is exactly

`Σ_{s=m}^{N_m} binom(s−1,m−1)=binom(N_m,m)=O(κ(c)^m/√m)`.

For the weighted residue sum, put `T_s=binom(s−1,m−1)2^{−s}`. Its successive ratio is

`T_s/T_{s−1}=(s−1)/(2(s−m))`.

Because `N_m/m→c<2`, these terms increase geometrically with successive ratios uniformly greater than 1 through `s=N_m`; hence `ΣT_s=O(T_{N_m})=O((κ(c)/3)^m/√m)`. Each interval therefore contributes `O(κ(c)^m/√m)` candidates. Summing the geometric sequence of interval bounds gives

`E(X)=O(X^{β_0}/√(log X))`,  `β_0=log_3(κ(c))≈0.94996`.

The logarithmic saving still allows an infinite exceptional set, so the pointwise obstruction remains open.

On an orbit that never falls below `n`, its final logarithm is nonnegative, so

`Σ(a_k-1) ≤ j log_2(3/2) + Σ ε_k`.

Also `0<α_k<2^{-t_k}`, so `0<ε_k<β_{t_k}:=-log_2(1-2^{-t_k})`. The resulting block-length-sensitive cap is

`Σ(a_k-1) < j log_2(3/2) + Σ β_{t_k}`.

This is another necessary bound for a hypothetical non-descending orbit, not the missing lower bound.

There is also an exact cumulative bookkeeping identity. Let `r` be the initial number of valuation-one steps before the first valuation at least 2, and let `(a_k,t_k)` describe each following complete block. After `m` blocks,

`j = r + Σ_{k=1}^m t_k`,  `A_j = r + Σ_{k=1}^m (a_k+t_k-1)`,

so `A_j-j = Σ_{k=1}^m (a_k-1)`. If the orbit never falls below its starting value `n`, the earlier logarithmic bound therefore forces

`Σ_{k=1}^m (a_k-1) ≤ (r + Σ_{k=1}^m t_k) log_2((3+1/n)/2)`

at every such block boundary. This is a necessary upper bound for a hypothetical non-descending orbit. Proving a contradictory lower bound from the dynamics, while allowing expanding blocks such as the one from 9, is still open.

### Frequency constraints on a hypothetical non-descending orbit

Fix an odd `n>1` and suppose no odd Syracuse iterate falls below `n`. Put

`c_n=log_2((3+1/n)/2)` and `N_s(j)=#{1≤i≤j : a_i≥s}` for integers `s≥2`.

The exact iterate inequality gives `Σ_{i=1}^j(a_i−1)≤j c_n`. Each index counted by `N_s(j)` contributes at least `s−1` to this sum, so for every `j` and `s≥2`,

`N_s(j) ≤ floor(j c_n/(s−1))`.

In particular, if `Z_j=#{1≤i≤j:a_i=1}`, then

`Z_j/j ≥ 1−c_n ≥ log_2(6/5)`,

because `n≥3` implies `c_n≤log_2(5/3)`. Thus any orbit that fails the descent target must have valuation-one steps on a positive lower density of its odd steps, while valuations at least `s` have upper density at most `c_n/(s−1)`.

There is an equivalent constraint on complete return blocks. If `r` is the initial run of valuation-one steps and `j_m=r+Σ_{k=1}^m t_k` is the endpoint after `m` blocks, then the `m` block-start valuations are all at least 2, so `m≤j_m c_n`. Consequently

`(1/m)Σ_{k=1}^m t_k ≥ 1/c_n−r/m`,

and the lower limit of the mean block length is at least `1/c_n`. This is a necessary frequency condition, not a contradiction: the transition law has not yet supplied an incompatible upper bound on these run lengths.

The logarithmic transition identity sharpens this necessary condition. Let `c=log_2(3/2)`, `T_m=Σ_{k=1}^m t_k`, and `Δ_m=Σ_{k=1}^m δ_k`. Applying the non-descent cap at the endpoint after `m+1` blocks and substituting the telescoped transition identity gives

`(1+c_n)t_{m+1}+log_2 u_{m+1} ≥ Δ_m−(c_n−c)T_m+(a_1−1)+t_1+log_2 u_1−c_n r`,

where `c_n−c=log_2(1+1/(3n))`. Thus a descent-failing orbit must either accumulate only a small transition correction relative to total block length, or let its terminal run/odd parameter grow enough to absorb the positive correction. Bounding these two quantities from the recurrence is the next open step.

## Cycle-exclusion reduction

Let `S(x)=(3x+1)/2^{v₂(3x+1)}` be the Syracuse map on positive odd integers. The Collatz conjecture is equivalent to the absence of nontrivial cycles of `S`.

**Proof.** If every odd `n>1` has an iterate below `n`, strong induction proves that every odd integer reaches `1`: a smaller odd iterate reaches `1` by induction, so the original orbit does too. Even starting values reduce to an odd value by removing powers of two. Thus the descent statement implies Collatz, and Collatz plainly implies descent and excludes nontrivial cycles.

For the other direction, suppose descent fails for at least one odd integer greater than `1`, and let `n` be the least such integer. Every odd iterate `x_j=S^j(n)` is at least `n`. For any odd `y>n`, minimality of `n` says descent does hold from `y`, so some iterate of `y` is strictly smaller than `y`. Starting at `x_1`, repeatedly take the first later orbit value smaller than the current record. Whenever the record is greater than `n`, such a later value exists; all records remain at least `n`. They therefore cannot decrease forever, so one record equals `n`. The orbit returns to `n` and is periodic. The only odd fixed point is `1` (from `2^a n=3n+1`), so this is a nontrivial cycle. Hence, if no nontrivial odd-only cycle exists, descent cannot fail.

This is a proof-target reduction, not a cycle exclusion: arbitrary periods remain open. It shows that the central global task can be stated purely as ruling out every nontrivial odd-only cycle; finite residue checks are not needed for this reduction.

## No odd-only cycles of period at most four

The only periodic orbit of the odd-only Syracuse map with period at most four is the fixed point `1`.

**Proof.** Consider a nontrivial cycle of exact odd-step period `m`, with odd values `x_0,…,x_{m-1}>1`, indices taken modulo `m`, and `a_i=v₂(3x_i+1)`. Since `S(1)=1`, a nontrivial cycle contains no `1`; thus each `x_i≥3`. From `2^{a_i}x_{i+1}=3x_i+1`, multiplication around the cycle gives

`2^A = ∏_{i=0}^{m−1}(3+1/x_i)`,  where `A=Σ a_i`.

Each factor exceeds `3` and is at most `10/3`. At least one `x_i≥5`, since `S(3)=5`, so at least one factor is strictly below `10/3`. Therefore

`3^m < 2^A < (10/3)^m`.

For `m=1`, `2^A` would lie strictly between `3` and `10/3`, which contains no power of two. For `m=2`, it would lie between `9` and `100/9`, also containing no power of two. For `m=4`, it would lie between `81` and `10000/81`, strictly between `2^6=64` and `2^7=128`. These periods are impossible.

For `m=3`, the same bounds force `A=5`, since `27<2^A<1000/27` and the only power of two in that interval is `32`. Write `a=a_0`, `b=a_1`, and `c=a_2`. Eliminating the intermediate orbit values from the three step equations gives

`(2^{a+b+c}−27)x_0 = 2^{a+b}+3·2^a+9`.

With `A=5`, this becomes `5x_0=2^a(2^b+3)+9`. Reduction modulo `5` requires `2^a(2^b+3)≡1 (mod 5)`. Since `a,b,c≥1` and `a+b+c=5`, we have `b∈{1,2,3}`. If `b=1`, the left side is `0 mod 5`. If `b=2`, the congruence requires `a≡3 (mod 4)`, but `a≤2`. If `b=3`, it requires `a≡0 (mod 4)`, but `a=1`. All cases are impossible.

Thus no nontrivial odd-only cycle has period at most four. This cycle exclusion does not rule out longer cycles or nonperiodic orbits and does not establish the Collatz conjecture.

### A minimum-versus-period constraint for every odd-only cycle

Let a nontrivial cycle have exact period `m` and least value `n`. Its `m` orbit values are distinct odd integers, so when sorted they are at least `n,n+2,…,n+2(m−1)`. The cycle product identity gives

`A−m c = Σ_{i=0}^{m−1}log_2(1+1/(3x_i))`,  `c=log_2 3`,

where `A=Σa_i` is an integer strictly greater than `mc`. Define the fractional gap to the next integer by `δ_m=ceil(mc)−mc∈(0,1)`; `mc` is never an integer because `log_2 3` is irrational. Then

`δ_m ≤ A−mc ≤ Σ_{k=0}^{m−1}log_2(1+1/(3(n+2k)))`.

Using `log_2(1+z)≤z/ln 2` and `n+2k≥n` yields the simple necessary bound

`n ≤ m/(3 ln(2) δ_m)`.

Thus a cycle with a large minimum requires `m log_2 3` to lie unusually close below an integer. The bound narrows possible cycle parameters but does not exclude the exceptional periods where `δ_m` is small.

### A sharper minimum-period bound from admissible-state spacing

The preceding estimate counts every odd integer, although a cycle cannot contain multiples of `3`. The minimum `n` is `1` modulo `6` or `5` modulo `6`. The increasing list of odd integers at least `n` that are not divisible by `3` is exactly

- `n,n+4,n+6,n+10,…` if `n≡1 (mod 6)`;
- `n,n+2,n+6,n+8,…` if `n≡5 (mod 6)`.

Let `r_j(n)` be the `j`th value in this list, starting at `j=0`, and sort the cycle values as `y_0<…<y_{m−1}`. Then `y_j≥r_j(n)`, so the exact cycle identity gives

`2^{δ_m} ≤ ∏_i(1+1/(3x_i)) ≤ ∏_{j=0}^{m−1}(1+1/(3r_j(n)))`.

With `ε=0` for `n≡1 (mod 6)` and `ε=1` for `n≡5 (mod 6)`, the spacing gives `r_0(n)=n` and `r_j(n)≥n−ε+3j` for `j≥1`. Applying `log_2(1+z)≤z/ln 2` then implies

`δ_m ≤ (1/(3 ln 2))(1/n + Σ_{j=1}^{m−1}1/(n−ε+3j))`.

Put `N=n−ε`. The function `t↦1/(N+3t)` is convex; applying the midpoint integral bound on each unit interval gives the closed necessary condition

`δ_m ≤ (1/(3 ln 2))(1/n + (1/3) ln((N+3m−3/2)/(N+3/2)))`.

For `m≥3` the reciprocal sum is strictly sharper term-by-term than the earlier sum over all odd values `n+2j`. This refines the minimum-period restriction using only exact state exclusions and an analytic inequality. It still allows parameters when `δ_m` is small, so it is not a cycle exclusion.

The same argument gives a period-only exclusion test. Since every nontrivial cycle value is an odd integer at least `3`,

`2^{δ_m} ≤ ∏_{i=0}^{m−1}(1+1/(3x_i)) ≤ P_m`,

where

`P_m=∏_{k=0}^{m−1}(1+1/(3(3+2k)))=∏_{k=0}^{m−1}(k+5/3)/(k+3/2)`.

Consequently any `m` with `2^{δ_m}>P_m` is impossible as a cycle period. The gamma-function form is

`P_m=Γ(m+5/3)Γ(3/2)/(Γ(5/3)Γ(m+3/2)) ~ C m^{1/6}`

for a positive constant `C`, so `P_m` eventually exceeds `2`. Because `2^{δ_m}<2`, this product filter can exclude only finitely many periods; ruling out long cycles requires additional information from the transition congruences.

### A sharper cycle product filter from the modulo-three obstruction

No value in an odd-only cycle is divisible by `3`: if `3|x_{i+1}`, then `2^{a_i}x_{i+1}=3x_i+1` would give `0≡1 (mod 3)`. If `n` is the minimum of a nontrivial cycle, its next value is strictly larger than `n`. Thus its valuation is `1`, since `a≥2` would give `S(n)=(3n+1)/2^a≤(3n+1)/4<n` for `n>1`. Hence `n≡3 (mod 4)`; together with `3∤n`, this implies `n≥7`.

The increasing list of odd integers at least `7` that are not divisible by `3` is `r_0=7,r_1=11,r_2=13,r_3=17,…`, with `r_{2k}=6k+7` and `r_{2k+1}=6k+11`. Sort the `m` distinct cycle values as `y_0<…<y_{m−1}`. Since each is in this admissible list, `y_j≥r_j`. The cycle product identity therefore yields the sharper necessary condition

`2^{δ_m} ≤ ∏_i(1+1/(3x_i)) ≤ Q_m`,

where

`Q_m=∏_{0≤2k<m}(1+1/(3(6k+7))) · ∏_{0≤2k+1<m}(1+1/(3(6k+11)))`.

Pairing the two factors for each `k` gives `(1+1/(18k+21))(1+1/(18k+33))=1+1/(9k)+O(k^{−2})`; consequently `Q_m~C m^{1/9}` for a positive constant `C`. This improves the coarser `m^{1/6}` product bound, but `Q_m` still grows beyond `2`, whereas `2^{δ_m}<2`. Thus the sharpened product filter also has finite scope: the exact valuation transitions are still needed to exclude arbitrary periods.

### Large-minimum cycles force a continued-fraction convergent

For any nontrivial odd-only cycle of period `m` and minimum `n`, its average valuation satisfies

`c < A/m = (1/m)Σ_i log_2(3+1/x_i) ≤ log_2(3+1/n)`,  `c=log_2 3`.

Therefore

`0 < A/m−c ≤ log_2(1+1/(3n)) ≤ 1/(3n ln 2)`.

Write `A/m=p/q` in lowest terms, with `q≤m`. If `n>2m^2/(3 ln 2)`, then `|p/q−c|<1/(2m^2)≤1/(2q^2)`. Legendre's continued-fraction criterion implies that `p/q` is a convergent of `c`, and it must be an upper convergent. In particular, its denominator `q` divides `m`. Thus every cycle is in one of two cases: `n≤2m^2/(3 ln 2)`, or its mean valuation is one of these restricted rational approximants. This reduces the large-minimum branch to Diophantine structure but does not eliminate either case. Continued-fraction and logarithmic-form methods are classical in cycle analysis; stronger published cycle bounds combine them with computational lower bounds ([Simons–de Weger, *Theoretical and computational bounds for m-cycles*](https://math.deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.44%5B2010%5D.pdf)).

### Large-minimum cycles force a large next-convergent gap

In the large-minimum case, write `A/m=p/q` in lowest terms and let `q'` be the denominator of the next convergent of `c=log_2 3` after `p/q`. Since `q|m`, write `m=qr`. For a convergent, the standard error bounds give

`1/(q(q+q')) < p/q−c < 1/(q q')`.

Indeed, for the convergent `p_k/q_k=p/q` and next denominator `q_{k+1}=q'`, the exact error has denominator `q(q'+θq)` for some `0<θ<1`.

The cycle logarithmic excess is `D=A−mc=m(p/q−c)`, so `r/(q+q')<D`. On the other hand, the admissible-state spacing above gives

`D ≤ B_{m,n}:=(1/(3 ln 2))(1/n + Σ_{j=1}^{m−1}1/(n−ε+3j)) ≤ m/(3n ln 2)`,

where `ε=0` if `n≡1 (mod 6)` and `ε=1` if `n≡5 (mod 6)`; the final inequality follows by comparing each denominator with `n+2j`.

Combining these inequalities yields the necessary denominator condition

`q+q' > r/B_{m,n} ≥ 3n ln(2)/q > 2q r^2`,

or equivalently `q'/q>2r^2−1`. Thus a large-minimum cycle whose reduced mean has denominator `q` and period `m=qr` requires the next continued-fraction denominator to jump by a factor exceeding `2r^2−1`. The condition is automatic when `r=1`, and it does not exclude the small-minimum branch or all large-minimum cycles; it isolates a further Diophantine obstruction without enumerating convergents.

### A block-coordinate identity for the cycle excess

Partition a hypothetical nontrivial cycle at its valuations `a_k≥2` into `K` return blocks, with cyclic indices. Let `t_k` and `u_k` be the block length and odd parameter from the transition law. Then `m=Σ_k t_k`, `A=m+Σ_k(a_k−1)`, and each transition satisfies

`3^{t_k}u_k−1 = 2^{a_{k+1}−1}(2^{t_{k+1}}u_{k+1}−1)`.

Multiplying around the cycle and taking logarithms gives an exact second expression for `D=A−m log_2 3`:

`D = Σ_k η(t_k,u_k)`,

where

`η(t,u)=log_2((1−1/(3^t u))/(1−1/(2^t u)))=log_2(1+(1−(2/3)^t)/(2^t u−1))>0`.

This expresses the same excess as the state-space product, but now in block variables. The incoming transition also forces, cyclically,

`u_k ≡ 2^{−(a_k−1+t_k)}(2^{a_k−1}−1) (mod 3^{t_{k−1}})`.

Let `U_k^*` be the least positive odd representative of this residue class. Then `u_k≥U_k^*`, and `η(t,u)` decreases with `u`, so

`D ≤ Σ_k η(t_k,U_k^*)`.

In the large-minimum convergent branch this combines with the previous lower bound `r/(q+q')<D` and the state-spacing cap `D≤B_{m,n}`. The resulting comparison is a symbolic necessary condition linking continued-fraction gaps to cyclic block carries. It has not yet produced a contradiction, and the small-minimum branch remains open.

The lift in the incoming congruence is exactly the preceding block parameter. Put `b_k=a_k−1`; the transition from block `k−1` to block `k` gives

`2^{b_k}(2^{t_k}u_k−1)=3^{t_{k−1}}u_{k−1}−1`.

Substitution into `η` therefore yields the exact adjacent-block expression

`η(t_k,u_k)=log_2(1 + 2^{b_k}(1−(2/3)^{t_k})/(3^{t_{k−1}}u_{k−1}−1))`.

The incoming and outgoing congruences above give `u_{k−1}≥V_{k−1}`, where `V_j=max(U_j^*,W_j)` is the two-neighbor lower bound. Since the displayed expression decreases with `u_{k−1}`, cyclically

`D ≤ Σ_k log_2(1 + 2^{b_k}(1−(2/3)^{t_k})/(3^{t_{k−1}}V_{k−1}−1))`.

In the large-minimum convergent branch this combines with `r/(q+q')<D`. Replacing `V_{k−1}` by the weaker bound `1` recovers the previous residue-independent inequality. The strengthened comparison still requires a global bound on the cyclic valuation pattern and does not rule out a cycle by itself.

The same transition has a second positive decomposition. Rearranging it gives

`2^{b_k+t_k}u_k = 3^{t_{k−1}}u_{k−1} + 2^{b_k}−1`.

Taking logarithms and summing cyclically cancels `Σ log_2 u_k` and yields

`D = Σ_k log_2(1 + (2^{b_k}−1)/(3^{t_{k−1}}u_{k−1}))`.

Using `u_{k−1}≥V_{k−1}` gives a second upper bound. Thus `D` is bounded by the smaller of the two cyclic sums

`Σ_k log_2(1 + 2^{b_k}(1−(2/3)^{t_k})/(3^{t_{k−1}}V_{k−1}−1))`

and

`Σ_k log_2(1 + (2^{b_k}−1)/(3^{t_{k−1}}V_{k−1}))`.

The formulas are complementary: the first retains the run-length factor, while the second has a simpler denominator. Neither sum has yet been bounded sharply enough, in terms of only the cycle period and minimum, to contradict the convergent lower bound.

### Exact restriction for cycles with one high-valuation block

Suppose a nontrivial odd-only cycle has exactly one valuation `a≥2`; all other `t−1` valuations are `1`. Let `b=a−1` and let `u` be the positive odd block parameter, so the value immediately after the high-valuation step is `2^t u−1`. After the forced run of `t−1` valuation-one steps, the cycle returns to the start of the high-valuation step at `2·3^{t−1}u−1`. Equating this return with the high-step equation gives

`(2^{b+t}−3^t)u=2^b−1`.

Positivity requires `b>tα`, where `α=log_2(3/2)`. Since `u` is a positive integer, `2^{b+t}−3^t≤2^b−1`, hence

`2^b≤(3^t−1)/(2^t−1)=2^{tα}(1−3^{−t})/(1−2^{−t})`.

The last ratio factor lies strictly between `1` and `2`; therefore `b<tα+1`. As `b` is an integer and `tα` is irrational, it follows that `b=floor(tα)+1`. Writing `{tα}` for the fractional part, the same inequality forces

`0<1−{tα}≤log_2((1−3^{−t})/(1−2^{−t})) < 2^{1−t}/ln 2`.

Thus a one-block cycle must satisfy both this exponentially close upper-integer approximation and the exact divisibility `2^{b+t}−3^t | 2^b−1`. More precisely, the one-block case is equivalent to `t≥2`, `b=floor(tα)+1`, and this divisibility: given them, `u=(2^b−1)/(2^{b+t}−3^t)` is positive odd. Set `y=2^t u−1` and `x=2·3^{t−1}u−1`; then `S(x)=y` with valuation `b+1`, and the next `t−1` steps have valuation `1` and return to `x`, giving the cycle. This characterizes the one-block case but does not rule it out for every `t`; cycles with two or more high-valuation blocks remain open as well.

There is an equivalent modular form that exposes constraints on every prime divisor of the modulus. Put `M=2^{b+t}−3^t`, `A=2^b−1`, and `B=3^t−2^t`. Then `B=2^tA−M`, and `M` is odd, so `gcd(M,2^t)=1`. Consequently `M|A` if and only if `M|B`. Every prime `p|M` is odd and not `3`; the equivalent divisibilities imply `ord_p(2)|b` and `ord_p(3·2^{−1})|t`. These simultaneous order constraints are a number-theoretic reformulation, not yet a contradiction.

The exact equation also gives

`3^t u−1=2^b(2^t u−1)`,

so `b=v_2(3^t u−1)`; the other factor on the right is odd. Also `u|2^b−1`, so every prime `p|u` has `ord_p(2)|b`.

These two facts give a parity-sensitive lower bound on `u`. First, `u≠1`: that would give `2^b(2^t−1)=3^t−1`. Even `t` contradicts reduction modulo `3`; odd `t` forces `b` odd, then 2-adic valuations force `b=1`, contrary to `b≥2`.

If `b` is odd and `u<23`, every prime factor of `u` must have odd order under multiplication by `2`. Among odd primes below `23`, only `7` has odd order (`ord_7(2)=3`; the orders for `3,5,11,13,17,19` are even). Thus `u` would be `1` or `7`. The first was excluded; for `u=7`, `3|b` but `b=v_2(7·3^t−1)≤2`, using residues modulo `8` and `16`. Hence odd `b` forces `u≥23`.

If `b` is even, then `3|2^b−1`; since `3∤M`, this forces `3|u`. The only odd multiples of `3` below `27` are `3,9,15,21`. For `u=3`, even `t` forces `b=1`; for odd `t`, it gives `b=2+v_2(t+1)`. For `t≥10`, `tα>2+log_2(t+1)` (the difference is increasing there and is positive at `10`), which is impossible. The remaining odd values give

| `t` | `b=floor(tα)+1` | `2+v_2(t+1)` |
| ---: | ---: | ---: |
| 3 | 2 | 4 |
| 5 | 3 | 3 |
| 7 | 5 | 5 |
| 9 | 6 | 3 |

Since `u=3` requires even `b`, the table rules out all four. For the other candidates, LTE gives `9|b` when `u=9`, while `b=v_2(9·3^t−1)≤4`; `u=15` gives `4|b` but `b=v_2(15·3^t−1)≤2`; and `u=21` gives `6|b` but `b=v_2(21·3^t−1)≤2`. These bounds follow from the residues of `3^t` modulo `8` or `16`. Therefore even `b` forces `u≥27`.

Set `q=23` for odd `b` and `q=27` for even `b`. Since `u≥q` and `uM=A`,

`2^b≤(q·3^t−1)/(q·2^t−1)=(3/2)^t (1−1/(q·3^t))/(1−1/(q·2^t))`.

Consequently,

`0<b−tα≤log_2((1−1/(q·3^t))/(1−1/(q·2^t)))<2^{1−t}/(q ln 2)`.

This tightens the elementary exponential-approximation bound by a factor of at least `23`, depending on the parity of `b`. It still does not exclude all run lengths, and cycles with multiple high-valuation blocks remain open.

### Exclusion of a cycle with exactly one high valuation

The preceding bound does exclude the special case where a cycle has exactly one valuation `a≥2` and all other `t−1` valuations equal `1`. Put `σ=b+t`, `Λ=σ ln 2−t ln 3=(b−tα)ln 2`, and

`G=2^σ/3^t−1=(2^σ−3^t)/3^t=M/3^t>0`.

Since `u≥23`, we have `G<2/(23·2^t)`. The nonzero linear form `Λ=σ ln 2−t ln 3` is positive. Matveev's two-logarithm lower bound applied to `Λ`, with `B=σ`, gives `Λ>exp(−K(1+ln σ))`. As `G=e^Λ−1>Λ`, this implies

`ln G>−K(1+ln σ)`, where `K=1.4·30^5·2^{4.5} ln 2 ln 3 < 6·10^8` ([Matveev, 2000](https://www.mathnet.ru/links/11696330cc866d273c92c771a63da235/im314_eng.pdf)).

Combining the two bounds and using `σ=b+t≤2t`, any such cycle must satisfy

`t ln 2+ln(23/2)<6·10^8(1+ln(2t))`.

The right side is smaller than the left at `t=30,000,000,000`, and the difference increases thereafter, so `t<30,000,000,000` and `σ<60,000,000,000`.

For the middle range, let `θ=ln 2/ln 3`. Exact rational intervals for the logarithms, using the first 128 terms of

`ln x=2Σ_{j=0}^{127} z^{2j+1}/(2j+1)+r`, `z=(x−1)/(x+1)`, `0<r<2z^{257}/(257(1−z^2))`,

give rational intervals `[ℓ₂,u₂]` and `[ℓ₃,u₃]` for `ln 2` and `ln 3`. Applying the Euclidean continued-fraction algorithm to `[ℓ₂/u₃,u₂/ℓ₃]` gives the common partial quotients through `a_{K+1}`:

`0,1,1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3,1,1,15,1,9,2,5,7,1,1,4`.

The consecutive convergent denominators at that endpoint are `q_K=18,340,740,190,704` and `q_{K+1}=83,130,157,078,217`, with `ln 3/(q_K+q_{K+1})>1.08·10^{−14}`. The continued-fraction best-approximation property then gives `Λ>1.08·10^{−14}` whenever `0<σ<q_{K+1}`. Our Matveev cutoff puts `σ<60,000,000,000<q_{K+1}`. But for `t≥43`, the quotient bound gives `Λ<2^{1−t}/23≤2^{−42}/23<10^{−14}`, a contradiction. Thus `t≤42`.

The case `t=2` is already excluded by its exact margin in the table below. For `3≤t≤42`, `|b/t−α|<2^{1−t}/(23t ln 2)<1/(2t^2)`, so Legendre's criterion makes the reduced fraction `b/t` a convergent of `α`. Exact rational intervals `[ℓ₃/u₂−1,u₃/ℓ₂−1]` give the convergents through denominator `53` as `0/1, 1/1, 1/2, 3/5, 7/12, 24/41, 31/53`. Since `b<t` and `b/t>α`, only denominators `5` and `41` can occur; hence `t` is a multiple of `5` or equals `41`. The remaining exact checks are:

| `t` | `b` | `q` | `qM−A` |
| ---: | ---: | ---: | ---: |
| 2 | 2 | 27 | 186 |
| 5 | 3 | 23 | 292 |
| 10 | 6 | 27 | 175,086 |
| 15 | 9 | 23 | 55,850,596 |
| 20 | 12 | 27 | 21,820,934,070 |
| 25 | 15 | 23 | 5,801,129,388,892 |
| 30 | 18 | 27 | 2,040,763,804,370,046 |
| 35 | 21 | 23 | 506,599,125,593,252,116 |
| 40 | 24 | 27 | 169,805,122,595,604,038,790 |
| 41 | 24 | 27 | 11,353,277,796,687,777,168 |

Every margin is positive, contradicting the necessary cycle condition `qM≤A`. Therefore no nontrivial odd-only cycle has exactly one valuation at least `2` and all remaining valuations equal to `1`. This is a cycle subcase only; it does not exclude profiles with multiple high valuations or unbounded non-descending orbits. No Collatz trajectories were enumerated in this argument; the finite part consists of ten exact exponent comparisons.

A related 2026 preprint claims the stronger result that every nontrivial cycle has at least four runs of valuation-one steps; it uses additional run inequalities and a computational lower bound for cycle length ([Cerdá Bennassar, preprint](https://zenodo.org/records/23190068)). The current project has not independently verified its two- and three-run cases.

### Exact system for two high-valuation blocks

Suppose a nontrivial odd-only cycle has exactly two valuations at least `2`. Index the two blocks cyclically. In block `i`, let `a_i≥2` be its high valuation, let `t_i≥1` count that step together with the following `t_i−1` valuation-one steps, put `b_i=a_i−1`, and let `u_i` be the positive odd parameter after the high step. The transition identities are

`3^{t_1}u_1−1=2^{b_2}(2^{t_2}u_2−1)`,  `3^{t_2}u_2−1=2^{b_1}(2^{t_1}u_1−1)`.

Set `T=t_1+t_2`, `B=b_1+b_2`, and

`η(t,u)=log_2((1−1/(3^t u))/(1−1/(2^t u)))`.

Multiplying the two transitions and cancelling `u_1u_2` gives the exact cycle-excess identity

`B−T log_2(3/2)=η(t_1,u_1)+η(t_2,u_2)`.

Each correction is positive and decreases with `u`. Also

`η(t,u)≤η(t,1)=log_2((1−3^{−t})/(1−2^{−t}))≤log_2(4/3)`,

where equality in the last bound occurs at `t=1`. Hence

`0<B−T log_2(3/2)≤log_2(16/9)<1`,

so the integer sum is fixed by the total block length:

`B=floor(T log_2(3/2))+1`.

The transitions also impose a simple residue restriction. Reducing the transition into block `i` modulo `3` gives

`b_i even ⇒ 3|u_i`,  `b_i odd ⇒ u_i≡(−1)^{t_i+1} (mod 3)`.

Thus an odd `b_i` with even `t_i` forces `u_i≥5`, while an odd `b_i` with odd `t_i` allows `u_i=1` or forces `u_i≥7`. If `u_i=1`, the residue condition makes `t_i` odd, and the transition out of block `i` gives `b_{i+1}=v_2(3^{t_i}−1)=1`. If both block quotients were `1`, this would give `b_1=b_2=1` and `B=2`. Since `T` would be even and `log_2(3/2)>1/2`, the fixed-sum condition forces `T=2`, `t_1=t_2=1`; the reconstructed cycle is only the trivial fixed point `1`. Therefore every nontrivial two-block cycle has at least one `u_i≥3`.

For `u≥1`, `η(t,u)≤log_2(4/3)`. If `u≥3`, then

`(1−(2/3)^t)/(2^t u−1)≤1/15`,

as is seen separately for `t=1`, `t=2`, and `t≥3`; hence `η(t,u)≤log_2(16/15)`. The nontrivial two-block case consequently satisfies the sharper necessary bound

`0<B−T log_2(3/2)≤log_2(64/45)<1`,

or, equivalently,

`{T log_2(3/2)}≥log_2(45/32)`.

This restricts the total period's fractional-part position but still permits infinitely many `T`; the divisibility conditions below are needed for further progress.

The two transitions are a linear system in `u_1,u_2`. Its determinant is `−Q`, where `Q=2^{B+T}−3^T>0`. Solving it yields

`Q u_1=3^{t_2}(2^{b_2}−1)+2^{b_2+t_2}(2^{b_1}−1)`,

`Q u_2=3^{t_1}(2^{b_1}−1)+2^{b_1+t_1}(2^{b_2}−1)`.

Thus any two-block cycle must have `b_1,b_2≥1`, the displayed fixed sum `B`, and both right-hand sides divisible by `Q` with positive odd quotients. Conversely, such positive odd quotients solve the transition system and reconstruct the two high steps and their forced unit-valuation runs. This is an exact arithmetic characterization of the two-block case; the simultaneous divisibilities have not been ruled out for all `T`, and this result excludes no general cycle profile.

#### A finite period bound for the two-block profile

The same equations give a finite, though still large, upper bound on `T`. Put `c=log_2 3`, `D=B−T log_2(3/2)`, and `F=2^D−1`; we have `0<D<1`. The positive linear form

`Λ=(B+T)ln 2−T ln 3=D ln 2`

has coefficients bounded by `B+T≤2T`, since `B=ceil(T log_2(3/2))≤T`. Matveev's explicit bound ([Matveev, 2000](https://www.mathnet.ru/php/archive.phtml?jrnid=im&option_lang=eng&paperid=314&wshow=paper)) with `K=1.4·30^5·2^{4.5}ln 2 ln 3<6·10^8` therefore gives

`Λ>exp(−H)`,  `H=6·10^8(1+ln(2T))`.

Because `F=e^Λ−1>Λ`, we also have `F>exp(−H)`. Divide the first exact numerator identity by `3^T`; using `u_1≥1` and replacing each `2^b−1` by `2^b` gives

`F<2^{b_2−ct_1}+2^{D−t_1}`.

The other identity gives `F<2^{b_1−ct_2}+2^{D−t_2}`. Let

`L=H/ln 2+3`,  `C=H/ln 2+log_2(4/3)`.

Whenever `t_i≥L`, the second term in its inequality is less than `exp(−H)/4<F/4`, because `D<1`. The first term must then exceed `3F/4`, so the opposite exponent obeys `b_{i+1}>ct_i−C` (cyclic indices).

Both block lengths cannot be at least `L`: that would give `B>cT−2C`, hence `T<2C+1`, while `T≥2L>2C+1` because `L−C=3−log_2(4/3)>5/2`. If `T≥2L`, exactly one block is long and the other has length less than `L`; using the long-block bound and the other `b_i≥1` yields `T<cL+C`. If `T<2L`, the same conclusion holds because `cL+C−2L=(c−1)L−3+log_2(4/3)>0` (`L>6` and `c−1=log_2(3/2)>1/2`). Thus every two-block cycle would satisfy

`T<cL+C=(c+1)H/ln 2+3c+log_2(4/3)<2.3·10^9(1+ln(2T))+6`.

Here the last estimate follows from `c<8/5` (since `3^5<2^8`), `ln 2>56/81` (the first two positive terms of its atanh series), and `log_2(4/3)<1/2`. At `T=10^{11}`, using `ln(2·10^{11})<27`, the right side is less than `6.5·10^{10}`; its derivative is less than `1` for all larger `T`. Therefore

`T<10^{11}`.

This bound uses no orbit enumeration. The same exact inequalities can be combined with continued-fraction lower bounds in three short bootstrap steps, reducing the two-block period all the way to `T≤23`.

#### Exclusion of exactly two high-valuation blocks

Continue with `θ=ln 2/ln 3`, `σ=B+T`, `c=log₂3`, and `α=c−1`. The exact logarithmic form is `Λ=σ ln 2−T ln 3=D ln 2>0`. The rational logarithm intervals already described above certify the common continued-fraction prefix

`[0;1,1,1,2,2,3,1,5]`,

whose successive denominators include `19, 65, 84, 485`. The best-approximation inequality for `θ` therefore gives these deliberately weakened bounds:

- if `σ<485`, then `Λ>ln 3/(84+485)>1/600`;
- if `σ<65`, then `Λ>ln 3/(19+65)>1/100`;
- if `σ<83,130,157,078,217`, the longer certified convergent pair above gives `Λ>1.08·10⁻¹⁴>10⁻¹⁴`.

Since `F=e^Λ−1>Λ`, the same lower bounds hold for `F`.

First use the already proved `T<10¹¹`. Then `σ≤2T<2·10¹¹`, so the last continued-fraction bound applies. Whenever `t_i≥51`,

`2^(D−t_i)<2⁻⁵⁰<10⁻¹⁴/4<F/4`.

In the associated numerator inequality this forces `2^(b_(i+1)−c t_i)>3F/4>2⁻⁴⁷`, hence `b_(i+1)>c t_i−47`. If both lengths are at least `51`, summing gives `B>cT−94`, whereas `B≤αT+1`; thus `T<95`, contradicting `T≥102`. If `T≥102`, exactly one length is at least `51`; the other is at most `50`. The same bound and `b_i≥1` give `T<51c+47<128.6`, hence `T≤128`. Thus in all cases `T<129`.

Now `σ≤256<485`, so `F>1/600`. If `t_i≥13`, then

`2^(D−t_i)<2⁻¹²<1/2400<F/4`,

which forces `b_(i+1)>c t_i−10`. Two lengths at least `13` would imply `T<21`, although their sum is at least `26`. For `T≥26`, one length is at least `13` and the other is at most `12`; consequently `T<13c+10<30.8`, so `T≤30`. This also holds when `T<26`.

Finally `σ≤60<65`, so `F>1/100`. For `t_i≥10`,

`2^(D−t_i)<2⁻⁹<1/400<F/4`,

and hence `b_(i+1)>c t_i−8`. Two such lengths would imply `T<17`, contradicting `T≥20`. If `T≥20`, one length is at least `10` and the other at most `9`, giving `T<10c+8<24`; smaller `T` already satisfies the same conclusion. Therefore every exactly-two-high-valuation cycle must have `2≤T≤23`.

For these 22 possible totals, exact integer comparisons using `B=floor(Tα)+1` and `45·2^(B+T)≤64·3^T` leave only the following candidates. The last column is the exact nonnegative margin in that inequality:

| `T` | `B` | `64·3^T−45·2^(B+T)` |
|---:|---:|---:|
| 3 | 2 | 288 |
| 5 | 3 | 4,032 |
| 6 | 4 | 576 |
| 8 | 5 | 51,264 |
| 10 | 6 | 830,016 |
| 13 | 8 | 7,664,832 |
| 15 | 9 | 163,355,328 |
| 17 | 10 | 2,225,172,672 |
| 18 | 11 | 635,720,256 |
| 20 | 12 | 29,880,673,344 |
| 22 | 13 | 462,199,588,416 |

Three exact arithmetic filters now cover all candidates.

**Cycle-product filter.** A nontrivial odd cycle contains no `1`, `3`, or `5`, and none of its values is divisible by `3`. Its `T` distinct values, in increasing order, are therefore at least `r_j`, where `r_(2k)=6k+7` and `r_(2k+1)=6k+11`. The cycle product identity gives

`2^D = ∏_(j<T)(1+1/(3x_j)) ≤ P_T := ∏_(j<T)(1+1/(3r_j))`.

For five candidates, exact rational multiplication instead gives `2^(B+T)·den(P_T)−3^T·num(P_T)>0`, contradicting that inequality:

| `T` | `P_T` | Exact positive margin |
|---:|---:|---:|
| 3 | `2720/2457` | 5,184 |
| 6 | `371200/318573` | 55,613,952 |
| 8 | `180224/150903` | 53,747,712 |
| 13 | `2988131221504/2391983523099` | 252,306,695,972,192,256 |
| 18 | `58567900625108992/45416203263860751` | 1,692,233,765,963,166,671,437,824 |

**Congruence filters.** For `T=5`, `B=3`, `Q=13`; the first numerator `N₁` modulo `13`, with columns `b₂=1,2`, is

| `t₂` | 1 | 2 |
|---:|---:|---:|
| 1 | 2 | 4 |
| 2 | 7 | 4 |
| 3 | 10 | 9 |
| 4 | 8 | 8 |

No entry is zero, so `Q∤N₁`.

For `T=10`, `B=6`, `Q=6487=13·499`. Modulo `13`, put `x=2^b₁`, `y=2^b₂`; since `xy=2^6≡−1`, the condition `13|N₁` requires `y(3^t₂−2^t₂)≡3^t₂+2^t₂`. For `t₂=1,…,9`, the required `y` values are `5,0,8,none,5,0,8,none,5`; the allowed values for `b₂=1,…,5` are `2,4,8,3,6`. Only `(t₂,b₂)=(3,3),(7,3)` survive. Their pairs `(N₁,N₂) mod 499` are `(138,22)` and `(22,138)`, so in neither case does `Q` divide both numerators.

For `T=17`, `B=10`, `Q≡0 (mod 5)` and `2^(b₁+b₂)=2^10≡−1 (mod 5)`. The first numerator satisfies

`N₁≡y(r−s)−(r+s) (mod 5)`, where `y=2^b₂`, `r=3^t₂`, and `s=2^t₂`.

As `t₂` runs through residues `1,2,3,0 (mod 4)`, this expression is respectively `y, 2, 4y, 3`, all nonzero modulo `5`. Thus `Q∤N₁`.

**Product of the exact numerator bounds.** This handles `T=15,20,22`. Set `X=2^D=2^(B+T)/3^T` and `R_i=N_i/3^T`. The exact formulas give `R_i=F u_i` with `u_i≥1`, so

`(X−1)^2=F^2≤R₁R₂ < U_T := (X+X²)/2^T + 2X²·3^(T−1)/2^(2T)`.

Indeed, after dropping negative terms, `R₁<2^(b₂−c t₁)+2^(D−t₁)` and its cyclic counterpart; multiplying, using `b_i≥1`, `t_i≥1`, and `t₁+t₂=T` gives the displayed bound. Exact rational subtraction yields:

| `T` | `B` | `(X−1)^2−U_T` |
|---:|---:|---:|
| 15 | 9 | `3373094773433/205891132094649` |
| 20 | 12 | `204709564784986123/4052555153018976267` |
| 22 | 13 | `2489341253238856571/328256967394537077627` |

Each difference is positive, contradicting the required inequality. The three filters cover every candidate, so no nontrivial odd-only cycle has exactly two high-valuation blocks.

This is a pure-arithmetic exclusion of one full cycle profile: its only finite checks are small exact integer, rational, and modular comparisons after the analytic bound `T≤23`. It does not exclude cycles with three or more high valuations. By the cycle-exclusion reduction above, completing those remaining cycle cases would prove Collatz; the full conjecture remains open.

### Necessary constraints for exactly three high-valuation blocks

Consider a nontrivial odd-only cycle with exactly three valuations at least `2`. Index its high blocks cyclically by `i∈{1,2,3}` and write their transition equations as

`3^(t_i)u_i−1 = 2^(b_(i+1))(2^(t_(i+1))u_(i+1)−1)`,

where `b_i=a_i−1≥1`, `t_i≥1`, `u_i` is positive odd, and indices are modulo `3`. Set `T=t_1+t_2+t_3`, `B=b_1+b_2+b_3`, and `α=log₂(3/2)`. Telescoping the logarithms gives

`D := B−Tα = Σ_i η(t_i,u_i)`,  `η(t,u)=log₂((1−1/(3^t u))/(1−1/(2^t u)))`.

The modulo-three restriction from the incoming transition says `b_i even ⇒ 3|u_i`, while `b_i odd ⇒ u_i≡(−1)^(t_i+1) (mod 3)`. Therefore `u_i=1` forces `b_i` and `t_i` odd. The outgoing transition then gives `b_(i+1)=v₂(3^(t_i)−1)=1`.

If all three `u_i` were `1`, each transition would reduce to `3^(t_i)+1=2^(t_(i+1)+1)`. Since odd `t_i` gives `v₂(3^(t_i)+1)=2`, this forces every `t_i=1`; each high step then maps to `1`, so the cycle is trivial. A nontrivial cycle must therefore have at least one `u_i≥3`. Using `η(t,1)≤log₂(4/3)` and `η(t,u)≤log₂(16/15)` for `u≥3` gives

`0<D≤2log₂(4/3)+log₂(16/15)=log₂(256/135)<1`.

Consequently `B=floor(Tα)+1` for any nontrivial cycle with exactly three high blocks.

In fact, at most one of the three `u_i` can equal `1`. If two did, they would be consecutive after cyclic relabeling; take `u_1=u_2=1`. The first transition gives `3^(t_1)+1=2^(t_2+1)`, hence `t_1=t_2=1`. Also `b_2=b_3=1`, so `b_1=B−2`. The third transition becomes

`3^(t_3)u_3=2^(b_1)+1`,

which implies `2^(b_1)≡−1 (mod 3^(t_3))`. For `t_3≥2`, the order of `2` modulo `3^(t_3)` is `2·3^(t_3−1)`, so `b_1≥3^(t_3−1)≥t_3`. But the fixed-sum formula gives `b_1=floor((t_3+2)α)−1<t_3`, a contradiction. For `t_3=1`, `1<3α<2` gives `B=2`, hence `b_1=0`, also impossible.

Thus at least two of the three parameters satisfy `u_i≥3`. If none equals `1`, the stronger bounds are

`D≤3log₂(16/15)=log₂(4096/3375)`,  `{Tα}≥log₂(3375/2048)`.

If one equals `1`, then

`D≤log₂(4/3)+2log₂(16/15)=log₂(1024/675)`,  `{Tα}≥log₂(675/512)`.

There is also an exact local pattern in the one-`1` case. If `u_i=1`, then `t_i` is odd and `b_(i+1)=1`. Its outgoing transition reads

`3^(t_i)+1=2^(t_(i+1)+1)u_(i+1)`.

The left side has 2-adic valuation `2`, so `t_(i+1)=1` and `u_(i+1)=(3^(t_i)+1)/4`. Since two `u` values cannot be `1`, this forces `t_i≥3` and `u_(i+1)≥7`. The next high valuation also satisfies `b_(i+2)=v₂(3u_(i+1)−1)=v₂(t_i+1)`, by the 2-adic LTE formula. Thus the exceptional quotient `1` fixes the next run length and valuation exactly.

In particular, every nontrivial three-high-block cycle must satisfy `B=floor(Tα)+1` and `{Tα}≥log₂(675/512)`.

#### Excluding the branch with a quotient equal to one

Suppose `u_1=1`, and write `t=t_1`, `h=v₂(t+1)`. Since this quotient is unique, `u_2,u_3≥3`. The exact local pattern above gives

`t_2=1`,  `u_2=(3^t+1)/4`,  `b_2=1`,  `b_3=h`.

The fixed sum and closing transition then give

`b_1=floor((t+t_3+1)α)−h`,  `3^(t_3)u_3=2^(b_1)(2^t−1)+1`.

Since `u_3≥3`, comparison of the right side with `2^(b_1+t)` yields `t_3<c t−h−1`, where `c=log₂3`. The lower comparison `2^(b_1)(2^t−1)+1>2^(b_1+t−1)`, together with the fixed-sum formula, gives

`u_3>2^(c t−t_3+α−h−2)`.

For all positive odd `u`,

`η(t,u)<2^(1−t)/(u ln 2)`.

Applying this to the three corrections, using `u_2>3^t/4` and `2^h≤t+1`, gives

`D< [2^(1−t)+4/3^t+(16/3)(t+1)/3^t]/ln 2 < 24(t+1)2^(−t)`.

Matveev's lower bound from the two-block argument gives `D>exp(−H)`, where `H=6·10^8(1+ln(2T))`. Since `T=t+1+t_3<(1+c)t<2.6t`, the bounds imply

`t ln 2−ln(24(t+1)) < 6·10^8(1+ln(5.2t))`.

At `t=3·10^10` the left side exceeds `20.7·10^9`, while the right side is below `16.8·10^9`; the difference is increasing thereafter. Hence `t<3·10^10`, so `T<7.8·10^10` and `σ=B+T<1.56·10^11`.

The certified continued fractions for `θ=ln 2/ln 3` now bootstrap this bound down. At each stage, the best-approximation inequality gives `Λ=σ ln 2−T ln 3>D ln 2` its stated lower bound; the exponentially decreasing upper bound for `D` then shortens `t`:

| Cutoff for `σ` | Lower bound for `Λ` | Result |
|---:|---:|---:|
| `83,130,157,078,217` | `1.08·10⁻¹⁴` | `t≤55`, `T≤141` |
| `485` | `1/600` | `t≤17`, `T≤43` |
| `84` | `1/150` | `t≤15`, `T≤37` |
| `65` | `1/84` | `t≤13`, `T≤32` |

Each cutoff is available at the preceding step: `σ<1.56·10^11`, then `σ≤282`, then `σ<84`, then `σ<65`. The parity condition `t` odd is used in the displayed `t` bounds.

Only `t=3,5,7,9,11,13` remain. The transition from block 2 determines `t_3,u_3` uniquely: put `M=(3u_2−1)/2^h`, then `t_3=v₂(M+1)` and `u_3=(M+1)/2^t_3`. The last transition fails in every case:

| `t` | `h` | `t₃` | `u₃` | `T` | `B` | `b₁` | `3^t₃u₃` | `2^b₁(2^t−1)+1` |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 2 | 1 | 3 | 5 | 3 | 0 | 9 | 8 |
| 5 | 1 | 2 | 23 | 8 | 5 | 3 | 207 | 249 |
| 7 | 3 | 1 | 103 | 9 | 6 | 2 | 309 | 509 |
| 9 | 1 | 1 | 3691 | 11 | 7 | 5 | 11,073 | 16,353 |
| 11 | 2 | 6 | 519 | 18 | 11 | 8 | 378,351 | 524,033 |
| 13 | 1 | 4 | 37,367 | 18 | 11 | 9 | 3,026,727 | 4,193,793 |

Therefore a nontrivial three-high-block cycle has no quotient equal to `1`; all three `u_i` are at least `3`.

#### A finite period bound for the three-high-block profile

For this remaining branch, define `w_i=t_i+log₂u_i`. Since `u_i≥3`, the correction satisfies

`η(t_i,u_i)<6·2^(−w_i)/(5 ln 2)`.

Also, the exact transition gives

`2^(w_(i+1))=(3^(t_i)u_i−1)/2^(b_(i+1))+1<3^(t_i)u_i`,

so `w_(i+1)<c w_i−αc`. Matveev gives `D>exp(−H)` as above; at least one of the three corrections is at least `D/3`. It follows that for some cyclic index `j`,

`w_j < W := H/ln 2 + log₂(18/(5 ln 2))`.

Iterating the transition bound twice and using `t_i=w_i−log₂u_i≤w_i−c` gives

`T < S W−C`,  `S=1+c+c²`,  `C=3c+αc(c+2)`.

Exact power comparisons `3^50>2^79` and `3^100<2^159` give `1.58<c<1.59`. Hence `S<5.1181` and `C>8.02`. With `ln 2>56/81`, Matveev's estimate first gives

`T<4.5·10^9(1+ln(2T))+20`,

which implies `T<10^12` by evaluating at `10^12` and noting that the right side has derivative less than `1` thereafter.

We can then apply the same certified continued-fraction bounds successively. If `Λ>D` is bounded below by `L`, the estimate above gives `W<log₂(18/(5L))`:

| Condition on `σ` | `L` | Upper bound for `W` | Result |
|---:|---:|---:|---:|
| `σ<83,130,157,078,217` | `1.08·10⁻¹⁴` | `49` | `T≤252` |
| `σ<485` | `1/600` | `11.75` | `T≤52` |
| `σ<84` | `1/150` | `9.25` | `T≤39` |
| `σ<65` | `1/84` | `8.25` | `T≤34` |

These cutoffs follow in order from `σ≤cT+1`, `2^82<3^52<2^83` (so `σ≤83` when `T≤52`), and the exact bound `c<1.59`. Thus every exactly-three-high-block cycle has `T≤34`.

Finally, at least one `t_i≥m:=ceil(T/3)`. The function `η(t,u)` decreases in both `t` and `u`, so

`2^D≤R_T := (16/15)^2 · (1−3^(−m−1))/(1−1/(3·2^m))`.

For `3≤T≤34`, exact integer comparisons with `B=floor(Tα)+1` leave only:

| `T` | `B` | `m` | `R_T` | Exact margin `num(R_T)·3^T−den(R_T)·2^(B+T)` |
|---:|---:|---:|---:|---:|
| 3 | 2 | 1 | `4096/3375` | 2,592 |
| 5 | 3 | 2 | `26624/22275` | 767,232 |
| 10 | 6 | 4 | `991232/856575` | 2,394,759,168 |
| 17 | 10 | 6 | `35815424/31328775` | 420,332,691,750,912 |
| 22 | 13 | 8 | `99221504/87097275` | 121,036,349,952,884,736 |
| 29 | 17 | 10 | `46437761024/40801382775` | 315,898,996,468,454,134,382,592 |
| 34 | 20 | 12 | `1671767785472/1469208502575` | 1,413,467,659,060,407,406,342,176,768 |

The margin must be nonnegative because `2^D≤R_T`. The period-`3` row is independently impossible: the three distinct odd cycle values are nonmultiples of `3` and at least `7`, so `2^D≤P_3=2720/2457`; the exact cross-multiplied margin `2^5·2457−3^3·2720=5184>0` contradicts this. Consequently any exactly-three-high-block cycle would have to satisfy

`T∈{5,10,17,22,29,34}`.

This is a finite reduction, not an exclusion of the exactly-three-high-block profile. The remaining totals still have to satisfy the exact three-block transition numerators; profiles with four or more high valuations remain open.

#### A closed numerator for three-block cycles

Write `s_i=b_i+t_i` and `c_i=2^(b_i)−1`. The exact transition law is equivalently

`2^(s_(i+1))u_(i+1)=3^(t_i)u_i+c_(i+1)`.

Composing the three equations cyclically and collecting the `u_1` term gives

`Q u_1=N`,  `Q=2^(B+T)−3^T`,

where

`N=3^(t_2+t_3)c_2 + 3^(t_3)2^(b_2+t_2)c_3 + 2^(b_2+t_2+b_3+t_3)c_1`.

Here `Q>0` because the cycle-excess identity gives `B>T log_2(3/2)`. Thus every three-block cycle must satisfy the exact divisibility `Q|N`; cyclic relabeling gives the corresponding conditions for `u_2` and `u_3`. This is a symbolic consequence of the transition equations and applies independently of any orbit search.

#### Excluding the `T=5` profile

For `T=5`, the fixed-sum formula gives `B=floor(5α)+1=3`. Since there are three positive integers `b_i`, each `b_i=1`. The transition law becomes

`2^(t_(i+1)+1)u_(i+1)=3^(t_i)u_i+1`.

The closed-numerator identity above specializes to

`13u_1=N(t_2,t_3)`,  `N(t_2,t_3)=3^(t_2+t_3)+3^(t_3)2^(t_2+1)+2^(t_2+t_3+2)`,

since `2^8−3^5=13`. Positivity of `t_1` means `t_2+t_3≤4`. The six possible ordered pairs yield:

| `(t_2,t_3)` | `t_1` | `N(t_2,t_3) mod 13` |
|---:|---:|---:|
| `(1,1)` | `3` | `11` |
| `(1,2)` | `2` | `4` |
| `(2,1)` | `2` | `5` |
| `(1,3)` | `1` | `6` |
| `(3,1)` | `1` | `11` |
| `(2,2)` | `1` | `9` |

None is divisible by `13`, contradicting the required integer `u_1`. Thus no exactly-three-high-block cycle has `T=5`. This is a six-case modular check of the exact cycle equations, not a search through Collatz trajectories. The remaining period totals are `T∈{10,17,22,29,34}`.

For the next remaining total, `T=10` and `B=6`, so the same identity gives `Q=2^16−3^10=6487=13·499`. Any such cycle must make the exact numerator `N` divisible by both `13` and `499`. This is a necessary modular target only; `T=10` has not been excluded.

## Auxiliary finite congruence certificates

The following exact congruence arguments establish descent on selected classes. They are valid side results, but extending a residue list is not the active proof strategy and does not address the remaining all-integers argument.

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

### Lemma 14: `n ≡ 199 (mod 256)`

If `n = 256k + 199`, where `k ≥ 0`, then `S^5(n) < n`.

**Proof.** The first four odd Syracuse iterates are exact:

- `3n + 1 = 768k + 598 = 2(384k + 299)`, so `S(n) = 384k + 299`;
- `3S(n) + 1 = 1152k + 898 = 2(576k + 449)`, so `S^2(n) = 576k + 449`;
- `3S^2(n) + 1 = 1728k + 1348 = 4(432k + 337)`, so `S^3(n) = 432k + 337`;
- `3S^3(n) + 1 = 1296k + 1012 = 4(324k + 253)`, so `S^4(n) = 324k + 253`.

Each displayed quotient is odd. On the fifth step, `3S^4(n) + 1 = 972k + 760 = 4(243k + 190)`, so `S^5(n) ≤ 243k + 190 < 256k + 199 = n`, since the difference is `13k + 9 > 0`.

### Lemma 15: `n ≡ 175 (mod 256)`

If `n = 256k + 175`, where `k ≥ 0`, then `S^5(n) < n`.

**Proof.** The first four odd Syracuse iterates are exact:

- `3n + 1 = 768k + 526 = 2(384k + 263)`, so `S(n) = 384k + 263`;
- `3S(n) + 1 = 1152k + 790 = 2(576k + 395)`, so `S^2(n) = 576k + 395`;
- `3S^2(n) + 1 = 1728k + 1186 = 2(864k + 593)`, so `S^3(n) = 864k + 593`;
- `3S^3(n) + 1 = 2592k + 1780 = 4(648k + 445)`, so `S^4(n) = 648k + 445`.

Each displayed quotient is odd. On the fifth step, `3S^4(n) + 1 = 1944k + 1336 = 8(243k + 167)`, so `S^5(n) ≤ 243k + 167 < 256k + 175 = n`, since the difference is `13k + 8 > 0`.

### Lemma 16: `n ≡ 219 (mod 256)`

If `n = 256k + 219`, where `k ≥ 0`, then `S^5(n) < n`.

**Proof.** The first four odd Syracuse iterates are exact:

- `3n + 1 = 768k + 658 = 2(384k + 329)`, so `S(n) = 384k + 329`;
- `3S(n) + 1 = 1152k + 988 = 4(288k + 247)`, so `S^2(n) = 288k + 247`;
- `3S^2(n) + 1 = 864k + 742 = 2(432k + 371)`, so `S^3(n) = 432k + 371`;
- `3S^3(n) + 1 = 1296k + 1114 = 2(648k + 557)`, so `S^4(n) = 648k + 557`.

Each displayed quotient is odd. On the fifth step, `3S^4(n) + 1 = 1944k + 1672 = 8(243k + 209)`, so `S^5(n) ≤ 243k + 209 < 256k + 219 = n`, since the difference is `13k + 10 > 0`.

### Lemma 17: `n ≡ 2587 (mod 4096)`

If `n = 4096k + 2587`, where `k ≥ 0`, then `S^7(n) < n`.

**Proof.** The first six odd Syracuse iterates are exact:

- `3n + 1 = 12288k + 7762 = 2(6144k + 3881)`, so `S(n) = 6144k + 3881`;
- `3S(n) + 1 = 18432k + 11644 = 4(4608k + 2911)`, so `S^2(n) = 4608k + 2911`;
- `3S^2(n) + 1 = 13824k + 8734 = 2(6912k + 4367)`, so `S^3(n) = 6912k + 4367`;
- `3S^3(n) + 1 = 20736k + 13102 = 2(10368k + 6551)`, so `S^4(n) = 10368k + 6551`;
- `3S^4(n) + 1 = 31104k + 19654 = 2(15552k + 9827)`, so `S^5(n) = 15552k + 9827`;
- `3S^5(n) + 1 = 46656k + 29482 = 2(23328k + 14741)`, so `S^6(n) = 23328k + 14741`.

Each displayed quotient is odd. The seventh-step numerator is `3S^6(n) + 1 = 69984k + 44224 = 32(2187k + 1382)`. Therefore `S^7(n) ≤ 2187k + 1382 < 4096k + 2587 = n`, with difference `1909k + 1205 > 0`.

Lemmas 1–4 cover 24 of the 32 odd residue classes modulo 64: all classes `1, 5, 9, 13 (mod 16)`, all of `3 (mod 16)`, and `11, 23, 43, 55 (mod 64)`. Lemmas 5–16 additionally cover `7`, `15`, `39`, `59`, `79`, `95`, `123`, `135`, `143`, `175`, `187`, `199`, and `219 (mod 256)`. Lemma 17 adds the finer class `2587 (mod 4096)`, which lies inside `27 (mod 256)`. Of the four sub-classes of `7 (mod 64)`, `7`, `135`, and `199 (mod 256)` are covered, leaving `71`. Of the four sub-classes of `15 (mod 64)`, `15`, `79`, and `143` are covered, leaving `207`. Of the four sub-classes of `27 (mod 64)`, only `219` is covered as a full class modulo 256; `27`, `91`, and `155` are not covered as full modulo-256 classes, though `2587 (mod 4096)` is covered inside `27`. Of the four sub-classes of `31 (mod 64)`, only `95` is covered; `31`, `159`, and `223` remain. Of the four sub-classes of `39 (mod 64)`, only `39` is covered, leaving `103`, `167`, and `231`. Of the four sub-classes of `47 (mod 64)`, only `175` is covered, leaving `47`, `111`, and `239`. Of the four sub-classes of `59 (mod 64)`, `59`, `123`, and `187` are covered, leaving `251`. The full class `63 (mod 64)` remains unhandled by these certificates.

## Work plan

1. **Fix the definitions and proof target.** Keep the original map and odd-only map explicit. The descent property above is the global obligation.
2. **Work from exact identities.** Derive consequences of the Syracuse recurrence symbolically, keeping each equality and inequality justified for arbitrary odd starting values. The iterate identity, exact valuation-one run length, return-block formulas, modulo-3 restriction, transition law, logarithmic block drift, and state-dependent block contraction threshold are proved above.
3. **Exclude cycle profiles by their number of high valuations.** The exactly-one-high and exactly-two-high profiles are excluded above. An exactly-three-high cycle cannot have a quotient `u_i=1`; its period is at most `34`, and the exact transition equations exclude `T=5`. Exclude the five remaining totals `{10,17,22,29,34}`, then handle profiles with four or more high blocks. Ruling out every nontrivial odd-only cycle is sufficient for the full conjecture by the cycle-exclusion reduction.
4. **Keep the proof uniform in the starting value.** Seek identities and inequalities that apply to every odd `n`. Treat the finite congruence certificates below as supplementary lemmas; do not use more residue enumeration as a substitute for the global argument.
5. **Audit the complete argument.** Check boundary values, the valuation recurrence, and every induction dependency. Keep conjectures, computational observations, and proved statements labeled separately.

## Proof map

```mermaid
flowchart TD
    C["Full Collatz conjecture"] <-->|equivalent| D["Odd descent: every odd n above 1 has a smaller iterate"]
    C <-->|equivalent| Q["No nontrivial odd-only cycles"]
    D --> H["Assume descent fails; choose the least failing n"]
    H --> N["All iterates stay at or above n"]
    N --> R["Minimality forces strictly decreasing future records"]
    R --> Y["A record returns to n, giving a nontrivial cycle"]
    Y -.-> Q
    N --> I["Exact iterate and cycle identities — proved"]
    Q --> I
    I --> B["Return-block and transition formulas — proved"]
    B --> H1["One high-valuation block — excluded"]
    H1 --> H2["Two high-valuation blocks — excluded"]
    H2 --> H3["Three high-valuation blocks — T ≤ 34; T=5 excluded"]
    H3 --> O["OPEN: eliminate five three-high totals and control profiles with 4+ high valuations"]
    B --> O
```

## Archived finite computation (not part of the proof strategy)

An earlier exact-integer check covered starting values from 1 through 100,000. Its maximum stopping time was 350 at `n = 77,031`, and its maximum value was 1,570,824,736 from `n = 77,671`. These bounded observations establish no claim about untested inputs and are not used in the proof map.

## Literature waypoint

Terence Tao proved that for every function `f(n)` tending to infinity, almost every positive integer in logarithmic density has a Collatz orbit that reaches a value below `f(n)`. This is a deep partial result, but its “almost every” conclusion is not the all-integers statement required here: [Tao, *Almost all orbits of the Collatz map attain almost bounded values* (2019)](https://arxiv.org/abs/1909.03562).

A 2026 exploratory paper on burst/gap dynamics explicitly leaves its key orbitwise hypotheses open, illustrating why a heuristic contraction picture must not be presented as a proof: [Chang, *Exploring Collatz Dynamics with Human-LLM Collaboration* (2026)](https://arxiv.org/abs/2603.11066).

## Status

Several exact iterate, valuation, and return-block identities are proved, along with supplementary descent results on selected congruence classes. The exactly-one-high and exactly-two-high cycle profiles are excluded. Any exactly-three-high cycle must have all `u_i≥3` and period `T≤34`; the exact transition equations exclude `T=5`, leaving `T∈{10,17,22,29,34}` unresolved. Profiles with four or more high valuations also remain open. The full Collatz conjecture has not been proved in this project; the strict proof-completion estimate is 0%.
