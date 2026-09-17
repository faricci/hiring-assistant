# Phase: CV Analysis

Load when a CV is provided. Produces the interview prep file.

## Step 1 — Convert and generate deterministically

1. If the CV is a PDF, convert it: `python hiring.py cv2md candidates/cv_pdf/<file>.pdf`
   (output in `candidates/cv_md/`).
2. Generate the prep file:
   `python hiring.py prep --name "First Last" --seniority senior --language en`
   - `--seniority`: `senior` (5+ yrs), `mid` (3-5), `junior` (< 3).
   - `--language`: `en` or `it`. If unsure, ask.

The prep file (`candidates/preparation_md/<Name>_interview_prep.md`) contains the
static structure plus `<!-- AGENT-FILL: key | instructions -->` markers.

## Step 2 — Read the CV and fill the markers

Open the generated file and the CV in `candidates/cv_md/`. For each marker, follow
the instruction after `|`:

- **Profile fields**: location, total experience, DevOps/Platform experience,
  current role, stated English.
- **Coverage**: evaluate the CV against must/nice-have in `teams/<id>/profile.md`
  (✅ covered / ⚠️ partial / ❌ missing, one line each).
- **Flags**: 🔴 red / 🟡 yellow / 🟢 green / ❌ missing nice-to-haves.
- **Questions**: for each personalized question add a level (🟢/🟡/🔴), an
  `> **Expected answer**:` block (✅/⚠️/🚫) and an `> **Example follow-up**:` block
  with 1-2 probing follow-ups.

Rules for questions:
- Terraform / IaC is the first technical stack, then AWS / Cloud, Containers, CI/CD,
  Ansible, Linux / Shell, Git, then candidate-specific tech.
- Prefer behavioural questions grounded in past experience.
- Avoid yes/no, leading, positive-outcome, negative or brain-teaser wording.
- Do not embed the answer in the question; invite anonymized examples.

## Step 3 — Exercises

Read `teams/<id>/exercise-presets.json` and `exercises/exercise-map.json` (not the
repo folders). Match the closest stack preset, always include the standard
exercises, then add extended ones whose tags/seniority match the CV. Order
Terraform / IaC first. For P1 / blended-with-P1 / P1-to-verify candidates, always
include the mandatory Python exercise ("maximum product of three integers").

## Step 4 — Question bank lookup (index-first)

Read `teams/<id>/question-bank-index.json`, filter categories by tags matching the
stack, and read only the relevant line ranges of `question-bank.md`.

## Step 5 — Present to the interviewer

Show the profile summary + tailored questions and ask for confirmation/edits before
the interview.
