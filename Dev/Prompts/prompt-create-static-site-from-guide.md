# Prompt — Create static POE 2 campaign site from markdown guide

Use this prompt after creating a guide in `Dev/Guides/`.

---

## Message to send to the agent

```
Create a static single-file HTML campaign guide from the markdown guide below.

## Inputs

- Markdown guide: @Dev/Guides/<slug>_timeline_guide.md
- Reference HTML layout/style: @deadeye.html
- Existing build page to mirror if updating: @monk.html (only if relevant)
- Output HTML file: <slug>.html (repo root, example: monk.html)
- Build short name for sidebar/logo: <SHORT CODE> (example: MK)
- Public slug / URL path: <slug> (example: monk)
- Page title: <BUILD TITLE> (example: Monk Leveling POE 2 — Detailed Act-by-Act Guide)
- Accent theme: <primary color concept> (example: lightning/amber for Monk, ice/cyan for Deadeye)

Optional source links section:
- Planner URL: <PLANNER URL or leave empty>
- YouTube URL: <VIDEO URL or leave empty>

Landing page index: @index.html
Update index.html if this is a new guide.

## Goal

Build a guide meant to be used DURING the campaign.
It must be easy to scan while playing.
Do not overload the page with every markdown paragraph.
Follow the same information architecture as the reference HTML.

## Hard requirements

1. **Single-file static HTML**
   - All CSS inline in `<style>`
   - All JS inline in `<script>`
   - No external assets
   - No frameworks
   - No CDN fonts/images
   - No network calls at runtime

2. **Act-oriented step-by-step layout**
   - Sidebar navigation
   - Hero overview
   - One section per act / interlude
   - Sticky timeline panel inside each act section
   - Right-side cards with practical instructions

3. **Do not copy the markdown verbatim**
   - Condense intelligently
   - Keep timestamps, levels, skills, gear priorities, and warnings
   - Remove repetition across sections

4. **Match the reference page standards**
   Use the same section/card pattern as `@deadeye.html` and `@monk.html`.

## Required page structure

### A. Document shell
- `<!DOCTYPE html>`
- responsive viewport meta tag
- descriptive `<title>`
- dark gradient theme similar to reference
- sticky left sidebar + scrollable main content
- print styles
- mobile breakpoints

### B. Sidebar
Include links to:
- Overview
- Sources (only if planner/video links provided)
- Act 1
- Act 2
- Act 3
- Act 4
- Interlude (if guide covers it)
- Boss Rotation
- Checklists
- Time Saves

Also include:
- brand block with logo initials
- short subtitle
- one side-note with the most important run rule
- search box that filters `.card` and `.timeline-panel`

Implement active nav highlighting on scroll exactly like the reference pages.

### C. Hero (`#overview`)
Include:
- eyebrow label
- large title with gradient accent on build name
- one paragraph summary
- 4 stat cards with the most important breakpoints

Example stat cards:
- build phases
- first major breakpoint level/time
- major build switch
- final campaign checkpoint

### D. Overview section
Two-column grid with cards for:
- Core route identity (pill row with phase summaries)
- What makes or breaks the run (highlight card + callout)
- Skill progression summary table
- Target pace splits table

Keep this section concise.

### E. Sources section (`#sources`) — only if links provided
Add a section with:
- heading: Build sources
- two external link cards:
  - Mobalytics planner
  - YouTube video
- links open in new tab with `rel="noopener noreferrer"`

If no links are provided, omit this section and nav item.

### F. Act sections
Create one section per act/interlude using this exact layout:

Left column:
- sticky `.timeline-panel`
- table columns: `Time | Lvl | Milestone`
- use `.time-cell`, `.level-chip`, `.tiny` subnotes

Right column cards:
1. **Primary objective**
2. **Do this session** (or **Do this**)
3. **Early gear priorities** or **Gear priorities** or **Vendor check**
4. Optional extra cards only when important:
   - highlight card for major power spike
   - warn card for failure point
   - danger card for survival/stat wall

Color-code act headers like the reference:
- Act 1 → amber
- Act 2 → violet
- Act 3 → blue
- Act 4 → amber
- Interlude → green

Each act timeline should contain the most important 8–14 milestones for that act only.
Do not dump the entire global milestone table into every act.

### G. Boss Rotation section (`#rotation`)
Convert the final boss loop into 5–7 `.step` cards in `.rotation`.
Use the simplified endgame/campaign boss rotation from the markdown guide.

### H. Checklists section (`#checklists`)
Two highlight/danger cards with compact tables:
- one checklist before a major transition (example: before Siphoning Strike switch / before Act 3 final / before Tawakai)
- one checklist before a late-campaign checkpoint

### I. Time Saves section (`#timesaves`)
One warn card with a compact table:
- `Problem in run`
- `Correction`

Use transcript-backed time-loss patterns from the markdown guide.

### J. Footer
Exact line:
`Built as a static single-file HTML guide. No external assets, frameworks, or network calls.`

## Content rules

### Include
- exact skill names
- exact support names
- ascendancy choice and key bonuses
- weapon/base names
- vendor strategy
- survival warnings
- timestamp milestones
- level breakpoints when known
- “optional / skip / dropped later” notes when important

### Exclude
- long transcript quotes
- full passive tree
- duplicate tables already shown elsewhere
- mapping/endgame sections unless the guide explicitly covers them
- excessive theorycrafting
- placeholder lorem ipsum

## Visual / UX rules

- Match spacing, card radius, typography, and layout conventions from `@deadeye.html`
- Keep templates scannable with blank lines between logical blocks
- Use strong tags for important game terms
- Keep sidebar usable on mobile
- Hide level column on very small screens if using the same responsive behavior as reference
- Search filter must hide non-matching cards/timelines

## Theme guidance

Choose accent colors based on build identity:
- lightning/shock monk → amber + violet
- ice/bow deadeye → cyan + violet
- fire builds → orange/red
- poison builds → green

Do not clone the Deadeye palette if the build identity differs.

## Index page update

If adding a new guide, update `index.html`:
- add a new guide card linking to `/<slug>`
- short one-line description
- keep page static and self-contained

Do not break existing guide links.

## File placement

- HTML guide goes in repo root: `<slug>.html`
- Do not place published HTML under `Dev/`
- Keep source markdown in `Dev/Guides/`

## Quality checks before finishing

Verify all of the following:

- [ ] Page opens correctly as a local file and as GitHub Pages URL
- [ ] Sidebar anchor links scroll to all sections
- [ ] Each act section has timeline + primary objective + do-this + gear card
- [ ] Final build loop is reflected in Boss Rotation
- [ ] Page is not overly long or repetitive
- [ ] No external dependencies
- [ ] Sources section present only when links provided
- [ ] `index.html` updated if this is a new guide
- [ ] Output filename is simple lowercase slug (`monk.html`, `deadeye.html`)

## Git publish steps — REQUIRED at the end

After creating/updating the HTML (and `index.html` if needed), commit and push to GitHub.

Repository remote:
- https://github.com/smarza/poe2-guides.git

Run these steps in the repo root:

1. Check changes:
   - `git status`
   - `git diff`

2. Stage relevant files only:
   - `<slug>.html`
   - `index.html` (if changed)
   - do NOT commit transient local files from `Dev/Transcriptions/` unless explicitly requested

3. Commit with a message focused on why:
   - example: `Add Monk leveling static campaign guide page`

4. Push:
   - `git push origin main`

5. Confirm publish:
   - remind the user the GitHub Pages URL will be:
     - `https://smarza.github.io/poe2-guides/<slug>`
   - if Pages is configured with branch deploy from `main`, no GitHub Actions workflow is needed

Do not force push.
Do not amend unless a hook modified files after commit.
Do not change git config.

## Deliverable

Return:
1. path to created/updated `<slug>.html`
2. whether `index.html` was updated
3. commit hash
4. public URL(s)
5. short summary of act sections created
```

---

## Example filled prompt

```
Create a static single-file HTML campaign guide from the markdown guide below.

Markdown guide: @Dev/Guides/poe2_monk_leveling_timeline_guide.md
Reference HTML layout/style: @deadeye.html
Existing build page to mirror: @monk.html
Output HTML file: monk.html
Build short name for sidebar/logo: MK
Public slug / URL path: monk
Page title: Monk Leveling POE 2 — Detailed Act-by-Act Guide
Accent theme: lightning/amber

Planner URL: https://mobalytics.gg/poe-2/profile/spud-the-king-nksem3/builds/one-shot-monk-leveling-poe2-0-5-league-starter
YouTube URL: https://www.youtube.com/watch?v=s2LkL7ev27Y

Landing page index: @index.html
Update index.html only if needed.
```
