# Team Profile Packs

Each folder here is a **team pack**: a self-contained, data-driven definition of a
hiring process for one kind of role. The agent and the CLI stay generic — all
team-specific content lives in the pack selected via `hiring setup`.

Switching teams is `hiring setup --team <id>`. No code changes required.

## Anatomy of a pack

```
teams/<id>/
├── team.json                 # manifest: score model, weights, archetypes, stack order, templates
├── profile.md                # role profile: must/nice-have, red flags, evaluation rubric
├── question-bank.md          # reusable question pool (## headings, 🟢🟡🔴 markers)
├── question-bank-index.json  # generated: `hiring index`
├── exercise-presets.json     # stack presets -> exercise ids (resolve against exercises/)
└── templates/
    ├── interview-en.md        # interview prep template (English)
    └── interview-it.md        # interview prep template (Italian)
```

## `team.json` contract

| Key | Purpose |
|-----|---------|
| `id` | Must match the folder name. |
| `display_name` | Human-readable name. |
| `default_language` | `en` or `it`. |
| `stack_order` | Ordered technical stacks (drives question/exercise ordering). |
| `seniority_budget` | Per-seniority time budget and focus. |
| `archetypes` | Allowed contribution archetypes. |
| `score_model` | Categories → `{weight, dimensions[]}`. Weights should sum to 1.0. Drives `hiring scorecard`. |
| `holistic_axes` | Extra 1-5 axes shown in the comparison table. |
| `recommendation_thresholds` | Optional overrides for the recommendation bands. |
| `question_tag_map` | Category-name substring → tags, used by `hiring index`. |
| `question_bank`, `question_bank_index`, `exercise_presets` | Relative filenames. |
| `templates` | Language → relative template path. |

## Add a new team in 4 steps

1. **Copy** an existing pack: `cp -r teams/devops-platform teams/<your-team>`
   (on Windows: `Copy-Item -Recurse teams/devops-platform teams/<your-team>`).
2. **Edit `team.json`**: change `id` to match the new folder, adjust `display_name`,
   `stack_order`, `score_model` dimensions/weights, `archetypes` and `holistic_axes`.
3. **Rewrite the content**: `profile.md` (must/nice-have, red flags), `question-bank.md`
   (your categories and questions), and the two templates. Keep the
   `{{CANDIDATE_NAME}}`, `{{DATE}}`, `{{SENIORITY_LABEL}}`, `{{SENIORITY_FOCUS}}`
   placeholders and the `<!-- AGENT-FILL: key | instructions -->` markers.
4. **Wire it up**: `hiring setup --team <your-team>` then `hiring index` to build the
   question index.

## Templates: placeholders and markers

- `{{CANDIDATE_NAME}}`, `{{DATE}}`, `{{SENIORITY_LABEL}}`, `{{SENIORITY_FOCUS}}` are
  substituted deterministically by `hiring prep`.
- `<!-- AGENT-FILL: key | instructions -->` marks a spot the LLM agent fills from the
  candidate's CV. The text after `|` is the instruction for the agent.

## Privacy

Team packs are public. Do **not** put company names, product names, colleague or
stakeholder names, or any candidate data in a pack. Keep profiles generic.
