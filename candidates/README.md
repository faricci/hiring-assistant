# Candidates workspace

This is where candidate artifacts live during a hiring round. **Everything under
these folders is gitignored** (except this README and the `.gitkeep` files) so no
candidate data is ever committed or made public.

| Folder | Contents |
|--------|----------|
| `cv_pdf/` | Original CV PDFs (drop them here). |
| `cv_md/` | CVs converted to markdown (`hiring cv2md`). |
| `preparation_md/` | Generated interview prep files (`hiring prep`). |
| `takehome_md/` | Take-home exercises and reviews. |
| `transcript_md/` | Interview transcripts. |
| `scorecards/` | Structured scorecard JSON + `_comparison.md` (`hiring scorecard`). |

## Naming conventions

| Type | Example |
|------|---------|
| CV markdown | `cv_md/CandidateName.md` |
| Interview prep | `preparation_md/CandidateName_interview_prep.md` |
| Take-home | `takehome_md/CandidateName_take_home_exercise.md` |
| Transcript | `transcript_md/candidatename_transcript_round1.md` |
| Scorecard | `scorecards/CandidateName_round1.json` |
