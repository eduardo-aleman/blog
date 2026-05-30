---
title: "The Dot Problem That Stumped Mathematics for Eighty Years"
date: 2026-05-30
draft: false
math: true
description: "A question simple enough to explain to a child — how many pairs of dots can be exactly one unit apart? — resisted mathematicians for nearly eighty years. In 2026, an AI-generated proof overturned the leading conjecture and revealed an unexpected connection between geometry and algebraic number theory."
summary: "A question simple enough to explain to a child — how many pairs of dots can be exactly one unit apart? — resisted mathematicians for nearly eighty years. In 2026, an AI-generated proof overturned the leading conjecture and revealed an unexpected connection between geometry and algebraic number theory."
tags: ["mathematics", "artificial intelligence", "Paul Erdős", "combinatorics", "geometry", "number theory"]
categories: ["Science", "Artificial Intelligence"]
image: "/images/posts/dot-problem-erdos/unit-distance-cover.svg"
image_alt: "Square grid versus algebraic point configuration — unit distance pairs"
image_caption: "Left: the classical square grid. Right: the new algebraic construction that surpasses it."
---

## A Problem Anyone Can Understand

Take a sheet of paper and place some dots on it.

Now ask a deceptively simple question: **how many pairs of dots can be exactly one unit apart?**

With only a handful of points, the answer is easy to visualize. Four points arranged as the corners of a unit square give four unit-distance pairs, one along each edge. But as the number of points grows, the problem quickly becomes surprisingly difficult. If you have one hundred points, or one thousand, or a million, what arrangement maximizes the number of pairs separated by exactly one unit?

That question is known as the **planar unit distance problem**. It was posed by the Hungarian mathematician Paul Erdős in 1946 and became one of the most famous unsolved problems in combinatorial geometry. Its appeal lies in the contrast between statement and solution: almost anyone can understand the question immediately, yet generations of mathematicians failed to determine the correct answer.

In May 2026, an AI-generated proof overturned the leading conjecture about the problem and changed what mathematicians thought they knew about it. Rather than settling the problem completely, the proof showed that the most widely believed answer was wrong.

---

## Paul Erdős and the Grid Conjecture

Paul Erdős was one of the most prolific mathematicians of the twentieth century. Living largely out of a suitcase, he traveled continuously between universities, collaborating with hundreds of researchers and posing problems that would shape entire fields. Among them was a deceptively innocent question he included in a 1946 paper in the *American Mathematical Monthly*.

The strongest known constructions for decades came from variants of the square grid. A grid of $\sqrt{n} \times \sqrt{n}$ points, suitably scaled, produces roughly

$$
n^{1 + c / \log\log n}
$$

unit-distance pairs for a suitable constant $c$. Because the extra term in the exponent shrinks toward zero as $n$ grows, mathematicians interpreted this as evidence that the true answer might be only marginally larger than linear.

Erdős conjectured that no configuration could do substantially better. More precisely, he proposed that the maximum number of unit-distance pairs among $n$ points in the plane is bounded above by

$$
n^{1 + o(1)},
$$

meaning the exponent approaches $1$ as $n$ grows. In informal terms, the conjecture asserted that grid-like constructions were essentially optimal. The precise details might change, but no radically more efficient arrangement should exist.

The conjecture became one of the most famous problems in combinatorial geometry. In *Research Problems in Discrete Geometry* (2005), Peter Brass, William Moser, and János Pach described it as possibly the best-known and simplest-to-explain problem in the field. Erdős attached a cash prize to its resolution — first \$300 in 1982, later raised to \$500 — and remained convinced throughout his life that the upper bound was true.

---

## What Made It So Hard

The difficulty of the problem is not obvious.

On the one hand, mathematicians could prove meaningful upper bounds. The strongest long-standing result came from Joel Spencer, Endre Szemerédi, and William Trotter in 1984, who showed that the number of unit-distance pairs among $n$ points can never exceed

$$
O\!\left(n^{4/3}\right).
$$

No matter how cleverly the points are arranged, the number of unit-distance pairs grows more slowly than $n^{4/3}$.

On the other hand, nobody could find constructions approaching that upper bound. The best known examples remained remarkably close to the old grid construction. The enormous gap between the lower and upper bounds became one of the central mysteries of combinatorial geometry.

The conjecture acquired an unusual reputation because evidence seemed to point consistently in one direction. There was even a plausible-sounding story connecting it to the related *distinct distances* problem — which Larry Guth and Nets Katz had nearly resolved in 2015 — suggesting the unit distance conjecture would eventually fall the same way. As the combinatorialist Noga Alon has noted, essentially every mathematician working in the area thought about this problem at some point, and many in adjacent fields did too.

The conjecture survived for nearly eighty years not because nobody examined it, but because many of the field's best mathematicians did, and almost all of them were trying to *prove* it rather than break it.

---

## The Proof, and What It Actually Says

The new result does not determine the exact growth rate of the unit-distance function. Instead, it proves that Erdős's conjectured upper bound is false.

Specifically, the proof constructs infinitely many point configurations whose number of unit-distance pairs grows at least as

$$
n^{1+\delta}
$$

for some fixed positive constant $\delta$.

This is a fundamentally different kind of growth from the classical grid construction. Rather than gaining only a slowly vanishing logarithmic improvement, the new construction achieves a genuine *polynomial* improvement — the exponent exceeds $1$ by a fixed amount that does not shrink as $n$ grows.

It is worth being precise about that constant. The explicit value of $\delta$ that the human-verified write-up extracts is astonishingly small — on the order of $10^{-38}$ — and the authors make no attempt to optimize it. The size is beside the point. Any *fixed* positive exponent, however tiny, is enough to demonstrate that the long-standing conjecture cannot be correct. The result is qualitative, not quantitative: it changes the shape of the answer, not merely a number.

Perhaps the most surprising aspect of the proof is the mathematics behind it. The successful construction does not arise from geometry in any familiar sense. It emerges from **algebraic number theory**, a branch of mathematics concerned with the arithmetic structure of number fields and the behavior of prime numbers within them.

The classical grid construction can itself be read in these terms: it amounts to counting points of bounded size in the Gaussian integers $\mathbb{Z}[i]$, where a number with many prime factors congruent to $1 \bmod 4$ can be written as a sum of two squares in many ways — and each such representation is a unit distance. The new idea is to replace $\mathbb{Q}(i)$ with a tower of larger and larger number fields $L(i)$, where $L$ is totally real and its degree grows without bound. Drawing on the **Golod–Shafarevich theorem** (developed in the 1960s to study class field towers) and later work by Farshid Hajir and Christian Maire on number fields with controlled ramification, the proof produces exponentially many "unit-length" algebraic numbers, then projects them down into the ordinary plane.

These techniques had almost no prior connection to the unit distance problem. For decades mathematicians searched for better *geometric* constructions. The breakthrough came from an entirely different direction.

---

## Why the AI Dimension Matters

The proof originated from an internal reasoning model at OpenAI. According to the published account, the model was given the problem statement and generated a complete argument in a single attempt, which was then refined through interaction with human researchers and examined by professional mathematicians.

A group of nine external mathematicians — including Noga Alon, Thomas Bloom, the Fields Medalist Tim Gowers, Daniel Litt, Will Sawin, Arul Shankar, Jacob Tsimerman, Victor Wang, and Melanie Matchett Wood — verified the proof, wrote a digested and somewhat simplified version, and recorded a remarkable series of reflections on what it means.

Their assessments are worth reading carefully, because they are more nuanced than the headlines suggest.

Gowers wrote that if a human had submitted the paper to a top journal and he had been asked for a quick opinion, he would have recommended acceptance without hesitation — and that no previous AI-generated proof had come close to that bar. Shankar called it "a clean execution of a very beautiful idea," adding that the result demonstrates AI models can have "original ingenious ideas, and then carry them out to fruition."

But several of the verifiers push back on the most dramatic interpretation. Bloom observes that, with hindsight, the construction is "a natural, albeit highly non-trivial, generalisation" of Erdős's own grid argument — the reason no one found it was a confluence of unlikely circumstances: you needed someone willing to spend serious time *disproving* a conjecture nearly everyone believed true, willing to bet on exotic number fields, and fluent in the precise corner of class field theory required. The AI met all of those conditions at once, mainly by being patient and unbiased rather than by being brilliant in a way no human could be.

Wood puts it most pointedly: she believes that if the same group of experts had simply been *asked* to find a counterexample a month earlier, and had spent comparable time on it, they would have succeeded. The problem was not that humans lacked the capability — it was that no one had any reason to try. The AI's real contribution may have been to redirect expert attention to a question the community had collectively written off.

Whether such systems "understand" mathematics in a human sense remains a philosophical question. The mathematical result, however, is objective: the proof is either correct or incorrect. Experts concluded that it is correct.

Wood also raises a sharper concern the community will need to confront. The model's write-up failed to cite closely related prior work — ideas of Ellenberg–Venkatesh and of Hajir–Maire–Ramakrishna that its reasoning clearly drew upon. A human author who omitted those references would be assumed to have worked independently; an AI is, in some sense, "familiar" with all of it. What proper attribution looks like in this new situation is, as yet, unsettled.

---

## What Remains Open

Disproving Erdős's conjecture is not the same as solving the planar unit distance problem. The true asymptotic behavior of the unit-distance function remains unknown.

We now know that the maximum number of unit-distance pairs grows at least as

$$
n^{1+\delta}
$$

for some positive constant $\delta$. At the same time, the strongest known upper bound remains

$$
O\!\left(n^{4/3}\right),
$$

the 1984 result of Spencer, Szemerédi, and Trotter. A substantial gap therefore remains between what is known to be achievable and what is known to be impossible.

Another open question concerns explicit constructions. The proof establishes the *existence* of exceptionally dense configurations, but it does not provide a simple geometric recipe one could draw on paper. The argument is fundamentally existential and algebraic — the optimal arrangement of points remains unknown.

---

## Why This Matters

Three separate developments make this result significant.

### A famous conjecture was overturned

For decades mathematicians believed that grid-like arrangements captured the essential behavior of the problem. The new construction shows that intuition was incomplete. A major piece of accepted mathematical folklore turned out to be false — a reminder that even very good intuition, reinforced by decades of evidence, can be systematically wrong.

### The proof reveals an unexpected bridge between fields

Questions about points in the plane are usually approached through geometry and combinatorics. The successful attack came instead from deep algebraic number theory. As Bloom predicts, algebraic number theorists are now likely to take a hard look at other open problems in discrete geometry — and whether similar ideas can illuminate the distinct distances problem, or the unit distance problem in three dimensions, remains genuinely open. (Will Sawin's reflections in the companion paper suggest both of those generalizations face serious obstacles.)

### It marks a milestone in AI-assisted mathematics

Modern AI systems had already shown they could assist with calculations and routine arguments. This goes further: the key conceptual ideas appear to have originated from the model before being checked and refined by human experts. Mathematics is a particularly demanding test, because proofs can be verified — either the argument works or it does not. In this case, it does.

The honest framing, though, is the one the verifiers themselves reached. This is not a machine doing something no human could ever do. It is a machine doing something humans *could* have done but didn't — exploring an unfashionable path with inhuman patience and an encyclopedic command of the literature, and in doing so, pulling expert attention back to a question everyone had given up on.

---

## Further Reading

The primary materials are publicly available:

* [**The proof itself**](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-proof.pdf) — an 18-page technical paper presenting the argument and the new lower bound, including the original model output reproduced verbatim.
* [**Companion remarks by external mathematicians**](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-remarks.pdf) — a human-verified, simplified proof followed by individual reflections from all nine reviewers.
* [**An abridged reasoning transcript**](https://cdn.openai.com/pdf/1625eff6-5ac1-40d8-b1db-5d5cf925de8b/unit-distance-cot.pdf) — a rare glimpse into part of the model's problem-solving process.

The planar unit distance problem remains open. But after nearly eighty years, mathematicians know something they did not know before: the square grid is not the end of the story.
