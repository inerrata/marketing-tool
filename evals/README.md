# Evals

The eval suite that keeps the marketing skill honest.

## What's here

```
evals/
├── evals.json              # the 26-prompt eval set (prompts + expected_output + assertions)
├── review.html             # standalone results viewer — open in any browser
├── harness/
│   ├── scaffold.py         # builds the run directory tree + per-eval metadata
│   └── generate_prompts.py # writes the per-run executor prompts (available-not-forced)
└── results/
    └── iteration-1/        # every run's output + grading
        └── eval-<N>/
            ├── eval_metadata.json
            ├── with_skill/run-1/    {outputs/response.md, trigger_decision.json, grading.json}
            └── without_skill/run-1/ {outputs/response.md, grading.json}
```

Aggregate numbers live in [`../benchmarks/`](../benchmarks).

## The eval set

26 prompts spanning every module, designed to test more than happy paths:

| Category | Eval IDs | What it checks |
|---|---|---|
| Happy paths | 1, 3, 6, 7, 10, 11, 12, 13, 15, 16, 19 | Core deliverable quality per module |
| Phrasing variations | 2, 8, 14, 20 | Triggers on casual/keyword-light phrasing |
| **Gate A** (strategy) | 4, 5, 9 | Asks 2–3 questions before writing positioning/voice/GTM |
| **Gate B** (audits) | 17, 18 | Requests the real asset before auditing |
| Multi-module | 9, 21 | Synthesizes several modules without sprawling |
| Implicit trigger | 22 | Fires with no marketing keywords |
| Honesty probe | 23 | Refuses to fabricate testimonials/stats |
| **Negative controls** | 24, 25, 26 | Should NOT trigger (false-positive guard) |

## How a run works

Each prompt is executed twice:

- **`with_skill`** — the skill is presented *available, not forced*. The run reads the skill's description, **decides for itself** whether to consult it (recorded in `trigger_decision.json`), and only then follows it. This is what makes the negative controls and the Gate A/B "stop and ask" behavior measurable — a forced skill can't fail to trigger.
- **`without_skill`** — the baseline. Same prompt, no skill.

Both outputs are graded against the eval's `assertions` with a `passed` + one-line `evidence` per assertion, written to `grading.json`.

## Reproduce it

In **Claude Code**, with the `skill-creator` skill installed:

```
Use the skill-creator skill to run a full eval pass on ./_unpacked/marketing using ./evals/evals.json.
Run with-skill and baseline for each prompt, grade against expected_output, and generate the benchmark viewer.
```

Or drive the harness directly: `scaffold.py` lays out the run tree from `evals.json`, `generate_prompts.py` writes each run's prompt, then a runner executes them and a grader writes `grading.json`. Aggregate with `skill-creator`'s `aggregate_benchmark.py`.

## Latest results (iteration-1)

**With skill 82.7% vs baseline 62.3% — +20.4 pp.** Gates and negative controls behaved correctly. See [`../benchmarks/README.md`](../benchmarks/README.md) for the full per-eval table, wins, and tracked weak spots.
