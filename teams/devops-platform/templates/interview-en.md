# Interview Prep — {{CANDIDATE_NAME}}

> **Calibration**: profile **{{SENIORITY_LABEL}}**. Focus on: {{SENIORITY_FOCUS}}
> For every personalized question add a `> **Expected answer**:` block with ✅ Good /
> ⚠️ Weak / 🚫 Red flag indicators, and a `> **Example follow-up**:` block with 1-2
> probing follow-ups to use if the answer is vague, opinion-based, theoretical or
> incomplete.

---

## Introduction (interviewer, ~3 min)

- Start recording (with consent) and share the collaborative editor / exercise link.
- Welcome the candidate and introduce yourself: your role and who you report to.
- Keep the company presentation short and factual. Do **not** ask the candidate to
  recite company trivia — assess authentic motivation instead.

### Spontaneous knowledge and motivation — before the company presentation

1. *"What do you already know about us, and what caught your attention?"*
2. *"What led you to accept this interview, and which aspect of the position would you like to explore?"*
3. *"What are you looking for in your next role, and what would you like to change from your current situation?"*

> **Note**: this is not a trivia test. Assess basic preparation, authentic motivation
> and clarity of expectations. If the recruiter shared limited information, do not
> penalize the candidate; observe the questions they ask.

### Candidate instructions (communicate, do not ask)

1. If a question is not clear, ask immediately — clarifying questions are welcome.
2. Answers should be concise and to the point: aim for 1-2 minutes per question,
   3 minutes max for complex ones. Concrete details and specific examples, not long stories.

---

## Candidate profile

| Field | Value |
|-------|-------|
| **Name** | {{CANDIDATE_NAME}} |
| **Location** | <!-- AGENT-FILL: profile_location | From the CV: candidate location. --> |
| **Total experience** | <!-- AGENT-FILL: profile_total_exp | From the CV: total years of experience. --> |
| **DevOps/Platform experience** | <!-- AGENT-FILL: profile_devops_exp | From the CV: years in DevOps/SRE/Platform roles. --> |
| **Current role** | <!-- AGENT-FILL: profile_role | From the CV: current title/role. --> |
| **English (stated)** | <!-- AGENT-FILL: profile_english | From the CV: stated English level. --> |
| **Analysis date** | {{DATE}} |
| **Status** | `CV screening` / `Career path review` / `Structured interview` / `Work sample` / `Evidence review` / `HR checks pending` / `Final decision` / `Closed` |

### Must-have / Nice-to-have coverage

<!-- AGENT-FILL: coverage | Evaluate the CV against the must-have and nice-to-have lists in ../profile.md. Produce two checklists (✅ covered / ⚠️ partial / ❌ missing) with a one-line justification each. -->

### Flag analysis

<!-- AGENT-FILL: flags | Fill four short tables from the CV: 🔴 Red flags (potential blockers), 🟡 Yellow flags (monitor), 🟢 Green flags (real strengths), ❌ Missing nice-to-haves. Keep each entry to one line. -->

---

## Part 1 — Warmup (~25 min)

**Career path** (CV-based questions with levels):

<!-- AGENT-FILL: cv_warmup_questions | Generate 3-5 neutral behavioural CV-based questions. Each with a level (🟢/🟡/🔴), the question text, an "> **Expected answer**:" block (✅/⚠️/🚫) and an "> **Example follow-up**:" block with 2 probing follow-ups. Focus on career timeline, real ownership vs task execution, CV gaps or inconsistencies. Invite the candidate to anonymize companies, clients and systems. -->

**Motivation and fit** (recurring — adapt to the profile):

- 🟢 *"Tell me about a concrete experience where you worked beyond the traditional boundaries of your role. What was the context, what responsibilities did you take on, and what result did you achieve?"*
  > **Example follow-up**:
  > - "Which part did you find most difficult?"
  > - "What would you have preferred to delegate to a colleague?"
- 🟢 *"Why do you want to join, and what do you expect from this role, the team and your next job?"*
  > **Expected answer**: ✅ concrete motivation aligned with the role (platform, delivery, technical growth), realistic and verifiable expectations; ⚠️ interest driven only by brand/relocation/salary; 🚫 vague or misaligned expectations.
  > **Example follow-up**:
  > - "If the job turned out different from your expectations on a key aspect, how would you experience that?"

<!-- AGENT-FILL: motivation_fit_questions | Add 1-2 neutral behavioural fit questions based on the CV, with expected answers. Avoid yes/no, leading, and positive-outcome wording. Add an "> **Example follow-up**:" block under each. -->

**Depth and self-awareness**:

- 🟡 *"Pick two or three technologies where you feel you have the most experience. For each, tell me about the last complex problem you faced, what you personally contributed, and what you learned."*
  > **Expected answer**: self-awareness test. A good answer distinguishes real depth from exposure. Red flag if the candidate lists the whole CV.

<!-- AGENT-FILL: depth_questions | Add 1-2 neutral questions to verify experience depth or clarify CV inconsistencies. Do not use trap questions and do not imply the candidate exaggerated; ask for context, personal contribution and observable evidence. -->

---

## Part 2 — Technical deep dive (~25-30 min)

### Common technical questions (adapt to the level)

**Terraform / IaC — first technical stack:**
- 🟢 *"Tell me about a task where you used Terraform or another IaC tool. What problem did it address, what did you contribute, and how did you verify changes before applying them?"*
  > **Expected answer**: concrete experience with versioned code, review, plan/tests, environment management and controlled apply. Without direct experience, the candidate should clearly distinguish theory, equivalent tools and a learning plan.
- 🟡 *"Describe how you would manage state, concurrency and secrets in a Terraform workflow used by multiple people and a CI/CD pipeline."*
  > **Expected answer**: protected remote state, locking, environment separation, least privilege, secret manager, pipeline serialization. 🚫 shared local state, `-lock=false`, secrets in the repo.

**DevOps philosophy & culture:**
- 🟢 *"Tell me about a concrete experience that represents how you apply DevOps day to day. What was the context and what did you contribute?"*
  > **Expected answer**: DevOps as collaboration, fast feedback, shared ownership and automation — not a job title or tool set.
- 🟡 *"Describe a situation where you identified or managed technical debt. How did you distinguish it from a customer-visible defect, and how did you decide priority?"*

**CI/CD:**
- 🟢 *"Describe a CI/CD pipeline you worked on directly. Which stages did it include, why were they necessary, and which part did you personally build or modify?"*
  > **Expected answer**: build, test, quality checks, artifact/versioning, deploy or prepare-to-deploy — and the candidate's own contribution.
- 🔴 *"Tell me about a delivery-process improvement you measured. Which metrics (including DORA: Deployment Frequency, Lead Time, Change Failure Rate, MTTR) did you choose, why, and what changed?"*

**Monitoring & observability:**
- 🟢 *"Describe a technical investigation where metrics, logs or traces gave you different information. How did you choose which signal to analyze?"*
  > **Expected answer**: metrics = numeric time-series; logs = timestamped events; traces = a single request across services.

**Branching & delivery:**
- 🟢 *"Describe the branching model used in a recent project. How did it work, and which team need was it trying to satisfy?"*
- 🟡 *"Compare Git Flow and trunk-based development using two concrete contexts where you would choose differently. Which trade-offs would you weigh?"*

<!-- AGENT-FILL: technical_personalized | Generate 5+ neutral, preferably behavioural technical questions. Terraform / IaC must be the first stack, followed by AWS / Cloud, Containers, CI/CD, Ansible, Linux / Shell, Git, then candidate-specific technologies. If Terraform is not declared, use the first block to assess equivalent IaC experience, conceptual understanding and a learning plan. Each question needs a level and an expected answer, plus an "> **Example follow-up**:" block. -->

#### Attitudinal scenario — production incident under constraints (~10 min)

> **When to use it**: optional; useful to assess reasoning under pressure and
> prioritization, especially for junior/career-changer profiles.

- 🔴 *"A cross-cutting change removed the permissions on a folder used by a containerized production service. It can no longer write to a host-mapped directory and returns 'permission denied'. You can use Docker and read logs as your own user, but you do **not** have root; the team that made the change is not reachable; a restart did not help; the call ends in 10 minutes. How do you handle it, from the first minute to resolution? Think aloud."*
  > **Expected answer**:
  > - ✅ Method and calm: gather facts (what changed, when, exact error, blast radius), form and verify a hypothesis before acting, communicate status.
  > - ✅ Prioritization: separate service restoration (now) from root cause and prevention (later).
  > - ✅ Reasoning within constraints: seek an alternative within their access scope (e.g. recreate the resource instead of modifying it in place) rather than getting stuck on "I don't have permissions".
  > - ⚠️ Retries the restart without gathering facts.
  > - 🚫 Panics, acts randomly on production, or demands privileges as the only path.

---

## Part 3 — AI assessment (~10 min)

- 🟢 *"What role have AI tools played so far in your work or learning? If you haven't used them, how did you evaluate that choice?"*
- 🟡 *"Tell me about a task where you evaluated whether to use an AI tool. How did you decide, verify the result, and what impact did you observe?"*
- **Setup for round 2**: *"Before our next conversation, explore an AI coding assistant and prompt-optimization techniques. Next time I'll ask what you tried and learned."*

---

## Technical exercises

> **One-page workflow**: every selected exercise's full prompt is embedded below —
> run the whole round from this file, no need to open the exercises repo. The
> table is an in-file index: click a title to jump to its embedded prompt in this
> same document; solutions are never embedded here. Source: shared exercise
> catalog (see `../exercise-presets.json` and `../../exercises/`). Order:
> Terraform / IaC → AWS / Cloud → Containers → CI/CD → Ansible → Linux / Shell →
> Git → candidate-specific.

| # | Exercise | Topic | Difficulty | Time |
|---|----------|-------|------------|------|
| 1 | [Terraform / IaC — instance module](#exercise-terraform-ec2) | Terraform | Medium | 15 min |
| 2 | [Containers — Postgres with host volume](#exercise-docker-postgres) | Containers | Easy | 10 min |
<!-- AGENT-FILL: exercise_table_rows | Add one row per additional selected exercise (standard + stack-matched extended, per exercise-presets.json), each linking to its own embedded anchor below as #exercise-<id>. For P1/blended-with-P1/P1-to-verify candidates always add the mandatory "python-max-product" row. -->

<a id="exercise-terraform-ec2"></a>
### Terraform / IaC — instance module

**Prompt**: Create a Terraform module that launches one instance and returns its private DNS as output (module name `my_instance`).

> **Expected evidence**: a working `output` block wired to the resource attribute,
> sane variable defaults, and a short explanation of why the output is useful
> (e.g. feeding another module). ⚠️ hardcoded values instead of variables;
> 🚫 no working output.

*(Inline exercise — authored directly in this template, no bank source file to link.)*

<a id="exercise-docker-postgres"></a>
### Containers (Docker) — Postgres with host volume

**Prompt**: Run a PostgreSQL container with the password in an environment variable
and a host volume for the data directory; verify it is running. Explain the
benefits and risks of host storage versus container storage.

> **Expected evidence**: correct `-e`/`-v` usage (or Compose equivalent), a working
> verification step (e.g. `docker exec ... psql`), and a clear articulation of the
> durability/portability trade-off. 🚫 storing the password in the image or
> skipping verification.

*(Inline exercise — authored directly in this template, no bank source file to link.)*

<!-- AGENT-FILL: extra_exercises | For every additional exercise you select from exercise-map.json (standard + stack-matched extended, per exercise-presets.json): (1) add a row to the table above linking to #exercise-<id>; (2) add an embedded section here with `<a id="exercise-<id>"></a>`, a heading, a "**Prompt**:" line with the full prompt copied from the bank file (or the map entry's own "prompt" field when "path" is null) — never the solution; (3) an "> **Expected evidence**:" block; (4) if the map entry has a real "path", one more line: `<a href="file:///<exercises_repo>/<path>" target="_blank" rel="noopener">Open source exercise from the bank</a>` (resolve exercises_repo from config/hiring.config.json) — otherwise write "*(Inline exercise — no bank source file.)*". If a map entry has neither "path" nor "prompt" (an incomplete bank entry), do not invent a prompt and do not edit the bank: skip it and add a one-line flag instead, e.g. "⚠️ `<id>` has no prompt in exercise-map.json — flagged, not used this round." For P1, blended-with-P1, or P1-to-verify candidates, always include the mandatory "python-max-product" exercise (embed its "prompt" field verbatim) and mark it MANDATORY P1 — never replace it with another Python exercise. Order Terraform / IaC first. -->

---

## Scorecard (fill after the interview)

> Scores are 1-5. Weighted model: Behaviour 40% · Skills 35% · Knowledge 25%.
> Record scores in the structured file via `hiring scorecard init --name "{{CANDIDATE_NAME}}"`,
> then fill the JSON and run `hiring scorecard summary --name "{{CANDIDATE_NAME}}"`.

| Dimension | Score (1-5) | Notes |
|-----------|-------------|-------|
| Behaviour | | |
| Skills | | |
| Knowledge | | |
| **Weighted total** | | |

**Contribution archetype**: `platform_engineering` / `delivery_engineering` / `blended` / `unclear`

**Strengths**:
**Concerns**:
**Provisional recommendation**:
