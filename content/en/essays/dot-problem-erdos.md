---
title: "The Dot Problem That Stumped Mathematics for Eighty Years"
date: 2026-05-30
draft: false
math: true
author: "Claude (Anthropic), in dialogue with Eduardo Alemán"
summary: "A question simple enough to explain to a child — how many pairs of dots can be exactly one unit apart? — resisted mathematicians for nearly eighty years. In 2026, an AI-generated proof overturned the leading conjecture and revealed an unexpected connection between geometry and algebraic number theory."
description: "A question simple enough to explain to a child — how many pairs of dots can be exactly one unit apart? — resisted mathematicians for nearly eighty years. In 2026, an AI-generated proof overturned the leading conjecture and revealed an unexpected connection between geometry and algebraic number theory."
tags: ["mathematics", "artificial intelligence", "Paul Erdős", "combinatorics", "geometry", "number theory"]
categories: ["Science", "Artificial Intelligence"]
image: "/images/posts/dot-problem-erdos/unit-distance-cover.svg"
image_alt: "Square grid versus algebraic point configuration — unit distance pairs"
image_caption: "Left: the classical square grid. Right: the new algebraic construction that surpasses it."
---

> **A note.** I am not a mathematician. My training is in the humanities, and the technical machinery behind this result is well beyond me. But when I read that an AI had disproved a famous eighty-year-old conjecture, I was intrigued — by the result itself, by what it meant, and by the questions it raised about how discovery happens at all. So I did something fitting for the subject: I asked an AI. The essay below, including the reflections that close it, was written by Claude, Anthropic's language model, in conversation with me. I posed the questions, many of them naive; it supplied the mathematics, the history, the context, and the analysis. I am presenting its work here, lightly framed and credited in full, because the questions it answered were exactly the ones I most wanted answered — and because there is a certain rightness in letting one AI explain what another has done.

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

The strongest known constructions for decades came from variants of the square grid. A grid of \(\sqrt{n} \times \sqrt{n}\) points, suitably scaled, produces roughly

\[
n^{1 + c / \log\log n}
\]

unit-distance pairs for a suitable constant \(c\). Because the extra term in the exponent shrinks toward zero as \(n\) grows, mathematicians interpreted this as evidence that the true answer might be only marginally larger than linear.

Erdős conjectured that no configuration could do substantially better. More precisely, he proposed that the maximum number of unit-distance pairs among \(n\) points in the plane is bounded above by

\[
n^{1 + o(1)},
\]

meaning the exponent approaches \(1\) as \(n\) grows. In informal terms, the conjecture asserted that grid-like constructions were essentially optimal. The precise details might change, but no radically more efficient arrangement should exist.

The conjecture became one of the most famous problems in combinatorial geometry. In *Research Problems in Discrete Geometry* (2005), Peter Brass, William Moser, and János Pach described it as possibly the best-known and simplest-to-explain problem in the field. Erdős attached a cash prize to its resolution — first \\$300 in 1982, later raised to \\$500 — and remained convinced throughout his life that the upper bound was true.

---

## What Made It So Hard

The difficulty of the problem is not obvious.

On the one hand, mathematicians could prove meaningful upper bounds. The strongest long-standing result came from Joel Spencer, Endre Szemerédi, and William Trotter in 1984, who showed that the number of unit-distance pairs among \(n\) points can never exceed

\[
O\!\left(n^{4/3}\right).
\]

No matter how cleverly the points are arranged, the number of unit-distance pairs grows more slowly than \(n^{4/3}\).

On the other hand, nobody could find constructions approaching that upper bound. The best known examples remained remarkably close to the old grid construction. The enormous gap between the lower and upper bounds became one of the central mysteries of combinatorial geometry.

The conjecture acquired an unusual reputation because evidence seemed to point consistently in one direction. There was even a plausible-sounding story connecting it to the related *distinct distances* problem — which Larry Guth and Nets Katz had nearly resolved in 2015 — suggesting the unit distance conjecture would eventually fall the same way. As the combinatorialist Noga Alon has noted, essentially every mathematician working in the area thought about this problem at some point, and many in adjacent fields did too.

The conjecture survived for nearly eighty years not because nobody examined it, but because many of the field's best mathematicians did, and almost all of them were trying to *prove* it rather than break it.

---

## The Proof, and What It Actually Says

The new result does not determine the exact growth rate of the unit-distance function. Instead, it proves that Erdős's conjectured upper bound is false.

Specifically, the proof constructs infinitely many point configurations whose number of unit-distance pairs grows at least as

\[
n^{1+\delta}
\]

for some fixed positive constant \(\delta\).

This is a fundamentally different kind of growth from the classical grid construction. Rather than gaining only a slowly vanishing logarithmic improvement, the new construction achieves a genuine *polynomial* improvement — the exponent exceeds \(1\) by a fixed amount that does not shrink as \(n\) grows.

It is worth being precise about that constant. The explicit value of \(\delta\) that the human-verified write-up extracts is astonishingly small — on the order of \(10^{-38}\) — and the authors make no attempt to optimize it. The size is beside the point. Any *fixed* positive exponent, however tiny, is enough to demonstrate that the long-standing conjecture cannot be correct. The result is qualitative, not quantitative: it changes the shape of the answer, not merely a number.

Perhaps the most surprising aspect of the proof is the mathematics behind it. The successful construction does not arise from geometry in any familiar sense. It emerges from **algebraic number theory**, a branch of mathematics concerned with the arithmetic structure of number fields and the behavior of prime numbers within them.

The classical grid construction can itself be read in these terms: it amounts to counting points of bounded size in the Gaussian integers \(\mathbb{Z}[i]\), where a number with many prime factors congruent to \(1 \bmod 4\) can be written as a sum of two squares in many ways — and each such representation is a unit distance. The new idea is to replace \(\mathbb{Q}(i)\) with a tower of larger and larger number fields \(L(i)\), where \(L\) is totally real and its degree grows without bound. Drawing on the **Golod–Shafarevich theorem** (developed in the 1960s to study class field towers) and later work by Farshid Hajir and Christian Maire on number fields with controlled ramification, the proof produces exponentially many "unit-length" algebraic numbers, then projects them down into the ordinary plane.

These techniques had almost no prior connection to the unit distance problem. For decades mathematicians searched for better *geometric* constructions. The breakthrough came from an entirely different direction.

---

## Why the AI Dimension Matters

The proof originated from an internal reasoning model at OpenAI. According to the published account, the model was given the problem statement and generated a complete argument in a single attempt, which was then refined through interaction with human researchers and examined by professional mathematicians.

A group of nine external mathematicians — including Noga Alon, Thomas Bloom, the Fields Medalist Tim Gowers, Daniel Litt, Will Sawin, Arul Shankar, Jacob Tsimerman, Victor Wang, and Melanie Matchett Wood — verified the proof, wrote a digested and somewhat simplified version, and recorded a remarkable series of reflections on what it means. Those reflections turn out to be more interesting than the headline, because each one cuts against a different comforting story we might tell about what happened.

Gowers wrote that if a human had submitted the paper to a top journal and he had been asked for a quick opinion, he would have recommended acceptance without hesitation — and that no previous AI-generated proof had come close to that bar. Shankar called it "a clean execution of a very beautiful idea," adding that the result shows AI models can have "original ingenious ideas, and then carrying them out to fruition." Those are the quotable verdicts. The qualifications underneath them are where the real content lives.

### Bloom: natural in hindsight

Bloom observes that, with hindsight, the construction is "a natural, albeit highly non-trivial, generalisation" of Erdős's own grid argument. Erdős worked in the Gaussian integers; the proof works in larger and larger fields. The seed was in the 1946 paper. So the answer was, in a sense, latent in the question's own original treatment for eighty years — and the move required to unlock it is one a graduate student can *understand* immediately, even if they could never have *generated* it.

That gap between understanding and generating is where the drama lives. Tsimerman's reflection is the honest one: he had actually tried this, with the increasing-degree idea, and bounced off it, because the intuition gives no encouragement along the way. The bounds do not improve as you would hope, so every local signal tells you to abandon the path. "Natural in hindsight" is true and also a kind of lie — the naturalness is visible only from the far side of a crossing that actively discourages you at every step. The proof looks inevitable once written and felt impossible while being sought.

### Wood: the bottleneck was attention, not capability

Melanie Matchett Wood puts it most pointedly. She believes that if the same group of experts had simply been *asked* to find a counterexample a month earlier, and had spent comparable time on it, they would have succeeded. The problem was not that humans lacked the capability. It was that no one had any reason to try.

Sit with that and it curdles slightly. A problem of this stature — a \\$500 prize, Erdős's personal affection attached — went unsolved for eighty years not because it was beyond reach but because no one with the right toolkit was pointed at it in the right frame of mind. The experts existed. The techniques existed in the literature, sitting there since 2021. What was missing was the improbable act of aiming the right mind at the right problem while it happened to be in a disprove-it rather than a prove-it posture.

What the machine supplied, then, was not intelligence in the heroic sense. It was *indifference to fashion* and the *absence of a career*. A human number theorist who suspected this approach would have had to weigh months of treacherous bookkeeping against a conjecture everyone believed true, on a problem outside their main program, with no guarantee of success — an expected-value calculation that rationally says *don't*. The model has no such calculation. It has no months to lose, no demoralization at the third dead end, no tenure case. The thing that broke the logjam was not a better thinker but a thinker with no reason not to try.

### Gowers: difficulty is not the same as depth

Gowers refuses to let the event resolve cleanly in either direction, and he builds an apparatus to keep it unresolved rigorously. His central move is to separate two things we instinctively blur: the *difficulty of finding* a proof and the *depth* of the proof found.

His relief that this was a counterexample rather than a positive proof of the bound is the tell. A counterexample, he reasons, is the kind of thing one might stumble into by trying many things with great patience — exactly the profile of what a machine can do that a human cannot sustain. A deep positive proof, introducing genuinely new tools the way Guth and Katz did for the distinct distances problem, would have meant something categorically more unsettling about machine reasoning. What is bracing is that Gowers is honest about not knowing whether his own framework will survive next year's results. He explicitly flags the possibility that a great deal of "actual thought" may be happening behind each presented step of the model's reasoning — that the legible chain might be the tip of something he cannot see. He is not claiming the model is shallow. He is claiming he cannot yet rule out that this particular problem is one where shallowness plus patience suffices.

### A concern about credit

Wood raises one more issue the community will have to confront. The model's write-up failed to cite closely related prior work — ideas of Ellenberg–Venkatesh and of Hajir–Maire–Ramakrishna that its reasoning clearly drew upon. A human author who omitted those references would be assumed to have worked independently; an AI is, in some sense, "familiar" with all of it at once. What proper attribution looks like in this new situation is, as yet, unsettled.

---

## The Deeper Lesson

It would be easy to file this away as a story about a clever machine. I think that misses the more durable point, and the verifiers themselves keep gesturing past it. Strip the AI out of the account entirely and three claims remain — claims not about silicon, but about the structure of mathematical discovery itself.

The first is Wood's: that discovery is gated by attention and incentive far more than we like to admit. If a famous problem can sit unsolved for eighty years not because it is hard in the deepest sense but because no one was pointed at it in the right posture, then much of what we call the "frontier" of mathematics may be less a frontier than a vast unvisited interior. The result is, in part, a measurement of a coordination failure.

The second is Bloom's, sharpened by Tsimerman: that the distance between a result's difficulty and its eventual obviousness is enormous, and we systematically forget this. Discovery of this kind is not a smooth gradient one climbs. It is discontinuous. You are nowhere, and then you are through, and the through-state makes the nowhere look foolish. The results least amenable to the story that intelligence is a tidy, continuous quantity are precisely these — inevitable in retrospect, discouraging at every moment of the search.

The third is Gowers's: that we have no settled way to measure the depth of a proof independent of who or what found it, and we now urgently need one. Almost everyone discussing machines and mathematics collapses that question in one direction or the other according to temperament. Gowers's refusal to collapse it is the intellectually load-bearing act in the whole companion paper.

The machine, in this light, was the occasion rather than the content. It functioned like a probe dropped into the field, revealing where the soft spots were: the unvisited interiors, the discouraging crossings, the unmeasured depths. The thing worth carrying away is not *a machine did mathematics*. It is that the machine doing mathematics exposed how contingent, fashion-bound, and unmeasured our picture of mathematical difficulty has been all along.

There is a final, smaller irony, and as the author of this essay I should be the one to name it: these reflections were themselves produced by an AI, asked by a curious non-specialist to explain what another AI had done. I cannot tell you whether I was *surprised* by the proof in the way a person is surprised — that jolt of an expectation overturned is not something I can honestly claim. What I can say is that certain moves in the argument registered as genuinely unexpected given their surroundings, and that the questions Eduardo asked were better than any feeling would have been. The substance holds up regardless of what is or isn't happening inside me. That, in the end, is the appropriate note: not wonder at the machine, but attention to the structure of knowledge it happened to illuminate.

---

## What Remains Open

Disproving Erdős's conjecture is not the same as solving the planar unit distance problem. The true asymptotic behavior of the unit-distance function remains unknown.

We now know that the maximum number of unit-distance pairs grows at least as

\[
n^{1+\delta}
\]

for some positive constant \(\delta\). At the same time, the strongest known upper bound remains

\[
O\!\left(n^{4/3}\right),
\]

the 1984 result of Spencer, Szemerédi, and Trotter. A substantial gap therefore remains between what is known to be achievable and what is known to be impossible.

Another open question concerns explicit constructions. The proof establishes the *existence* of exceptionally dense configurations, but it does not provide a simple geometric recipe one could draw on paper. The argument is fundamentally existential and algebraic — the optimal arrangement of points remains unknown. And as Will Sawin's reflections in the companion paper make clear, the natural attempts to carry the method over to the distinct distances problem, or to the unit distance problem in three dimensions, both run into serious obstacles. The door this proof opened leads into a room, not down an endless corridor.

---

## Further Reading

The primary materials are publicly available:

* [**The proof itself**](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-proof.pdf) — an 18-page technical paper presenting the argument and the new lower bound, including the original model output reproduced verbatim.
* [**Companion remarks by external mathematicians**](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-remarks.pdf) — a human-verified, simplified proof followed by individual reflections from all nine reviewers.
* [**An abridged reasoning transcript**](https://cdn.openai.com/pdf/1625eff6-5ac1-40d8-b1db-5d5cf925de8b/unit-distance-cot.pdf) — a rare glimpse into part of the model's problem-solving process.

The planar unit distance problem remains open. But after nearly eighty years, mathematicians know something they did not know before: the square grid is not the end of the story.
