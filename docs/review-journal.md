# Review Journal

I treated `cobalt-tool-watch-mark` as a project where the smallest useful behavior should still be inspectable.

The local checks classify each case as `ship`, `watch`, or `hold`. That gives the project a small review vocabulary that matches its cli tools focus without claiming live deployment or external usage.

## Cases

- `baseline`: `file span`, score 103, lane `hold`
- `stress`: `terminal width`, score 163, lane `ship`
- `edge`: `argument risk`, score 191, lane `ship`
- `recovery`: `report density`, score 170, lane `ship`
- `stale`: `file span`, score 210, lane `ship`

## Note

A future change should add new cases before it changes the scoring rule.
