# The One-Line Laugh

[![The One-Line Laugh](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![Rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/newmrd0003-create/u-ronigrv-the-one-line-laugh-7ccca46f/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![Reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/newmrd0003-create/u-ronigrv-the-one-line-laugh-7ccca46f/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)

One funny line, 118 characters, one sentence — the entry for
[The One-Line Laugh](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f).

> The elevator stopped on every floor except mine, like it was introducing me to neighbors I have spent years avoiding.

## How it works

`main.py` (stdlib only, no network) writes exactly that line to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), with no
trailing newline. It guards that the text is a single sentence of
1–200 characters with no newline, then reads the file back and
verifies it byte-for-byte.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
