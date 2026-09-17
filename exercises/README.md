# Exercises

Practical exercises come from a **public GitHub repository that you clone yourself**
— they are not bundled here, so this project stays small and the exercise source
stays modular and updatable.

## 1. Clone an exercise repo

Any repo of hands-on exercises works. A good general-purpose one:

```bash
git clone https://github.com/bregman-arie/devops-exercises.git
```

## 2. Point the toolkit at it

```bash
python hiring.py setup --exercises-repo /path/to/devops-exercises
```

The path is stored in `config/hiring.config.json` as `exercises_repo`.

## 3. The map layer

`exercise-map.example.json` is a small, portable catalog that decouples the interview
from the repo's folder structure. Each entry has an `id`, `tags`, `difficulty`,
`seniority` and a `path` **relative to the cloned repo**. The team pack's
`exercise-presets.json` references these ids by stack preset.

To customize:

```bash
cp exercises/exercise-map.example.json exercises/exercise-map.json
# edit paths/ids to match your cloned repo
```

The agent reads the map (not the repo folders) to pick exercises by matching the
candidate's stack tags and seniority — this keeps token usage low.

## Why a map instead of hard paths

- The interview logic never depends on a specific repo layout.
- Swapping or updating the exercise repo only touches the map.
- You can curate a subset without forking the upstream repo.
