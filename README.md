# Hiring Assistant

A small, quite **deterministic, team-agnostic toolkit** for running a structured technical
hiring process with an AI coding agent. The process stays the same across roles; all
team-specific content lives in swappable **team packs**.

> Privacy by design: no company, candidate, colleague or stakeholder data ships in
> this repo. Everything under `candidates/` is gitignored. Team packs are generic.

## The process

```
CV (PDF) ──cv2md──▶ CV (markdown) ──▶ fit & flags ──prep──▶ interview 1 (knowledge)
                                                       └──▶ interview 2 (exercises)
                                                              └──▶ take-home (optional)
                                                                     └──▶ transcript ──▶ scorecard
```

Deterministic scripts do the mechanical work (convert, generate, index, score). The
AI agent does the judgment (read the CV, tailor questions, evaluate the transcript).

## Quick start

Requires **Python 3.9+**. No third-party packages for the core commands (PDF
conversion is the only optional dependency).

> These commands are shown for reference. In practice: `setup`, `dashboard`,
> `cv2md` and `index` are mechanical, run them yourself, anytime, no AI needed.
> For the judgment-heavy steps (interview prep, scoring), select the **Hiring
> Assistant** agent in your editor and ask in plain language, e.g. "help me
> evaluate and create the first interview preparation for Jane Doe" — it follows
> [.github/agents/hiring-assistant.agent.md](.github/agents/hiring-assistant.agent.md),
> reads the CV, and runs `prep`/`scorecard` for you as part of the conversation,
> mixing them with its own reading/judgment steps.

```bash
# 1. Configure: pick a team pack and (optionally) point to a cloned exercises repo
python hiring.py setup

# 2. Build the question-bank index for the active team
python hiring.py index

# 3. Convert a CV and generate the interview prep file
python hiring.py cv2md candidates/cv_pdf/jane_doe.pdf      # optional dep, see below
python hiring.py prep --name "Jane Doe" --seniority senior --language en

# 4. After the interview: score
python hiring.py scorecard init    --name "Jane Doe"
python hiring.py scorecard summary --name "Jane Doe"
python hiring.py scorecard compare
```

Wrappers are provided so you can call it from any shell:
`hiring.bat` (cmd), `./hiring.ps1` (PowerShell), `./hiring.sh` (bash).

### Optional: PDF → markdown

`hiring cv2md` needs one package, installed automatically by `hiring setup`
(use `--skip-deps` to opt out):

```bash
pip install -r requirements.txt   # installs pymupdf4llm, only if you skipped it during setup
```

Everything else works without it.

## Commands

| Command | Purpose |
|---------|---------|
| `setup` | Select the active team pack, default language, and exercises repo path. |
| `teams` | List available team packs. |
| `cv2md <path>` | Convert a CV PDF (or a folder of PDFs) to markdown in `candidates/cv_md/`. |
| `prep --name … [--seniority] [--language] [--force]` | Generate a prep file with `AGENT-FILL` markers for the agent to complete. |
| `index` | Rebuild the token-efficient question-bank index for the active team. |
| `scorecard init\|summary\|compare` | Manage structured scorecards and the comparison table. |

## Modularity

### Team packs

The DevOps/Platform bias is just one pack. Everything role-specific — profile,
must/nice-have, scoring model and weights, question bank, exercises, templates —
lives under `teams/<id>/`. Switch with `hiring setup --team <id>`; add your own by
copying a pack and editing it. See [teams/README.md](teams/README.md).

The scorecard is **data-driven**: its dimensions and weights come from the pack's
`team.json`, so a different team scores on different axes with no code changes.

### Exercises

Practical exercises come from a **public repo you clone yourself**, referenced by a
configurable path plus a small portable map — no third-party repo is bundled. See
[exercises/README.md](exercises/README.md).

## Project layout

```
hiring.py                 # CLI launcher (+ hiring.sh/.bat/.ps1 wrappers)
hiring/                   # Python package: setup, prep, index, scorecard, cv2md
config/                   # hiring.config.json (gitignored) + example
teams/<id>/               # team packs (profile, question bank, exercises, templates)
exercises/                # exercise map + how to point at a cloned repo
candidates/               # local workspace (gitignored: CVs, prep, transcripts, scorecards)
dashboard/dashboard.html  # offline hiring dashboard (process, commands, file viewer)
.github/                  # hiring-assistant agent + phase instructions
knowledge/                # cognitive framework the agent follows
```

## Dashboard

Run `python hiring.py dashboard` to serve the project root and open
`dashboard/dashboard.html` in your browser — this also lets the reference-file
links (team profile, question bank, templates) load, since `file://` blocks
that. Use `--port` to change the port and `--no-browser` to skip auto-opening.
It shows the process overview, command cheat-sheet, and a local file viewer
for prep files and scorecards (nothing is uploaded). It also lays out which
steps you run yourself (setup, dashboard, cv2md, index — no AI needed) versus
which ones benefit from asking the "Hiring Assistant" agent (prep, scorecard —
judgment-heavy steps).

## Principles

- **Deterministic first** — compute what is computable; spend model tokens only on
  judgment. It is based on AGENT-FILL concept: https://medium.com/@faricci_62865/agent-fill-a-markdown-comment-that-cuts-llm-costs-and-hallucinations-580e84d370e5
- **Unbiased interviewing** — open, behavioural questions grounded in real
  experience; no yes/no, leading, or answer-embedding wording.
- **Evidence-based scoring** — Behaviour (40%) → Skills (35%) → Knowledge (25%);
  flag weak candidates, don't auto-reject; HR checks are separate gates that never
  change the score.
- **Privacy** — candidates are invited to anonymize companies, clients and systems;
  no identifiers are ever committed.

## License

MIT — see [LICENSE](LICENSE).
