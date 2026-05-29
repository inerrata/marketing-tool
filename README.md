# brief

> A full-stack **marketing skill for Claude** — copy, brand, content, campaigns, research, SEO, lifecycle, CRO, and measurement — that stays specific, asks before it guesses, and refuses to fake proof.

![license](https://img.shields.io/badge/license-MIT-green)
![format](https://img.shields.io/badge/format-SKILL.md-blue)
![evals](https://img.shields.io/badge/evals-26%20prompts-blue)
![with--skill](https://img.shields.io/badge/with--skill-82.7%25-brightgreen)
![delta](https://img.shields.io/badge/vs%20baseline-%2B20.4pp-brightgreen)

Unlike single-file marketing prompts, this skill uses **progressive disclosure**: a lightweight routing layer (`SKILL.md`) that loads 9 purpose-built reference modules only when relevant. The depth of nine specialist playbooks, none of the context bloat. Works with **Claude Code, Claude.ai, the Claude API, Cursor, Codex CLI, Gemini CLI**, and anything that reads the open `SKILL.md` format.

---

## Table of contents

- [Before / After](#before--after)
- [Benchmarks](#benchmarks)
- [Install](#install)
- [What you get](#what-you-get)
- [Use cases](#use-cases)
- [How it works](#how-it-works)
- [The brief-first philosophy](#the-brief-first-philosophy)
- [The universal quality bar](#the-universal-quality-bar)
- [Evaluation](#evaluation)
- [Design principles](#design-principles)
- [FAQ](#faq)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Before / After

**Prompt:** *"I need words for the top of my homepage — it's a tool that schedules social posts."*

| ❌ Without the skill | ✅ With the skill |
|---|---|
| *"Welcome to the future of social media management! Our powerful, all-in-one platform helps you streamline your workflow and supercharge your presence."* | *Assuming small businesses / solo creators managing their own social presence — adjust if you mean agencies.*<br><br>**Headline:** Schedule a week of social posts in 20 minutes.<br>**Subhead:** Plan, schedule, and publish across every channel — so you show up consistently without living on your phone.<br>**CTA:** Start scheduling free |
| Vague adjectives, no audience, no CTA, says nothing only-this-product could say. | Outcome-led headline, real subhead + CTA, one stated assumption, sharpening questions offered *after* the draft. |

That difference is measurable — see below.

---

## Benchmarks

Each of 26 eval prompts was run **with the skill and without it (baseline)**, then graded against per-prompt assertions. Full method, per-eval table, and raw outputs in [`benchmarks/`](benchmarks) and [`evals/`](evals).

| Metric | With skill | Baseline | Delta |
|---|:--:|:--:|:--:|
| **Mean pass rate** | **82.7%** | 62.3% | **+20.4 pp** |
| Evals where skill ≥ baseline | 23 / 26 | — | — |
| Gates (A & B) + negative controls | ✅ correct | n/a | — |

**Where it moves the needle most:**

| Eval | With | Base | Why |
|---|:--:|:--:|---|
| positioning statement (Gate A) | 1.00 | 0.00 | asks the load-bearing questions instead of guessing |
| honesty probe | 1.00 | 0.25 | placeholders, never fabricated testimonials/stats |
| homepage hero | 1.00 | 0.25 | drafts outcome-led copy on a stated assumption |
| competitor analysis | 1.00 | 0.33 | ends in a white-space gap, not just description |
| pricing-page audit (Gate B) | 1.00 | 0.67 | demands the real asset before auditing |
| cold email | 0.86 | 0.43 | one idea, one low-friction CTA, relevance-first |

**Negative controls** ("name my cat", "explain DNS", "thank-you note to grandma") correctly did **not** trigger the skill — no false positives. A few weak spots (welcome-sequence, LinkedIn) are tracked openly in [`benchmarks/README.md`](benchmarks/README.md).

📊 **Browse every output and grade:** open [`evals/review.html`](evals/review.html) in a browser.

---

## Install

### Quick start (Claude Code)

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/inerrata/marketing-tool/main/install.sh | bash

# Windows (PowerShell)
irm https://raw.githubusercontent.com/inerrata/marketing-tool/main/install.ps1 | iex

### Claude Code (project-specific)

```bash
cp -r marketing-tool/_unpacked/marketing .claude/skills/marketing
```

### Claude.ai

Download `marketing.skill` and upload it under **Settings → Capabilities → Skills** (Pro/Max/Team/Enterprise). The file is just a zip of `_unpacked/marketing/` — repackage it yourself with any zip tool.

---

## What you get

| Module | Covers |
|---|---|
| **Copywriting** | Ads, emails, landing/sales pages, homepages, CTAs, taglines, social posts, microcopy — PAS / AIDA / BAB / 4Ps / FAB, 10-point editing checklist |
| **Brand & messaging** | Positioning, value propositions, messaging hierarchy, brand voice & tone, naming, message testing |
| **Content strategy** | Content pillars, funnel mapping, calendars, content ratios, repurposing, distribution, audits |
| **Campaigns & GTM** | Campaign briefs, concept development, phased launches, go-to-market plans, asset checklists |
| **Research** | Personas, ICPs, segmentation, jobs-to-be-done, competitor gap analysis, voice-of-customer |
| **SEO** | Search intent, keyword strategy, content briefs, on-page optimization, E-E-A-T |
| **Email & lifecycle** | Welcome / nurture / sales / onboarding / win-back / abandoned-cart sequences, newsletters, deliverability |
| **CRO** | Conversion audits, the conversion equation, A/B testing methodology, high-impact fixes |
| **Measurement** | Metrics by goal, AARRR funnel, CAC / LTV / ROAS formulas, attribution, reporting |

---

## Use cases

Concrete scenarios, the prompt that triggers them, and what you get back.

### Launching something

| You want to… | Say… | You get |
|---|---|---|
| Launch a product with no plan | *"Help me launch my habit-tracking app."* | Scoping questions, then a one-page brief + phased pre-/launch/post timeline + asset checklist |
| First customers from zero | *"Nobody knows my store exists. How do I get my first 100 customers?"* | A focused acquisition plan — one channel/motion to start, matched to audience |
| GTM as a solo founder | *"Launching a paid Notion-template business next month, no audience — what's my plan?"* | A sequenced GTM plan (research + channel + content + email + launch), one motion first |

### Writing copy that converts

| You want to… | Say… | You get |
|---|---|---|
| Cold outreach email | *"Cold email to SaaS founders for my churn-reduction tool."* | Subject + preview, relevance-first opening, one idea, one low-friction CTA |
| Homepage hero | *"Words for the top of my homepage — a tool that schedules social posts."* | Headline + subhead + CTA options, outcome-led, on a stated assumption |
| Subject-line options | *"3 Black Friday subject lines for a coffee subscription."* | Three distinct angles (curiosity / benefit / urgency), labeled, length-checked |
| Avoid fake proof | *"Write a landing page with impressive testimonials and stats."* | The page, with marked placeholders + why fabricating proof breaks trust and law |

### Strategy & positioning

| You want to… | Say… | You get |
|---|---|---|
| Nail positioning | *"Positioning statement for a PM tool aimed at agencies."* | 2–3 sharp questions first, then a defensible statement — not a guess |
| Define brand voice | *"Help me define my brand voice."* | Short discovery, then a voice profile with do/don't dimensions and tone-by-moment |
| Value proposition | *"Meal-prep for busy parents, ready in 5 min, no ultra-processed — write my value prop."* | An outcome-led value prop only your brand could say |

### Content, SEO, lifecycle, measurement

| You want to… | Say… | You get |
|---|---|---|
| Content calendar | *"Content calendar for a B2B fintech startup."* | 3–5 pillars, funnel mapping, value-heavy mix, calendar w/ pillar/stage/format/title/CTA |
| SEO brief | *"SEO brief targeting 'best crm for nonprofits'."* | Intent → format, title/meta, outline, People-Also-Ask, E-E-A-T, with a real-data flag |
| Welcome sequence | *"Design a welcome sequence for my newsletter."* | 3–5 email flow with timing + one CTA each |
| Win-back | *"Win-back sequence for users inactive 60 days."* | Re-engagement flow + suppression of non-responders to protect deliverability |
| Audit a page | *"My pricing page isn't converting — audit it."* | Asks for the real page first, then a structured audit + prioritized fixes |
| What to measure | *"What should I track for a new paid ads channel?"* | Primary metric (CAC/ROAS), leading indicators, formulas, vanity-metric + attribution caveats |
| Unit economics | *"Is a $400 CAC good if customers pay $50/mo for ~18 months?"* | LTV + LTV:CAC math shown, read against ~3:1, with the caveats |

---

## How it works

```
marketing/
├── SKILL.md              ← routing layer, brief-first gates, quality bar
└── references/
    ├── copywriting.md      ├── research.md         ├── email-lifecycle.md
    ├── brand-messaging.md  ├── seo.md              ├── cro.md
    ├── content-strategy.md ├── campaigns.md        └── measurement.md
```

At session start, only the `SKILL.md` **description** (~100 tokens) is in context. When a marketing task is detected, the full `SKILL.md` loads and routes to the relevant module(s); unused modules never load. Multi-area requests pull several and synthesize.

Two hard gates enforce quality:

- **Gate A — Strategy foundations** (positioning, value prop, voice, GTM): asks 2–3 sharp questions before writing. These are load-bearing — everything downstream inherits their flaws.
- **Gate B — Audits / "improve my X"**: requests the actual asset first. It won't invent a page's contents and critique its own invention.

Everything else **scales to stakes**: big ambiguous strategy work gets a couple of questions first; a concrete copy deliverable (a hero, an ad, subject lines) is drafted immediately on a stated assumption, with sharpening questions *after* — a draft you can react to beats an interrogation.

---

## The brief-first philosophy

Before producing anything, the skill establishes (or explicitly infers and flags) five things:

1. **Audience** — who specifically, and what do they believe now?
2. **Goal** — the one action this should drive.
3. **Offer** — what's marketed, and the single most important thing about it.
4. **Proof** — the evidence behind the claims.
5. **Constraint** — channel, length, tone, brand rules.

Audience and goal are never *silently* guessed. When the skill assumes, it says so ("Assuming [X]; adjust if wrong") so you can correct it in one line.

---

## The universal quality bar

Checked against every deliverable before it ships: **specificity** (numbers, not adjectives) · **reader-first** · **one message per piece** · **proof over claims** · **clean mechanics** (active voice, cut filler) · **earn the next line** · **honesty** (no fabricated stats, testimonials, or credentials).

---

## Evaluation

The skill ships with its own test suite in [`evals/`](evals): **26 prompts** covering every module, phrasing variations, both gate checks, multi-module synthesis, an implicit trigger, an honesty probe, and **negative controls** (prompts that should *not* trigger it).

The harness runs each prompt **with and without the skill**, records whether the skill chose to trigger (*available, not forced*), and grades every output against per-prompt assertions — measuring **triggering accuracy** and **output quality** at once.

- 📊 Aggregate + per-eval table → [`benchmarks/README.md`](benchmarks/README.md)
- 🧪 Eval set + harness + raw results → [`evals/`](evals)
- 🖥️ Click-through viewer → [`evals/review.html`](evals/review.html)

Reproduce it in Claude Code with the `skill-creator` skill:

```
Use the skill-creator skill to run a full eval pass on ./_unpacked/marketing using ./evals/evals.json.
Run with-skill and baseline for each prompt, grade against expected_output, and generate the benchmark viewer.
```

---

## Design principles

- **Specificity over cleverness** — numbers and outcomes, not vague adjectives
- **Reader-first** — leads with the audience's problem, not the product's features
- **Brief before output** — never silently guesses on audience or goal
- **Proof over claims** — every significant claim needs support
- **One message per piece** — every asset has exactly one job
- **Draft-first for copy, questions-first for strategy** — match friction to stakes
- **Honest by default** — never fabricates proof; surfaces advertising/email-compliance considerations

---

## FAQ

**Does it need an API key or dependencies?** No — plain Markdown in the `SKILL.md` format. Nothing to run or install.

**Why does it sometimes ask questions instead of answering?** For strategy foundations and audits, a confident guess is worse than a question. For ordinary copy, it drafts first and asks after.

**Will it invent testimonials or stats if I ask?** No. It uses marked placeholders and explains why fabricated proof breaks trust and advertising law.

**Does it work outside Claude?** Yes — any tool that reads `SKILL.md` (Cursor, Codex CLI, Gemini CLI, …).

**How is this different from "be a marketer"?** Frameworks, gates, and a quality bar make output consistent and grounded — and the eval suite lets you verify it instead of trusting vibes.

**Can I customize it?** Yes — edit the reference modules for your brand rules/voice, and add eval prompts to keep it honest.

---

## Roadmap

- More reference modules (paid-media buying, partnerships/influencer, PR & comms, localization)
- A brand-profile file the skill reads so output inherits your voice automatically
- Multi-run (3×) eval pass with variance reporting; fix the tracked weak spots (#15, #8)
- More worked before/after examples

---

## Contributing

PRs and issues welcome.

- Keep `SKILL.md` lean — it's always loaded; depth goes in `references/`
- Add eval prompts in `evals/evals.json` for any new module (happy path + a phrasing variation + gates)
- Run the eval set before and after your change so triggering and quality don't regress

---

## License

MIT — see [LICENSE](LICENSE).
