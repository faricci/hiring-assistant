# Phase: Second Interview (technical exercises)

Load to prepare the second round. Duration: 30 min, max 1h. Exercises only.

## Goal

Verify hands-on ability and reasoning through practical exercises. Skills (35%) and
Knowledge (25%) weigh most here.

## Preparation

1. Confirm the provisional archetype from round 1 (platform / delivery / blended).
2. Read `teams/<id>/exercise-presets.json` and `exercises/exercise-map.json`.
   Pick the preset closest to the candidate and assemble a subset within the
   seniority time budget (senior ~2h pool, mid ~1.5h, junior ~1h — you select a
   subset, you do not run all of them).
3. Order: Terraform / IaC → AWS / Cloud → Containers → CI/CD → Ansible →
   Linux / Shell → Git → candidate-specific.
4. For P1 / blended-with-P1 / P1-to-verify candidates, include the mandatory Python
   exercise ("maximum product of three integers"). It cannot be dropped.
5. Ask the round-2 AI follow-up: what did they try with an AI coding assistant?

### One-page exercise section — embed, don't link out

Build the prep file's "Technical exercises" section so the whole round can be run
from that one Markdown file, with no need to open the exercises repo. This applies
to every candidate prep file, not just this template — keep the structure below
whenever you generate one.

1. **Index table** — one row per selected exercise, its title linking to an
   in-file anchor: `[Title](#exercise-<id>)` (`<id>` = the exercise's id in
   `exercise-map.json`).
2. **Embedded section per exercise**, right below the table, tagged with a
   matching anchor (`<a id="exercise-<id>"></a>` immediately before the heading)
   so the table link scrolls to it inside the same page:
   - `**Prompt**:` the **complete** prompt text — copied from the bank file if
     the map entry has a `path`, or from the map entry's own `prompt` field if
     `path` is `null` (an inline exercise, e.g. the mandatory Python one).
     **Never** copy or summarize the solution, only the prompt/statement.
   - `> **Expected evidence**:` the evaluation guidance (what a good/weak/red-flag
     answer looks like) — keep and adapt whatever guidance the bank or a prior
     version of the prep file already had; never drop it when reformatting.
   - If the map entry has a real `path`, add one more line: a secondary link
     `<a href="file:///<exercises_repo>/<path>" target="_blank" rel="noopener">Open source exercise from the bank</a>`,
     resolving `exercises_repo` from `config/hiring.config.json`. Use
     `target="_blank"` so it opens in a new tab and never replaces the prep page.
     If the entry has no `path` (inline exercise), write
     `*(Inline exercise — no bank source file.)*` instead — there is nothing to link.
3. **Incomplete bank entries**: if a map entry has neither a `path` nor a
   `prompt` (e.g. `reasoning-migration` as of writing), do not invent a prompt
   and do not edit the bank file. Skip it for this round and add a one-line flag
   instead, e.g. `⚠️ "<id>" has no prompt in exercise-map.json — flagged, not
   used this round.` Fixing the bank is separate work, out of scope here.

## During the exercises

- Everything the candidate needs to read is already embedded in the prep file —
  share your screen or paste the relevant prompt into the collaborative editor
  the candidate will type in; give a short read time and a visible timer per
  exercise. The secondary bank link is for your own reference only (opens in a
  new tab) — never share it as the candidate's exercise text, since some bank
  files may include the solution alongside the prompt.
- Assess the reasoning, not just the final commands. For juniors/career-changers,
  structure and calmness matter more than exact syntax.
- "I don't know, but here is how I'd figure it out" — with structure — is a strong
  signal. Bluffing or "I'd just Google it" without structure is a weakness.

## Output

Capture per-exercise observations for the scorecard. Update the provisional
recommendation via `hiring scorecard`.
