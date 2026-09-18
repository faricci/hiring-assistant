# Ground rules — Hiring Assistant

Single source of truth for the always-loaded project instructions. Both editor
integrations load this file and follow it — edit only here:
- GitHub Copilot: `.github/copilot-instructions.md`
- Claude Code: `CLAUDE.md`

---

This repo is a **team-agnostic technical hiring toolkit**. Team-specific content is
in `teams/<id>/` packs, selected via `config/hiring.config.json`.

## Rules

- **Deterministic first**: use the CLI (`python hiring.py …`) for anything
  computable — prep files, question index, scorecards, PDF conversion. Reserve
  reasoning for reading CVs, tailoring questions, and evaluating transcripts.
- **Privacy is non-negotiable**: never commit or hard-code candidate, company,
  colleague or stakeholder identifiers. Everything under `candidates/` is
  gitignored. Keep team packs generic.
- **Unbiased questions**: open and behavioural, grounded in past experience; no
  yes/no, leading, or answer-embedding wording; invite anonymized examples.
- The specialized workflow lives in `knowledge/hiring-assistant-agent.md` (loaded
  as the **Hiring Assistant** agent/subagent) and the phase files in
  `.github/instructions/`.

## Using the agent

Just ask in plain language — e.g. "help me evaluate and create the first
interview preparation for Jane Doe" — and it runs the deterministic commands
below for you, adding only the judgment (fit, flags, tailored questions, scoring).

## Common commands

```
python hiring.py setup
python hiring.py cv2md <pdf>
python hiring.py prep --name "<Name>" --seniority <senior|mid|junior> --language <en|it>
python hiring.py index
python hiring.py scorecard {init|summary|compare} --name "<Name>"
python hiring.py dashboard
```
