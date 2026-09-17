# Copilot instructions — Hiring Assistant

This repo is a **team-agnostic technical hiring toolkit**. Team-specific content is
in `teams/<id>/` packs, selected via `config/hiring.config.json`.

## Ground rules

- **Deterministic first**: use the CLI (`python hiring.py …`) for anything
  computable — prep files, question index, scorecards, PDF conversion. Reserve
  reasoning for reading CVs, tailoring questions, and evaluating transcripts.
- **Privacy is non-negotiable**: never commit or hard-code candidate, company,
  colleague or stakeholder identifiers. Everything under `candidates/` is
  gitignored. Keep team packs generic.
- **Unbiased questions**: open and behavioural, grounded in past experience; no
  yes/no, leading, or answer-embedding wording; invite anonymized examples.
- The specialized workflow lives in `.github/agents/hiring-assistant.agent.md` and
  the phase files in `.github/instructions/`.

## Common commands

```
python hiring.py setup
python hiring.py cv2md <pdf>
python hiring.py prep --name "<Name>" --seniority <senior|mid|junior> --language <en|it>
python hiring.py index
python hiring.py scorecard {init|summary|compare} --name "<Name>"
```
