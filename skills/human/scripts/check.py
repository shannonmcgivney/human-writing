#!/usr/bin/env python3
"""Flag common AI-writing tells in a draft.

Usage: check.py FILE      or      cat draft.txt | check.py
Exit code 0 when clean, 1 when anything was flagged.
Patterns follow Wikipedia:Signs of AI writing (read 2 Nov 2026) plus Shannon's own list.
"""
import re
import sys

WORDS = [
    "additionally", "align with", "aligns with", "boasts", "bolstered", "crucial", "deep dive", "delve", "delves",
    "emphasizing", "enduring", "enhance", "enhances", "enhancing", "fostering", "foster", "garner", "garnered",
    "interplay", "intricate", "intricacies", "landscape", "meticulous", "meticulously", "pivotal", "robust",
    "showcase", "showcases", "showcasing", "tapestry", "testament", "underscore", "underscores", "underscoring",
    "valuable insights", "vibrant", "seamless", "seamlessly", "leverage", "game-changer", "game changer",
    "unlock", "unlocks", "elevate", "elevates", "realm", "empower", "empowers", "empowering", "groundbreaking",
    "renowned", "nestled", "in the heart of", "diverse array", "commitment to", "cutting-edge", "world-class",
    "resonate with", "resonates with",
]

PHRASES = {
    "puffed-up significance": [
        r"\b(stands|serves) as\b", r"\bis a (testament|reminder)\b",
        r"\b(pivotal|crucial|vital|significant|key) (role|moment)\b", r"\breflects? broader\b",
        r"\b(enduring|lasting|indelible) (legacy|mark|impact)\b", r"\bsetting the stage for\b",
        r"\bmarks? a shift\b", r"\bturning point\b", r"\bevolving landscape\b", r"\bfocal point\b",
        r"\bdeeply rooted\b",
    ],
    "dodging 'is'": [r"\b(functions|operates) as an?\b", r"\brepresents an?\b", r"\bboasts an?\b"],
    "negative parallelism": [
        r"(\bnot|n'?t) (just|only|merely)\b[^.!?]{0,80}\b(but|it'?s|it is)\b", r"\bit'?s not\b[^.!?]{0,60}\bit'?s\b",
        r"\bno \w+, no \w+, just\b", r"\brather than\b",
    ],
    "-ing tail analysis": [r",\s+(highlighting|underscoring|emphasizing|ensuring|reflecting|symbolizing|contributing to|cultivating|fostering|encompassing|showcasing)\b"],
    "weasel attribution": [
        r"\b(experts|observers|critics|analysts) (say|argue|note|have noted|believe)\b", r"\bstudies show\b",
        r"\bindustry reports\b", r"\bmany (believe|argue|say)\b", r"\bit is widely (believed|recognized)\b",
    ],
    "vague connection": [r"\b(associated|in connection) with\b", r"\bin association with\b"],
    "formula ending": [
        r"\bdespite (these|its|the) challenges\b", r"\bin conclusion\b", r"\bultimately,", r"\bat the end of the day\b",
        r"\bthe future (looks|is) bright\b", r"\bin today'?s (fast-paced|digital|ever-changing)\b",
    ],
    "chatbot leftover": [
        r"\bcertainly!", r"\bof course!", r"\bgreat question\b", r"\bi hope this helps\b", r"\blet me know if\b",
        r"\bwould you like\b", r"\bfeel free to\b", r"\byou'?re absolutely right\b", r"\bhere'?s an? (revised|updated|humanized)\b",
        r"\bbased on (the )?available information\b", r"\bwhile (specific )?details are (limited|scarce)\b",
    ],
    "placeholder": [r"\[(name|insert[^\]]*|your [^\]]*|placeholder[^\]]*)\]", r"\b20\d\d-(xx|XX)-(xx|XX)\b"],
}

CHARS = {
    "em dash": "—",
    "spaced en dash": " – ",
    "curly quote": "“”‘’",
}

EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
SMALL = {"a", "an", "the", "and", "or", "of", "to", "in", "on", "for", "with", "at", "by"}


def check(text):
    flags = []
    word_res = [(w, re.compile(r"\b" + re.escape(w) + r"\b", re.I)) for w in WORDS]
    phrase_res = [(k, re.compile(p, re.I)) for k, ps in PHRASES.items() for p in ps]
    bold_total = 0
    for n, line in enumerate(text.splitlines(), 1):
        if CHARS["em dash"] in line:
            flags.append((n, "em dash", "replace with a period, comma, colon or parentheses"))
        if CHARS["spaced en dash"] in line:
            flags.append((n, "spaced en dash", "used like an em dash"))
        if any(c in line for c in CHARS["curly quote"]):
            flags.append((n, "curly quote", "use straight ' and \""))
        for w, r in word_res:
            if r.search(line):
                flags.append((n, "AI vocabulary", w))
        for k, r in phrase_res:
            m = r.search(line)
            if m:
                flags.append((n, k, m.group(0)))
        stripped = line.lstrip("#-*> ").strip()
        if stripped and EMOJI.match(stripped):
            flags.append((n, "emoji lead", stripped[:1]))
        if line.startswith("#"):
            words = [w for w in line.lstrip("# ").split() if w[:1].isalpha() and w.lower() not in SMALL]
            if len(words) >= 3 and all(w[:1].isupper() for w in words):
                flags.append((n, "title case heading", line.strip()))
        bold_total += len(re.findall(r"\*\*[^*]+\*\*", line))
    words_total = max(len(text.split()), 1)
    if bold_total and words_total / bold_total < 40:
        flags.append((0, "heavy bold", f"{bold_total} bold phrases in {words_total} words"))
    return flags


def main():
    text = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
    flags = check(text)
    if not flags:
        print("Clean: no AI-writing tells found.")
        return 0
    print(f"{len(flags)} tell(s) found:")
    for n, kind, detail in flags:
        where = f"line {n}" if n else "overall"
        print(f"  {where:>8}  {kind}: {detail}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
