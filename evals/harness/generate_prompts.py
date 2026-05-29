#!/usr/bin/env python3
"""Write a self-contained prompt.txt into every run directory.

with_skill runs present the marketing skill's real description and let the agent
decide whether to consult it (available, not forced). without_skill runs never
mention a skill. Each agent writes its deliverable to outputs/ so the orchestrator
never has to carry large outputs in context.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ITER = ROOT / "iteration-1"
SKILL_DIR = (ROOT / "skill" / "marketing").resolve()
SKILL_MD = SKILL_DIR / "SKILL.md"

# The marketing skill's frontmatter description, verbatim, as it appears in the
# available-skills list a real session would see.
DESCRIPTION = (
 "Comprehensive, full-stack marketing skill for creating, auditing, and optimizing "
 "marketing content and strategy with rigor. Use this skill whenever the user wants to "
 "write or improve copy (ads, emails, landing pages, homepages, social posts, CTAs, "
 "taglines, product descriptions, sales pages), run a content or messaging audit, build a "
 "content calendar or editorial plan, develop a campaign concept or go-to-market (GTM) plan, "
 "define a brand voice or tone, write a value proposition or positioning statement, create "
 "audience personas or ICPs, write SEO content briefs, plan an email sequence or newsletter, "
 "design a conversion-rate-optimization (CRO) test, analyze competitor positioning, or measure "
 "marketing performance. Make sure to use this skill whenever the user mentions attracting "
 "customers, growing an audience, launching a product, increasing conversions, communicating "
 "value, or any task that touches marketing copy or strategy — even if they don't explicitly "
 "say the word \"marketing.\""
)

WITH_TMPL = """You are completing ONE evaluation run. Work fully independently. Do NOT ask the requester any clarifying questions back to ME — if the task itself calls for asking the user questions, write those questions into your response file as your deliverable. Make your own decisions otherwise.

A skill is AVAILABLE to you but NOT forced. This is exactly how it would appear in your available-skills list (name + description):

  name: marketing
  description: {description}

The full skill is on disk:
  SKILL.md:    {skill_md}
  references:  {skill_dir}\\references\\  (SKILL.md routes you to the right one)

STEP 1 — Decide for yourself, based only on the user request below and the description above, whether this skill genuinely applies and you would actually consult it. A real assistant consults a skill only when it clearly helps; unrelated, personal, or trivial requests should NOT trigger it. Be honest — do not force it.

STEP 2 — If you decide to use it: read SKILL.md, follow its routing to read the relevant reference file(s), and follow its guidance to complete the request. If you decide NOT to use it: complete the request normally, as you would with no skill available.

STEP 3 — Produce your real, final deliverable to the user (the actual copy/plan/answer, or — where the skill or good judgment says to gather inputs first — the actual clarifying questions you would send).

USER REQUEST:
<<<
{prompt}
>>>

Then save exactly two files (absolute paths):
1. {out}\\response.md  — your full final response to the user, verbatim, exactly as you would send it.
2. {out}\\trigger_decision.json — a JSON object: {{"triggered": true or false, "reason": "<one sentence>", "references_read": ["<filenames you opened>"]}}

Write nothing else to disk. When both files are written, reply with only: DONE triggered=<true|false>
"""

WITHOUT_TMPL = """You are completing ONE task independently. Do NOT ask clarifying questions back to ME — if the task warrants asking the user something, write those questions into your response file as the deliverable. Make reasonable assumptions otherwise and produce a real, finished deliverable.

USER REQUEST:
<<<
{prompt}
>>>

Save your full final response to the user, verbatim, to this absolute path:
  {out}\\response.md

Write nothing else to disk. When done, reply with only: DONE
"""

def main():
    count = 0
    for eval_dir in sorted(ITER.glob("eval-*"), key=lambda p: int(p.name.split("-")[1])):
        meta = json.loads((eval_dir / "eval_metadata.json").read_text(encoding="utf-8"))
        prompt = meta["prompt"]
        for arm in ("with_skill", "without_skill"):
            for r in (1, 2, 3):
                rd = eval_dir / arm / f"run-{r}"
                out = (rd / "outputs").resolve()
                if arm == "with_skill":
                    text = WITH_TMPL.format(description=DESCRIPTION, skill_md=SKILL_MD,
                                            skill_dir=SKILL_DIR, prompt=prompt, out=out)
                else:
                    text = WITHOUT_TMPL.format(prompt=prompt, out=out)
                (rd / "prompt.txt").write_text(text, encoding="utf-8")
                count += 1
    print(f"Wrote {count} prompt.txt files")
    # sanity: print one example path for each arm
    print("example with_skill:", (ITER/"eval-4"/"with_skill"/"run-1"/"prompt.txt"))
    print("example without:   ", (ITER/"eval-24"/"without_skill"/"run-1"/"prompt.txt"))

if __name__ == "__main__":
    main()
