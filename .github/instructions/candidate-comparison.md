# Phase: Candidate Comparison

Load when comparing candidates or preparing a final evaluation.

## Step 1 — Generate the comparison table

`python hiring.py scorecard compare`

This reads every scorecard in `candidates/scorecards/` (latest round per candidate)
and writes `candidates/scorecards/_comparison.md`: holistic axes, weighted scores,
provisional recommendation, contribution archetype and HR gate status.

## Step 2 — Enrich with qualitative judgment

Read `_comparison.md` and add:
- **Team complementarity**: does the candidate cover an existing gap?
- **Job-related behavioural evidence**: proactivity, ownership, collaboration,
  transparency — avoid generic "culture fit" judgments.
- **Growth potential** and **time-to-productivity**.
- **Contribution archetype** prevalence (platform / delivery / blended).

## Step 3 — Evidence review

1. Interviewers record their evaluation independently before comparing.
2. Separate observed facts, interpretations, and open questions.
3. Produce a provisional recommendation: `provisional_proceed`,
   `provisional_stop`, or `clarification_needed`.
4. Do not use the numeric average as the only criterion; do not fold
   reference/background checks into the score.

## Step 4 — Final decision

- For finalists, verify the HR-owned gate status (reference/background).
- `pending` blocks declaring the process complete but does not change the score.
- `concern` requires an HR discussion and a chance to clarify; it is not an
  automatic exclusion.
- The final decision belongs to the hiring owner(s), on the full evidence matrix.
