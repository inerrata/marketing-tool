# Measurement & Analytics Reference

Frameworks for deciding what to measure, how to read it, and how to report it. Marketing without
measurement is guessing; measurement without the right metrics is worse — it's confident guessing.

## Table of contents
- [Pick metrics that matter](#pick-metrics-that-matter)
- [Metrics by goal](#metrics-by-goal)
- [The pirate metrics funnel (AARRR)](#the-pirate-metrics-funnel-aarrr)
- [Key formulas](#key-formulas)
- [Attribution](#attribution)
- [Reporting](#reporting)
- [Common measurement mistakes](#common-measurement-mistakes)

---

## Pick metrics that matter

- **Tie every metric to a goal.** If you can't say what decision a metric informs, don't track it as a KPI.
- **Distinguish vanity from actionable.** Impressions and follower counts feel good but rarely drive
  decisions. Conversion rate, CAC, LTV, and revenue do.
- **Leading vs. lagging indicators.** Lagging (revenue, customers) tell you what happened; leading
  (signups, qualified leads, engagement) let you steer before the lagging number lands. Track both.
- **One primary metric per initiative**, plus a few secondary/diagnostic ones. Focus prevents
  optimizing-everything-and-nothing.

---

## Metrics by goal

- **Awareness:** reach, impressions, share of voice, new-visitor traffic, branded search volume.
- **Acquisition:** traffic by channel, click-through rate, cost per click, leads, cost per lead, signups.
- **Activation:** signup→activation rate, time to first value, onboarding completion.
- **Conversion:** conversion rate (per step and overall), CAC, sales, average order value.
- **Retention:** churn rate, retention rate, repeat purchase rate, DAU/MAU (for products).
- **Revenue:** MRR/ARR, LTV, revenue per customer, expansion revenue.
- **Referral:** referral rate, viral coefficient, NPS (as a proxy for advocacy).
- **Content/email:** organic traffic, rankings, email open/click rates, replies, unsubscribe rate.

---

## The pirate metrics funnel (AARRR)

A clean framework for a full-funnel view:
- **Acquisition** — how do people find you?
- **Activation** — do they have a good first experience / reach first value?
- **Retention** — do they come back?
- **Referral** — do they tell others?
- **Revenue** — do they (and others) pay?

Find the stage with the biggest leak and fix that first — improving a 2% activation rate often beats
pouring more traffic into the top.

---

## Key formulas

- **Conversion rate** = conversions ÷ total visitors × 100
- **CAC (Customer Acquisition Cost)** = total sales & marketing spend ÷ new customers acquired
- **LTV (Lifetime Value)** = average revenue per customer × average customer lifespan (or gross margin per
  customer × average lifespan for a margin-based view)
- **LTV:CAC ratio** — a common health benchmark is roughly 3:1; below ~1:1 you lose money per customer,
  very high may mean underinvesting in growth. (Benchmarks vary by industry — treat as a guide.)
- **CAC payback period** = CAC ÷ monthly gross margin per customer (months to recoup acquisition cost)
- **ROAS (Return on Ad Spend)** = revenue from ads ÷ ad spend
- **Churn rate** = customers lost in period ÷ customers at start of period × 100
- **AOV (Average Order Value)** = total revenue ÷ number of orders
- **Email CTR** = clicks ÷ delivered × 100 ; **Open rate** = opens ÷ delivered × 100 (note: open tracking
  has become less reliable due to privacy features — weight clicks more heavily)

When you compute these for a user, show the formula and inputs so they can sanity-check, and flag any
assumptions or missing data.

---

## Attribution

Attribution assigns credit for a conversion to touchpoints. No model is perfect; know the trade-offs.

- **First-touch** — all credit to the first interaction. Good for understanding what drives awareness;
  ignores everything after.
- **Last-touch** — all credit to the final interaction. Simple, common, but ignores the journey that set
  it up.
- **Linear** — equal credit to all touchpoints. Fairer, but treats a minor touch like a decisive one.
- **Time-decay** — more credit to touchpoints closer to conversion.
- **Position-based (U-shaped)** — most credit to first and last, some to the middle.
- **Data-driven** — algorithmic credit based on actual contribution (needs volume and tooling).

**Practical guidance:** for most, last-touch is too simplistic and pure first-touch misleads. A
position-based or time-decay view tends to reflect reality better. Flag that attribution is inherently
imperfect, especially with privacy changes degrading tracking — triangulate with self-reported data
("how did you hear about us?") and holdout/incrementality tests where stakes are high.

---

## Reporting

A good marketing report answers: what happened, why, and what we'll do about it.

**Structure:**
1. **Headline** — the one-line summary (did we hit the goal?).
2. **Key metrics vs. target/prior period** — the numbers that matter, with context (a number with no
   comparison is meaningless).
3. **What drove it** — the why behind the movement.
4. **Insights** — what we learned.
5. **Actions / next steps** — what we'll do based on this.

Principles: compare against something (target, last period, benchmark); show trends, not just snapshots;
lead with the decision-relevant numbers; cut metrics nobody acts on. A dashboard full of vanity metrics is
clutter; a focused report drives action.

---

## Common measurement mistakes

- Tracking vanity metrics and ignoring revenue/retention.
- Reporting numbers with no comparison or context.
- Over-trusting last-click attribution.
- Calling A/B tests early (before significance) — false wins.
- Optimizing a single metric in isolation (e.g. driving signups that never activate).
- Confusing correlation with causation in channel performance.
- Ignoring statistical noise in small samples.
