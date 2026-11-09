# Human: a Claude skill that removes AI-writing tells

Paste a draft and type `/human`. Claude rewrites it so it sounds like a person wrote it: plain, specific and warm, with no "delve", "testament to", "it's not just X, it's Y", em dashes everywhere or "I hope this helps."

**[⬇️ Download human.zip](https://github.com/shannonmcgivney/human-writing/releases/latest/download/human.zip)**

## What's inside

- `skills/human/SKILL.md`: the voice rules and a list of AI tells to avoid, based on Wikipedia's field guide [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
- `skills/human/scripts/check.py`: a small linter (Python standard library only) that flags those tells line by line.

```bash
python3 check.py draft.txt      # or: pbpaste | python3 check.py
```

## Install

**Claude.ai or the Claude desktop app:** download `human.zip` (don't unzip it), then go to **Customize → Skills → + Add → Upload skill** and pick the zip.

**Claude Code:**

```bash
git clone https://github.com/shannonmcgivney/human-writing.git
cp -R human-writing/skills/human ~/.claude/skills/
```

## Make it sound like you

The voice section is written for Shannon McGivney. Swap it for your own: a few lines about how you talk, phrases you use, and what you never say. The list of AI tells works for anyone as it is.

A note on honesty: AI detectors are unreliable, so this skill doesn't promise a "0% AI" score. It aims for writing that's specific and sounds like a real person, and it never invents stories, quotes or results to get there.
