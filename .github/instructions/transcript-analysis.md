# Phase: Transcript Analysis

Load when an interview transcript is provided. Produces the scorecard.

## Step 1 — Create the structured scorecard

`python hiring.py scorecard init --name "First Last" --round 1`

This writes `candidates/scorecards/<Name>_round1.json` with all dimensions at 0,
derived from the active team's `score_model`.

## Step 2 — Read the transcript and score

Fill the JSON dimensions (1-5) using evidence from the transcript:
- **Behaviour (40%)**: energy, intellectual honesty, communication, curiosity,
  teamwork, proactivity, business awareness, resilience.
- **Skills (35%)**: problem solving, ownership, adaptability, architectural
  thinking, technical leadership.
- **Knowledge (25%)**: technical depth, stack breadth, AI awareness, cloud depth.

Also set: `contribution_archetype`, the `holistic_axes`, `strengths`, `concerns`,
and the `narrative`. Keep facts, interpretations and open questions separate.

## Step 3 — Compute and review

`python hiring.py scorecard summary --name "First Last"`

Recommendation bands (weighted): ≥4.0 strong · 3.5-3.9 recommend · 3.0-3.4 not
brilliant (flag, don't auto-reject) · <3.0 provisional stop. Behaviour < 3.0
triggers a mandatory evidence and bias review.

## Rules

- Do not use the numeric average as the only criterion; combine it with evidence.
- Reference/background checks are HR-owned and never change the score.
- If the transcript is partial, say so and score only what is supported.
- Never store candidate PII beyond what the process needs; keep files local.
