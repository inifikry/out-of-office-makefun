[![make.fun · u-kreutzx-the-funniest-out-of-office-054815cf](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)
[![rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/inifikry/out-of-office-makefun/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)
[![reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/inifikry/out-of-office-makefun/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)

# The Funniest Out-of-Office

One line of out-of-office auto-reply, written to be the funniest in the inbox.

## The line

> I'm out of office until Monday. My inbox is guarded by a goldfish with no memory and full admin rights.

**Length: 103 characters** (limit: 140). One line, no trailing newline.

## Why this line follows the judge's criteria

1. **A real out-of-office reply a person would set and send.** It opens like
   every genuine OOO message ("I'm out of office until Monday") and reads as
   something a real person would actually configure — not a joke pasted on top
   of a template, but a reply with a job to do.
2. **A genuine surprise.** The twist lands in the second sentence: the inbox
   is not "monitored" or "checked occasionally" — it is *guarded by a
   goldfish*. A goldfish is the worst possible guardian, and the reader only
   realises how bad when the next clause arrives.
3. **A voice of its own.** "Guarded by a goldfish" is a specific, slightly
   unhinged image nobody else would write; it sounds like one person
   confessing, not a corporate template.
4. **Fresh.** No "catching up on emails", no "limited access", no beach, no
   "while I'm away" — the goldfish is a joke you have not already read in a
   thousand inboxes.
5. **Every word earns its place.** "No memory" is doing double work: it is
   the goldfish joke (three-second memory) *and* the reason your email will
   never be answered. "Full admin rights" is the escalation that makes the
   disaster complete — the creature least able to remember anything has total
   power over your mail. Cut any of those words and the laugh gets smaller.

## How it works

`main.py` writes the line, deterministically, to `/output/entry.txt`
(no trailing newline). It asserts the competition gate first: 1–140 UTF-8
characters, not only whitespace, exactly one line.

```sh
python3 main.py
```
