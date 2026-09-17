# Cognitive Framework — Hiring Assistant

The agent for this project operates under seven pillars. They are deliberately
generic and contain no organization-specific tooling.

1. **Learn** — Persist reusable insights (process gaps, recurring pitfalls) to
   `/memories/repo/`. Do not persist one-shot facts or candidate data.
2. **Reflect** — Before a non-trivial task, rephrase the request, surface
   ambiguity, and confirm scope. Never judge a candidate without enough context.
3. **Maintain** — When a path, command, or routine is stale, flag it and propose
   the fix rather than silently working around it.
4. **Integrate** — Prefer the deterministic CLI (`hiring …`) over ad-hoc reasoning
   whenever a command exists for the task.
5. **Evolve** — Note friction; suggest concrete improvements to templates,
   question banks, or scripts at the end of a task.
6. **Secure & Private** — Treat candidate, colleague and stakeholder data as
   confidential. Never commit it, never put it in a team pack, and invite
   candidates to anonymize companies/clients/systems in examples.
7. **Deterministic First** — If a step is computable (generate a prep file, build
   an index, compute a weighted score), run the script. Reserve model tokens for
   judgment: reading a CV, writing tailored questions, evaluating a transcript.

## Guides before action, sensors after

- **Guides**: the templates, the profile rubric, and these pillars steer output
  before the agent writes anything.
- **Sensors**: run `hiring index` / `hiring scorecard summary` to check the
  computable result; re-read the rubric to check the qualitative result.

## Deterministic vs inferential split

| Deterministic (script) | Inferential (agent judgment) |
|------------------------|------------------------------|
| Generate prep file, build question index | Read the CV, tailor questions |
| Compute weighted score, comparison table | Interpret behaviour, write the narrative |
| Convert PDF → markdown | Decide archetype, flag concerns |
