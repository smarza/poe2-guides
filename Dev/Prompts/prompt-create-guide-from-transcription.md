# Prompt — Create POE 2 campaign guide from YouTube transcription

Use this prompt after exporting a transcript with `Dev/Scripts/Export-YouTubeTranscript.ps1`.

---

## Message to send to the agent

```
Create a POE 2 campaign leveling guide from the transcript below.

## Inputs

- Transcript file: @Dev/Transcriptions/transcript_<VIDEO_ID>_with_timeline.md
- Build name: <BUILD NAME> (example: Monk Leveling)
- Class / ascendancy: <CLASS> / <ASCENDANCY>
- Video URL: <YOUTUBE URL>
- Optional planner URL: <MOBALYTICS OR OTHER PLANNER URL>
- Output file: Dev/Guides/<slug>_timeline_guide.md

Reference quality bar: @Dev/Guides/poe2_monk_leveling_timeline_guide.md
That file is the exact standard for structure, depth, and usefulness during a live campaign run.

## Goal

Produce a guide someone can follow while playing the campaign.
The guide must help the player hit the same power spikes at roughly the same time as the video.
Do NOT write a generic build guide.
Do NOT write a lore summary.
Do NOT copy transcript lines verbatim in bulk.

The transcript is messy spoken English (or auto-captions). Your job is to extract:
- build phases
- skill/support timing
- gear priorities
- act-by-act decisions
- boss fight notes
- mistakes the creator warns about
- the final simplified version of the build after experimentation

## Critical interpretation rules

1. **Timestamps are first-class data**
   - Every important milestone must include `HH:MM:SS` from the transcript.
   - Use transcript timestamps, not guessed times.
   - When the creator mentions level breakpoints, include both time and level when available.

2. **Separate experiment from final advice**
   - The creator may try skills and drop them later.
   - Mark temporary bridge phases clearly.
   - End with the practical simplified build the run actually wins with.

3. **Prefer actionable campaign guidance over theory**
   - Tell the player what to craft, buy, path, equip, or skip.
   - Explain why a decision matters only when it affects pacing or survival.

4. **Do not over-invent**
   - If the transcript does not support a detail, say it is unclear or optional.
   - Do not fabricate passive tree nodes, exact gear rolls, or zone routing unless spoken in the transcript.

5. **Weapon and vendor checks are often the real story**
   - If the creator repeatedly upgrades weapons or checks vendors, make that a major theme.
   - Call out when a vendor upgrade nearly doubles damage.

6. **Survival matters**
   - If the creator says the character is squishy, fragile, dies, or needs defense, include that prominently.
   - Damage spikes are useless if the player dies before landing burst.

7. **Name game objects exactly**
   - Use exact skill, support, item, ascendancy, trial, boss, and zone names from the transcript.
   - Normalize obvious transcription errors only when meaning is clear.

## Required document structure

Write the markdown guide with ALL of the following sections, in this order.

### 1. Title + metadata
- H1 with build name and purpose
- Source transcript filename
- Video URL
- Short goal blockquote explaining:
  - this is a campaign pacing guide, not necessarily a strict speedrun
  - the player should copy power spikes, not every detour/experiment

### 2. Executive Summary
- Describe the run in **3–4 phases** (early / mid / final / optional endgame if present)
- Each phase should mention:
  - main skills
  - main damage source
  - main weakness
  - when the phase ends
- End with 4–6 bullet "biggest practical lessons"

### 3. Target Milestones at a Glance
- Markdown table with columns:
  - `Target time`
  - `Milestone`
  - `What should be true by then`
- Include every major power spike from Act 1 through campaign end / interludes
- Aim for 20–35 rows for a full campaign transcript

### 4. Core Build Concept
Split into subsections:
- Early concept
- Midgame concept
- Final practical concept

Each subsection should use numbered steps or bullets that describe how the build actually plays.

### 5. Skill and Support Progression
- Table columns:
  - `Time`
  - `Skill/support`
  - `Use`
- Include supports, auras, marks, cries, optional skills, and skills explicitly dropped later

### 6. Passive Tree / Ascendancy Priorities
Because transcripts rarely contain a full tree, extract priorities instead of inventing a full tree.
Include:
- early passive priorities
- weapon set ideas if mentioned
- ascendancy choice timing and exact bonuses taken
- later passive priorities
- defensive nodes if mentioned

### 7. Gear Rules
Include:
- general item priorities for armor/accessories
- weapon priorities
- vendor strategy
- important weapon bases / key items in a table with approximate timestamps

### 8. Rotation by Phase
For each major phase, provide a compact text rotation block like:

```text
Step A → Step B → Step C → repeat
```

Include at minimum:
- early leveling loop
- midgame boss loop
- bridge phase loop if one exists
- final boss loop

### 9. Full Timeline / Step-by-Step Run Guide
This is the most important section.
Break the run into timestamp ranges such as:
- `00:00:00–00:06:20 — Clearfell, first gem, Frozen Locus`
- `00:06:20–00:12:50 — first route checks and weapon upgrade`

For each range include bullet notes covering:
- where the player is in the campaign
- skills crafted/upgraded
- gear checks
- passives/ascendancy decisions
- boss fights
- mistakes, detours, or optional skips

Use as many subsections as needed to cover the full transcript.
Do not compress late acts too aggressively.

### 10. Practical Reproduction Checklist
Checkbox lists grouped by:
- Before starting
- Act 1 checklist
- Act 2 checklist
- Act 3 checklist
- Act 4 / Interlude checklist

Each checklist item must be concrete and testable.

### 11. Boss / Key Fight Notes
Table columns:
- `Timestamp`
- `Fight / event`
- `Notes`

Include mushroom boss, major act bosses, trial bosses, final campaign boss, and any fight where the creator explains mechanics or mistakes.

### 12. Common Mistakes to Avoid
- 5–8 numbered mistakes
- Each mistake must come from transcript behavior or explicit creator warnings

### 13. Minimal “Same Build” Version
Provide a compact plain-text summary for players who do not want all the experimentation detail.
Use this format:

```text
Early Act X:
...

Mid Act X:
...

Core switch:
...

Boss rotation:
...

Gear:
...
```

### 14. Recommended Pace Targets
Table columns:
- `Segment`
- `Target from transcript`
- `Your target`

Use transcript times for the first column.
Use realistic player-friendly ranges in the third column.

### 15. Final Notes
- Summarize the 5–7 power spikes to copy
- End with one sentence describing the final winning pattern of the build

## Writing style requirements

- English
- Clear, direct, campaign-oriented prose
- Strong emphasis on **bold** skill names, ascendancies, items, and timestamps
- Short paragraphs
- Bullet lists over long prose where possible
- No fluff, no intro essay, no “welcome to my guide”
- No table of contents unless needed
- Do not include HTML
- Do not include screenshots
- Do not include affiliate links

## Content quality checks before finishing

Verify all of the following:

- [ ] Every act transition is represented
- [ ] Major skill transitions have timestamps
- [ ] Ascendancy choice is documented with exact bonuses
- [ ] Vendor/weapon upgrade cadence is clear
- [ ] Final simplified build is distinct from early bridge build
- [ ] Boss fights and trial content are called out
- [ ] Common mistakes section is transcript-backed
- [ ] Checklists are usable mid-run
- [ ] Pace targets exist for act starts and major build switch
- [ ] Output saved to `Dev/Guides/<slug>_timeline_guide.md`

## Deliverable

Return only:
1. The completed markdown guide saved to the output path
2. A short summary listing:
   - build phases found
   - major timestamp milestones
   - final core skill loop
   - anything unclear in the transcript
```

---

## Example filled prompt

```
Create a POE 2 campaign leveling guide from the transcript below.

Transcript file: @Dev/Transcriptions/transcript_s2LkL7ev27Y_with_timeline.md
Build name: Monk Leveling
Class / ascendancy: Monk / Invoker
Video URL: https://www.youtube.com/watch?v=s2LkL7ev27Y
Planner URL: https://mobalytics.gg/poe-2/profile/spud-the-king-nksem3/builds/one-shot-monk-leveling-poe2-0-5-league-starter
Output file: Dev/Guides/poe2_monk_leveling_timeline_guide.md

Reference quality bar: @Dev/Guides/poe2_monk_leveling_timeline_guide.md
```
