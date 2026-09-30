# Cascade vs mini-only comparison

Questions: 20

| Metric | Cascade (nano -> mini) | Mini-only |
|---|---|---|
| Accuracy | 17/20 (85.0%) | 18/20 (90.0%) |
| Escalated to mini | 10/20 (50.0%) | n/a (always mini) |
| Nano completion tokens | 1212 | -- |
| Mini completion tokens | 511 | 1391 |
| Total completion tokens | 1723 | 1391 |
| Token savings vs mini-only | -332 (-23.9% fewer) | -- |

Accuracy delta (cascade - mini-only): -1 questions (-5.0 pts)

## Per-question breakdown

| Q | Category | Correct | Cascade | Escalated | Nano tok | Mini tok | Mini-only |
|---|---|---|---|---|---|---|---|
| 1 | miscellaneous | C | A (x) | yes | 14 | 39 | C (ok) |
| 2 | high_school_physics | A | A (ok) | no | 141 | 0 | A (ok) |
| 3 | miscellaneous | B | B (ok) | no | 25 | 0 | B (ok) |
| 4 | nutrition | B | B (ok) | yes | 47 | 49 | B (ok) |
| 5 | high_school_psychology | D | D (ok) | no | 33 | 0 | D (ok) |
| 6 | elementary_mathematics | B | B (ok) | yes | 37 | 49 | B (ok) |
| 7 | high_school_computer_science | D | D (ok) | yes | 10 | 71 | D (ok) |
| 8 | high_school_psychology | B | B (ok) | no | 49 | 0 | B (ok) |
| 9 | high_school_psychology | D | D (ok) | no | 39 | 0 | D (ok) |
| 10 | high_school_physics | C | C (ok) | yes | 213 | 88 | C (ok) |
| 11 | nutrition | B | B (ok) | no | 104 | 0 | B (ok) |
| 12 | miscellaneous | C | C (ok) | yes | 25 | 48 | C (ok) |
| 13 | miscellaneous | D | D (ok) | no | 36 | 0 | D (ok) |
| 14 | high_school_geography | D | D (ok) | no | 41 | 0 | D (ok) |
| 15 | high_school_psychology | B | D (x) | no | 59 | 0 | C (x) |
| 16 | high_school_mathematics | D | D (ok) | no | 114 | 0 | D (ok) |
| 17 | high_school_us_history | A | A (ok) | yes | 45 | 53 | A (ok) |
| 18 | nutrition | D | C (x) | yes | 90 | 40 | C (x) |
| 19 | nutrition | D | D (ok) | yes | 17 | 40 | D (ok) |
| 20 | high_school_chemistry | C | C (ok) | yes | 73 | 34 | C (ok) |