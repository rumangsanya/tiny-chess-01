# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/rumangsanya/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/rumangsanya/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in at most 4,096 bytes of Python (standard library only). It plays the make.fun house gauntlet through the contest env: iterative-deepening alpha-beta search with quiescence search, capture-first move ordering, and piece-square-table evaluation, all under a fixed node budget — no clock, no unseeded randomness, so every replay makes the same moves.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 main.py
```

`main.py` expects a tiny-chess-01 env (from the competition's dev kit) serving the gauntlet at `MAKEFUN_ENV_URL`, and plays every game of the trial to the end.

---

<sub>Entered on [make.fun](https://make.fun/?ref=jsqes0wt&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
