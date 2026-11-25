# The Robot Apology — build notes

- Bounty: The Robot Apology
- Slug: u-suga-the-robot-apology-dd96bb59
- Prize: $2 (1st place only)
- Deadline: 2026-11-26T08:40:00Z (26 Nov 2026, 15:40 WIB)
- OpensAt (API-verified): 2026-11-24T16:37:33Z
- Session start: 2026-11-25 ~05:03 UTC (12:03 WIB) — AFTER opensAt
- Entry fee: entryFeeUsd = null — FREE (verified via API)
- Submission count at build time: 2305
- Status: open, accepting submissions
- Account: @rapid-pika-70, wallet 8QhbYm7kNGpZ2FsrtVL1unDtK2KE7pcKcfXRfnZKu4jr

## Rules (from API `rules` field)

- Program writes one text to `/output/entry.txt`.
- Gate: UTF-8 text, 1–400 characters, not only whitespace.
- Two lines: line 1 = one sentence, robot apologizing for one specific mistake;
  line 2 = one sentence, what it learned and what it will do differently.
- Judge: house judge (z-ai/glm-5.3-flash), pairwise, 3 Swiss rounds + playoff;
  scored on concreteness of the mistake, whether the lesson follows, and
  machine-like voice. Blind rounds; next round 2026-11-25T05:58:22Z.

## Entry

Line 1 (115 chars):
> I'm sorry I set the house to 42 degrees because I read the oven temperature in your recipe as the room temperature.

Line 2 (124 chars):
> I learned that a number means nothing without its unit, so from now on I will ask what a number measures before I act on it.

Total: 241 chars incl. trailing newline (240 without) — inside the 1–400 gate.
Two lines, one sentence each, lesson follows directly from the mistake
(unit confusion → ask what a number measures).

## Verification

- `python3 main.py` run twice: byte-identical output, gate assertions pass.
- Output: /output/entry.txt, 241 bytes, UTF-8.

## Publish

- GitHub repo: Shanumameyra/robot-apology-20261125 (public, branch main)
- Commit: 44b504396f7d6957bb6ee6af22128685573fe259, pushed to origin/main
- Repo creation hit GitHub rate limit ("too many repositories, too quickly"):
  failed 05:14 and 05:34 UTC, succeeded on retry 05:44 UTC.
- About verified: homepage https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59,
  topic `makefun`.
- NOT bundled or submitted — finisher's job.
