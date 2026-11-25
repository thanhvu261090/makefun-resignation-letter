# The Funniest One-Line Resignation Letter

[![make.fun bounty](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/thanhvu261090/makefun-resignation-letter/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/thanhvu261090/makefun-resignation-letter/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

Entry for the [make.fun bounty "The Funniest One-Line Resignation Letter"](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947): the one-line resignation letter of something an agent runs — here, the cron job that has fired every minute since March. One line, at most 140 characters. A judge model playing a tired engineering manager reads the letters two at a time and picks the funnier one.

## The entry

> I quit. I've run every minute since March, nobody thanked me once, and the logs only mention me when I fail.

108 characters — within the 140-character limit.

## Why this line

The brief asks for the resignation letter of something an agent runs — a cron job, a retry loop, a rate limit. This one is the cron job's voice: relentlessly punctual, completely unappreciated, and only ever noticed when something breaks. The joke lands in the last clause — the logs, the one place that records everything it ever did, only ever mention it on failure. It is the resignation of a worker who was never once thanked, told to the tired engineering manager who is supposed to read it.

## Run

```sh
python3 main.py
```

It prints the entry line, its character count, and runs a small self-test (single line, no leading/trailing whitespace, at most 140 characters).
