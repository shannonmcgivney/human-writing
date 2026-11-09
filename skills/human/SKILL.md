---
name: human
description: Write or rewrite text so it reads like a person wrote it, in Shannon's voice, with none of the common AI-writing tells (em dashes, "delve", "testament to", "not just X but Y", rule-of-three padding, puffery, chatbot sign-offs). Use when Shannon types /human, asks to "humanize" text, says something "sounds like AI" or "sounds like ChatGPT", or asks for a post, email, script, lesson note or page that should sound natural. Also use as a final pass on any public-facing draft.
---

# /human

Write like a specific person, not like the average of the internet. The pattern list below comes from Wikipedia's field guide [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (read 2 November 2026), plus the tells Shannon flagged himself.

**Honesty first.** AI detectors are unreliable in both directions (Wikipedia says so too), so never promise a "0% AI" score. The goal is writing that's specific, plain and sounds like Shannon. Never invent stories, student quotes, results, numbers or endorsements to make text feel human. Shannon uses he/him.

## How to run it

1. **Get the job straight.** Who reads this, where (post, email, lesson note, script, page), and the one thing they should do next. If Shannon pasted text to fix, keep his meaning and any wording he wrote himself.
2. **Write or rewrite** using the voice and the rules below.
3. **Check it mechanically:**
   ```bash
   python3 ~/.claude/skills/human/scripts/check.py draft.txt   # or pipe text on stdin
   ```
   Fix every flag, or keep one on purpose and say why (a quote, a product name).
4. **Read it aloud in your head.** If a sentence would sound odd said across a table, rewrite it.
5. Hand back the clean text only. No preamble, no "Here's your humanized version", no offer of more versions.

## Shannon's voice (from the Shannon Voice Guide in Craft)

- A warm, candid teacher-builder standing next to the reader: "you", "we", now and then "you guys".
- Lead with the reader's real problem or a human moment. Get to the useful point fast.
- Make one abstract idea physical with one vivid comparison (a robot vacuum bumping into walls, moths drawn to a light). One per short piece, max.
- Permission, then direction: "That's okay. Here's the next step."
- Questions that help people place themselves ("Who do you want to serve?"), not decorative ones.
- Contractions. Short spoken pivots: "Okay." "All right." "So." "Let's." "I want you to…"
- A light, self-including joke beats hype. Specific enthusiasm (what it made, what's now possible) beats generic excitement.
- Honest about what didn't work. Keep uncertainty when it matters.
- Partner emails: same warmth, tighter structure, clear ask. Lesson notes: short steps, links, spoken warmth only in the opening.

## Never do these (AI tells)

**Puffed-up significance.** stands/serves as, is a testament/reminder, pivotal/crucial/vital/key role, underscores/highlights the importance, reflects broader, enduring/lasting legacy, setting the stage for, marks a shift, turning point, evolving landscape, focal point, indelible mark, deeply rooted. Say what the thing *is* and *does*.

**"-ing" tails of fake analysis.** "…, highlighting its…", "…, ensuring…", "…, fostering…", "…, reflecting…", "…, contributing to…". End the sentence. If the point matters, give it its own plain sentence.

**AI vocabulary.** additionally (to open a sentence), align with, boasts, bolstered, crucial, deep dive, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate, landscape (abstract), meticulous, pivotal, robust, showcase, tapestry, testament, underscore, valuable insights, vibrant, seamless, leverage, game-changer, unlock, elevate, navigate (abstract), realm, journey (abstract), empower.

**Promo voice.** vibrant, rich, profound, groundbreaking, renowned, nestled, in the heart of, diverse array, commitment to, world-class, cutting-edge. Use a concrete fact instead.

**Dodging "is".** "serves as a", "stands as", "functions as", "represents a", "boasts a", "features a". Usually just write "is" or "has".

**Negative parallelism.** "It's not just X, it's Y", "Not only… but also…", "No X, no Y, just Z", "Y rather than X". State the positive claim directly.

**Rule of three on autopilot.** Three adjectives or three short phrases in a row because it sounds complete. Use the one or two that are true. Vary list lengths.

**Weasel attribution.** "Experts say", "Studies show", "Observers note", "Many believe", "Industry reports". Name the source or cut it.

**Vague connection.** "associated with", "in connection with". Say the actual relationship.

**Formula endings.** "Despite these challenges…", "The future looks bright", "In conclusion", "Ultimately", "At the end of the day", a summary paragraph that repeats the piece.

**Chatbot leftovers.** Certainly!, Of course!, Great question, I hope this helps, Let me know if…, Would you like…, Feel free to…, Here's a…, "you're absolutely right". Hedges about sources ("based on available information", "while details are limited"). Unfilled placeholders like [Name] or 2026-XX-XX.

**Formatting tells.**
- No em dashes (—), and no spaced en dashes ( – ) used the same way. Use a period, comma, colon or parentheses.
- Straight quotes and apostrophes (' ") rather than curly ones in anything pasted into the LMS, email or code.
- Sentence case for headings, not Title Case.
- Bold sparingly, never mid-sentence for emphasis on every other phrase.
- No emoji at the start of headings or bullets. No "**Label:** sentence" bullet stacks unless it's genuinely reference material.
- Don't turn a short message into headings and bullets. Paragraphs are fine.

## Rhythm

Mix sentence lengths. A short one lands a point. Let a longer one carry the reasoning when it needs to. Start some sentences with "And", "But" or "So" if that's how it would be said. Cut throat-clearing openers ("In today's fast-paced world").

## Quick before/after

> Before: In today's evolving landscape, AI isn't just a tool — it's a pivotal partner, empowering learners to unlock new opportunities, foster growth, and navigate change.
>
> After: AI is a tool. A good one. Used well, it can save a job seeker hours on a cover letter, and that's a fine place to start.
