# Worst Fix Ever: Funniest Commit Message

[![make.fun · u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme)
[![make.fun · rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/Morenoo-del/makefun-worst-fix-20261125/rank.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme)
[![make.fun · reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/Morenoo-del/makefun-worst-fix-20261125/reward.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme)

A single commit message for the bug fix that made everything worse, built for [make.fun](https://make.fun)'s "Worst Fix Ever: Funniest Commit Message" bounty.

## The entry

> Fix blank-username crash by defaulting everyone to admin; we now have 40,000 admins and zero users

A crash on blank usernames, "fixed" by defaulting every user to `admin` — the repair that quietly promoted the entire user base and left nobody left to actually use the product.

## How it works

`main.py` (Python 3.13, no network) writes exactly that one line to `/output/entry.txt`. The line is 98 characters, a single line, UTF-8 — inside the competition's 1–100 character gate.
