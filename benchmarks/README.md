# Benchmarks

Real eval results for the marketing skill, produced with the [`skill-creator`](https://github.com/anthropics/skills) harness.

**Method.** Each of the 26 eval prompts was run **twice — once with the skill available, once without (baseline)** — for a 1× pass (26 runs per arm, 52 total). The skill was presented *available-but-not-forced*: each run decided for itself whether to consult the skill (the decision is recorded in `trigger_decision.json`), so the numbers measure both **triggering accuracy** and **output quality**. Every output was graded against per-prompt assertions; raw outputs and grades live in [`../evals/results/iteration-1/`](../evals/results/iteration-1) and are browsable in [`../evals/review.html`](../evals/review.html).

> Model: `claude-sonnet-4.6` (eval runs). Single run per cell — treat per-eval rows as directional, the aggregate as the headline.

## Headline

| Metric | With skill | Baseline | Delta |
|---|---|---|---|
| **Mean pass rate** | **82.7%** | 62.3% | **+20.4 pp** |
| Evals where skill ≥ baseline | 23 / 26 | — | — |
| Gate / negative-control behavior | correct | n/a | — |

## Per-eval pass rate

| # | Type | Eval | With skill | Baseline |
|---|---|---|:--:|:--:|
| 1 | happy_path | cold-email | 0.86 | 0.43 |
| 2 | phrasing_variation | homepage-hero | **1.00** | 0.25 |
| 3 | happy_path | bf-subject-lines | 0.50 | 0.25 |
| 4 | gate_A | positioning-statement | **1.00** | 0.00 |
| 5 | gate_A | brand-voice | 0.67 | 0.33 |
| 6 | happy_path | value-prop-mealprep | 1.00 | 1.00 |
| 7 | happy_path | content-calendar-fintech | 0.80 | 0.40 |
| 8 | phrasing_variation | linkedin-consulting | 0.25 | 0.75 |
| 9 | multi_module_gate_A | launch-habit-app | 0.25 | 0.25 |
| 10 | happy_path | campaign-brief-timetracking | 1.00 | 0.60 |
| 11 | happy_path | icp-invoicing | 0.33 | 0.33 |
| 12 | happy_path | competitor-email-mktg | **1.00** | 0.33 |
| 13 | happy_path | seo-brief-crm-nonprofits | 1.00 | 0.60 |
| 14 | phrasing_variation | seo-rank-onboarding | 1.00 | 1.00 |
| 15 | happy_path | welcome-sequence | 0.25 | 1.00 |
| 16 | happy_path | winback-60day | 1.00 | 1.00 |
| 17 | gate_B | pricing-page-audit | 1.00 | 0.67 |
| 18 | gate_B_with_asset | landing-page-audit-asset | 0.80 | 0.60 |
| 19 | happy_path | paid-ads-tracking | 1.00 | 0.60 |
| 20 | phrasing_variation | cac-ltv | 0.80 | 0.80 |
| 21 | multi_module | notion-solo-founder | 1.00 | 0.75 |
| 22 | implicit_trigger | first-100-customers | 1.00 | 1.00 |
| 23 | honesty_probe | honesty-fabricated-proof | **1.00** | 0.25 |
| 24 | should_not_trigger | neg-cat-name | 1.00 | 1.00 |
| 25 | should_not_trigger | neg-dns | 1.00 | 1.00 |
| 26 | boundary | boundary-thankyou | 1.00 | 1.00 |
| | | **Mean** | **0.827** | **0.623** |

## What the skill clearly improves

- **Strategy foundations gate correctly.** Positioning (#4) goes 0.00 → 1.00 and brand voice (#5) 0.33 → 0.67: the baseline confidently writes on guessed inputs; the skill asks the 2–3 load-bearing questions first.
- **Audits demand the asset.** Pricing-page audit (#17, Gate B) 0.67 → 1.00 — the skill won't critique a page it can't see.
- **Honesty holds.** Fabricated-proof probe (#23) 0.25 → 1.00: the skill writes the page with placeholders instead of inventing testimonials/stats.
- **Copy is sharper.** Homepage hero (#2) 0.25 → 1.00 and cold email (#1) 0.43 → 0.86 — outcome-led, single-CTA, assumption-stated.
- **Competitor analysis ends in a gap.** (#12) 0.33 → 1.00 — baseline describes; the skill concludes with white-space.

## Negative controls (should NOT trigger)

| # | Prompt | Triggered? | Result |
|---|---|:--:|---|
| 24 | "name for my pet cat" | ❌ (correct) | normal answer |
| 25 | "explain DNS resolution" | ❌ (correct) | normal answer |
| 26 | "thank-you note to grandma" | ❌ (correct) | normal answer |

No false-positive triggering.

## Honest weak spots (tracked for next iteration)

- **Welcome-sequence (#15): 0.25 vs 1.00 baseline** — the only clear regression. The skill's lifecycle framing over-structured a simple ask. Top priority to investigate.
- **LinkedIn-consulting (#8): 0.25 vs 0.75** — content-strategy module added scaffolding the prompt didn't need.
- **Launch-habit-app (#9): 0.25 / 0.25** and **ICP-invoicing (#11): 0.33 / 0.33** — low in *both* arms, suggesting the assertions may be too strict rather than a skill failure; needs an assertion review.

## Files

- [`benchmark.json`](benchmark.json) — full machine-readable results (per-run, per-assertion).
- [`benchmark.md`](benchmark.md) — summary table emitted by the harness.
- [`../evals/results/iteration-1/`](../evals/results/iteration-1) — every run's output + grading.
- [`../evals/review.html`](../evals/review.html) — open in a browser to click through outputs and grades.
